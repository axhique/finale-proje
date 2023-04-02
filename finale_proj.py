

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
    def set_stock(self,stock):
         self.stock= stock
    
    def __str__(self):
        return f'FoodID :{self.foodid} \nName :{self.name} \nQuantity :{self.quantity} \nPrice :{self.price} \nDiscount :{self.discount} \nStock :{self.stock}'

adminname="aashiq"
admin_pass=1234

class Admin:
    
    food_items = []
    
    def add_food_item(self):
        foodid = int(input("Food Id :")) 
        name=input("Name of food :")
        quantity=input("Quantity :")
        price=float(input("Price :"))
        discount=float(input("Discount :"))
        stock=int(input("Stock :"))
        food_item = FoodItem(foodid ,name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print(f"Added {name} to the menu.")

    def edit_food_item(self):
        food_id = (input("Enter FoodID: "))
        for item in self.food_items:
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
                print("Food item edited successfully!\n")
                break
        print("Food item not found!\n")
    
    def view_food_items(self):
        print("List of all food items:")
        for item in self.food_items:
             print (item ,'\n')
             
    def remove_food_item(self):
        food_id = (input("Enter FoodID: "))
        for index,item in enumerate(self.food_items):
            if item.get_foodid() == food_id:
                del self.food_items[index]
                print("Food item removed successfully!\n")
                return
        print("Food item not found!\n")

class User:
    def __init__(self,userid,name,phone_no,email,address,user_password):
        self.userid=userid
        self.name=name
        self.phone_no=phone_no
        self.email=email
        self.address=address
        self.user_password=user_password
    def get_userid(self):
        return self.userid
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
users=[]      

def get_order_input():
    
    print("---------- MENU ----------")
    food_obj=Admin()
    for i in food_obj.food_items:
        print(f"{i.get_foodid()} -- {i.get_name()} --- {i.get_quantity()} -- RS{i.get_price()}")
    print("--------------------------")
    
    order_input = input("Enter the IDs of the food items you want to order (separated by commas): ")
    order_ids = order_input.strip().split(",")
    for j in order_ids:
        for item in food_obj.food_items:
            if j == item.get_foodid() :
                return j
        order_ids.append(j)
    
    else:
        print("invaid food ids ")
    return order_ids

orders=[]       

def confirm_order(order_ids):
    temp_list=[]
    print("---------- ORDER ----------")
    ad_obj=Admin()
    total_price = 0
    for i in  order_ids:
        for j in ad_obj.food_items:
            if i == j.get_foodid():
                print(f"{i.get_foodid()} -- {i.get_quantity()} -- RS{i.get_price()}")
                p=f"{i.get_foodid()} -- {i.get_quantity()} -- RS{i.get_price()}"
                total_price += i.get_price()
                temp_list.append(p)
            
    print(f"Total Price: INR {total_price}")
    print("---------------------------")
    confirm = input("Confirm your order (y/n): ")
    if confirm.lower() == "y":
        print("Order placed successfully!")
        orders.extend(temp_list)
    else:
        print("Order cancelled.")
        
def order_history():
    for i in orders:
        print(i,'\n')

def update_profile():
    uid=input("enter your usedid ")
    for i in users:
        if uid == i.get_userid():
    
            print("Enter your details below to update your profile: ")
            name = input("Name: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")
            password = input("Password: ")
            i.set_name(name)
            i.set_phone(phone)
            i.set_email(email)
            i.set_address(address)
            i.set_password(password)
            print ("profile updated successfully")
    
    
    else:
        print("User not found. Please register first.")
        
def user_registration():
        userid=input("enter your id (integers) ")
        username=input("Enter your name ")
        phone=input("enter your phone number ")
        email=input("enter email ")
        address=input("enter adress")
        password=input("enter password")
        user1=User(userid,username,phone,email,address,password)
        users.append(user1)
    
def user_login():
    name=input("Enter username ")
    passw=input("enter password ")
    for i in users:
        if name == i.get_uname() and passw ==i.get_password():
            while True:
                print (f"********welcome {i.get_uname()}********")
                choice=int(input("0.EXIT 1.place order 2.order history 3.update profile"))
                if choice ==1:
                    print("********place order*******")
                    order=get_order_input()
                    confirm_order(order)
                elif choice == 2:
                    print("*******order history*******")
                    order_history()
                elif choice == 3:
                    print("*******update profile id******")
                    update_profile()
                elif choice==0:
                    break
        else:
            print("Invalid username or password") 
            

              
def user_run():
    print("-------welcome user-------")
    
    while True:
        route=int(input('0.EXIT 1.register  2.log in'))
        if route == 1:
            print("------user registration-------")
            user_registration()
        elif route==2:
            print("------user login------")
            user_login()
        elif route==0:
            break
        
        
    
            
def admin_run():
    a_n=input("Enter admin name :")
    a_p=int(input("Enter the password"))
    ad_obj=Admin()
    if a_n == adminname and a_p == admin_pass:
      print (f"------welcome {adminname}-------")
      while True:  
        
        adc=int(input("0.EXIT   1.add   2.edit   3.view all   4.remove "))
        if adc== 1:
            print("***** add food ******")
            ad_obj.add_food_item()
        elif adc == 2:
            print("***** edit food ******")
            ad_obj.edit_food_item()
        elif adc == 3:
            print("***** view all food ******")
            ad_obj.view_food_items()
        elif adc == 4 :
            print("***** remove food ******")
            ad_obj.remove_food_item()
        elif adc==0:
            break
    else:
        print(f'Invalid Admin')



    
while True:
    choice=int(input("0.EXIT 1.Admin 2.User "))
    if choice==0:
        break
    if choice == 1:
           admin_run() 
    elif choice == 2:
            user_run()