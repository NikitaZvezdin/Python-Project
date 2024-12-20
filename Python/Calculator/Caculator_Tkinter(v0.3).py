from tkinter import *
windows = Tk()
windows['bg'] = '#000000'
windows.title('Calculator')
windows.geometry('400x500')
windows.resizable(height=False, width=False)
icon = PhotoImage(file='logocalculation.png')
windows.iconphoto(False, icon)

entry = Entry(windows, font=('Amstrad CPC464', 36), fg='#000000', bg='#39FF14')
entry.pack(fill=X, pady=40)
entry.insert(END, '>')

frame_button = Frame(windows, bg='#39FF14')
frame_button.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.7)
def add_0():
    entry.insert(END, '0')
def add_1():
    entry.insert(END, '1')
def add_2():
    entry.insert(END, '2')
def add_3():
    entry.insert(END, '3')
def add_4():
    entry.insert(END, '4')
def add_5():
    entry.insert(END, '5')
def add_6():
    entry.insert(END, '6')
def add_7():
    entry.insert(END, '7')
def add_8():
    entry.insert(END, '8')
def add_9():
    entry.insert(END, '9')
def add_plus():
    entry.insert(END, '+')
def add_minus():
    entry.insert(END, '-')
def add_multiply():
    entry.insert(END, '*')
def add_share():
    entry.insert(END, '/')
def add_evenly():
    entry.insert(END, '=')
def add_evenly():
    input_entry = entry.get()[1:]
    input_entry = input_entry.replace(' ', '')
    try:
        result = eval(input_entry)
        entry.delete(0, END)
        entry.insert(END, '>')
        entry.insert(END, result)
    except ZeroDivisionError as e:
        entry.delete(0, END)
        entry.insert(END, '>')
        entry.insert(END, 'ERROR')
    except SyntaxError as e:
        entry.delete(0, END)
        entry.insert(END, '>')
        entry.insert(END, 'ERROR')
btn_0 = Button(frame_button, text='0', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_0)
btn_0.place(x=210, y=20, width=50, height=50)

btn_1 = Button(frame_button, text='1', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_1)
btn_1.place(x=210, y=80, width=50, height=50)

btn_2 = Button(frame_button, text='2', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_2)
btn_2.place(x=210, y=140, width=50, height=50)

btn_3 = Button(frame_button, text='3', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_3)
btn_3.place(x=210, y=200, width=50, height=50)

btn_4 = Button(frame_button, text='4', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_4)
btn_4.place(x=210, y=260, width=50, height=50)

btn_5 = Button(frame_button, text='5', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_5)
btn_5.place(x=150, y=20, width=50, height=50)

btn_6 = Button(frame_button, text='6', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_6)
btn_6.place(x=150, y=80, width=50, height=50)

btn_7 = Button(frame_button, text='7', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_7)
btn_7.place(x=150, y=140, width=50, height=50)

btn_8 = Button(frame_button, text='8', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_8)
btn_8.place(x=150, y=200, width=50, height=50)

btn_9 = Button(frame_button, text='9', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_9)
btn_9.place(x=150, y=260, width=50, height=50)

btn_plus = Button(frame_button, text='+', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_plus)
btn_plus.place(x=50, y=20, width=50, height=50)

btn_minus = Button(frame_button, text='-', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_minus)
btn_minus.place(x=50, y=80, width=50, height=50)

btn_multiply = Button(frame_button, text='*', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_multiply)
btn_multiply.place(x=50, y=140, width=50, height=50)

btn_share = Button(frame_button, text='/', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_share)
btn_share.place(x=50, y=200, width=50, height=50)

btn_evenly = Button(frame_button, text='=', bg='#000000', fg='#39FF14', borderwidth = 0, font=('Amstrad CPC464', 14), command=add_evenly)
btn_evenly.place(x=50, y=260, width=50, height=50)
windows.mainloop()


