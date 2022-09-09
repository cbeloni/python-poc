from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData

engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'


if __name__ == '__main__':
    users: list = [User()]
    metadata_obj = MetaData()
    tbl = Table("foo",metadata_obj,
        Column("bar",String),
        Column("nome", String),
        Column("sobrenome", String),
        Column("idade", Integer)
    )
    Base.metadata.drop_all(bind=engine)
    #Base.metadata.create_all(bind=engine, tables=[tbl])
    Base.metadata.create_all(bind=engine)
