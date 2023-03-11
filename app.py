from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select
from decouple import config



## Create SQL Table inside the database that we define
## This is one table
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

## Now lets create rows in the table
hero1 = Hero(name="Ironman", secret_name="Tony Strac")
hero2 = Hero(name="Spider-man", secret_name="Peter Parker")
hero3 = Hero(name="Dr Strange", secret_name="Stphen Strange")

engine = create_engine(config('DATABASE_URL'))

SQLModel.metadata.create_all(engine)


## Write the data to database
with Session(engine) as session:
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()

## Read from Database
with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Dr Strange")
    hero = session.exec(statement).first()
    print(hero)

