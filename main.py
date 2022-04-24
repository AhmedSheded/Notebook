from tkinter import *
from database import *


def submit():
    head = title.get('1.0', END)
    body = subject.get('1.0', END)
    mycursor.execute("INSERT Notes(title, subject, created_date) VALUES(%s, %s, %s)", (head, body, datetime.now()))
    db.commit()
    title.delete('1.0', END)
    subject.delete('1.0', END)


def get_all_notes():
    old_notes = Tk()
    old_notes.config(padx=25, pady=25)
    mycursor.execute('SELECT * FROM Notes')

    row=0
    column=0
    for x in mycursor:
        frame = Frame(old_notes, bd=3, relief=RAISED, padx=20, pady=20, bg='light yellow', width=50, height=50)
        frame.grid(row=row, column=column)
        Label(frame, text=x[1], pady=5, padx=5, bg='light yellow', font=('Arial', 25)).pack()
        Label(frame, text=x[2], pady=5, padx=5, bg='light yellow', font=('Ink Free', 20)).pack()
        Label(frame, text=x[3], pady=5, padx=5, bg='light yellow').pack()
        column += 1
        if column > 4:
            row+=1
            column=0

    window.destroy()





window = Tk()
window.title('Notebook')
Label(window, text='Title').pack()
title = Text(window, bg='light yellow', font=('Arial', 25), height=1, width=30, pady=5, padx=5)
title.pack()
Label(window, text='Subject').pack()
subject = Text(window, bg='light yellow', font=('Ink Free', 20), height=15, width=30
               , padx=20,
               pady=20,
               fg='purple')
subject.pack()

button = Button(window, command=submit, text='save note')
button.pack(side='left')
Button(window, command=get_all_notes, text='Old notes').pack(side='right')


window.mainloop()


