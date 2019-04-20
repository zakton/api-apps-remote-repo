import os

DEBUG = True
SECRET_KEY = 'rULaRtEob2LECVdssyYKzWDG'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data-dev.sqlite3')

# My addition (zak) ... to be added in production
SQLALCHEMY_TRACK_MODIFICATIONS = False
