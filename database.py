from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://analytics_user:analytics_pass@db/analytics_db"

engine = create_engine(DATABASE_URL, connect_args={"options": "-c client_encoding=utf8"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()