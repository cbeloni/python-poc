from dotenv import load_dotenv
import os
user = os.environ['USER']
print(user)

###https://www.twilio.com/blog/environment-variables-python

#setando valor default
database_url = os.environ.get('DATABASE_URL', 'sqlite:///:memory:')
print(database_url)

#DATABASE_URL=ORACLE python config_enviroment.py

load_dotenv("test.env")
private_key = os.environ.get('PRIVATE_KEY', 'NAO_CARREGADO')
print(f"private_key: {private_key}")
