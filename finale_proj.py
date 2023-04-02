""" project contains two main paths Admin and user :
Admin:
        admin is predefined and can only login not register . admin can perform actions such as add, edit,
        view and delete  food items    from Menu
            adminname="aashiq"  password=1234
        
user:
        user have to register first , only after that user can perform actions such as 
        order food ,view order history  and  update the profile 

"""
import re

users=[]      
food_items = [] 
class FoodItem:
    def __init__(self,foodid, name, quantity, price, discount, stock):
        self.foodid=foodid
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
     
    def get_foodid(self):
        return self.foodid
    def set_name(self,name):
        self.name =name
    def get_name(self):
        return self.name
    def set_quantity(self,quantity):
         self.quantity = quantity
    def get_quantity(self):
        return self.quantity 
    def set_price(self,price):
         self.price = price
    def get_price(self):
         return self.price 
    def set_discount(self,discount):
         self.discount = discount
    def get_discount(self):
        return self.discount
    def set_stock(self,stock):
         self.stock= stock
    
    def __str__(self):
        return f'FoodID :{self.foodid} \nName :{self.name} \nQuantity :{self.quantity} \nPrice :{self.price} \nDiscount :{self.discount} \nStock :{self.stock}'


    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#admin functions:
class Admin:
    adminname="aashiq"
    admin_pass=1234

    def add_food_item(self):  
        print("Taken IDs are  :",end="")
        for k in food_items:
            print(k.get_foodid(),end=',')
        try:           
            foodid=int(input("\nEnter a food id (integer)  "))
            name=input("Name of food :")
            quantity=input("Quantity :")
            price=float(input("Price :"))
            discount=float(input("Discount :"))
            stock=(input("Stock :"))
            food_item = FoodItem(foodid ,name, quantity, price, discount, stock)
            food_items.append(food_item)
            print()
            print(f"Added {name} to the menu.")
        except:
            print("enter proper details .")
        


    def edit_food_item(self):
        for i in food_items:
            print(f"{i.get_foodid()}.{i.get_name()}",end=' ')
        food_id = int(input("\nEnter FoodID: "))
        for item in food_items:
            if food_id == item.get_foodid():
                nm = input(f"Enter new name : ") 
                item.set_name(nm)
                q= input(f"Enter new quantity : ")
                item.set_quantity(q)
                p= float(input(f"Enter new price : "))
                item.set_price(p)
                di= float(input(f"Enter new discount : "))
                item.set_discount(di)
                st = int(input(f"Enter new stock : "))
                item.set_stock(st)
                print()
                print("Food item edited successfully!\n")
                return
            
        print("Food item not found!\n")

    def view_food_items(self):
        if len(food_items)>0:
            print("List of all food items:")
            for item in food_items:
                    print (item ,'\n')
        else:
            print("No food items available")
                
    def remove_food_item(self):
        food_id = int(input("Enter FoodID: "))
        for index,item in enumerate(food_items):
            if item.get_foodid() == food_id:
                del food_items[index]
                print()
                print("Food item removed successfully!\n")
                return
        print("Food item not found!\n")
        
#--------------------------------------------------------------------------------------------------------------------------------

#user functions

  
class User:
    def __init__(self,name,phone_no,email,address,user_password):
        
        self.name=name
        self.phone_no=phone_no
        self.email=email
        self.address=address
        self.user_password=user_password
        self.orders=[]     
        
    def get_uname(self):
        return self.name
    def set_uname(self,name):
        self.name=name  
    def set_phone(self,phno):
        self.phone_no=phno
    def set_email(self,email):
        self.email=email
    def set_address(self,address):
        self.address=address
    def set_password(self,password):
        self.user_password=password
    def get_password(self):
        return self.user_password
    

    def place_order(self):
        print("---------- MENU ----------")
        print( "Id -- food --- quantity --- price ")
        if len(food_items) ==0 :
            print("No food available")
        else:
            for i in food_items:
                print(f"{i.get_foodid()} -- {i.get_name()} --- {i.get_quantity()} -- RS{i.get_price()}")
            print("--------------------------")
            order_input =input("Enter the IDs of the food items you want to order (separated by commas): ").split(",")
            order=[]
            for i in order_input:
                order.append(int(i))
            
            temp_list=[]
            print("---------- ORDER ----------")
            price = 0
            discount = 0
            for i in order:
                for j in food_items:
                    if i == j.get_foodid():
                        print(f"{j.get_foodid()} -- {j.get_name()} -- {j.get_quantity()} -- Rs {j.get_price()}")
                        p=f"{j.get_foodid()} -- {j.get_name()} -- {j.get_quantity()} -- Rs {j.get_price()}"
                        price += j.get_price()
                        discount += j.get_discount()
                        temp_list.append(p)
            final_price=price-discount      
            print(f"Price: Rs {price}")
            print(f"Discount: Rs {discount}")
            print(f"Final price: Rs {final_price}")
            t=f"Final Price: Rs {final_price}\n"
            temp_list.append(t)
            print("---------------------------")
            while True:
                confirm = input("Confirm your order (y/n): ")
                if confirm.lower() == "y":
                    print("Order placed successfully!")
                    self.orders.extend(temp_list)
                    break
                elif  confirm.lower() == "n":
                    print("Order cancelled.")
                    break
                else:
                    print("Enter valid key")

    def order_history(self):
        for i in self.orders:
            print(i)
        print()
        
    def update_profile(self):
        
        print("Enter your details below to update your profile: ")
        name = input("Name: ").lower()
        phone_input = input("Phone number: ")
        phone = re.match(r"^[6-9][0-9]{9}$", phone_input)
        email_input = input("Email: ")
        email = re.match(r"^[a-z0-9]+@{1}[a-z]+\.[a-z]+$", email_input)
        address = input("Address: ")
        password = input("Password: ")
        if phone and email and password:
            self.name=name
            self.phone_no=phone
            self.email=email
            self.address=address
            self.user_password=password
            print ("profile updated successfully")
            return
        else:
            print("Invalid phone number or email address.")
            print("updation failed :(")
            
            
def user_registration():
    username = input("Name: ").lower()
    phone_input = input("Phone number: ")
    phone = re.match(r"^[6-9][0-9]{9}$", phone_input)
    email_input = input("Email: ")
    email = re.match(r"^[a-z0-9]+@{1}[a-z]+\.[a-z]+$", email_input)
    address = input("Address: ")
    password = input("Password: ")
    if phone and email and password:
        users.append(User(username, phone_input, email_input, address, password))
        print("Registered successfully!")
    else:
        print("Invalid phone number or email address.")
        print("Registartion failed :(")


    
def user_login():
    name=input("Enter username ").lower()
    passw=input("enter password ")
    for i in users:
        if name == i.get_uname() and passw ==i.get_password():
            while True:
                print (f"---------welcome {i.get_uname()}----------")
                choice=int(input("0.EXIT 1.place order 2.order history 3.update profile  "))
                if choice ==1:
                    print("---------place order---------")
                    i.place_order()
                elif choice == 2:
                    print("--------order history---------")
                    i.order_history()
                elif choice == 3:
                    print("--------update profile id--------")
                    i.update_profile()
                elif choice==0:
                    break
                else :
                    print("enter a valid key")

    else:
        print("user not fount, Register first")
        
    
def user_run():
    while True:
        print("------- Welcome -------")
        route=int(input('0.EXIT 1.register  2.log in '))
        if route == 1:
            print("------user registration-------")
            user_registration()
        elif route==2:
            print("------user login------")
            user_login()
        elif route==0:
            break
        else:
            print("enter a valid key")
        
            
def admin_run():
    try:
        admin=Admin()
        a_n=input("Enter admin name  ")
        a_p=int(input("Enter the password  "))
        if a_n == admin.adminname and a_p == admin.admin_pass:
            print (f"------welcome {admin.adminname}-------")
            while True:  
                try:
                    adc=int(input("0.EXIT   1.add   2.edit   3.view all   4.remove "))
                    
                    if adc== 1:
                        print("------ add food ------")
                        admin.add_food_item()
                    elif adc == 2:
                        print("------ edit food -------")
                        admin.edit_food_item()
                    elif adc == 3:
                        print("------ view all food --------")
                        admin.view_food_items()
                    elif adc == 4 :
                        print("-------- remove food --------")
                        admin.remove_food_item()
                    elif adc==0:
                        break
                    else:
                        print ("    enter a valid key")
                except:
                    print("invalid opretaion")
            
    except:
            print(f'Invalid Admin')



    
while True:
    try:
        choice=int(input("0.EXIT 1.Admin 2.User "))
        if choice == 0:
            break
        if choice == 1:
            admin_run() 
        elif choice == 2:
            user_run()
    except:
        print("Invalid key")