'''
Beinhaltet alle Klassen und Kind-Klassen zu Daten rund um Personen.
'''

import datetime as dt
import itertools

# import kurs_klassen as kk

# TODO: Wolfgang: wie können wir das konsistent machen mit Importen:
# date
# kk.check_age


class Person:
    '''
    Parent Class Person beinhaltet alle Person.
    Child Classes hierzu: Participant, Trainer                                                                       FRAGE!
    '''


    def __init__(self, first_name, last_name, street, house_number, zip_code, city, email, birthdate_year, birthdate_month, birthdate_day, gender):
        '''
        TODO: :param person_id: fortlaufendenden Autowert einfügen
        :param first_name: Vorname (string)
        :param last_name: Nachname (string)
        :param street: Straße (string)
        :param house_number: Hausnummer (integer)
        :param zip_code: PLZ (5-stelliger integer)
        :param city: Ort (string)
        :param email: Email-Adresse (string)
        :param birthdate: Geburtsdatum (aktuell: string) TODO: in der GUI wollen wir 3 konkrete Argumente dd mm yyyy abfragen
        :param gender: Geschlecht: über GUI Auswahl von 3 Geschlechtern möglich
        '''

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.street = street.title()
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city.title()
        self.email = email.lower()
        self.birthdate_year = birthdate_year
        self.birthdate_month = birthdate_month
        self.birthdate_day = birthdate_day
        self.birthdate = dt.date(birthdate_year, birthdate_month, birthdate_day)                # juhuuuu!
        self.gender = gender
        self.age = self.calc_age(self.birthdate)
        self.join_date = dt.date.today()

    def calc_age(self, birthdate):
        today = dt.date.today()
        try:
            birthday = birthdate.replace(year=today.year)
        except ValueError:
            birthday = birthdate.replace(year=today.year,
                                         month=birthdate.month + 1, day=1)

        if birthday > today:
            age_result = today.year - birthdate.year - 1
            return age_result

        else:
            age_result = today.year - birthdate.year
            return age_result

# TODO: Instanz bilden & Alter abfragen

    #def change_join_date(self,new_date):


class Participant(Person):
    '''
    Child Class Participant der Parent Class Person beinhaltet zusätzliche Attribute.
    '''

    def __init__(self, first_name, last_name, street, house_number, zip_code, city, email, birthdate, gender,
                 athleticism, experience_with_ft, payment_form):
        '''
        :param athleticism: How often a person has trained on average within the past 12 months (string, in GUI bestimmte Anzahl an Möglichkeiten)
        :param experience_with_ft: Experience with Functional Training (bool, ja/nein)
        :param payment_form: form of payment (e.g. credit card, debit) (string, in GUI bestimmte Anzahl an Möglichkeiten)
        '''

        super().__init__(first_name, last_name, street, house_number, zip_code, city, email, birthdate, gender)
        self.athleticism = athleticism
        self.experience_with_ft = experience_with_ft
        self.payment_form = payment_form

# TODO: Payment-Form als unabhängige Klasse

class Trainer(Person):
    '''
    Child Class Trainer der Parent Class Person beinhaltet zusätzliche Attribute.
    '''

    def __init__(self, first_name, last_name, street, house_number, zip_code, city, email, birthdate, gender, salary,
                 experience_as_trainer):
        '''
        :param salary: individual salary per hour of trainer (integer)
        :param experience_as_trainer: number of years experience as an athletic trainer (integer)
        '''

        super().__init__(first_name, last_name, street, house_number, zip_code, city, email, birthdate, gender)
        self.salary = salary
        self.experience_as_trainer = experience_as_trainer


class BusinessParticipant(Participant):
    '''
    (Grand-)Child Class BusinessParticipant der Child Class Participant beinhaltet zusätzliche Attribute.
    '''

    def __init__(self, first_name, last_name, street, house_number, zip_code, city, email, birthdate, gender,
                 athleticism, experience_with_ft, payment_form, company_name, coupon_code):
        '''
        :param company_name: name of company that participant works for (string)
        :param coupon_code: coupon code for sports course given to employee by employer (string)
        '''

        super().__init__(first_name, last_name, street, house_number, zip_code, city, email, birthdate, gender,
                         athleticism, experience_with_ft, payment_form)
        self.company_name = company_name
        self.coupon_code = coupon_code
