from tkinter import messagebox

import admin_TableViewApplicationClasses as tvac
import enum as Enum
import personen_instanzen as pi
from personen_klassen import *


# class Person:
#
#     def __init__(self, pre_name, last_name, course_numbers=['']):
#         self.pre_name = pre_name
#         self.last_name = last_name
#         self.course_numbers = list(course_numbers)


class CourseBook(list):

    def __init__(self, courses):
        super(CourseBook, self).__init__(courses)

    def get_main_entry_data(self):
        result = []
        for course in self:
            result.append([course.first_name, course.last_name, course.street, course.house_number, course.zip_code,
                           course.city, course.email, course.birthdate_year, course.birthdate_month, course.birthdate_day, course.gender])
        return result

    def set_main_entry_data(self, course_index, main_entry_edit_data):
        course = self[course_index]
        course.pre_name = main_entry_edit_data[0]
        course.last_name = main_entry_edit_data[1]
        course.course_numbers[0] = main_entry_edit_data[2]

    def add_main_entry_data(self, main_entry_edit_data):
        self.append(Person(main_entry_edit_data[0], main_entry_edit_data[1], main_entry_edit_data[2], main_entry_edit_data[3], main_entry_edit_data[4], main_entry_edit_data[5], main_entry_edit_data[6], int(main_entry_edit_data[7]), int(main_entry_edit_data[8]), int(main_entry_edit_data[9]), main_entry_edit_data[10]))

    def delete_main_entry_index(self, course_index):
        self.pop(course_index)

    def get_course_number_data(self, course_index):
        course = self[course_index]
        result = []
        for course_number in course.course_numbers:
            result.append([course_number])
        return result

    def set_course_number_data(self, course_index, course_number_index, course_number_data):
        course = self[course_index]
        course.course_numbers[course_number_index] = course_number_data

    def add_course_number_data(self, course_index, course_number_data):
        course = self[course_index]
        course.course_numbers.append(course_number_data)

    def delete_course_number_index(self, course_index, course_number_index):
        course = self[course_index]
        course.course_numbers.pop(course_number_index)
        if not len(course.course_numbers):
            course.course_numbers = ['']


class CourseApp(tvac.BaseApplication):

    class ShowType(Enum.Enum):
        CourseBook = 1
        COURSENUMBERSS = 2

    def __init__(self, height, width, course_book):
        self.course_book = course_book
        self.course_index = 0

        self.course_book_label_text = 'Personen-Übersicht'
        self.course_book_columns = ('Vorname', 'Nachname', 'Straße', 'Hausnummer', 'Postleitzahl', 'Ort', 'Email', 'Geburtsjahr', 'Geburtsmonat', 'Geburtstag', 'Geschlecht')
        self.course_book_menu = (('Eintrag', ('Neu', self.new_entry), ('Löschen', self.delete_entry)),
                                ('Anzeigen', ('ReadMe', self.do_show_numbers)))

        self.phone_nummer_columns = ('Nummer',)
        self.course_number_menu = (('Eintrag', ('Neu', self.new_entry), ('Löschen', self.delete_entry)),
                                  ('Anzeigen', ('Phone Book', self.do_show_course_book)))

        self.show_type = CourseApp.ShowType.CourseBook

        super(CourseApp, self).__init__(height, width,
                                        label_text=self.course_book_label_text,
                                        columns=self.course_book_columns,
                                        menu=self.course_book_menu,
                                        data_sequences=self.course_book.get_main_entry_data())

    def do_show_numbers(self, *args):
        messagebox.showinfo('Tadaaaaaaaaaaaaaaaa!', 'Lieber Wolfgang, viele Grüße von Chris, Filip, Hajo und Manuela :-)')

        # self.show_type = CourseApp.ShowType.COURSENUMBERSS
        #
        # self.course_index = self.tableView.get_selected_index()
        #
        # course = self.course_book[self.course_index]
        # self.create_view(label_text='Telefonnummer von ' + course.pre_name + ' ' + course.last_name,
        #                  columns=self.phone_nummer_columns,
        #                  menu=self.course_number_menu,
        #                  data_sequences=self.course_book.get_course_number_data(self.course_index))

    def do_show_course_book(self, *args):
        self.show_type = CourseApp.ShowType.CourseBook

        self.create_view(label_text=self.course_book_label_text,
                         columns=self.course_book_columns,
                         menu=self.course_book_menu,
                         data_sequences=self.course_book.get_main_entry_data(),
                         index_to_select=self.course_index)

    def new_entry(self, *args):
        new_entry_data = super(CourseApp, self).new_entry()
        if new_entry_data is not None:
            if self.show_type == CourseApp.ShowType.CourseBook:
                self.course_book.add_main_entry_data(new_entry_data)
            elif self.show_type == CourseApp.ShowType.COURSENUMBERSS:
                self.course_book.add_course_number_data(self.course_index, new_entry_data)

    def delete_entry(self):
        deleted_index = super(CourseApp, self).delete_entry()
        if deleted_index is not None:
            if self.show_type == CourseApp.ShowType.CourseBook:
                self.course_book.delete_main_entry_index(deleted_index)
            elif self.show_type == CourseApp.ShowType.COURSENUMBERSS:
                self.course_book.delete_course_number_index(self.course_index, deleted_index)

    def edit_action(self, *args):
        edit_entry_data = super(CourseApp, self).edit_action()
        if edit_entry_data is not None:
            if self.show_type == CourseApp.ShowType.CourseBook:
                self.course_index = self.tableView.get_selected_index()
                self.course_book.set_main_entry_data(self.course_index, edit_entry_data)
            elif self.show_type == CourseApp.ShowType.COURSENUMBERSS:
                course_number_index = self.tableView.get_selected_index()
                self.course_book.set_course_number_data(self.course_index, course_number_index, edit_entry_data)

    def do_second(self, *args):
        print('mache irgendwas')



if __name__ == '__main__':

    app = CourseApp(400, 400, CourseBook((
        Person('Filip', 'Berus', 'Hauptstraße', '1b', '10245', 'Berlin', 'filip@gmail.com', 1982, 4, 2, 'm'),
        Person('Hajo', 'Kiener', 'Breite Straße', '20a', '22159', 'Hamburg', 'hajo@gmail.com', 1965, 3, 2,'m'),
        Person('Chris', 'Koch', 'Lechhauser Str.', '50', '86167', 'Augsburg', 'chris@gmail.com', 1986, 4, 11,'m'),
        Person('Manuela', 'Hebel', 'Maxstraße', '5', '86159', 'Augsburg', 'manuela@gmail.com', 1985, 12, 13,'w'),
        pi.person005,
        pi.person006,
        pi.person007,
        pi.person008,
        pi.person009,
        pi.person010,
        pi.person011,
        pi.person012
    )))

    app.run()
