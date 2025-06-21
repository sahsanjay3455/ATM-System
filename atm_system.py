# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()
# cursor.execute(
#     "create table if not exists customer (name varchar(30),acc varchar(20),bal int,pin varchar(8))"
# )
# print("table is created")


# class atm:
#     bank = "nepal bank limited"
#     branch = "mahuwan"

#     @classmethod
#     def bank_details(cls):
#         print("bank name:", cls.bank)
#         print("branch:", cls.branch)


#     def input_details_of_employee(self):
#         self.name = input("enter employee name:")
#         self.acc = input("enter employee acc/no:")
#         self.bal = int(input("enter intial bal:"))
#         if self.bal<500:
#             print('bal most be greater than 500🧐')
#             self.bal = int(input("enter intial bal:"))
            
            
#         self.pin = input("enter the pin:")

#         cursor.execute(
#             f'insert into customer values("{self.name}","{self.acc}","{self.bal}","{self.pin}")'
#         )
#         conn.commit()
#         print("data is inserted into db✅💻")

#     def employee_details(self):
#         print('1.specific employee details:')
#         print('2.all employee details:')
#         num=int(input('-----enter the choice----:'))
#         if num==1:
#             curr_pin = input("enter the pin:")
#             db_pin = cursor.execute(f'select pin from customer where pin="{curr_pin}"').fetchone()
            

#             if curr_pin == db_pin[0]:
#                 list1 = cursor.execute(
#                     f'select * from customer where pin="{curr_pin}"'
#                 ).fetchall()
#                 for item in list1:
#                     print(item)
#             else:
#                 print("pin not matched")
                
#         if num==2:
#             list1 = cursor.execute(f'select * from customer').fetchall()
#             for item in list1:
#                     print(item)
            

#     def deposite(self):
#          curr_pin = input("enter your pin🔐:")
#          db_pin = cursor.execute(f'select pin from customer where pin="{curr_pin}"').fetchone()
            

#          if curr_pin == db_pin[0]:
#              curr_bal=int(input('enter the bal:'))
#              db_bal = cursor.execute(f'select bal from customer where pin="{curr_pin}"').fetchone()
#              print('data base amount:',db_bal)
#              curr_bal+=db_bal[0]
#              cursor.execute(f'update customer set bal={curr_bal} where pin="{curr_pin}"')
#              conn.commit()
#              print('balance is depostied 💰')
             
#          else:
#             print("pin not matched")
        

#     def withdraw(self):
#         curr_pin = input("enter your pin🔐:")
#         db_pin = cursor.execute(f'select pin from customer where pin="{curr_pin}"').fetchone()
            

#         if curr_pin == db_pin[0]:
#              curr_bal=int(input('enter the bal:'))
#              db_bal = cursor.execute(f'select bal from customer where pin="{curr_pin}"').fetchone()
#              new_bal=db_bal[0]
#              if curr_bal<new_bal:
#                 new_bal-=curr_bal
#                 print('data remaining bal:',new_bal)
                
#                 cursor.execute(f'update customer set bal={new_bal} where pin="{curr_pin}"')
#                 conn.commit()
#                 print('balance is withdraw 💰')
                
#              else:
#                 print("you have no sufficient balance😩")
                 
                
#         else:
#             print("your pin is incorrect ❌")
        
#     def delete(self):
#         print('1.delete specific employee details:')
#         print('2.delete all employee details:')
#         num=int(input('-----enter the choice----:'))
#         if num==1:
#             curr_pin = input("enter the pin:")
#             db_pin = cursor.execute(f'select pin from customer where pin="{curr_pin}"').fetchone()
            

#             if curr_pin == db_pin[0]:
#                  cursor.execute(
#                     f'delete from customer where pin="{curr_pin}"'
#                 )
#                  conn.commit()
               
#             else:
#                 print("pin not matched")
                
#         if num==2:
#             cursor.execute(f'delete from customer')
#             conn.commit()

            
         
           
        
        
        
        
        
        
        
        
        


# customer1 = atm()
# while 1:
#     print("----------------------------")
#     print("1.enter the new details of employee:")
#     print("2.show the details of bank:")
#     print("3.show the employee details:")
#     print("4.Deposite amount")
#     print("5.Withdraw amount")
#     print("6.delete the details")
#     print("")

#     num = int(input("enter the choice:"))
#     if num == 1:
#         customer1.input_details_of_employee()
#     if num == 2:
#         customer1.bank_details()
#     if num == 3:
#         customer1.employee_details()
#     if num == 4:
#         customer1.deposite()
#     if num == 5:
#         customer1.withdraw()
        
#     if num==6:
#         customer1.delete()
        
#     if num > 6:
#         print("thank for visiting our app 😀❤️")
#         break


import sqlite3
import streamlit as st
from datetime import datetime

# Connect to the database
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS customer (
        name TEXT,
        acc TEXT,
        bal INTEGER,
        pin TEXT
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        acc TEXT,
        type TEXT,
        amount INTEGER,
        timestamp TEXT
    )
    """
)

# Streamlit UI
st.set_page_config(page_title="ATM System", layout="centered")
st.title("🏦 Nepal Bank Limited ATM System")
st.markdown("### Branch: Mahuwan")

menu = [
    "Enter New Employee Details",
    "Show Bank Details",
    "Show Employee Details",
    "Deposit Amount",
    "Withdraw Amount",
    "Delete Employee Details",
    "Transaction History"
]

choice = st.sidebar.selectbox("Choose an Option", menu)

# Bank Details
if choice == "Show Bank Details":
    st.subheader("🏦 Bank Details")
    st.info("""
    - **Bank Name**: Nepal Bank Limited
    - **Branch**: Mahuwan
    """)

# Insert Employee
elif choice == "Enter New Employee Details":
    st.subheader("➕ Add New Employee")
    with st.form(key='employee_form'):
        name = st.text_input("Enter employee name")
        acc = st.text_input("Enter account number")
        bal = st.number_input("Enter initial balance", min_value=0)
        pin = st.text_input("Enter 4-digit PIN", type='password')
        submit = st.form_submit_button("Add Employee")

        if submit:
            if bal < 500:
                st.error("Balance must be at least 500 🧐")
            else:
                cursor.execute("INSERT INTO customer VALUES (?, ?, ?, ?)", (name, acc, bal, pin))
                cursor.execute("INSERT INTO transactions (acc, type, amount, timestamp) VALUES (?, 'Initial Deposit', ?, ?)", (acc, bal, datetime.now().isoformat()))
                conn.commit()
                st.success("Employee data inserted into DB ✅")

# Show Employee
elif choice == "Show Employee Details":
    st.subheader("👤 Employee Details")
    option = st.radio("Choose", ["Specific", "All"])

    if option == "Specific":
        pin = st.text_input("Enter PIN to view details", type='password')
        if st.button("Fetch Details"):
            result = cursor.execute("SELECT * FROM customer WHERE pin = ?", (pin,)).fetchall()
            if result:
                st.table(result)
            else:
                st.error("PIN not found ❌")

    elif option == "All":
        result = cursor.execute("SELECT * FROM customer").fetchall()
        st.table(result)

# Deposit
elif choice == "Deposit Amount":
    st.subheader("💰 Deposit Money")
    pin = st.text_input("Enter PIN", type='password')
    deposit_amount = st.number_input("Enter deposit amount", min_value=1)
    if st.button("Deposit"):
        db_data = cursor.execute("SELECT acc, pin FROM customer WHERE pin = ?", (pin,)).fetchone()
        if db_data:
            acc = db_data[0]
            old_bal = cursor.execute("SELECT bal FROM customer WHERE pin = ?", (pin,)).fetchone()[0]
            new_bal = old_bal + deposit_amount
            cursor.execute("UPDATE customer SET bal = ? WHERE pin = ?", (new_bal, pin))
            cursor.execute("INSERT INTO transactions (acc, type, amount, timestamp) VALUES (?, 'Deposit', ?, ?)", (acc, deposit_amount, datetime.now().isoformat()))
            conn.commit()
            st.success(f"Deposited successfully! New Balance: {new_bal}")
        else:
            st.error("Incorrect PIN ❌")

# Withdraw
elif choice == "Withdraw Amount":
    st.subheader("💸 Withdraw Money")
    pin = st.text_input("Enter PIN", type='password')
    withdraw_amount = st.number_input("Enter withdrawal amount", min_value=1)
    if st.button("Withdraw"):
        db_data = cursor.execute("SELECT acc, pin FROM customer WHERE pin = ?", (pin,)).fetchone()
        if db_data:
            acc = db_data[0]
            curr_bal = cursor.execute("SELECT bal FROM customer WHERE pin = ?", (pin,)).fetchone()[0]
            if withdraw_amount <= curr_bal:
                new_bal = curr_bal - withdraw_amount
                cursor.execute("UPDATE customer SET bal = ? WHERE pin = ?", (new_bal, pin))
                cursor.execute("INSERT INTO transactions (acc, type, amount, timestamp) VALUES (?, 'Withdraw', ?, ?)", (acc, withdraw_amount, datetime.now().isoformat()))
                conn.commit()
                st.success(f"Withdrawal successful! Remaining Balance: {new_bal}")
            else:
                st.error("Insufficient Balance 😩")
        else:
            st.error("Incorrect PIN ❌")

# Delete
elif choice == "Delete Employee Details":
    st.subheader("🗑️ Delete Employee Details")
    option = st.radio("Delete Mode", ["Specific", "All"])

    if option == "Specific":
        pin = st.text_input("Enter PIN to delete", type='password')
        if st.button("Delete Employee"):
            result = cursor.execute("SELECT * FROM customer WHERE pin = ?", (pin,)).fetchone()
            if result:
                acc = result[1]
                cursor.execute("DELETE FROM customer WHERE pin = ?", (pin,))
                cursor.execute("INSERT INTO transactions (acc, type, amount, timestamp) VALUES (?, 'Delete Account', 0, ?)", (acc, datetime.now().isoformat()))
                conn.commit()
                st.success("Employee record deleted ✅")
            else:
                st.error("PIN not found ❌")

    elif option == "All":
        if st.button("Delete All Records"):
            cursor.execute("DELETE FROM customer")
            cursor.execute("DELETE FROM transactions")
            conn.commit()
            st.success("All records deleted 🗑️✅")

# Transaction History
elif choice == "Transaction History":
    st.subheader("📜 Transaction History")
    acc_filter = st.text_input("Enter account number to view transactions")
    if st.button("Show Transactions"):
        data = cursor.execute("SELECT * FROM transactions WHERE acc = ? ORDER BY timestamp DESC", (acc_filter,)).fetchall()
        if data:
            st.table(data)
        else:
            st.warning("No transactions found for this account.")
