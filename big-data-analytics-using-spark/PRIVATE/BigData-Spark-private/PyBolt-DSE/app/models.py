from app import db

class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(30))
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    jobs = db.relationship('Job', backref='user', lazy='dynamic')
    grades = db.relationship('Grade', backref='user', lazy='dynamic')


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)  # python 2

    def __repr__(self):
        return '<User %r>' % (self.email)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    homework = db.Column(db.Integer)
    code = db.Column(db.Text)
    timestamp = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'))
    status=db.Column(db.String(40))
    duration=db.Column(db.String(40))
    error=db.Column(db.Text)
    stdout=db.Column(db.Text)
    final=db.Column(db.Boolean, default=False)
    appId = db.Column(db.String(20))

    def __repr__(self):
        return '<Job %r>' % (self.id)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    homework = db.Column(db.Integer)
    job_id = db.Column(db.Integer)
    marks = db.Column(db.String(20))
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'))
    remark = db.Column(db.Text)
    def __repr__(self):
        return '<Grade:%r HW:%r User:%r Job:%r>' % (self.marks, self.homework, self.user_id, self.job_id)
