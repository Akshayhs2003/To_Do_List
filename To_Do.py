from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List App')
        self.root.geometry('650x410+300+150')
        self.root.config(bg='#f5f5f5')

        self.label1 = Label(self.root, text='To-Do List App',
                            font='Arial, 30 bold', width=20, bd=5, bg='#3498db', fg='white')
        self.label1.pack(side="top", fill=BOTH, padx=10, pady=10)

        self.label2 = Label(self.root, text='Add Task',
                            font='Arial, 18 bold', width=10, bd=10, bg='orange', fg='#333333')
        self.label2.place(x=40, y=70)

        self.label3 = Label(self.root, text='Tasks',
                            font='Arial, 18 bold', width=10, bd=10, bg='orange', fg='#333333')
        self.label3.place(x=320, y=70)

        self.main_text = Listbox(self.root, height=9, bd=5, width=30, font="Arial, 15 bold", bg='white', selectbackground='white')
        self.main_text.place(x=280, y=120)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial, 10 bold')
        self.text.place(x=20, y=120)

        add_button = Button(self.root, text='Add Task', command=self.add_task,
                            font='Arial, 12 bold', bd=5, bg='#2ecc71', fg='white')
        add_button.place(x=15, y=200)

        delete_button = Button(self.root, text='Delete Task', command=self.delete_task,
                               font='Arial, 12 bold', bd=5, bg='#e74c3c', fg='white')
        delete_button.place(x=150, y=200)

        clear_all_button = Button(self.root, text='Clear All Tasks', command=self.clear_all_tasks,
                                  font='Arial, 12 bold', bd=5, bg='#f39c12', fg='white')
        clear_all_button.place(x=15, y=280)

        theme_button = Button(self.root, text='Switch Theme', command=self.switch_theme,
                              font='Arial, 12 bold', bd=5, bg='#8e44ad', fg='white')
        theme_button.place(x=15, y=340)

        # Set initial theme
        self.switch_theme()

    def add_task(self):
        content = self.text.get(1.0, END)
        if content.strip():
            self.main_text.insert(END, content)
            with open('savedtasks.txt', 'a') as file:
                file.write(content)
            self.text.delete(1.0, END)

    def delete_task(self):
        selected_task_index = self.main_text.curselection()
        if selected_task_index:
            self.main_text.delete(selected_task_index)
            tasks = self.main_text.get(0, END)
            with open('savedtasks.txt', 'w') as file:
                file.writelines(tasks)

    def clear_all_tasks(self):
        self.main_text.delete(0, END)
        with open('savedtasks.txt', 'w') as file:
            file.write('')

    def switch_theme(self):
        current_theme = self.root.option_get('theme', 'theme')
        new_theme = 'light' if current_theme == 'dark' else 'dark'

        # Configure the theme for the entire application
        self.root.tk_setPalette(
            background='#2c3e50' if new_theme == 'dark' else '#f5f5f5',
            foreground='#ecf0f1' if new_theme == 'dark' else '#333333'
        )

        # Configure individual elements with the new theme
        elements_to_configure = ['TButton', 'Label', 'Listbox', 'Text']
        for element in elements_to_configure:
            self.root.option_add(f'*{element}*background', '#2c3e50' if new_theme == 'dark' else '#f5f5f5')
            self.root.option_add(f'*{element}*foreground', '#ecf0f1' if new_theme == 'dark' else '#333333')

        # Set the new theme
        self.root.option_add('*theme', new_theme)

        # Update specific widget elements
        self.root.option_add('*TButton*highlightBackground', '#2ecc71' if new_theme == 'dark' else '#3498db')
        self.root.option_add('*TButton*highlightColor', '#2ecc71' if new_theme == 'dark' else '#3498db')
        self.root.option_add('*TButton*background', '#3498db' if new_theme == 'dark' else '#2ecc71')
        self.root.option_add('*TButton*foreground', 'white' if new_theme == 'dark' else '#2c3e50')
        self.root.option_add('*TButton*borderWidth', 5)
        self.root.option_add('*TButton*relief', 'flat')
        self.root.option_add('*TButton.padding', [10, 10])
        self.root.option_add('*TButton*font', 'Arial 12 bold')

        # Set initial theme
        self.root.option_add('*TButton*background', '#3498db' if new_theme == 'dark' else '#2ecc71')
        self.root.option_add('*TButton*foreground', 'white' if new_theme == 'dark' else '#2c3e50')
        self.root.option_add('*TButton*borderWidth', 5)
        self.root.option_add('*TButton*relief', 'flat')
        self.root.option_add('*TButton.padding', [10, 10])
        self.root.option_add('*TButton*font', 'Arial 12 bold')
        self.root.option_add('*TButton*highlightBackground', '#2ecc71' if new_theme == 'dark' else '#3498db')
        self.root.option_add('*TButton*highlightColor', '#2ecc71' if new_theme == 'dark' else '#3498db')

        self.root.option_add('*Label.background', '#ecf0f1' if new_theme == 'dark' else '#dcdcdc')
        self.root.option_add('*Label.foreground', '#2c3e50')

        self.root.option_add('*Listbox.background', '#34495e' if new_theme == 'dark' else '#ffffff')
        self.root.option_add('*Listbox.selectBackground', '#2ecc71' if new_theme == 'dark' else '#3498db')

        self.root.option_add('*Text.background', '#34495e' if new_theme == 'dark' else '#ffffff')

        self.root.option_add('*theme', new_theme)


if __name__ == "__main__":
    root = Tk()
    app = Todo(root)
    root.mainloop()
