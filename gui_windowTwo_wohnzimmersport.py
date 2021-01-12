import tkinter as tk
import tkinter.ttk as ttk
import kurs_instanzen as ki
import kurs_klassen as kk

def open_anmeldung():
    import gui_windowThree


STEELBLUEEINS = "#63B8FF"
STEELBLUEZWEI = "#5CACEE"
STEELBLUEDREI = "#4F94CD"
STEELBLUEVIER = "#36648B"

windowTwo_wohnzimmersport = tk.Tk()
windowTwo_wohnzimmersport.title(f'Wähle Deinen {ki.wohnzimmersport01.course_type}-Kurs aus!')
windowTwo_wohnzimmersport.geometry('900x500')
windowTwo_wohnzimmersport.config(bg='grey')

# wir bauen eine Zeile:
label_wohnzimmersport01 = tk.Label(windowTwo_wohnzimmersport, text=f'Startdatum: {ki.wohnzimmersport01.start_date}    |    '
                                                              f'Kursdauer: {str(ki.wohnzimmersport01.duration)} Wochen    |    '
                                                              f'Trainer: {ki.wohnzimmersport01.trainer_name}')

label_wohnzimmersport01.grid(row=0, column=0, sticky='nswe')
label_wohnzimmersport01.config(bg=STEELBLUEEINS, font=('arial', 14))

label_wohnzimmersport01_bg = tk.Label(windowTwo_wohnzimmersport, text='')
label_wohnzimmersport01_bg.grid(row=0, column=1, sticky='nswe')
label_wohnzimmersport01_bg.config(bg=STEELBLUEDREI)

button_wohnzimmersport01 = tk.Button(windowTwo_wohnzimmersport, text='Anmelden', font=('arial', 12), command=open_anmeldung)
button_wohnzimmersport01.grid(row=0, column=1)

windowTwo_wohnzimmersport.rowconfigure(0, weight=1)
windowTwo_wohnzimmersport.columnconfigure(0, weight=4)
windowTwo_wohnzimmersport.columnconfigure(1, weight=3)

# wir bauen zweite Zeile

label_wohnzimmersport02 = tk.Label(windowTwo_wohnzimmersport, text=f'Startdatum: {ki.wohnzimmersport02.start_date}    |    '
                                                              f'Kursdauer: {str(ki.wohnzimmersport02.duration)} Wochen    |    '
                                                              f'Trainer: {ki.wohnzimmersport02.trainer_name}')

label_wohnzimmersport02.grid(row=1, column=0, sticky='nswe')
label_wohnzimmersport02.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_wohnzimmersport02_bg = tk.Label(windowTwo_wohnzimmersport, text='')
label_wohnzimmersport02_bg.grid(row=1, column=1, sticky='nswe')
label_wohnzimmersport02_bg.config(bg=STEELBLUEDREI)

button_wohnzimmersport02 = tk.Button(windowTwo_wohnzimmersport, text='Anmelden', font=('arial', 12),command=open_anmeldung)
button_wohnzimmersport02.grid(row=1, column=1)

windowTwo_wohnzimmersport.rowconfigure(1, weight=1)


# wir bauen dritte Zeile

label_wohnzimmersport03 = tk.Label(windowTwo_wohnzimmersport, text=f'Startdatum: {ki.wohnzimmersport03.start_date}    |    '
                                                              f'Kursdauer: {str(ki.wohnzimmersport03.duration)} Wochen    |    '
                                                              f'Trainer: {ki.wohnzimmersport03.trainer_name}')

label_wohnzimmersport03.grid(row=2, column=0, sticky='nswe')
label_wohnzimmersport03.config(bg=STEELBLUEEINS, font=('arial', 14))

label_wohnzimmersport03_bg = tk.Label(windowTwo_wohnzimmersport, text='')
label_wohnzimmersport03_bg.grid(row=2, column=1, sticky='nswe')
label_wohnzimmersport03_bg.config(bg=STEELBLUEDREI)

button_wohnzimmersport03 = tk.Button(windowTwo_wohnzimmersport, text='Anmelden', font=('arial', 12), command=open_anmeldung)
button_wohnzimmersport03.grid(row=2, column=1)

windowTwo_wohnzimmersport.rowconfigure(2, weight=1)


# wir bauen vierte Zeile

label_wohnzimmersport04 = tk.Label(windowTwo_wohnzimmersport, text=f'Startdatum: {ki.wohnzimmersport04.start_date}    |    '
                                                              f'Kursdauer: {str(ki.wohnzimmersport04.duration)} Wochen    |    '
                                                              f'Trainer: {ki.wohnzimmersport04.trainer_name}')

label_wohnzimmersport04.grid(row=3, column=0, sticky='nswe')
label_wohnzimmersport04.config(bg=STEELBLUEZWEI, font=('arial', 14))

label_wohnzimmersport04_bg = tk.Label(windowTwo_wohnzimmersport, text='')
label_wohnzimmersport04_bg.grid(row=3, column=1, sticky='nswe')
label_wohnzimmersport04_bg.config(bg=STEELBLUEDREI)

button_wohnzimmersport04 = tk.Button(windowTwo_wohnzimmersport, text='Anmelden', font=('arial', 12), command=open_anmeldung)
button_wohnzimmersport04.grid(row=3, column=1)

windowTwo_wohnzimmersport.rowconfigure(3, weight=1)








windowTwo_wohnzimmersport.mainloop()