import datetime
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import kurs_instanzen as ki
import kurs_klassen as kk
import personen_klassen as pk

STEELBLUEEINS = "#63B8FF"
STEELBLUEZWEI = "#5CACEE"
STEELBLUEDREI = "#4F94CD"
STEELBLUEVIER = "#36648B"

windowThree = tk.Tk()

# Custom Style for Radiobuttons below (Row 9)
style = ttk.Style()
style.configure('TLabelframe', background=STEELBLUEZWEI)
style.configure('TLabelframe.Label', background=STEELBLUEZWEI)
style.configure('TRadiobutton', background=STEELBLUEZWEI)

windowThree.geometry('750x900')
windowThree.title('Bitte gebe Deine Anmeldeinformationen ein!')
windowThree.config(bg=STEELBLUEZWEI)


# Definint Button Action

### OLD VERSION OF BUTTON ACTION:
# def print_values():
#     print('Sie haben folgende Daten eingegeben:')
#     print(f'\nVorname: {entry_first_name.get()}')
#     print(f'Nachname: {entry_last_name.get()}')
#     print(f'Straße: {entry_street.get()}')
#     print(f'Hausnummer: {entry_housenumber.get()}')
#     print(f'PLZ: {entry_zip.get()}')
#     print(f'Stadt: {entry_city.get()}')
#     print(f'Email: {entry_email.get()}')
#     print(f'Geburtsjahr: {entry_yyyy.get()}')
#     print(f'Geburtsmonat: {entry_mm.get()}')
#     print(f'Geburtstag: {entry_tt.get()}')
#     print(f'Geschlecht: {radio_gender_int.get()}')
#     print(f'Sportlichkeit: {radio_sport_int.get()}')
#     print(f'Functional Training: {radio_ft_int.get()}')
#     print(f'Zahlungsart: {menu_zahlungsart_selected.get()}')


### NEW VERSION OF BUTTON ACTION:

# Erzeugung eines Files mit allen Input-Daten aus windowThree
# TODO: aus unersichtlichem Grund schreibt diese Funktion die Strings nicht wie von Methode writelines vorgesehen in jeweils eine neue Zeile.
# Hat zu Beginn funktioniert, jetzt geht's nicht mehr. Keine Ahnung warum.

def create_txt_file_with_person_data():
    f = open('personenliste.txt', 'a')
    f.writelines(f'{entry_first_name.get()}, {entry_last_name.get()}, {entry_street.get()}, {entry_housenumber.get()}, '
                 f'{entry_zip.get()}, {entry_city.get()}, {entry_email.get()}, {entry_yyyy.get()}, {entry_mm.get()}, '
                 f'{entry_tt.get()}, {radio_gender_int.get()}\n')
    f.close()

    if messagebox.showinfo('Anmeldung', 'Sie haben sich erfolgreich zu Ihrem ausgewählten Kurs angemeldet!'):
        windowThree.quit()


################ first column

# column 0, row 0: first name
label_first_name = tk.Label(windowThree, text='Vorname: ')
label_first_name.grid(row=0, column=0, sticky='nsw', padx=5)
label_first_name.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 1: last name
label_last_name = tk.Label(windowThree, text='Nachname: ')
label_last_name.grid(row=1, column=0, sticky='nsw', padx=5)
label_last_name.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 2: street
label_street = tk.Label(windowThree, text='Straße: ')
label_street.grid(row=2, column=0, sticky='nsw', padx=5)
label_street.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 3: housenumber
label_housenumber = tk.Label(windowThree, text='Hausnummer: ')
label_housenumber.grid(row=3, column=0, sticky='nsw', padx=5)
label_housenumber.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 4: zip
label_zip = tk.Label(windowThree, text='PLZ: ')
label_zip.grid(row=4, column=0, sticky='nsw', padx=5)
label_zip.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 5: city
label_city = tk.Label(windowThree, text='Stadt: ')
label_city.grid(row=5, column=0, sticky='nsw', padx=5)
label_city.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 6: email
label_email = tk.Label(windowThree, text='Email: ')
label_email.grid(row=6, column=0, sticky='nsw', padx=5)
label_email.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 7: birthdate_1
label_birthdate1 = tk.Label(windowThree, text='')
label_birthdate1.grid(row=7, column=0, sticky='nsw', padx=5)
label_birthdate1.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 8: birthdate
label_birthdate2 = tk.Label(windowThree, text='Geburtstag: ')
label_birthdate2.grid(row=8, column=0, sticky='nsw', padx=5)
label_birthdate2.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 9: gender
label_gender = tk.Label(windowThree, text='Geschlecht: ')
label_gender.grid(row=9, column=0, sticky='nsw', padx=5)
label_gender.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 10: athleticism
label_athleticism = tk.Label(windowThree, text='Wie oft hast Du in den letzten\n12 Monaten Sport getrieben? ')
label_athleticism.grid(row=10, column=0, sticky='nsw', padx=5)
label_athleticism.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 11: experience with functional training
label_experience = tk.Label(windowThree, text='Hast du Erfahrung mit\nFunctional Training? ')
label_experience.grid(row=11, column=0, sticky='nsw', padx=5)
label_experience.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 12: payment form
label_payment_form = tk.Label(windowThree, text='Zahlungsart: ')
label_payment_form.grid(row=12, column=0, sticky='nsw', padx=5)
label_payment_form.config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))

# column 0, row 13: submit button
label_button = tk.Label(windowThree, text='')
label_button.grid(row=13, column=0, sticky='nsw', padx=5)
label_button.config(bg=STEELBLUEZWEI)

windowThree.rowconfigure(0, weight=1)
windowThree.rowconfigure(1, weight=1)
windowThree.rowconfigure(2, weight=1)
windowThree.rowconfigure(3, weight=1)
windowThree.rowconfigure(4, weight=1)
windowThree.rowconfigure(5, weight=1)
windowThree.rowconfigure(6, weight=1)
windowThree.rowconfigure(7, weight=1)
windowThree.rowconfigure(8, weight=1)
windowThree.rowconfigure(9, weight=1)
windowThree.rowconfigure(10, weight=1)
windowThree.rowconfigure(11, weight=1)
windowThree.rowconfigure(12, weight=1)
windowThree.rowconfigure(13, weight=1)
# windowThree.rowconfigure(14, weight=1)
# windowThree.rowconfigure(15, weight=1)
# windowThree.rowconfigure(16, weight=1)
# windowThree.rowconfigure(17, weight=1)
# windowThree.rowconfigure(18, weight=1)

############ second-fourth column
# Hajo adds:

# - Important: Textvariable implemented on all entry widgets
# - TODO: Check use of intVar, esp. use of '' for empty "string" - Use of None resulted in default value = 0, bad.

# - testing bg = STEELBLUEEINS für compromise blue/white on row 0
# - set label font with .config(bg=STEELBLUEZWEI, font=('Arial', 11, 'bold'))
# - set entry-widget font with .config(font=('Arial', 11)) on entry-fields where needed (= plain, not bold)
# - deleted "colspan = 2" from entry_zip  widget (now: same size as street_number)
# - added one radio btn widget as starting point / to  copy from
# - added custom style for LabelFrame's background color (see top of file)

# column 1-3, row 0
entry_first_name = tk.Entry(windowThree)
entry_first_name.grid(row=0, column=1, columnspan=3, sticky='ew', padx=10)
entry_first_name_text = tk.StringVar(windowThree, '')
entry_first_name.config(textvariable=entry_first_name_text, font=('Arial', 11))

# column 1-3, row 1
entry_last_name = tk.Entry(windowThree)
entry_last_name.grid(row=1, column=1, columnspan=3, sticky='ew', padx=10)
entry_last_name_text = tk.StringVar(windowThree, '')
entry_last_name.config(textvariable=entry_last_name_text, font=('Arial', 11))

# column 1-3, row 2
entry_street = tk.Entry(windowThree)
entry_street.grid(row=2, column=1, columnspan=3, sticky='ew', padx=10)
entry_street_text = tk.StringVar(windowThree, '')
entry_street.config(textvariable=entry_street_text, font=('Arial', 11))

# column 1-3, row 3
entry_housenumber = tk.Entry(windowThree)
entry_housenumber.grid(row=3, column=1, sticky='ew', padx=10)
entry_housenumber_int = tk.IntVar(windowThree, '')
entry_housenumber.config(textvariable=entry_housenumber_int, font=('Arial', 11))

# column 1-3, row 4
entry_zip = tk.Entry(windowThree)
entry_zip.grid(row=4, column=1, sticky='ew', padx=10)
entry_zip_int = tk.IntVar(windowThree, '')
entry_zip.config(textvariable=entry_zip_int, font=('Arial', 11))

# column 1-3, row 5
entry_city = tk.Entry(windowThree)
entry_city.grid(row=5, column=1, columnspan=3, sticky='ew', padx=10)
entry_city_text = tk.StringVar(windowThree, '')
entry_city.config(textvariable=entry_city_text, font=('Arial', 11))

# column 1-3, row 6
entry_email = tk.Entry(windowThree)
entry_email.grid(row=6, column=1, columnspan=3, sticky='ew', padx=10)
entry_email_text = tk.StringVar(windowThree, '')
entry_email.config(textvariable=entry_email_text, font=('Arial', 11))

# column 1, row 7
label_tt = tk.Label(windowThree, text='TT')
label_tt.grid(row=7, column=1, sticky='sew')
label_tt.config(bg=STEELBLUEZWEI, font=('Arial', 10))

# column 2, row 7
label_mm = tk.Label(windowThree, text='MM')
label_mm.grid(row=7, column=2, sticky='sew')
label_mm.config(bg=STEELBLUEZWEI, font=('Arial', 10))

# column 3, row 7
label_yyyy = tk.Label(windowThree, text='YYYY')
label_yyyy.grid(row=7, column=3, sticky='sew')
label_yyyy.config(bg=STEELBLUEZWEI, font=('Arial', 10))

# column 1, row 8
entry_tt = tk.Entry(windowThree)
entry_tt.grid(row=8, column=1, sticky='ew', padx=10)
entry_tt_int = tk.IntVar(windowThree, '')
entry_tt.config(textvariable=entry_tt_int, font=('Arial', 11))

# column 2, row 8
entry_mm = tk.Entry(windowThree)
entry_mm.grid(row=8, column=2, sticky='ew', padx=10)
entry_mm_int = tk.IntVar(windowThree, '')
entry_mm.config(textvariable=entry_mm_int, font=('Arial', 11))

# column 3, row 8
entry_yyyy = tk.Entry(windowThree)
entry_yyyy.grid(row=8, column=3, sticky='ew', padx=10)
entry_yyyy_int = tk.IntVar(windowThree, '')
entry_yyyy.config(textvariable=entry_yyyy_int, font=('Arial', 11))

# column 1-3, row 9
label_frame_gender = ttk.Labelframe(windowThree)
# For style definition (background color) see TOP
label_frame_gender.config(text='')
label_frame_gender.grid(row=9, column=1, columnspan=3, sticky='nwes', padx=10, pady=20)
radio_gender_int = tk.IntVar(windowThree, 99)

radiobutton_maennlich = ttk.Radiobutton(label_frame_gender)
radiobutton_maennlich.config(text='männlich', variable=radio_gender_int, value=0)
radiobutton_maennlich.grid(row=0, column=0)

radiobutton_weiblich = ttk.Radiobutton(label_frame_gender)
radiobutton_weiblich.config(text='weiblich', variable=radio_gender_int, value=1)
radiobutton_weiblich.grid(row=0, column=1)

radiobutton_3 = ttk.Radiobutton(label_frame_gender)
radiobutton_3.config(text='keine Angabe', variable=radio_gender_int, value=2)
radiobutton_3.grid(row=0, column=2)

label_frame_gender.columnconfigure(0, weight=1)
label_frame_gender.columnconfigure(1, weight=1)
label_frame_gender.columnconfigure(2, weight=1)

# column 1-3, row 10
label_frame_sport = ttk.Labelframe(windowThree)
# For style definition (background color) see TOP

label_frame_sport.config(text='')
label_frame_sport.grid(row=10, column=1, sticky='nwes', padx=10, pady=20)
radio_sport_int = tk.IntVar(windowThree, 99)

radiobutton_bishernie = ttk.Radiobutton(label_frame_sport)
radiobutton_bishernie.config(text='gar nicht', variable=radio_sport_int, value=0)
radiobutton_bishernie.grid(row=0, column=1, sticky='w')

radiobutton_viermalprowoche = ttk.Radiobutton(label_frame_sport)
radiobutton_viermalprowoche.config(text='bis zu 1x /Woche', variable=radio_sport_int, value=1)
radiobutton_viermalprowoche.grid(row=1, column=1, sticky='w')

radiobutton_zweimalprowoche = ttk.Radiobutton(label_frame_sport)
radiobutton_zweimalprowoche.config(text='bis zu 2x /Woche', variable=radio_sport_int, value=2)
radiobutton_zweimalprowoche.grid(row=2, column=1, sticky='w')

radiobutton_mehralszweiprowoche = ttk.Radiobutton(label_frame_sport)
radiobutton_mehralszweiprowoche.config(text='mehr als 2x /Woche', variable=radio_sport_int, value=3)
radiobutton_mehralszweiprowoche.grid(row=3, column=1, sticky='w')

label_frame_sport.rowconfigure(0, weight=1)
label_frame_sport.rowconfigure(1, weight=1)
label_frame_sport.rowconfigure(2, weight=1)
label_frame_sport.rowconfigure(3, weight=1)

# column 1-3, row11
label_frame_ft = ttk.Labelframe(windowThree)
# For style definition (background color) see TOP

label_frame_ft.config(text='')
label_frame_ft.grid(row=11, column=1, sticky='nwes', padx=10, pady=20)
radio_ft_int = tk.IntVar(windowThree, 99)

radiobutton_ja = ttk.Radiobutton(label_frame_ft)
radiobutton_ja.config(text='ja', variable=radio_ft_int, value=0)
radiobutton_ja.grid(row=0, column=1, sticky='w')

radiobutton_etwas = ttk.Radiobutton(label_frame_ft)
radiobutton_etwas.config(text='etwas', variable=radio_ft_int, value=1)
radiobutton_etwas.grid(row=1, column=1, sticky='w')

radiobutton_nein = ttk.Radiobutton(label_frame_ft)
radiobutton_nein.config(text='nein', variable=radio_ft_int, value=2)
radiobutton_nein.grid(row=2, column=1, sticky='w')

# column 1-3, row 12
menu_zahlungsart_selected = tk.StringVar()
menu_zahlungsart = ttk.OptionMenu(windowThree, menu_zahlungsart_selected, 'Dummy', 'Rechnung', 'Kreditkarte',
                                  'Sparschwein', 'PayPal', 'Gutschein', 'Tauschhandel', 'Wein')
menu_zahlungsart_selected.set('Bitte auswählen…')
menu_zahlungsart.grid(row=12, column=1, sticky='we', padx=10)

# column 0-3, row 13
button_anmelden = tk.Button(windowThree, text='Anmelden', command=create_txt_file_with_person_data)
button_anmelden.grid(row=13, column=1, sticky='we', padx=10, pady=30)

windowThree.columnconfigure(0, weight=2)
windowThree.columnconfigure(1, weight=1)
windowThree.columnconfigure(2, weight=1)
windowThree.columnconfigure(3, weight=1)

# TODO: Bild einfügen

# TEMP
# TODO: Change this simple function call to meaningful button action


windowThree.mainloop()
