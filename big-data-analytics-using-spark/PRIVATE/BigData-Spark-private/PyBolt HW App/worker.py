from app import db, models
import time
import requests
import config

while True:
	pending_jobs=models.Job.query.filter(models.Job.status=="Pending").all()
	running_jobs=models.Job.query.filter(models.Job.status=="running").all()
	app_ids=''
	for job in pending_jobs:
		if job.appId :
			app_ids += job.appId +','
	for job in running_jobs:
		if job.appId:
			app_ids += job.appId +','

	if app_ids != '':
		app_ids = app_ids[:-1]
		res = requests.post(config.SPARK_QUERY_API, data={'app_ids':app_ids})
		if res.status_code == requests.codes.ok:
			job_array=res.json()
			# print job_array
			for job in job_array:
				appId=job['appId']
				j=models.Job.query.filter(models.Job.appId==appId).first()
				if j:
					if "status" in job:
						if job['status']=='running' or job['status']=='compiling':
							j.status='running'
						elif job['status']=='pending':
							j.status='Pending'
						else:
							print "Updating status of:", appId
							j.status=job['status']
							j.error=job['stderr']
							j.stdout=job['stdout']
							if "duration" in job:
								j.duration = job['duration']
			db.session.commit()
	time.sleep(2)

