import tkinter as tk
import tkinter.ttk as ttk
import tkinter.simpledialog as tk_dialog


class TableView(ttk.Treeview):

    def __init__(self, master, columns, data_sequences=None, index_to_select=0):
        tree_view_columns = tuple('Col ' + str(i) for i in range(1, len(columns)))
        super(TableView, self).__init__(master,
                                        selectmode='browse',
                                        columns=tree_view_columns)
        self.heading('#0', text=columns[0])
        index = 0
        for tree_view_column in tree_view_columns:
            index += 1
            self.heading(tree_view_column, text=columns[index])
        #
        self.selected_item = None
        self.item_list = []
        if data_sequences is not None:
            self.set_all_data(data_sequences, index_to_select)
        self.selection_set(self.selected_item)
        # add scroll bars:
        self.vertical_scrollbar = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        self.horizontal_scrollbar = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        self.configure(yscrollcommand=self.vertical_scrollbar.set)
        self.configure(xscrollcommand=self.horizontal_scrollbar.set)
        self.grid(row=1, column=0, sticky='nswe')
        self.vertical_scrollbar.grid(row=1, column=2, sticky='nse')
        self.vertical_scrollbar.configure(command=self.yview)
        self.horizontal_scrollbar.grid(row=2, column=0, sticky='swe')
        self.horizontal_scrollbar.configure(command=self.xview)
        # check the selection:
        self.bind('<<TreeviewSelect>>', self.check_focus)

    def check_focus(self, *args):
        current_focus_item = self.focus()
        if current_focus_item != '':
            self.selected_item = current_focus_item

    @staticmethod
    def item_as_list(item):
        result = [str(item['text'])]
        for it in item['values']:
            result.append(str(it))
        return result

    def set_all_data(self, data_sequences, index_to_select=0):
        if len(self.item_list):
            for item in self.item_list:
                self.delete(item)
            self.item_list.clear()
        #
        for data_sequence in data_sequences:
            self.item_list.append(self.insert('', 'end', text=data_sequence[0], values=data_sequence[1:]))
        #
        if len(self.item_list) > 0:
            self.selected_item = self.item_list[index_to_select]
            self.selection_set(self.selected_item)

    def get_all_data(self):
        return [self.item_as_list(self.item(item))
                for item in self.item_list]

    def get_selected_data(self):
        return self.item_as_list(
            self.item(self.selected_item))

    def set_selected_data(self, data_sequence):
        self.item(self.selected_item, text=data_sequence[0])
        self.item(self.selected_item, values=data_sequence[1:])

    def insert_and_select(self, data_sequence, index='end'):
        insert_entry = self.insert('', index, text=data_sequence[0], values=data_sequence[1:])
        self.item_list.append(insert_entry)
        self.selected_item = insert_entry
        self.selection_set(self.selected_item)

    def delete_selected(self):
        if self.selected_item is not None:
            index = self.index(self.selected_item)
            self.item_list.remove(self.selected_item)
            self.selection_remove(self.selected_item)
            self.delete(self.selected_item)
            self.selected_item = None
            return index

    def get_selected_index(self):
        if self.selected_item is not None:
            return self.index(self.selected_item)


class EditDialog(tk_dialog.Dialog):

    def __init__(self, parent, title, columns, data_sequence=None):
        self.columns = columns
        self.data_sequence = data_sequence
        self.edit_result = None
        self.column_dict = {}
        super(EditDialog, self).__init__(parent, title)

    def body(self, master):
        row = 0
        for column in self.columns:
            tk.Label(master, text=column).grid(row=row)
            entry = tk.Entry(master)
            entry.grid(row=row, column=1)
            self.column_dict[column] = entry
            row += 1

        if self.data_sequence is not None:
            data_sequence_iterator = iter(self.data_sequence)
            for entry in self.column_dict.values():
                entry.insert(0, next(data_sequence_iterator))

        return self.column_dict[self.columns[0]]

    def apply(self):
        self.edit_result = tuple(str(entry.get())
                                 for entry in self.column_dict.values())


class BaseApplication:

    def __init__(self, height, width, label_text, columns, menu=None, data_sequences=None):
        self.root = tk.Tk()
        self.root.minsize(width=width, height=height)
        self.root.grid()
        self.root.title('ZimmerSport - Admin Console')

        top_level_window = self.root.winfo_toplevel()
        top_level_window.rowconfigure(1, weight=1)
        top_level_window.columnconfigure(0, weight=1)

        self.create_menu(menu)

        self.label_text = tk.StringVar(self.root)
        self.label = tk.Label(self.root, textvariable=self.label_text).grid(row=0, column=0, sticky='w')

        self.columns = None
        self.tableView = None

        self.create_view(label_text, columns, menu, data_sequences)

    def create_menu(self, menu):
        if menu is not None:
            menu_bar = tk.Menu(self.root)
            for menu_entry in menu:
                iter_menu = iter(menu_entry)
                label = next(iter_menu)
                new_menu = tk.Menu(menu_bar, tearoff=0)
                for sub_entry in iter_menu:
                    new_menu.add_command(label=sub_entry[0], command=sub_entry[1])
                menu_bar.add_cascade(label=label, menu=new_menu)
            self.root.config(menu=menu_bar)

    def create_view(self, label_text, columns, menu=None, data_sequences=None, index_to_select=0):

        self.create_menu(menu)
        self.label_text.set(label_text)
        self.columns = columns

        self.tableView = TableView(self.root,columns=self.columns,
                                   data_sequences=data_sequences,index_to_select=index_to_select)

        self.tableView.bind('<Double-Button-1>', self.edit_action)

    def new_entry(self, *args):
        edit_dialog = EditDialog(self.root, 'New', self.columns)
        if edit_dialog.edit_result is not None:
            self.tableView.insert_and_select(edit_dialog.edit_result)
            return edit_dialog.edit_result

    def delete_entry(self, *args):
        return self.tableView.delete_selected()

    def edit_action(self, *args):
        edit_dialog = EditDialog(self.root, 'Edit', self.columns,
                                 self.tableView.get_selected_data())
        if edit_dialog.edit_result is not None:
            self.tableView.set_selected_data(edit_dialog.edit_result)
            return edit_dialog.edit_result

    def run(self):
        self.root.mainloop()
