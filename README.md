# To_Do_List
This is a simple To-Do List application built using the Tkinter library in Python. Here's a breakdown of the key features and components of the code:

1. Tkinter GUI:
   - The GUI (Graphical User Interface) is created using Tkinter, a standard GUI toolkit in Python.

2. Labels:
   - Three labels are added for the title, "Add Task" section, and "Tasks" section.

3. Listbox and Text Widgets:
   - A Listbox widget (`self.main_text`) is used to display the list of tasks.
   - A Text widget (`self.text`) is used for the user to input new tasks.

4. Adding Tasks:
   - The `add` function is called when the "Add Task" button is pressed.
   - It retrieves the content from the Text widget (`self.text`), checks if it's not empty, adds the content to the Listbox, and appends the task to a file named 'savedtasks.txt'.

5. Deleting Tasks:
   - The `delete` function is called when the "Delete Task" button is pressed.
   - It gets the index of the selected task in the Listbox (`self.main_text`), deletes the task from the Listbox, and updates the 'savedtasks.txt' file accordingly.

6. Main Application Loop:
   - The Tkinter main loop (`root.mainloop()`) is used to run the application.

7. Styling:
   - The GUI elements are styled using various font sizes, colors, and positioning.

8. File Handling:
   - The tasks are saved and loaded from a file named 'savedtasks.txt'. The file is opened in append mode when adding tasks and in write mode when deleting tasks.

Overall, this application provides a basic To-Do List functionality with the ability to add and delete tasks, and it persists the tasks in a text file for future sessions.
