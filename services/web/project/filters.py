
from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from project.models import school, startkwalificatie, uitschrijving, inschrijving, leerjaar, leerling, locatie, loopbaanstap, onderwijsloopbaan, onderwijsniveau, onderwijssoort, ouder_of_verzorger


class schoolFilter(FilterSet):
    class Meta:
        model = school
        fields = {
            "naam": [...],
            "id": [...] }

class startkwalificatieFilter(FilterSet):
    class Meta:
        model = startkwalificatie
        fields = {
            "datumbehaald": [...],
            "id": [...] }

class uitschrijvingFilter(FilterSet):
    class Meta:
        model = uitschrijving
        fields = {
            "datum": [...],
            "diplomabehaald": [...],
            "id": [...] }

class inschrijvingFilter(FilterSet):
    class Meta:
        model = inschrijving
        fields = {
            "datum": [...],
            "id": [...] }

class leerjaarFilter(FilterSet):
    class Meta:
        model = leerjaar
        fields = {
            "eindjaar": [...],
            "startjaar": [...],
            "id": [...] }

class leerlingFilter(FilterSet):
    class Meta:
        model = leerling
        fields = {
            "kwetsbare_jongere": [...],
            "voornaam": [...],
            "achternaam": [...],
            "adres": [...],
            "leeftijd": [...],
            "id": [...] }

class locatieFilter(FilterSet):
    class Meta:
        model = locatie
        fields = {
            "adres": [...],
            "id": [...] }

class loopbaanstapFilter(FilterSet):
    class Meta:
        model = loopbaanstap
        fields = {
            "klas": [...],
            "onderwijstype": [...],
            "schooljaar": [...],
            "id": [...] }

class onderwijsloopbaanFilter(FilterSet):
    class Meta:
        model = onderwijsloopbaan
        fields = {
            "id": [...] }

class onderwijsniveauFilter(FilterSet):
    class Meta:
        model = onderwijsniveau
        fields = {
            "id": [...] }

class onderwijssoortFilter(FilterSet):
    class Meta:
        model = onderwijssoort
        fields = {
            "omschrijving": [...],
            "onderwijstype": [...],
            "id": [...] }

class ouder_of_verzorgerFilter(FilterSet):
    class Meta:
        model = ouder_of_verzorger
        fields = {
            "id": [...] }


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {school: schoolFilter(), startkwalificatie: startkwalificatieFilter(), uitschrijving: uitschrijvingFilter(), inschrijving: inschrijvingFilter(), leerjaar: leerjaarFilter(), leerling: leerlingFilter(), locatie: locatieFilter(), loopbaanstap: loopbaanstapFilter(), onderwijsloopbaan: onderwijsloopbaanFilter(), onderwijsniveau: onderwijsniveauFilter(), onderwijssoort: onderwijssoortFilter(), ouder_of_verzorger: ouder_of_verzorgerFilter()}

