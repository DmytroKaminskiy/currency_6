from sqlalchemy import create_engine, MetaData
meta = MetaData()

engine = create_engine('sqlite:///college.db', echo = True)
