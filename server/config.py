from os import environ
from dotenv import load_dotenv
    
load_dotenv()
    
class Config:
        SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'postgresql://maingi:maingi1122@localhost:5432/late_showw_db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY', '9ATallelV47-zLIeRd2_O9ogQ7Z_ZL1fQRB0D46lnWU')  # Replace with a secure key