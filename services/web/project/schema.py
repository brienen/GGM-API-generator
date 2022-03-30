
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from project.models import school as schoolModel
from project.models import startkwalificatie as startkwalificatieModel
from project.models import uitschrijving as uitschrijvingModel
from project.models import inschrijving as inschrijvingModel
from project.models import leerjaar as leerjaarModel
from project.models import leerling as leerlingModel
from project.models import locatie as locatieModel
from project.models import loopbaanstap as loopbaanstapModel
from project.models import onderwijsloopbaan as onderwijsloopbaanModel
from project.models import onderwijsniveau as onderwijsniveauModel
from project.models import onderwijssoort as onderwijssoortModel
from project.models import ouder_of_verzorger as ouder_of_verzorgerModel
from project.filters import MyFilterableConnectionField

    
class school(SQLAlchemyObjectType):
    class Meta:
        model = schoolModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class startkwalificatie(SQLAlchemyObjectType):
    class Meta:
        model = startkwalificatieModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class uitschrijving(SQLAlchemyObjectType):
    class Meta:
        model = uitschrijvingModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class inschrijving(SQLAlchemyObjectType):
    class Meta:
        model = inschrijvingModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class leerjaar(SQLAlchemyObjectType):
    class Meta:
        model = leerjaarModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class leerling(SQLAlchemyObjectType):
    class Meta:
        model = leerlingModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class locatie(SQLAlchemyObjectType):
    class Meta:
        model = locatieModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class loopbaanstap(SQLAlchemyObjectType):
    class Meta:
        model = loopbaanstapModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class onderwijsloopbaan(SQLAlchemyObjectType):
    class Meta:
        model = onderwijsloopbaanModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class onderwijsniveau(SQLAlchemyObjectType):
    class Meta:
        model = onderwijsniveauModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class onderwijssoort(SQLAlchemyObjectType):
    class Meta:
        model = onderwijssoortModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
            
class ouder_of_verzorger(SQLAlchemyObjectType):
    class Meta:
        model = ouder_of_verzorgerModel
        interfaces = (relay.Node, )
        connection_field_factory = MyFilterableConnectionField.factory
        

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    school = MyFilterableConnectionField(school.connection, sort=school.sort_argument())
    startkwalificatie = MyFilterableConnectionField(startkwalificatie.connection, sort=startkwalificatie.sort_argument())
    uitschrijving = MyFilterableConnectionField(uitschrijving.connection, sort=uitschrijving.sort_argument())
    inschrijving = MyFilterableConnectionField(inschrijving.connection, sort=inschrijving.sort_argument())
    leerjaar = MyFilterableConnectionField(leerjaar.connection, sort=leerjaar.sort_argument())
    leerling = MyFilterableConnectionField(leerling.connection, sort=leerling.sort_argument())
    locatie = MyFilterableConnectionField(locatie.connection, sort=locatie.sort_argument())
    loopbaanstap = MyFilterableConnectionField(loopbaanstap.connection, sort=loopbaanstap.sort_argument())
    onderwijsloopbaan = MyFilterableConnectionField(onderwijsloopbaan.connection, sort=onderwijsloopbaan.sort_argument())
    onderwijsniveau = MyFilterableConnectionField(onderwijsniveau.connection, sort=onderwijsniveau.sort_argument())
    onderwijssoort = MyFilterableConnectionField(onderwijssoort.connection, sort=onderwijssoort.sort_argument())
    ouder_of_verzorger = MyFilterableConnectionField(ouder_of_verzorger.connection, sort=ouder_of_verzorger.sort_argument())


schema = graphene.Schema(query=Query)

