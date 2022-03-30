
from project.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Boolean, Date, Enum, Table
from sqlalchemy.orm import backref, relationship
import enum



class onderwijstypeEnum(enum.Enum):
    Vmbo_T = "Vmbo_T"
    Vmbo_K = "Vmbo_K"
    Vmbo_B = "Vmbo_B"
    Havo = "Havo"
    Vwo = "Vwo"

        


school_onderwijssoort_table = Table("school_onderwijssoort_table", Base.metadata,
    Column("school_id", ForeignKey("school.id", deferrable=True), primary_key=True),
    Column("onderwijssoort_id", ForeignKey("onderwijssoort.id", deferrable=True), primary_key=True)
)
school_onderwijsloopbaan_table = Table("school_onderwijsloopbaan_table", Base.metadata,
    Column("school_id", ForeignKey("school.id", deferrable=True), primary_key=True),
    Column("onderwijsloopbaan_id", ForeignKey("onderwijsloopbaan.id", deferrable=True), primary_key=True)
)


class school(Base):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True)  
    naam = Column(String)

    onderwijssoort = relationship("onderwijssoort", secondary=school_onderwijssoort_table, backref="school")
    onderwijsloopbaan = relationship("onderwijsloopbaan", secondary=school_onderwijsloopbaan_table, backref="school")

        
class startkwalificatie(Base):
    __tablename__ = "startkwalificatie"
    id = Column(Integer, primary_key=True)  
    datumbehaald = Column(Date)


        
class uitschrijving(Base):
    __tablename__ = "uitschrijving"
    id = Column(Integer, primary_key=True)  
    datum = Column(Date)
    diplomabehaald = Column(Boolean)

    schoolID = Column(ForeignKey("school.id", deferrable=True), index=True, nullable=False)
    school = relationship("school", backref="uitschrijving")
    leerlingID = Column(ForeignKey("leerling.id", deferrable=True), index=True, nullable=False)
    leerling = relationship("leerling", backref="uitschrijving")

        
class inschrijving(Base):
    __tablename__ = "inschrijving"
    id = Column(Integer, primary_key=True)  
    datum = Column(Date)

    onderwijssoortID = Column(ForeignKey("onderwijssoort.id", deferrable=True), index=True)
    onderwijssoort = relationship("onderwijssoort", backref="inschrijving")
    schoolID = Column(ForeignKey("school.id", deferrable=True), index=True, nullable=False)
    school = relationship("school", backref="inschrijving")
    leerlingID = Column(ForeignKey("leerling.id", deferrable=True), index=True, nullable=False)
    leerling = relationship("leerling", backref="inschrijving")

        
class leerjaar(Base):
    __tablename__ = "leerjaar"
    id = Column(Integer, primary_key=True)  
    eindjaar = Column(Integer)
    startjaar = Column(Integer)


        
class leerling(Base):
    __tablename__ = "leerling"
    id = Column(Integer, primary_key=True)  
    kwetsbare_jongere = Column(Boolean)
    voornaam = Column(String)
    achternaam = Column(String)
    adres = Column(String)
    leeftijd = Column(Integer)
    geslacht = Column(String)

    startkwalificatieID = Column(ForeignKey("startkwalificatie.id", deferrable=True), index=True)
    startkwalificatie = relationship("startkwalificatie", backref="leerling")

        
class locatie(Base):
    __tablename__ = "locatie"
    id = Column(Integer, primary_key=True)  
    adres = Column(String)

    schoolID = Column(ForeignKey("school.id", deferrable=True), index=True)
    school = relationship("school", backref="locatie")

        
class loopbaanstap(Base):
    __tablename__ = "loopbaanstap"
    id = Column(Integer, primary_key=True)  
    klas = Column(Integer)
    onderwijstype = Column(String)
    schooljaar = Column(String)


        
class onderwijsloopbaan(Base):
    __tablename__ = "onderwijsloopbaan"
    id = Column(Integer, primary_key=True)  

    leerlingID = Column(ForeignKey("leerling.id", deferrable=True), index=True, nullable=False)
    leerling = relationship("leerling", backref="onderwijsloopbaan")

        
class onderwijsniveau(Base):
    __tablename__ = "onderwijsniveau"
    id = Column(Integer, primary_key=True)  


        
class onderwijssoort(Base):
    __tablename__ = "onderwijssoort"
    id = Column(Integer, primary_key=True)  
    omschrijving = Column(String)
    onderwijstype = Column(String)


        
class ouder_of_verzorger(Base):
    __tablename__ = "ouder_of_verzorger"
    id = Column(Integer, primary_key=True)  


        
