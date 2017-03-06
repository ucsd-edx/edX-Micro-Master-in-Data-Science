from app import db, models
jobs = models.Job.query.filter(models.Job.status=="final").group_by(models.Job.user_id).all()
pids = [str(job.user_id) for job in jobs]

cleared = []
with open("cleared.txt","rb") as l:
    f = l.read()
    cleared = f.split("\r")

waitlist = []
with open("waitlist.txt","rb") as l:
    f = l.read()
    waitlist = f.split("\r")


cleared_submitted = sum([1 for i in cleared if i in pids])
waitlist_submitted = sum([1 for i in waitlist if i in pids])
print "Students who have submitted hw1: "
print cleared_submitted, waitlist_submitted



jobs = models.Job.query.group_by(models.Job.user_id).all()
pids = [str(job.user_id) for job in jobs]
no_cl = sum([1 for i in cleared if i not in pids])
no_wl = sum([1 for i in waitlist if i not in pids])
print "Students with no submissions at all"
print no_cl, no_wl
