import os 


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///workessentials.db'
    MAIL_SERVER = 'smtpout.secureserver.net'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'jerry@workessentials.info'
    MAIL_PASSWORD = 'Swordfish2001'
    # Environment Variables Examples = os.environ.get('VariableName')