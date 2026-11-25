import database
import math


def gettext(text):
    while(True):
        if(text.strip()!=""):
            return text.strip()
        else:
            print("This field is mandatory")
            text=input("Enter properly :")

        
def getprice(number):
    while(True):
        try:
            if(number.strip()==""):
                print("This field is mandatory")
            elif(float(number)<=0 or not math.isfinite(float(number))):
                print("Number should be greater than zero")
            else:
                return float(number)
            
        except ValueError:
            print("This field cannot contain letters")
        number=input("Enter properly :")


def getquantity(number):
    while(True):
        try:
            if(number.strip()==""):
                print("This field is mandatory")
            elif(int(number)<0):
                print("Number should not be negative")
            else:
                return int(number)
            
        except ValueError:
            print("This field should contain only whole numbers")
        number=input("Enter properly :")


def getnumber(number):
    while(True):
        try:
            if(number.strip()==""):
                print("This field is mandatory")
            elif(int(number)<=0):
                print("Number should be greater than zero")
            else:
                return int(number)
            
        except ValueError:
            print("This field should contain only whole numbers")
        number=input("Enter properly :")


def getproductnames(text):
    productnames=[]
    productnames=database.getproductnames()
    while(True):
        if(text.strip()==""):
            print("This field is mandatory")
        elif(text.strip()  in productnames):
            print("This product name already exists")
        else:
            return text.strip()
        text=input("Enter properly :")


def getcategoryname(text):
    categorynames=[]
    categorynames=database.getcategorynames()

    while(True):
        if(text.strip()==""):
            print("This field is mandatory")
        elif(text.strip() in categorynames):
            print("This category name already exists")
        else:
            return text.strip()
        text=input("Enter properly :")


def getcategoryproductconnectionvalidation(category):
    categorynames=[]
    categorynames=database.getcategorynames()
    while(True):
        if(category.lower().strip() in categorynames):
            return category.lower().strip()
        elif(category.lower().strip()==""):
            print("This field is mandatory")
        else:
            print("Choose from category names")
        for i in categorynames:
            print(i)
        category=input("Enter properly :")
