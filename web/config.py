import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="mooc3-ptg-sv.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="sa@mooc3-ptg-sv" #TODO: Update value
    POSTGRES_PW="Aa@12345678"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://svbus-mooc3-namspace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=MTcxOSinxynP53rulrwgd+iozr0IQWOjCgCBtzPduXw=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='queue-mooc3'
    ADMIN_EMAIL_ADDRESS: 'mr0phong0dh@gmai.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False