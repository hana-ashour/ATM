from functools import partial
from tkinter import *
import csv

file = open("ATM.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
password_counter = 3
login_window = '\0'
password_window = '\0'
menu_window = '\0'
cash_window = '\0'
balance_window = '\0'
change_window = '\0'
services_window = '\0'
fawry_window = '\0'


def save():
    filename = 'ATM.csv'
    with open(filename, 'w', newline="") as my_file:
        csvwriter = csv.writer(my_file)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)


def login_screen():
    main_window.destroy()
    global login_window
    login_window = Tk()
    login_window.title("Login Page")
    login_window.geometry("500x500")  # change size of window, and postion to be fixed
    login_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    login_image = Label(
        login_window,
        image=img1
    )
    login_image.pack()
    username = Label(login_window, text="Please enter your account number: ", font='arial')
    username.place(x=0, y=180)
    username_var = Entry(login_window, width=20, textvariable=username)
    username_var.place(x=230, y=180)
    enter = Button(login_window, text="Enter", highlightbackground="lightskyblue",
                   command=partial(login_function, username_var))
    enter.place(x=450, y=180)
    login_window.mainloop()


def password_screen(user):
    global login_window
    global password_window
    login_window.destroy()
    password_window = Tk()
    password_window.title("Password Page")
    password_window.geometry("500x500")
    password_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        password_window,
        image=img1
    )
    imgg.pack()
    password = Label(password_window, text="Please enter your password: ", font='arial')
    password.place(x=0, y=180)
    password_var = Entry(password_window, width=20, textvariable=password, show="*")
    password_var.place(x=230, y=180)
    login = Button(password_window, text="Enter", highlightbackground="lightskyblue",
                   command=partial(password_function, user=user, password=password_var))
    login.place(x=450, y=180)
    password_window.mainloop()


def cash_function(user, amount):
    global cash_window
    x = amount.get()
    if x == '':
        empty = Label(cash_window,
                      text='Please fill all details!',
                      font=('arial', 15), fg="red")
        empty.place(x=50, y=220, width=500)

    elif int(x) > 5000:
        error = Label(cash_window, text="Invalid amount, Please re-enter amount less than 5000", font='arial',
                      fg="red")
        error.place(x=50, y=220, width=500)
        amount.delete(0, 'end')

    elif int(x) <= 0:
        error3 = Label(cash_window, text='Invalid amount, Please re-enter valid amount', font='arial', fg="red")
        error3.place(x=50, y=220, width=500)
        amount.delete(0, 'end')
    elif int(x) % 100 != 0:
        error2 = Label(cash_window, text="Invalid amount, Please re-enter amount of multiples of 100", font='arial',
                       fg="red")
        error2.place(x=50, y=220, width=500)
        amount.delete(0, 'end')
    else:
        if int(user[3]) >= int(x):
            for account in rows:
                if account[0] == user[0]:
                    account[3] = (int(user[3]) - int(x))
            save()
            complete = Label(cash_window,
                             text='Successful withdrawal, thank you for using THE_ATM!\nYou will be directed to the home page by clicking on back',
                             font=('arial', 15), fg="red")
            complete.place(x=50, y=220, width=500)
            amount.delete(0, 'end')

        else:
            error4 = Label(cash_window,
                           text='No sufficient balance!\nYou will be directed to the home page by clicking on back',
                           font='arial', fg="red")
            error4.place(x=50, y=220, width=500)
            amount.delete(0, 'end')
        # main_page(user)
        # cash_window.destroy()


def cash_screen(user):
    global menu_window
    global cash_window
    menu_window.destroy()
    cash_window = Tk()
    cash_window.title("Cash withdraw")
    cash_window.geometry("500x500")
    cash_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        cash_window,
        image=img1
    )
    imgg.pack()
    money = Label(cash_window, text="Maximum amount to withdraw is 5000LE.\nAmount entered must be multiples of 100LE",
                  font='arial')
    money.place(x=0, y=0)
    enter_amount = Label(cash_window, text="Please amount to withdraw: ", font='arial')
    enter_amount.place(x=0, y=180)
    amount_var = Entry(cash_window, width=20, textvariable=enter_amount)
    amount_var.place(x=230, y=180)
    enter_button = Button(cash_window, text="Enter", highlightbackground="lightskyblue",
                          command=partial(cash_function, user=user, amount=amount_var))
    enter_button.place(x=450, y=180)
    back_button = Button(cash_window, text="Back", highlightbackground="red",
                         command=partial(back_cash_screen, user=user))
    back_button.place(x=450, y=270)
    cash_window.mainloop()


def back_cash_screen(user):
    global cash_window
    cash_window.destroy()
    main_page(user)


def balance_screen(user):
    global menu_window
    global balance_window
    menu_window.destroy()
    balance_window = Tk()
    balance_window.title("Balance inquiry")
    balance_window.geometry("500x500")
    balance_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        balance_window,
        image=img1
    )
    imgg.pack()
    balance_label = Label(balance_window, text=f'User Full name is {user[1]}.\nYour balance is {user[3]}',
                          font='arial')
    balance_label.place(x=130, y=180)
    balance_ok = Button(balance_window, text="OK", highlightbackground="lightskyblue",
                        command=partial(exit_balance, user=user))
    balance_ok.place(x=370, y=390, width=120, height=60)
    balance_window.mainloop()


def exit_balance(user):
    global balance_window
    balance_window.destroy()
    main_page(user)


def exit_change(user):
    global change_window
    change_window.destroy()
    main_page(user)


def exit_services(user):
    global services_window
    services_window.destroy()
    main_page(user)


def exit_fawry(user):
    global fawry_window
    fawry_window.destroy()
    main_page(user)


def password_change_function(user, password, password2):
    global change_window
    x = password.get()
    y = password2.get()
    if len(x) != 4 or len(y) != 4:
        len_error = Label(change_window, text="Invalid password, Please re-enter password with four digits",
                          font='arial',
                          fg="red")
        len_error.place(x=0, y=50, width=500)
        password.delete(0, 'end')
        password2.delete(0, 'end')
    elif x != y:
        same_error = Label(change_window, text="Please re-enter same passwords",
                           font='arial',
                           fg="red")
        same_error.place(x=0, y=50, width=500)
        password.delete(0, 'end')
        password2.delete(0, 'end')
    else:
        for account in rows:
            if account[0] == user[0]:
                account[2] = y
        save()
        complete = Label(change_window,
                         text='Password changed successfully.\nYou will be directed to the home page by clicking on back',
                         font=('arial', 15), fg="red")
        complete.place(x=0, y=50, width=500)


def password_change_screen(user):
    global menu_window
    global change_window
    menu_window.destroy()
    change_window = Tk()
    change_window.title("Password Change")
    change_window.geometry("500x500")
    change_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        change_window,
        image=img1
    )
    imgg.pack()
    password_change = Label(change_window, text="Please enter your four digit new password: ", font='arial')
    password_change.place(x=0, y=180)
    password_change2 = Label(change_window, text="Please re-enter your new password: ", font='arial')
    password_change2.place(x=0, y=260)
    password_change_var = Entry(change_window, width=20, textvariable=password_change, show='*')
    password_change_var.place(x=280, y=180)
    password_change2_var = Entry(change_window, width=20, textvariable=password_change2, show='*')
    password_change2_var.place(x=280, y=260)
    saved = Button(change_window, text="Save", highlightbackground="lightskyblue",
                   command=partial(password_change_function, user=user, password=password_change_var,
                                   password2=password_change2_var))
    saved.place(x=0, y=450)
    back_button = Button(change_window, text="Back", highlightbackground="red",
                         command=partial(exit_change, user=user))
    back_button.place(x=450, y=450)
    change_window.mainloop()


def services_screen(user):
    global services_window
    global menu_window
    menu_window.destroy()
    services_window = Tk()
    services_window.title("Fawry services")
    services_window.geometry("500x500")
    services_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        services_window,
        image=img1
    )
    imgg.pack()
    name = Label(services_window, text=f'Welcome {user[1]}', font='arial')
    name.place(x=0, y=0)
    orange = Button(services_window, text="Orange", highlightbackground="orange",
                    command=partial(fawry_screen, user=user))
    orange.place(x=70, y=110, width=120, height=60)
    etisalat = Button(services_window, text="Etisalat", highlightbackground="green",
                      command=partial(fawry_screen, user=user))
    etisalat.place(x=70, y=220, width=120, height=60)
    vodafone = Button(services_window, text="Vodafone", highlightbackground="red",
                      command=partial(fawry_screen, user=user))
    vodafone.place(x=340, y=110, width=120, height=60)
    we = Button(services_window, text="We", highlightbackground="purple", command=partial(fawry_screen, user=user))
    we.place(x=340, y=220, width=120, height=60)
    back_button = Button(services_window, text="Back", command=partial(exit_services, user=user))
    back_button.place(x=370, y=390, width=120, height=60)
    services_window.mainloop()


def fawry_screen(user):
    global services_window
    global fawry_window
    services_window.destroy()
    fawry_window = Tk()
    fawry_window.title("Fawry Services")
    fawry_window.geometry("500x500")
    fawry_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        fawry_window,
        image=img1
    )
    imgg.pack()
    text_print = Label(fawry_window, text="Click back to go to the services menu",
                       font='arial')
    text_print.place(x=0, y=0)
    phone_number = Label(fawry_window, text="Please enter phone number: ", font='arial')
    phone_number.place(x=0, y=180)
    phone_amount = Label(fawry_window, text="Please enter amount to pay: ", font='arial')
    phone_amount.place(x=0, y=260)
    phone_var = Entry(fawry_window, width=20, textvariable=phone_number)
    phone_var.place(x=260, y=180)
    phoneamount_var = Entry(fawry_window, width=20, textvariable=phone_amount)
    phoneamount_var.place(x=260, y=260)
    done_button = Button(fawry_window, text="Done", highlightbackground="lightskyblue",
                         command=partial(services_function, user=user, amount=phoneamount_var, phone=phone_var))
    done_button.place(x=0, y=300)
    back_button = Button(fawry_window, text="Back", highlightbackground="red",
                         command=partial(exit_fawry, user=user))
    back_button.place(x=450, y=300)
    fawry_window.mainloop()


def services_function(user, amount, phone):
    global fawry_window
    x = amount.get()
    y = phone.get()
    if x == '' or y == '':
        empty = Label(fawry_window,
                      text='Please fill all details!',
                      font=('arial', 15), fg="red")
        empty.place(x=50, y=350, width=500)
        amount.delete(0, 'end')
        phone.delete(0, 'end')
    elif int(x) <= 0:
        error3 = Label(fawry_window, text='Invalid amount, Please re-enter valid amount', font='arial', fg="red")
        error3.place(x=50, y=350, width=500)
        amount.delete(0, 'end')
    elif len(y) != 11:
        error = Label(fawry_window, text='Invalid phone number, Please re-enter valid phone number', font='arial',
                      fg="red")
        error.place(x=50, y=350, width=500)
        phone.delete(0, 'end')
    elif int(user[3]) >= int(x):
        for account in rows:
            if account[0] == user[0]:
                account[3] = (int(user[3]) - int(x))
        save()
        complete = Label(fawry_window,
                         text='Successful payment, thank you for using THE_ATM!',
                         font=('arial', 15), fg="red")
        complete.place(x=50, y=350, width=500)
        amount.delete(0, 'end')
        phone.delete(0, 'end')
    else:
        error4 = Label(fawry_window,
                       text='No sufficient balance!',
                       font='arial', fg="red")
        error4.place(x=50, y=350, width=500)
        amount.delete(0, 'end')


def main_page(user):
    global menu_window
    menu_window = Tk()
    menu_window.title("Main Menu")
    menu_window.geometry("500x500")
    menu_window.eval('tk::PlaceWindow . center')
    img1 = PhotoImage(file="subb.png")
    imgg = Label(
        menu_window,
        image=img1
    )
    imgg.pack()
    name = Label(menu_window, text=f'Welcome {user[1]}', font='arial')
    name.place(x=0, y=0)
    cash_withdraw = Button(menu_window, text="Cash withdraw", command=partial(cash_screen, user=user))
    cash_withdraw.place(x=70, y=110, width=120, height=60)
    balance_inquiry = Button(menu_window, text="Balance Inquiry", command=partial(balance_screen, user=user))
    balance_inquiry.place(x=70, y=220, width=120, height=60)
    fawry_services = Button(menu_window, text="Fawry Services", command=partial(services_screen, user=user))
    fawry_services.place(x=340, y=110, width=120, height=60)
    password_change = Button(menu_window, text="Password Change", command=partial(password_change_screen, user=user))
    password_change.place(x=340, y=220, width=120, height=60)
    exitt = Button(menu_window, text="EXIT", command=menu_window.destroy)
    exitt.place(x=370, y=390, width=120, height=60)
    menu_window.mainloop()


def password_function(user, password):
    flag = 0
    global password_counter
    global password_window
    if user[2] == password.get():
        flag = 1
        password_window.destroy()
        main_page(user)
    elif password.get() == '':
        empty = Label(password_window,
                      text='Please fill password section!',
                      font=('arial', 15), fg="red")
        empty.place(x=50, y=220, width=300)

    else:
        password_counter = password_counter - 1
        block = Label(password_window, text=f'Incorrect password,{password_counter} trial(s) left ', font='arial',
                      fg="red")
        block.place(x=50, y=220, width=300)
        password.delete(0, 'end')
    if flag == 0 and password_counter == 0:
        for account in rows:
            if account[0] == user[0]:
                account[4] = 0
        save()
        blocked()
        password_window.destroy()


def login_function(username):
    global login_window
    flag = 0
    x = username.get()
    for account in rows:
        if x == account[0]:
            user = account
            if int(account[4]) == 0:
                blocked()
                username.delete(0, 'end')
            else:
                password_screen(user)
            flag = 1
    if flag == 0:
        block = Label(login_window, text=f'Incorrect ID', font='arial',
                      fg="red")
        block.place(x=260, y=220)
        username.delete(0, 'end')


def blocked():
    block_window = Tk()
    block_window.title("Blocked Page")
    block_window.geometry("500x500")  # change size of window, and postion to be fixed
    block_window.eval('tk::PlaceWindow . center')
    block = Label(block_window, text="THIS ACCOUNT IS BLOCKED!!!", font='arial')
    block.place(x=160, y=180)
    close = Button(block_window, text="CLOSE", highlightbackground="lightskyblue", command=block_window.destroy)
    close.place(x=225, y=210)


main_window = Tk()  # to create window
main_window.title("ATM")  # change the title
main_window.geometry("500x500")  # change size of window, and postion to be fixed
main_window.eval('tk::PlaceWindow . center')
img = PhotoImage(file="main.png")
label = Label(
    main_window,
    image=img
)
label.pack()
text = Label(main_window, text="WELCOME TO OUR ATM", font=('arial', 15))
text.place(x=160, y=180)
login = Button(main_window, text="Login", command=login_screen)
login.place(x=225, y=210)
main_window.mainloop()
