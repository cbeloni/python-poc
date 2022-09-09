from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData
from faker import Faker
import random

engine = create_engine("mysql+pymysql://root:some_pass@192.168.0.14/pydb?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    sobrenome = Column(String(50))
    idade = Column(Integer)

if __name__ == '__main__':
    metadata_obj = MetaData()
    tbl = Table("user",metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("nome", String(50)),
        Column("sobrenome", String(50)),
        Column("idade", Integer)
    )
    #Base.metadata.drop_all(bind=engine, tables=[tbl])
    #Base.metadata.create_all(bind=engine, tables=[tbl])
    #Base.metadata.create_all(bind=engine)

    
    #User().__table__.create(engine)
    
    #phone_number, address,  company, country, date, date_between, email, 
    #
    
    faker = Faker()
    for item in range(10):
        nome = faker.name().split()
        usuario: User = User(nome=nome[0], sobrenome=' '.join(nome[1:]),idade=random.randrange(18, 101))
        session.add_all([usuario])
        session.commit()
    
    retorno_usuario = session.query(User).filter_by(nome="caue").all()
    print(retorno_usuario)
    

    

    
