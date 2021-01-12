import admin_TableViewApplicationClasses as tvac
import enum as Enum
import personen_instanzen as pi
from personen_klassen import *
import kurs_instanzen as ki
from kurs_klassen import *


# class course:
#
#     def __init__(self, pre_name, last_name, participants_list=['']):
#         self.pre_name = pre_name
#         self.last_name = last_name
#         self.participants_list = list(participants_list)


class CourseBook(list):

    def __init__(self, courses):
        super(CourseBook, self).__init__(courses)

    def get_main_entry_data(self):
        result = []
        for course in self:
            result.append([course.course_id, course.start_date, course.duration, course.min_participants, course.max_participants,
                           course.trainer_name, course.participants_list[0]])
        return result

    def set_main_entry_data(self, course_index, main_entry_edit_data):
        course = self[course_index]
        course.pre_name = main_entry_edit_data[0]
        course.last_name = main_entry_edit_data[1]
        course.participants_list[0] = main_entry_edit_data[2]

    def add_main_entry_data(self, main_entry_edit_data):
        self.append(Course(main_entry_edit_data[0], main_entry_edit_data[1], main_entry_edit_data[2], main_entry_edit_data[3], main_entry_edit_data[4], main_entry_edit_data[5], [main_entry_edit_data[6]]))

    def delete_main_entry_index(self, course_index):
        self.pop(course_index)

    def get_course_number_data(self, course_index):
        course = self[course_index]
        result = []
        for course_number in course.participants_list:
            result.append([course_number])
        return result

    def set_course_number_data(self, course_index, course_number_index, course_number_data):
        course = self[course_index]
        course.participants_list[course_number_index] = course_number_data

    def add_course_number_data(self, course_index, course_number_data):
        course = self[course_index]
        course.participants_list.append(course_number_data)

    def delete_course_number_index(self, course_index, course_number_index):
        course = self[course_index]
        course.participants_list.pop(course_number_index)
        if not len(course.participants_list):
            course.participants_list = ['']


class CourseApp(tvac.BaseApplication):

    class ShowType(Enum.Enum):
        CourseBook = 1
        COURSENUMBERS = 2

    def __init__(self, height, width, course_book):
        self.course_book = course_book
        self.course_index = 0

        self.course_book_label_text = 'Kurs-Übersicht'
        self.course_book_columns = ('Kursnummer', 'Starttermin', 'Dauer', 'min. Teilnehmerzahl', 'max. Teilnehmerzahl', 'Trainername', 'Teilnehmerliste')
        self.course_book_menu = (('Eintrag', ('Neu', self.new_entry), ('Löschen', self.delete_entry)),
                                ('Anzeigen', ('Teilnehmerliste', self.do_show_numbers)))

        self.phone_nummer_columns = ('Teilnehmer',)
        self.course_number_menu = (('Eintrag', ('Neu', self.new_entry), ('Löschen', self.delete_entry)),
                                  ('Anzeigen', ('Kursliste', self.do_show_course_book)))

        self.show_type = CourseApp.ShowType.CourseBook

        super(CourseApp, self).__init__(height, width,
                                        label_text=self.course_book_label_text,
                                        columns=self.course_book_columns,
                                        menu=self.course_book_menu,
                                        data_sequences=self.course_book.get_main_entry_data())

    def do_show_numbers(self, *args):
        self.show_type = CourseApp.ShowType.COURSENUMBERS

        self.course_index = self.tableView.get_selected_index()

        course = self.course_book[self.course_index]
        self.create_view(label_text='Teilnehmerliste von ' + course.course_id,
                         columns=self.phone_nummer_columns,
                         menu=self.course_number_menu,
                         data_sequences=self.course_book.get_course_number_data(self.course_index))

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
            elif self.show_type == CourseApp.ShowType.COURSENUMBERS:
                self.course_book.add_course_number_data(self.course_index, new_entry_data)

    def delete_entry(self):
        deleted_index = super(CourseApp, self).delete_entry()
        if deleted_index is not None:
            if self.show_type == CourseApp.ShowType.CourseBook:
                self.course_book.delete_main_entry_index(deleted_index)
            elif self.show_type == CourseApp.ShowType.COURSENUMBERS:
                self.course_book.delete_course_number_index(self.course_index, deleted_index)

    def edit_action(self, *args):
        edit_entry_data = super(CourseApp, self).edit_action()
        if edit_entry_data is not None:
            if self.show_type == CourseApp.ShowType.CourseBook:
                self.course_index = self.tableView.get_selected_index()
                self.course_book.set_main_entry_data(self.course_index, edit_entry_data)
            elif self.show_type == CourseApp.ShowType.COURSENUMBERS:
                course_number_index = self.tableView.get_selected_index()
                self.course_book.set_course_number_data(self.course_index, course_number_index, edit_entry_data)

    def do_second(self, *args):
        print('mache irgendwas')



if __name__ == '__main__':

    app = CourseApp(400, 400, CourseBook((
        ki.wohnzimmersport01,
        ki.wohnzimmersport02,
        ki.wohnzimmersport03,
        ki.wohnzimmersport04,
        ki.buerozimmersport01,
        ki.buerozimmersport02,
        ki.buerozimmersport03,
        ki.buerozimmersport04,
        ki.hotelzimmersport01,
        ki.hotelzimmersport02,
        ki.hotelzimmersport03,
        ki.hotelzimmersport04,
        ki.kinderzimmersport01,
        ki.kinderzimmersport02,
        ki.kinderzimmersport03,
        ki.kinderzimmersport04
    )))

    app.run()
