'''
Beinhaltet alle Klassen und Kind-Klassen zu Daten rund um die Sportkurse.
'''


class Course:
    '''
    Parent Class Course beinhaltet alle allgemeinen Attribute zu Kursen.
    '''

    def __init__(self, course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list = ['']):
        '''
        :param course_id: unique course number (integer)
        :param start_date: start date of course (date)
        :param duration: duration of course in weeks (integer)
        :param max_participants: minimum number of participants for course to start
        :param max_participants: maximum number of participants allowed
        :param trainer_name: name of trainer in charge
        :param participants_list: list of all participants registered for this course
        '''

        self.course_id = course_id
        self.start_date = start_date
        self.duration = duration
        self.min_participants = min_participants
        self.max_participants = max_participants
        self.trainer_name = trainer_name
        self.participants_list = participants_list
 #       self.end_date = self.calc_end_date()


      #  def calc_end_date():
        # TODO: calc_end_date

       # def add_participant():
       #     participants_list.append()
        # TODO: add_participant


class KinderZimmerSport(Course):
    '''
    Child Class KinderZimmerSport beinhaltet zusätzliche Attribute, die nur für KinderZimmerSport gelten.
    '''

    def __init__(self, course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list):
        '''
        no additional parameters
        # TODO: Wolfgang: gehören hier auch untenstehenden Attribute rein.
        '''

        super().__init__(course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list)
        self.max_age = 16
        self.course_type = 'KinderZimmerSport'

        ### TODO: check_age


    def check_age(self, person):
        if person.age <= self.max_age:
           print('Juhu, du darfst teilnehmen!')
        else:
           print('Du bist leider zu alt!')



# kinderzimmersport_1 = KinderZimmerSport(1, 'Oktober', 8, 6, 12, 'Andy', [], 16)
#
# KinderZimmerSport.check_age(kinderzimmersport_1)


class WohnZimmerSport(Course):
    '''
    Child Class WohnZimmerSport beinhaltet zusätzliche Attribute, die nur für WohnZimmerSport gelten.
    '''

    def __init__(self, course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list, utilities):
        '''
        :param utilities: utilitites neccessary for course participation
        '''

        super().__init__(course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list)
        self.utilities = utilities
        self.course_type = 'WohnZimmerSport'


class HotelZimmerSport(Course):
    '''
    Child Class HotelZimmerSport beinhaltet zusätzliche Attribute, die nur für HotelZimmerSport gelten. Aktuell beinhaltet
    die Child Class HotelZimmerSport noch keine individuellen Attribute, wurde jedoch gebildet, um später weiter angepasst zu werden.
    TODO: add attributes
    '''

    def __init__(self, course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list):
        '''
        aktuell keine zusätzlichen Parameter
        '''

        super().__init__(course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list)
        self.course_type = 'HotelZimmerSport'


class BueroZimmerSport(Course):
    '''
    Child Class BüroZimmerSport beinhaltet zusätzliche Attribute, die nur für HotelZimmerSport gelten. Aktuell beinhaltet
    die Child Class HotelZimmerSport noch keine individuellen Attribute, wurde jedoch gebildet, um später weiter angepasst zu werden.
    TODO: add attributes
    '''

    def __init__(self, course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list):
        '''
        aktuell keine zusätzlichen Parameter
        '''

        super().__init__(course_id, start_date, duration, min_participants, max_participants, trainer_name, participants_list)
        self.course_type = 'BüroZimmerSport'