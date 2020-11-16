import os
class Config:
    SECRET_KEY = 'c8eef30eb9f4b4e0608bd7fca6e18c5d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('USER_EMAIL')
    MAIL_PASSWORD = os.environ.get('USER_PASS')