import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
UPLOAD_FOLDER = os.path.join(basedir, 'codes')

HOMEWORK = 4

SPARK_UPLOAD_API = "http://52.87.103.168/submit"
SPARK_QUERY_API = "http://52.87.103.168/apps"

ADMINS = frozenset(['saurabh3949@gmail.com'])
SECRET_KEY = 'bhahblahblah'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

STUDENTS_LIST = os.path.join(basedir, 'students.csv')

DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}
