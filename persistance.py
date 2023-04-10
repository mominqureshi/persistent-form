# Tkinter Project
import tkinter as tk
import sqlite3
from sqlite3 import Error


def create_database():
    conn = sqlite3.connect('customers.db')
    conn.close()


# create a table, remember to comment after creating table to avoid errors
conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE general_info(name PRIMARY KEY, DOB TEXT, gender TEXT, address TEXT,
cell INTEGER)''')
cursor.execute('''CREATE TABLE medical_info(blood TEXT, allergy TEXT, emrg INTEGER, med_Con TEXT,
illness TEXT)''')
conn.commit()
conn.close()


# create functions that add data
def add_person(name, DOB, gender, address, phone_num):
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO general_info(name, DOB, gender, address, cell) VALUES (?, ?, ?, ?, ?)",
                    (name, DOB, gender, address, phone_num))

    conn.commit()
    conn.close()

def add_person2(name, blood_type, allergies, contact, med_conditions, illness):
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medical_info(name, blood, allergy, emrg, med_Con, illness) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, blood_type, allergies, contact, med_conditions, illness))
    conn.commit()
    conn.close()


class App(tk.Tk):
    def __init__(root, *args, **kwargs):
        tk.Tk.__init__(root, *args, **kwargs)

        root.title("TTC Medical Database")
        root.geometry("700x600")

        root.frames = {}
        for F in (Frame0, Frame1, Frame2):
            frame = F(root)
            root.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        root.show_frame(Frame0)

        # defining the menu and submenu 

        menu = tk.Menu(root)
        root.config(menu=menu)

        Page_menu = tk.Menu(menu)
        menu.add_cascade(label="Page", menu=Page_menu)
        Page_menu.add_command(label="Welcome", command=lambda: root.show_frame(Frame0))
        Page_menu.add_command(label="General Information", command=lambda: root.show_frame(Frame1))
        Page_menu.add_command(label="Medical Information", command=lambda: root.show_frame(Frame2))

        def quit_app():
            root.destroy()

        Quit_menu = tk.Menu(menu)
        menu.add_cascade(label='Quit', menu=Quit_menu)
        Quit_menu.add_command(label="Quit App", command=quit_app)

    def show_frame(root, cont):
        frame = root.frames[cont]
        frame.tkraise()


# Making a window for the instructions on how to use the application 

class Frame0(tk.Frame):
    def __init__(root, parent):
        tk.Frame.__init__(root, parent)

        instruction_label = tk.Label(root, text='You can switch between windows using the menu bar on top.')
        instruction_label.grid(row=1, column=0, sticky=tk.W)

        i2_label = tk.Label(root, text='The menu bar can also be used to quit the application.')
        i2_label.grid(row=2, column=0, sticky=tk.W)
        
        i3_label = tk.Label(root, text='To add data to the database press the "Add Data" button')
        i3_label.grid(row=3, column=0, sticky=tk.W)


# Making the second window that will be used for more general information like name, DOB etc

class Frame1(tk.Frame):
    
    def __init__(root, parent):
        tk.Frame.__init__(root, parent)

        General_label = tk.Label(root, text='General Information')
        General_label.grid(row=0, column=2, sticky=tk.W)

        name_label = tk.Label(root, text='Name')
        name_label.grid(row=3, column=0, sticky=tk.W)
        name_entry = tk.Entry(root)
        name_entry.grid(row=3, column=1)

        DOB_label = tk.Label(root, text='Date of Birth')
        DOB_label.grid(row=4, column=0, sticky=tk.W)
        DOB_entry = tk.Entry(root)
        DOB_entry.grid(row=4, column=1)

        Gender_label = tk.Label(root, text='Gender')
        Gender_label.grid(row=5, column=0, sticky=tk.W)
        # Making the selectiong menu for the gender tab
        gender_options = ['Male', 'Female', 'Prefer not to disclose']
        gender_var = tk.StringVar(root)
        gender_var.set(gender_options[0])
        gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
        gender_menu.grid(row=5, column=1)

        address_label = tk.Label(root, text='Address')
        address_label.grid(row=6, column=0, sticky=tk.W)
        address_entry = tk.Entry(root)
        address_entry.grid(row=6, column=1)

        cell_label = tk.Label(root, text='Phone Number:')
        cell_label.grid(row=7, column=0, sticky=tk.W)
        cell_entry = tk.Entry(root)
        cell_entry.grid(row=7, column=1)
        
        add_button = tk.Button(root, text='Add Data', command=lambda: root.add_data(name_entry.get(),DOB_entry.get(),gender_var.get(),address_entry.get(),cell_entry.get()))
        add_button.grid(row=8, column=4)
           
        def add_data(root, name, DOB, gender, address, phone_num):
            add_person(name, DOB, gender, address, phone_num)        


# Making the third window that will have the medical information 

class Frame2(tk.Frame):
    def __init__(root, parent):
        tk.Frame.__init__(root, parent)

        Medical_label = tk.Label(root, text='Medical Information')
        Medical_label.grid(row=0, column=1, sticky=tk.W)

        blood_label = tk.Label(root, text='Blood Type')
        blood_label.grid(row=1, column=0, sticky=tk.W)
        blood_entry = tk.Entry(root)
        blood_entry.grid(row=1, column=1)

        allergy_label = tk.Label(root, text='Allergies ')
        allergy_label.grid(row=2, column=0, sticky=tk.W)
        allergy_entry = tk.Entry(root)
        allergy_entry.grid(row=2, column=1)

        emrg_label = tk.Label(root, text='Emergency Contact')
        emrg_label.grid(row=3, column=0, sticky=tk.W)
        emrg_entry = tk.Entry(root)
        emrg_entry.grid(row=3, column=1)

        med_Con_label = tk.Label(root, text='Medical Conditions')
        med_Con_label.grid(row=4, column=0, sticky=tk.W)
        med_Con_entry = tk.Entry(root)
        med_Con_entry.grid(row=4, column=1)

        ill_label = tk.Label(root, text='Any illness you suffered from recently?')
        ill_label.grid(row=5, column=0, sticky=tk.W)

        # Defining a funtion for the entry box to pop up if other is selected
        def entry_box(selection):
            if selection == 'Other':
                entry_label = tk.Label(root, text='Please specify the illness:')
                entry_label.grid(row=6, column=0, sticky=tk.W)

                entry_box = tk.Entry(root)
                entry_box.grid(row=6, column=1)
            else:
                try:
                    entry_label.destroy()
                    entry_box.destroy()
                except:
                    pass
                    # Making a drop down menu for the illnesses

        ill_options = ['None', 'COVID 19', 'Monkey Pox', 'Flu', 'Other']
        ill_var = tk.StringVar(root)
        ill_var.set(ill_options[0])
        ill_menu = tk.OptionMenu(root, ill_var, *ill_options, command=entry_box)
        ill_menu.grid(row=5, column=1)
        
        add_button = tk.Button(root, text='Add Data', command=lambda: root.add_data(name_entry.get(),DOB_entry.get(),gender_var.get(),address_entry.get(),cell_entry.get()))
        add_button.grid(row=6, column=4)
           
        def add_data(root, name, DOB, gender, address, phone_num):
            add_person(name, DOB, gender, address, phone_num)         

        def quit_app():
            root.destroy()
            root.quit()

        quit = tk.Button(root, text='Quit App', command=quit_app)
        quit.grid(row=7, column=3, sticky=tk.W)


if __name__ == "__main__":
    app = App()
    app.mainloop()
