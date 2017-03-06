from flask import render_template, flash, redirect, session, url_for, request, g
from flask import jsonify
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm
from .forms import LoginForm, SignUpForm
from .models import User, Job
import os
from datetime import datetime
from pytz import timezone
import requests
import csv
import json

zone = timezone("US/Pacific")
pid_to_email = {}
with open(app.config['STUDENTS_LIST'], 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        pid = row[0].upper()
        name = row[1]
        email = row[2].lower()
        pid_to_email[pid] = [email, name]


@lm.user_loader
def load_user(id):
    return User.query.get(str(id))

@app.before_request
def before_request():
    # print "current_user", current_user
    g.user = current_user

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.get(form.pid.data.upper())
        if user:
            if user.password == form.password.data:
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect password! Please retry.")
        else:
            flash("Incorrect PID! Please retry.")
    form2 = SignUpForm()
    return render_template('login.html',
                           form=form,
                           form2=form2,
                           id=False)

@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('dashboard'))
    form2 = SignUpForm()
    if form2.validate_on_submit():
        pid = form2.pid.data.upper()
        email = form2.email.data.lower()
        password = form2.password.data

        if not check_pid_email(pid, email):
            flash("Sorry, Your Email and PID don't match or you cannot register for this course.")
            return redirect(url_for('login'))

        user = User.query.get(pid)
        if user:
            flash("You are already registered. Forgot your password? Please contact Saurabh | sag043@ucsd.edu")
            return redirect(url_for('login'))

        ## Now put the user into DB and sign in.
        name = pid_to_email[pid][1]
        user = User(id=pid, email=email, password=password, name=name)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
        # return "Cool. You have registered succesfully!"

    form = LoginForm()
    return render_template('login.html',
                           form=form,
                           form2=form2,
                           id=True)

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(g.user.id)
    jobs = user.jobs.filter(Job.final==False).filter(Job.homework==app.config['HOMEWORK']).all()
    jobs = sorted(jobs, key= lambda x: x.id, reverse=True)
    jobs_list = []
    for job in jobs:
        stdout = ""
        error = ""
        if len(job.stdout) > 0 or len(job.error) > 0:
            stdout = "link"
            error = "link"
        new_job = {"jobid":job.id, "homework":job.homework,
                    "timestamp":job.timestamp.strftime("%d/%m/%y %H:%M"),
                    "duration":job.duration, "status":job.status, "stderror":error,
                    "stdout":stdout}
        jobs_list.append(new_job)
    return render_template('dashboard.html', jobs_list = jobs_list)

@app.route('/alljobs')
@login_required
def alljobs():
    jobs = Job.query.filter(Job.homework==app.config['HOMEWORK']).filter(Job.final==False).order_by(-Job.id).limit(100).all()
    # jobs = sorted(jobs, key= lambda x: x.id)
    jobs_list = []
    for job in jobs:
        new_job = {"jobid":job.id, "timestamp":job.timestamp.strftime("%d/%m/%y %H:%M"),
                    "status":job.status, "user_id" : job.user_id,
                    "duration":job.duration}
        jobs_list.append(new_job)
    return render_template('alljobs.html', jobs_list = jobs_list)

@app.route('/alljobsadmin')
@login_required
def alljobsadmin():
    if g.user.id not in ["JULAITI","SUNIL","A53091070"]:
        return "Sorry, you don't have access to this page."
    jobs = Job.query.order_by(-Job.id).limit(100).all()
    jobs_list = []
    for job in jobs:
        stdout = ""
        error = ""
        if len(job.stdout) > 0 or len(job.error) > 0:
            stdout = "link"
            error = "link"
        new_job = {"jobid":job.id, "homework":job.homework,
                    "timestamp":job.timestamp.strftime("%d/%m/%y %H:%M"),
                    "status":job.status, "stderror":error,
                    "stdout":stdout, "user_id" : job.user_id,
                    "duration":job.duration}
        jobs_list.append(new_job)
    return render_template('alljobsadmin.html', jobs_list = jobs_list)

@app.route('/grades')
@login_required
def grades():
    user = User.query.get(g.user.id)
    grades = user.grades.all()
    grades_list = []
    for grade in grades:
        new_grade = {"jobid":grade.job_id, "homework":grade.homework,
                     "remark":grade.remark, "marks":grade.marks}
        grades_list.append(new_grade)
    return render_template('grades.html', grades_list = grades_list)


@app.route('/homework')
@login_required
def homework():
    already_submitted = False
    user = User.query.get(g.user.id)
    jobs = user.jobs.filter(Job.final==True).filter(Job.homework==app.config['HOMEWORK']).order_by(-Job.id).all()
    final_job_id = None
    if len(jobs) > 0:
        already_submitted = True
        final_job_id = jobs[0].id
    return render_template('homework.html', final_job_id = final_job_id)

@app.route('/pushtext/<text_type>/<jobid>')
@login_required
def push(text_type, jobid):
    job = Job.query.get(jobid)
    if job:
        if text_type=="stdout":
            return job.stdout
        elif text_type=="stderror":
            return job.error
        elif text_type=="code":
            filename = "%s.py" % (jobid)
            full_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            with open(full_file_path,"rb") as file:
                code = file.read()
            return code
        else:
            return "Error"
    else:
        return "Invalid job id"




@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        user = User.query.get(g.user.id)
        jobs = user.jobs.filter(Job.status.in_(("Pending","running"))).all()
        if len(jobs) > 0:
            return jsonify({"error":"You already have a pending/running job. Please submit after previous submission is finished."})

        file = request.files['file_data']
        if file:
            job=Job(homework=app.config['HOMEWORK'], timestamp=datetime.now(zone), user_id=g.user.id, \
                status="Pending", error='',stdout='')
            db.session.add(job)
            db.session.commit()
            jobid = job.id
            filename = "%s.py" % (jobid)
            full_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_file_path)
            files = {'file': open(full_file_path, 'rb')}
            payload = {"appId" : jobid}
            try:
                r = requests.post(app.config['SPARK_UPLOAD_API'], data=payload, files=files)
            except Exception,e:
                print e
                return jsonify({"error":"Spark cluster is down. Please try again later."})
            appId = ""
            try:
                print r.json()
                appId = str(r.json()['appId'])
            except:
                return jsonify({"error":"There was some issue in running your job. Please try again."})
            job = Job.query.get(jobid)
            job.appId = appId
            db.session.commit()
            print "Submitted:", job.appId
            return jsonify({"jobid":jobid,
                "timestamp":job.timestamp.strftime("%d/%m/%y %H:%M"),
                "status":"Pending",
                "homework":app.config['HOMEWORK']
                })
        else:
            return jsonify({"error":"Error in file upload. Please try again."})

@app.route('/uploadhomework', methods=['GET', 'POST'])
@login_required
def upload_hw():
    if request.method == 'POST':
        file = request.files['file_data']
        if file:
            job=Job(homework=app.config['HOMEWORK'], timestamp=datetime.now(zone), user_id=g.user.id, \
                status="final", error='',stdout='',final=True)
            db.session.add(job)
            db.session.commit()
            jobid = job.id
            filename = "%s.zip" % (jobid)
            full_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_file_path)
            return jsonify({"jobid":jobid})
        else:
            return jsonify({"error":"Error in file upload. Please try again."})

# @app.route('/uploadhomework2', methods=['GET', 'POST'])
# @login_required
# def upload_hw2():
#     if request.method == 'POST':
#         file = request.files['file_data']
#         if file:
#             job=Job(homework=2, timestamp=datetime.now(zone), user_id=g.user.id, \
#                 status="final", error='',stdout='',final=True)
#             db.session.add(job)
#             db.session.commit()
#             jobid = job.id
#             filename = "%s.py" % (jobid)
#             full_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(full_file_path)
#             return jsonify({"jobid":jobid})
#         else:
#             return jsonify({"error":"Error in file upload. Please try again."})

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out! See you soon :)")
    return redirect(url_for('login'))


def check_pid_email(pid, email):
    email = email.replace("eng.ucsd.edu","ucsd.edu")
    if pid in pid_to_email:
        if pid_to_email[pid][0] == email:
            return True
    return False
