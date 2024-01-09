# importing the required modules  
import tkinter as tk                   
from tkinter import ttk                 
from tkinter import messagebox          
import sqlite3 as sql                   
  
# defining the function to add custom_tasks to the list  
def add_custom_task():  
    # getting the string from the entry field  
    task_custom_string = TASK_entry_field.get()  
    # checking whether the string is empty or not  
    if len(task_custom_string) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        # adding the string to the custom_tasks list  
        custom_tasks.append(task_custom_string)  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('insert into custom_tasks values (?)', (task_custom_string ,))  
        # calling the function to update the list  
        list_update()  
        # deleting the entry in the entry field  
        TASK_entry_field.delete(0, 'end')  
  
# defining the function to update the list  
def list_update():  
    # calling the function to clear the list  
    clear_list()  
    # iterating through the strings in the list  
    for task in custom_tasks:  
        # using the insert() method to insert the custom_tasks in the list box  
        task_listbox.insert('end', task)  
  
# defining the function to delete a task from the list  
def delete_task():  
    # using the try-except method  
    try:  
        # getting the selected entry from the list box  
        the_value = task_listbox.get(task_listbox.curselection())  
        # checking if the stored value is present in the custom_tasks list  
        if the_value in custom_tasks:  
            # removing the task from the list  
            custom_tasks.remove(the_value)  
            # calling the function to update the list  
            list_update()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from custom_tasks where title = ?', (the_value,))  
    except:  
        # displaying the message box with 'No Item Selected' message for an exception  
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
# function to delete all custom_tasks from the list  
def delete_all_custom_tasks():  
    # displaying a message box to ask user for confirmation  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    # if the value turns to be True  
    if message_box == True:  
        # using while loop to iterate through the custom_tasks list until it's empty   
        while(len(custom_tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            custom_tasks.pop()  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('delete from custom_tasks')  
        # calling the function to update the list  
        list_update()  
  
# function to clear the list  
def clear_list():  
    # using the delete method to delete all entries from the list box  
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():  
    # printing the elements from the custom_tasks list  
    print(custom_tasks)  
    # using the destroy() method to close the application  
    guiWindow.destroy()  
  
# function to retrieve data from the database  
def retrieve_database():  
    # using the while loop to iterate through the elements in the custom_tasks list  
    while(len(custom_tasks) != 0):  
        # using the pop() method to pop out the elements from the list  
        custom_tasks.pop()  
    # iterating through the rows in the database table  
    for row in the_cursor.execute('select title from custom_tasks'):  
        # using the append() method to insert the titles from the table in the list  
        custom_tasks.append(row[0])  
  
# main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = tk.Tk()  
    # setting the title of the window  
    guiWindow.title("To-Do List Manager - BK")  
    # setting the geometry of the window  
    guiWindow.geometry("500x500+750+250")  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color to #87CEEB  
    guiWindow.configure(bg = "#87CEEB")  
  
    # using the connect() method to connect to the database  
    the_connection = sql.connect('listOfcustom_tasks.db')  
    # creating the cursor object of the cursor class  
    the_cursor = the_connection.cursor()  
    # using the execute() method to execute a SQL statement  
    the_cursor.execute('create table if not exists custom_tasks (title text)')  
  
    # defining an empty list  
    custom_tasks = []  
      
    # defining frames using the tk.Frame() widget  
    header_frame = tk.Frame(guiWindow, bg = "#87CEEB")  
    functions_frame = tk.Frame(guiWindow, bg = "#87CEEB")  
    listbox_frame = tk.Frame(guiWindow, bg = "#87CEEB")  
  
    # using the pack() method to place the frames in the application  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("SF Proverbial Gothic Bold Oblique Font", "35"),  
        background = "#87CEEB",  
        foreground = "#FFFF00"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 20, pady = 20)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#87CEEB",  
        foreground = "#000000"  
    )  
    # using the place() method to place the label in the application  
    task_label.place(x = 30, y = 40)  
      
    # defining an entry field using the ttk.Entry() widget  
    TASK_entry_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    # using the place() method to place the entry field in the application  
    TASK_entry_field.place(x = 30, y = 80)  
  
    # adding buttons to the application using the ttk.Button() widget  
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_custom_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All custom_tasks",  
        width = 24,  
        command = delete_all_custom_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    # using the place() method to set the position of the buttons in the application  
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  
    # defining a list box using the tk.Listbox() widget  
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 30,  
        height = 18,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    # using the place() method to place the list box in the application  
    task_listbox.place(x = 10, y = 20)  
  
    # calling some functions  
    retrieve_database()  
    list_update()  
    # using the mainloop() method to run the application  
    guiWindow.mainloop()  
    # establishing the connection with database  
    the_connection.commit()  
    the_cursor.close()  