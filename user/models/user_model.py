from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = 'mysql+pymysql://root:khush952004@localhost/ONLINE_EXAM_SYSTEM'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Reflect the existing tables
Base = automap_base() #base class that will be used to automatically map classes to tables in the database.
Base.prepare(engine, reflect=True) #The reflect=True argument tells SQLAlchemy to inspect the database and load all table definitions.

# Map to the existing tables
User = Base.classes.user
Student = Base.classes.student

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


    