from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650x410+300+150')

        self.label1 = Label(self.root, text='To-Do-List-App',
                            font='Arial, 25 bold', width=10, bd=5, bg='#3498db', fg='white')
        self.label1.pack(side="top", fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='Arial, 18 bold', width=10, bd=10, bg='#ecf0f1', fg='#2c3e50')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='Arial, 18 bold', width=10, bd=10, bg='#ecf0f1', fg='#2c3e50')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="italic, 15 bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial, 10 bold')
        self.text.place(x=20, y=120)

        # ===============ADDING TASKS============#

        def add():
            content = self.text.get(1.0, END)
            if content.strip():  # Check if content is not empty or whitespace
                self.main_text.insert(END, content)
                with open('savedtasks.txt', 'a') as file:
                    file.write(content)
                self.text.delete(1.0, END)  # Clear the text input after adding

        add_button = Button(self.root, text='Add Task', command=add,
                            font='italic, 12 bold', bd=5, bg='#2ecc71', fg='white')
        add_button.place(x=30, y=180)

        # ===============DELETING TASKS============#

        def delete():
            selected_task_index = self.main_text.curselection()
            if selected_task_index:
                self.main_text.delete(selected_task_index)
                tasks = self.main_text.get(0, END)
                with open('savedtasks.txt', 'w') as file:
                    file.writelines(tasks)

        delete_button = Button(self.root, text='Delete Task', command=delete,
                               font='italic, 12 bold', bd=5, bg='#e74c3c', fg='white')
        delete_button.place(x=30, y=280)

if __name__ == "__main__":
    root = Tk()
    app = Todo(root)
    root.mainloop()
