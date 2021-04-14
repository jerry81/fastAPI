from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config

config = Config(".env")
USERNAME = config('MYSQL_ROOT_USER', cast=str)
PSWD = config('MYSQL_ROOT_PASSWORD', cast=str)
DB = config('MYSQL_DATABASE', cast=str)
print ('DB is ', DB)
SERVICE_NAME = "db" if DB == "gs" else "dbtest"
DB_URL = f'mysql+pymysql://{USERNAME}:{PSWD}@{SERVICE_NAME}:3306/{DB}' # connect string to mysql

engine = create_engine(
    DB_URL, pool_pre_ping=True
)
print('engine is ', engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('sesson lcao', SessionLocal)
Base = declarative_base()
print('base created')