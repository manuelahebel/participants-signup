import tkinter as tk
import tkinter.ttk as ttk
import kurs_instanzen as ki
import kurs_klassen as kk

STEELBLUEEINS = "#63B8FF"
STEELBLUEZWEI = "#5CACEE"
STEELBLUEDREI = "#4F94CD"
STEELBLUEVIER = "#36648B"

def open_anmeldung():
    import gui_windowThree

windowTwo_hotelzimmersport = tk.Tk()
windowTwo_hotelzimmersport.title(f'Wähle Deinen {ki.hotelzimmersport01.course_type}-Kurs aus!')
windowTwo_hotelzimmersport.geometry('900x500')
windowTwo_hotelzimmersport.config(bg='grey')

# wir bauen eine Zeile:
label_hotelzimmersport01 = tk.Label(windowTwo_hotelzimmersport, text=f'Startdatum: {ki.hotelzimmersport01.start_date}    |    '
                                                              f'Kursdauer: {str(ki.hotelzimmersport01.duration)} Wochen    |    '
                                                              f'Trainer: {ki.hotelzimmersport01.trainer_name}')

label_hotelzimmersport01.grid(row=0, column=0, sticky='nswe')
label_hotelzimmersport01.config(bg=STEELBLUEEINS, font=('arial', 14))

label_hotelzimmersport01_bg = tk.Label(windowTwo_hotelzimmersport, text='')
label_hotelzimmersport01_bg.grid(row=0, column=1, sticky='nswe')
label_hotelzimmersport01_bg.config(bg=STEELBLUEDREI)

button_hotelzimmersport01 = tk.Button(windowTwo_hotelzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_hotelzimmersport01.grid(row=0, column=1)

windowTwo_hotelzimmersport.rowconfigure(0, weight=1)
windowTwo_hotelzimmersport.columnconfigure(0, weight=4)
windowTwo_hotelzimmersport.columnconfigure(1, weight=3)

# wir bauen zweite Zeile

label_hotelzimmersport02 = tk.Label(windowTwo_hotelzimmersport, text=f'Startdatum: {ki.hotelzimmersport02.start_date}    |    '
                                                              f'Kursdauer: {str(ki.hotelzimmersport02.duration)} Wochen    |    '
                                                              f'Trainer: {ki.hotelzimmersport02.trainer_name}')

label_hotelzimmersport02.grid(row=1, column=0, sticky='nswe')
label_hotelzimmersport02.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_hotelzimmersport02_bg = tk.Label(windowTwo_hotelzimmersport, text='')
label_hotelzimmersport02_bg.grid(row=1, column=1, sticky='nswe')
label_hotelzimmersport02_bg.config(bg=STEELBLUEDREI)

button_hotelzimmersport02 = tk.Button(windowTwo_hotelzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_hotelzimmersport02.grid(row=1, column=1)

windowTwo_hotelzimmersport.rowconfigure(1, weight=1)


# wir bauen dritte Zeile

label_hotelzimmersport03 = tk.Label(windowTwo_hotelzimmersport, text=f'Startdatum: {ki.hotelzimmersport03.start_date}    |    '
                                                              f'Kursdauer: {str(ki.hotelzimmersport03.duration)} Wochen    |    '
                                                              f'Trainer: {ki.hotelzimmersport03.trainer_name}')

label_hotelzimmersport03.grid(row=2, column=0, sticky='nswe')
label_hotelzimmersport03.config(bg=STEELBLUEEINS, font=('arial', 14))

label_hotelzimmersport03_bg = tk.Label(windowTwo_hotelzimmersport, text='')
label_hotelzimmersport03_bg.grid(row=2, column=1, sticky='nswe')
label_hotelzimmersport03_bg.config(bg=STEELBLUEDREI)

button_hotelzimmersport03 = tk.Button(windowTwo_hotelzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_hotelzimmersport03.grid(row=2, column=1)

windowTwo_hotelzimmersport.rowconfigure(2, weight=1)


# wir bauen vierte Zeile

label_hotelzimmersport04 = tk.Label(windowTwo_hotelzimmersport, text=f'Startdatum: {ki.hotelzimmersport04.start_date}    |    '
                                                              f'Kursdauer: {str(ki.hotelzimmersport04.duration)} Wochen    |    '
                                                              f'Trainer: {ki.hotelzimmersport04.trainer_name}')

label_hotelzimmersport04.grid(row=3, column=0, sticky='nswe')
label_hotelzimmersport04.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_hotelzimmersport04_bg = tk.Label(windowTwo_hotelzimmersport, text='')
label_hotelzimmersport04_bg.grid(row=3, column=1, sticky='nswe')
label_hotelzimmersport04_bg.config(bg=STEELBLUEDREI)

button_hotelzimmersport04 = tk.Button(windowTwo_hotelzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_hotelzimmersport04.grid(row=3, column=1)

windowTwo_hotelzimmersport.rowconfigure(3, weight=1)

windowTwo_hotelzimmersport.mainloop()