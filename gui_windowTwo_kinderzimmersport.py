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

windowTwo_kinderzimmersport = tk.Tk()
windowTwo_kinderzimmersport.title(f'Wähle Deinen {ki.kinderzimmersport01.course_type}-Kurs aus!')
windowTwo_kinderzimmersport.geometry('900x500')
windowTwo_kinderzimmersport.config(bg='grey')

# wir bauen eine Zeile:
label_kinderzimmersport01 = tk.Label(windowTwo_kinderzimmersport, text=f'Startdatum: {ki.kinderzimmersport01.start_date}    |    '
                                                              f'Kursdauer: {str(ki.kinderzimmersport01.duration)} Wochen    |    '
                                                              f'Trainer: {ki.kinderzimmersport01.trainer_name}')

label_kinderzimmersport01.grid(row=0, column=0, sticky='nswe')
label_kinderzimmersport01.config(bg=STEELBLUEEINS, font=('arial', 14))

label_kinderzimmersport01_bg = tk.Label(windowTwo_kinderzimmersport, text='')
label_kinderzimmersport01_bg.grid(row=0, column=1, sticky='nswe')
label_kinderzimmersport01_bg.config(bg=STEELBLUEDREI)

button_kinderzimmersport01 = tk.Button(windowTwo_kinderzimmersport, text='Anmelden', font=('arial', 12), command=open_anmeldung)
button_kinderzimmersport01.grid(row=0, column=1)

windowTwo_kinderzimmersport.rowconfigure(0, weight=1)
windowTwo_kinderzimmersport.columnconfigure(0, weight=4)
windowTwo_kinderzimmersport.columnconfigure(1, weight=3)

# wir bauen zweite Zeile

label_kinderzimmersport02 = tk.Label(windowTwo_kinderzimmersport, text=f'Startdatum: {ki.kinderzimmersport02.start_date}    |    '
                                                              f'Kursdauer: {str(ki.kinderzimmersport02.duration)} Wochen    |    '
                                                              f'Trainer: {ki.kinderzimmersport02.trainer_name}')

label_kinderzimmersport02.grid(row=1, column=0, sticky='nswe')
label_kinderzimmersport02.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_kinderzimmersport02_bg = tk.Label(windowTwo_kinderzimmersport, text='')
label_kinderzimmersport02_bg.grid(row=1, column=1, sticky='nswe')
label_kinderzimmersport02_bg.config(bg=STEELBLUEDREI)

button_kinderzimmersport02 = tk.Button(windowTwo_kinderzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_kinderzimmersport02.grid(row=1, column=1)

windowTwo_kinderzimmersport.rowconfigure(1, weight=1)


# wir bauen dritte Zeile

label_kinderzimmersport03 = tk.Label(windowTwo_kinderzimmersport, text=f'Startdatum: {ki.kinderzimmersport03.start_date}    |    '
                                                              f'Kursdauer: {str(ki.kinderzimmersport03.duration)} Wochen    |    '
                                                              f'Trainer: {ki.kinderzimmersport03.trainer_name}')

label_kinderzimmersport03.grid(row=2, column=0, sticky='nswe')
label_kinderzimmersport03.config(bg=STEELBLUEEINS, font=('arial', 14))

label_kinderzimmersport03_bg = tk.Label(windowTwo_kinderzimmersport, text='')
label_kinderzimmersport03_bg.grid(row=2, column=1, sticky='nswe')
label_kinderzimmersport03_bg.config(bg=STEELBLUEDREI)

button_kinderzimmersport03 = tk.Button(windowTwo_kinderzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_kinderzimmersport03.grid(row=2, column=1)

windowTwo_kinderzimmersport.rowconfigure(2, weight=1)


# wir bauen vierte Zeile

label_kinderzimmersport04 = tk.Label(windowTwo_kinderzimmersport, text=f'Startdatum: {ki.kinderzimmersport04.start_date}    |    '
                                                              f'Kursdauer: {str(ki.kinderzimmersport04.duration)} Wochen    |    '
                                                              f'Trainer: {ki.kinderzimmersport04.trainer_name}')

label_kinderzimmersport04.grid(row=3, column=0, sticky='nswe')
label_kinderzimmersport04.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_kinderzimmersport04_bg = tk.Label(windowTwo_kinderzimmersport, text='')
label_kinderzimmersport04_bg.grid(row=3, column=1, sticky='nswe')
label_kinderzimmersport04_bg.config(bg=STEELBLUEDREI)

button_kinderzimmersport04 = tk.Button(windowTwo_kinderzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_kinderzimmersport04.grid(row=3, column=1)

windowTwo_kinderzimmersport.rowconfigure(3, weight=1)


windowTwo_kinderzimmersport.mainloop()