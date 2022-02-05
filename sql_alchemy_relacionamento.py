from cmath import phase
from pymysql import OperationalError
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData
from dataclasses import dataclass

def conn_mysql():
    engine = create_engine("mysql+pymysql://root:some_pass@192.168.0.14:3306/classicmodels", echo=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    return declarative_base(), session, engine
    
def conn_sqlite():
    engine = create_engine('sqlite:///:memory:', echo=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    Base =  declarative_base()    
    return Base, session, engine
    
try:    
    Base, session, engine = conn_mysql()
except Exception as e:
    print("Erro ao conectar, utilizando banco em memória")
    print(e)
    Base, session, engine = conn_sqlite()
        
@dataclass(init=True)
class Employee(Base):
    __tablename__ = 'employees'

    employee_number:int = Column('employeeNumber', Integer, primary_key=True)
    first_name:str = Column('firstName', String(50))
    last_name:str = Column('lastName', String(50))
    email:str = Column('email', String(100))
    office_code = Column('officeCode', Integer, ForeignKey('offices.officeCode'))
    office = relationship("Office")
    
@dataclass(init=True)
class Office(Base):
    __tablename__ = 'offices'
    
    office_code:int = Column('officeCode', Integer, primary_key=True)
    address_line1:str = Column('addressLine1', String(50))
    state:str = Column('state', String(50))
    phone:str = Column('phone', String(50))
    city:str = Column('city', String(50))    

if __name__ == '__main__':
    if session.bind.name == 'sqlite':
        Base.metadata.create_all(bind=engine)
        office = Office(office_code = "1", address_line1="rua sete", state="sp", phone="119999444443", city="santo andré")        
        session.add_all([office])        
        
        employee = Employee(first_name="Leslie", last_name = "Nilson", email = "leslie@mail.com", office_code  = 1)
        session.add_all([employee])
    
    employees = session.query(Employee).filter(Employee.first_name == "Leslie").all()
    
    if employees:
        print("--------------------employees--------------------")
        print ("Len: " +  str(len(employees)) + " - " +  str(employees[0]))
        print (employees[0].office)
        
        print("--------------------office--------------------")
        office = session.query(Office).filter(Office.office_code == "1").one()    
        print(office)
