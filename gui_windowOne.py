'''
User Interfaces:
Window 1: Shows all different course types and offers a button to proceed to the next window.
Window 2: Shows all courses of a course type, showing start and end date as well as trainer name. With a button
            the course choice can be selected. Next window opens.
Window 3: Sign-Up Window: all personal data has to be entered and submitted via click of a button.
Window 4: Participants List: alter data, sort data.
'''

########### Window 1 ##################

import tkinter as tk
import tkinter.ttk as ttk
#import gui_windowTwo_wohnzimmersport as gw

STEELBLUEEINS = "#63B8FF"
STEELBLUEZWEI = "#5CACEE"
STEELBLUEDREI = "#4F94CD"
STEELBLUEVIER = "#36648B"

windowOne = tk.Tk()
windowOne.geometry('700x500')
windowOne.title('ZimmerSport - Wähle Deinen Kurstyp!')
windowOne.config(bg='grey')

"""
label für die 'hintergrundfarbe' für das feld Wohnzimmersport
"""
label_wohnzimmersport_bg = tk.Label(windowOne, text='')
label_wohnzimmersport_bg.grid(row=0, column=0, sticky='nesw')
label_wohnzimmersport_bg.config(bg=STEELBLUEEINS)

"""
Eigentliches label 'WohinzimmerSport'
"""
label_wohnzimmersport_title = tk.Label(windowOne, text='WohnZimmerSport', bg=STEELBLUEEINS, font=('arial', 18, 'bold'))
label_wohnzimmersport_title.grid(row=0, column=0, sticky='n')

"""
label für die Beschreibung von Wohnzimmersport
"""
label_wohnzimmersport_beschreibung = tk.Label(windowOne, text='Hier wir die beschreibung von\nWohnzimmersport', bg=STEELBLUEEINS)
label_wohnzimmersport_beschreibung.grid(row=0, column=0)
"""
label für die 'hintergrundfarbe' für das feld bürozimmerpsort
"""
label_buerozimmersport_bg = tk.Label(windowOne, text='')
label_buerozimmersport_bg.grid(row=1, column=0, sticky='nesw')
label_buerozimmersport_bg.config(bg=STEELBLUEZWEI)

"""
Eigentliches label 'Büruozimmersport'
"""
label_buerozimmersport_title = tk.Label(windowOne, text='BüroZimmerSport', bg=STEELBLUEZWEI, font=('arial', 18, 'bold'))
label_buerozimmersport_title.grid(row=1, column=0, sticky='n')
"""
label für die beschreibung von Bürozimmerpsort
"""
label_buerozimmersport_beschreibung = tk.Label(windowOne, text='Hier wir die beschreibung von\nBürozimmersport', bg=STEELBLUEZWEI)
label_buerozimmersport_beschreibung.grid(row=1, column=0)

"""
label für die 'hintergrundfarbe' für das feld bürozimmerpsort
"""
label_kinderzimmersport_bg = tk.Label(windowOne, text='')
label_kinderzimmersport_bg.grid(row=0, column=1, sticky='nesw')
label_kinderzimmersport_bg.config(bg=STEELBLUEDREI)

"""
Eigentliches label 'Büruozimmersport'
"""
label_kinderzimmersport_title = tk.Label(windowOne, text='KinderZimmerSport', bg=STEELBLUEDREI, font=('arial', 18, 'bold'))
label_kinderzimmersport_title.grid(row=0, column=1, sticky='n')

"""
label für die beschreibung von Kinderzimmersport
"""
label_kinderzimmersport_beschreibung = tk.Label(windowOne, text='Hier wir die beschreibung von\nKinderzimmersport', bg=STEELBLUEDREI)
label_kinderzimmersport_beschreibung.grid(row=0, column=1)


"""
label für die 'hintergrundfarbe' für das feld hotelzimmersport
"""
label_hotelzimmersport_bg = tk.Label(windowOne, text='')
label_hotelzimmersport_bg.grid(row=1, column=1, sticky='nesw')
label_hotelzimmersport_bg.config(bg=STEELBLUEVIER)

"""
label für die beschreibung von Hotelzimmersport
"""
label_hotelzimmersport_beschreibung = tk.Label(windowOne, text='Hier wir die beschreibung von\nHotelzimmersport', bg=STEELBLUEVIER)
label_hotelzimmersport_beschreibung.grid(row=1, column=1)


"""
Eigentliches label 'hotelzimmersport'
"""
label_hotelzimmersport_title = tk.Label(windowOne, text='HotelZimmerSport', bg=STEELBLUEVIER, font=('arial', 18, 'bold'))
label_hotelzimmersport_title.grid(row=1, column=1, sticky='n')



"""
Buttons für die einzelnen Felder
    - WohinzimmerSport
    - buerozimmersport
    - kinderzimmersport
    - hotelzimmersport  
"""


def open_wohnzimmersport_courses():
    import gui_windowTwo_wohnzimmersport


def open_buerozimmersport_courses():
    import gui_windowTwo_buerozimmersport


def open_kinderzimmersport_courses():
    import gui_windowTwo_kinderzimmersport


def open_hotelzimmersport_courses():
    import gui_windowTwo_hotelzimmersport


button_wohnzimmersport = tk.Button(windowOne, text='Zum Kurs', width=20, command=open_wohnzimmersport_courses)
button_wohnzimmersport.grid(row=0, column=0, sticky='s', pady=50)

button_buerozimmersport = tk.Button(windowOne, text='Zum Kurs', width=20, command=open_buerozimmersport_courses)
button_buerozimmersport.grid(row=1, column=0, sticky='s', pady=50)

button_kinderzimmersport = tk.Button(windowOne, text='Zum Kurs', width=20, command=open_kinderzimmersport_courses)
button_kinderzimmersport.grid(row=0, column=1, sticky='s', pady=50)

button_hotelzimmersport = tk.Button(windowOne, text='Zum Kurs', width=20, command=open_hotelzimmersport_courses)
button_hotelzimmersport.grid(row=1, column=1, sticky='s', pady=50)

windowOne.rowconfigure(0, weight=1)
windowOne.rowconfigure(1, weight=1)
windowOne.columnconfigure(0, weight=1)
windowOne.columnconfigure(1, weight=1)


windowOne.mainloop()
