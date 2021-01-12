from tkinter import messagebox

import admin_TableViewApplicationClasses as tvac
import enum as Enum
import personen_instanzen as pi
from personen_klassen import *


# class Person:
#
#     def __init__(self, pre_name, last_name, phone_numbers=['']):
#         self.pre_name = pre_name
#         self.last_name = last_name
#         self.phone_numbers = list(phone_numbers)


class PhoneBook(list):

    def __init__(self, persons):
        super(PhoneBook, self).__init__(persons)

    def get_main_entry_data(self):
        result = []
        for person in self:
            result.append([person.first_name, person.last_name, person.street, person.house_number, person.zip_code,
                           person.city, person.email, person.birthdate_year, person.birthdate_month,
                           person.birthdate_day, person.gender])
        return result

    def set_main_entry_data(self, person_index, main_entry_edit_data):
        person = self[person_index]
        person.pre_name = main_entry_edit_data[0]
        person.last_name = main_entry_edit_data[1]
        person.phone_numbers[0] = main_entry_edit_data[2]

    def add_main_entry_data(self, main_entry_edit_data):
        self.append(Person(main_entry_edit_data[0], main_entry_edit_data[1], [main_entry_edit_data[2]]))

    def delete_main_entry_index(self, person_index):
        self.pop(person_index)

    def get_phone_number_data(self, person_index):
        person = self[person_index]
        result = []
        for phone_number in person.phone_numbers:
            result.append([phone_number])
        return result

    def set_phone_number_data(self, person_index, phone_number_index, phone_number_data):
        person = self[person_index]
        person.phone_numbers[phone_number_index] = phone_number_data

    def add_phone_number_data(self, person_index, phone_number_data):
        person = self[person_index]
        person.phone_numbers.append(phone_number_data)

    def delete_phone_number_index(self, person_index, phone_number_index):
        person = self[person_index]
        person.phone_numbers.pop(phone_number_index)
        if not len(person.phone_numbers):
            person.phone_numbers = ['']


class SampleApp(tvac.BaseApplication):
    class ShowType(Enum.Enum):
        PHONEBOOK = 1
        PHONENUMBERS = 2

    def __init__(self, height, width, phone_book):
        self.phone_book = phone_book
        self.person_index = 0

        self.phone_book_label_text = 'Personen-Übersicht'
        self.phone_book_columns = (
        'Vorname', 'Nachname', 'Straße', 'Hausnummer', 'Postleitzahl', 'Ort', 'Email', 'Geburtsjahr', 'Geburtsmonat',
        'Geburtstag', 'Geschlecht')
        self.phone_book_menu = (('Eintrag', ('Neu', self.new_entry), ('Löschen', self.delete_entry)),
                                ('Anzeigen', ('ReadMe', self.do_show_numbers)))

        self.phone_nummer_columns = ('Nummer',)
        self.phone_number_menu = (('Eintrag', ('Neu', self.new_entry), ('Löschen', self.delete_entry)),
                                  ('Anzeigen', ('Phone Book', self.do_show_phone_book)))

        self.show_type = SampleApp.ShowType.PHONEBOOK

        super(SampleApp, self).__init__(height, width,
                                        label_text=self.phone_book_label_text,
                                        columns=self.phone_book_columns,
                                        menu=self.phone_book_menu,
                                        data_sequences=self.phone_book.get_main_entry_data())

    def do_show_numbers(self, *args):
        messagebox.showinfo('Tadaaaaaaaaaaaaaaaa!',
                            'Lieber Wolfgang, viele Grüße von Chris, Filip, Hajo und Manuela :-)')

        # self.show_type = SampleApp.ShowType.PHONENUMBERS
        #
        # self.person_index = self.tableView.get_selected_index()
        #
        # person = self.phone_book[self.person_index]
        # self.create_view(label_text='Telefonnummer von ' + person.pre_name + ' ' + person.last_name,
        #                  columns=self.phone_nummer_columns,
        #                  menu=self.phone_number_menu,
        #                  data_sequences=self.phone_book.get_phone_number_data(self.person_index))

    def do_show_phone_book(self, *args):
        self.show_type = SampleApp.ShowType.PHONEBOOK

        self.create_view(label_text=self.phone_book_label_text,
                         columns=self.phone_book_columns,
                         menu=self.phone_book_menu,
                         data_sequences=self.phone_book.get_main_entry_data(),
                         index_to_select=self.person_index)

    def new_entry(self, *args):
        new_entry_data = super(SampleApp, self).new_entry()
        if new_entry_data is not None:
            if self.show_type == SampleApp.ShowType.PHONEBOOK:
                self.phone_book.add_main_entry_data(new_entry_data)
            elif self.show_type == SampleApp.ShowType.PHONENUMBERS:
                self.phone_book.add_phone_number_data(self.person_index, new_entry_data)

    def delete_entry(self):
        deleted_index = super(SampleApp, self).delete_entry()
        if deleted_index is not None:
            if self.show_type == SampleApp.ShowType.PHONEBOOK:
                self.phone_book.delete_main_entry_index(deleted_index)
            elif self.show_type == SampleApp.ShowType.PHONENUMBERS:
                self.phone_book.delete_phone_number_index(self.person_index, deleted_index)

    def edit_action(self, *args):
        edit_entry_data = super(SampleApp, self).edit_action()
        if edit_entry_data is not None:
            if self.show_type == SampleApp.ShowType.PHONEBOOK:
                self.person_index = self.tableView.get_selected_index()
                self.phone_book.set_main_entry_data(self.person_index, edit_entry_data)
            elif self.show_type == SampleApp.ShowType.PHONENUMBERS:
                phone_number_index = self.tableView.get_selected_index()
                self.phone_book.set_phone_number_data(self.person_index, phone_number_index, edit_entry_data)

    def do_second(self, *args):
        print('mache irgendwas')


f = open('personenliste.txt', 'r+')

f_string = f.read()

f_string_splitted = f_string.split(', ')

print(f_string_splitted[0])



if __name__ == '__main__':
    app = SampleApp(400, 400, PhoneBook((
        Person(f_string_splitted[0], f_string_splitted[1], f_string_splitted[2], f_string_splitted[3], f_string_splitted[4],
               f_string_splitted[5], f_string_splitted[6], int(f_string_splitted[7]), int(f_string_splitted[8]),
               int(f_string_splitted[9]), f_string_splitted[10]),
        Person(f_string_splitted[0], f_string_splitted[1], f_string_splitted[2], f_string_splitted[3],
               f_string_splitted[4],
               f_string_splitted[5], f_string_splitted[6], int(f_string_splitted[7]), int(f_string_splitted[8]),
               int(f_string_splitted[9]), f_string_splitted[10]),
        Person(f_string_splitted[0], f_string_splitted[1], f_string_splitted[2], f_string_splitted[3],
               f_string_splitted[4],
               f_string_splitted[5], f_string_splitted[6], int(f_string_splitted[7]), int(f_string_splitted[8]),
               int(f_string_splitted[9]), f_string_splitted[10]),
        Person(f_string_splitted[0], f_string_splitted[1], f_string_splitted[2], f_string_splitted[3],
               f_string_splitted[4],
               f_string_splitted[5], f_string_splitted[6], int(f_string_splitted[7]), int(f_string_splitted[8]),
               int(f_string_splitted[9]), f_string_splitted[10])
    )))

    app.run()

f.close()

