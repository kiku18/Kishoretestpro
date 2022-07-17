# PYTHON ATM PROGRAM
import sqlite3


def widthdraw_cash(pini):
    amount = int(input("Enter the amount of money you want to withdraw: "))
    conn = sqlite3.connect(r'C:\Users\kumar\atm.db')
    cur = conn.cursor()
    sql = f"select balance from userdata where pin={pini}"
    print(sql)
    o = cur.execute(sql)
    for a in o:
        amt = a
    amtv = amt[0]
    conn.commit()
    cur.close()
    balanceupdate(amount, pini, amtv)


def balanceupdate(amount,pini,amtv):
    conn = sqlite3.connect(r'C:\Users\kumar\atm.db')
    cur = conn.cursor()
    baln = amtv - amount
    sql = f"update userdata set balance ={baln} where pin ={pini}"
    print(sql)
    cur.execute(sql)
    conn.commit()
    cur.close()

    if amount >amtv:
        print("You don't have sufficient balance to make this withdrawal")

def balance_enquiry(pini):
    conn = sqlite3.connect(r'C:\Users\kumar\atm.db')
    cur = conn.cursor()
    sql = f"select balance from userdata where pin={pini}"
    o = cur.execute(sql)
    for a in o:
        amt = a
    print(f"Total balance {amt[0]} Rupees")
    conn.commit()
    cur.close()


def checkpin(pini):
    is_quit = False
    conn=sqlite3.connect(r'C:\Users\kumar\atm.db')
    cur=conn.cursor()
    sql=f"select pin from userdata where pin={pini}"
    o=cur.execute(sql)
    user=o.fetchone()
    if user is None:
        print("User pin is not available in the system")
    else:
        while is_quit == False:
            print("what do you want to do")
            print(" Enter 1 to Withdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Quit")

            query = int(input("Enter the number corresponding to the activity you want to do: "))

            if query == 1:
                widthdraw_cash(pini)
            elif query == 2:
                balance_enquiry(pini)
            elif query == 3:
                is_quit = True

            else:
                print("Please enter a correct value shown")


print("Welcome to the Bank of Puruda ATM")
pini = int(input('Please enter your four digit pin: '))
checkpin(pini)









