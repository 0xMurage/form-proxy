from sqlalchemy import Column, TIMESTAMP, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Model(Base):
    __abstract__ = True
    created_at = Column('created_at', TIMESTAMP, default=func.now())
