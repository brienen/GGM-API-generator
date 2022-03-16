from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from faker import Faker
import random
import pandas as pd


import logging
logger = logging.getLogger()


engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
import project.models as models


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    try: 
        logger.info("Seeding database with fake onderwijs data")
        # import all modules here that might define models so that
        # they will be registered properly on the metadata.  Otherwise
        # you will have to import them first before calling init_db()
        from project.models import leerjaar, leerling, school, onderwijssoort, inschrijving

        fake = Faker(['nl_NL', 'no_NO'])
        # Create the fixtures
        

        jaar = leerjaar(startjaar="2000", eindjaar="2001")
        db_session.add(jaar)

        '''
        naam = Column(String)
        onderwijssoort = relationship("onderwijssoort", secondary=school_onderwijssoort_table, backref="school")
        '''
        school1 = school(naam='Piet Hein School')
        db_session.add(school1)
        school2 = school(naam='School met de Bijbel')
        db_session.add(school2)
        school3 = school(naam='Koning Karel College')
        db_session.add(school3)
        '''
        omschrijving = Column(String)
        onderwijstype = Column(String)
        '''
        for soort in ["VMBO-T", 'VMBO-K', "VMBO-B", "HAVO", "VWO"]:
            os = onderwijssoort(omschrijving=soort, onderwijstype=soort)
            school1.onderwijssoort.append(os)
            school2.onderwijssoort.append(os)
            if not "-" in soort: 
                school3.onderwijssoort.append(os)
            db_session.add(os)
        
        for _ in range(300):
            l = leerling(voornaam=fake.first_name(), achternaam=fake.last_name(), kwetsbare_jongere=True if random.randint(0,5) < 2 else False, adres=fake.address())
            sch = [school1, school2, school3][fake.random_int(min=0, max=2)]
            os = sch.onderwijssoort[fake.random_int(min=0, max=len(sch.onderwijssoort)-1)]

            ins = inschrijving(datum=fake.date_between(start_date='-20y', end_date='today'), school=sch, leerling=l, onderwijssoort=os)
            db_session.add(l)
            db_session.add(ins)


        db_session.commit()
    except Exception as err:
        logger.warn(f"Error while loading onderwijs data, are onderwijs class available? Message {err}")


    try:
        logger.info("Seeding database with monument data from Delft")

        from project.models import beschermde_status

        df = pd.read_excel("Monumenten.xlsx", header=1)
        for index, row in df.iterrows():
            b = beschermde_status(naam=row['OBJECTNAAM'], omschrijving=row['TOOLTIP'], type=row['TYPE'] )
            db_session.add(b)
            print(row['OBJECTNAAM'], row['OPMERKING'])

        db_session.commit()
    except Exception as err:
        logger.warn(f"Error while loading monument data, are monument classes available? Message {err}")



    
