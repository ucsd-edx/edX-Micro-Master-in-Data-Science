from app import db, models
import config
import csv

HW = 1
GRADEFILE = "HW1_graded_dse.csv"

with open('../Students/HomeworkSubmissions/' + GRADEFILE, 'rb') as f:
    try:
        reader = csv.DictReader(f)
    except Exception, e:
        print str(e)
    for row in reader:
        grade = models.Grade(homework = HW,
                             job_id = int(row['jobid']),
                             marks = row['grade'],
                             user_id = row['pid'],
                             remark = row['remarks'])
        db.session.add(grade)
    db.session.commit()
    print "All grades added successfully!"
