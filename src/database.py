from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config

config = Config(".env")
USERNAME = config('MYSQL_USER', cast=str)
print('Username', USERNAME)
PSWD = config('MYSQL_PASSWORD', cast=str)
DB = config('MYSQL_DATABASE', cast=str)
DB_URL = f'mysql+pymysql://{USERNAME}:{PSWD}@db:3306/{DB}' # connect string to mysql
print('url is ', DB_URL)
engine = create_engine(
    DB_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()