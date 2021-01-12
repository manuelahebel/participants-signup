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

windowTwo_buerozimmersport = tk.Tk()
windowTwo_buerozimmersport.title(f'Wähle Deinen {ki.buerozimmersport01.course_type}-Kurs aus!')
windowTwo_buerozimmersport.geometry('900x500')
windowTwo_buerozimmersport.config(bg='grey')

# wir bauen eine Zeile:
label_buerozimmersport01 = tk.Label(windowTwo_buerozimmersport, text=f'Startdatum: {ki.buerozimmersport01.start_date}    |    '
                                                              f'Kursdauer: {str(ki.buerozimmersport01.duration)} Wochen    |    '
                                                              f'Trainer: {ki.buerozimmersport01.trainer_name}')

label_buerozimmersport01.grid(row=0, column=0, sticky='nswe')
label_buerozimmersport01.config(bg=STEELBLUEEINS, font=('arial', 14))

label_buerozimmersport01_bg = tk.Label(windowTwo_buerozimmersport, text='')
label_buerozimmersport01_bg.grid(row=0, column=1, sticky='nswe')
label_buerozimmersport01_bg.config(bg=STEELBLUEDREI)

button_buerozimmersport01 = tk.Button(windowTwo_buerozimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_buerozimmersport01.grid(row=0, column=1)

windowTwo_buerozimmersport.rowconfigure(0, weight=1)
windowTwo_buerozimmersport.columnconfigure(0, weight=4)
windowTwo_buerozimmersport.columnconfigure(1, weight=3)

# wir bauen zweite Zeile

label_buerozimmersport02 = tk.Label(windowTwo_buerozimmersport, text=f'Startdatum: {ki.buerozimmersport02.start_date}    |    '
                                                              f'Kursdauer: {str(ki.buerozimmersport02.duration)} Wochen    |    '
                                                              f'Trainer: {ki.buerozimmersport02.trainer_name}')

label_buerozimmersport02.grid(row=1, column=0, sticky='nswe')
label_buerozimmersport02.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_buerozimmersport02_bg = tk.Label(windowTwo_buerozimmersport, text='')
label_buerozimmersport02_bg.grid(row=1, column=1, sticky='nswe')
label_buerozimmersport02_bg.config(bg=STEELBLUEDREI)

button_buerozimmersport02 = tk.Button(windowTwo_buerozimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_buerozimmersport02.grid(row=1, column=1)

windowTwo_buerozimmersport.rowconfigure(1, weight=1)


# wir bauen dritte Zeile

label_buerozimmersport03 = tk.Label(windowTwo_buerozimmersport, text=f'Startdatum: {ki.buerozimmersport03.start_date}    |    '
                                                              f'Kursdauer: {str(ki.buerozimmersport03.duration)} Wochen    |    '
                                                              f'Trainer: {ki.buerozimmersport03.trainer_name}')

label_buerozimmersport03.grid(row=2, column=0, sticky='nswe')
label_buerozimmersport03.config(bg=STEELBLUEEINS, font=('arial', 14))

label_buerozimmersport03_bg = tk.Label(windowTwo_buerozimmersport, text='')
label_buerozimmersport03_bg.grid(row=2, column=1, sticky='nswe')
label_buerozimmersport03_bg.config(bg=STEELBLUEDREI)

button_buerozimmersport03 = tk.Button(windowTwo_buerozimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_buerozimmersport03.grid(row=2, column=1)

windowTwo_buerozimmersport.rowconfigure(2, weight=1)


# wir bauen vierte Zeile

label_buerozimmersport04 = tk.Label(windowTwo_buerozimmersport, text=f'Startdatum: {ki.buerozimmersport04.start_date}    |    '
                                                              f'Kursdauer: {str(ki.buerozimmersport04.duration)} Wochen    |    '
                                                              f'Trainer: {ki.buerozimmersport04.trainer_name}')

label_buerozimmersport04.grid(row=3, column=0, sticky='nswe')
label_buerozimmersport04.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_buerozimmersport04_bg = tk.Label(windowTwo_buerozimmersport, text='')
label_buerozimmersport04_bg.grid(row=3, column=1, sticky='nswe')
label_buerozimmersport04_bg.config(bg=STEELBLUEDREI)

button_buerozimmersport04 = tk.Button(windowTwo_buerozimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_buerozimmersport04.grid(row=3, column=1)

windowTwo_buerozimmersport.rowconfigure(3, weight=1)


windowTwo_buerozimmersport.mainloop()