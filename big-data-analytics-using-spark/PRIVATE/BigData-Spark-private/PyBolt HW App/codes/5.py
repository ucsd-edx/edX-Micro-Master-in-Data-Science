from app import db, models

u = models.User(nickname='Saurabh', email='sag043@ucsd.edu',
                id="admin",password="admin")
db.session.add(u)
db.session.commit()