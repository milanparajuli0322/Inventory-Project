import database

def gettext(text):
    while(True):
        while(text.strip()!=""):
            return text.strip()
        else:
            print("This field is mandatory")
            text=input("Enter properly :")
        
def getprice(number):
    while(True):
        try:
            while(number.strip()!="" and float(number)>0):
                return float(number)
            else:
                print("This field is mandatory and should be more than 0")
                number=input("Enter properly :")
        except ValueError:
            print("This field cannot contain letters")
            number=input("Enter properly :")

def getquantity(number):
    while(True):
        try:
            while(number.strip()!="" and int(number)>=0):
                return int(number)
            else:
                print("This field is mandatory and should not be negative")
                number=input("Enter properly :")
        except ValueError:
            print("This field cannot contain letters")
            number=input("Enter properly :")

def getnumber(number):
    while(True):
        try:
            while(number.strip()!="" and int(number)>0):
                return int(number)
            else:
                print("This field is mandatory and should enter positive whole numbers")
                number=input("Enter properly :")
        except ValueError:
            print("This field should contain only positive whole numbers")
            number=input("Enter properly :")

def product():
    while(True):
        productsmenu=["Sub Menu","1.Add Products","2.View All Products","3.Search Products","4.Update Product","5.Delete Product","6.Back to main menu"]
        for i in productsmenu:
            print(i)
        productoption=input("Enter the operation number :")
        productoption=getnumber(productoption)

        match productoption:
            case 1:
                productname=input("Enter the product name :")
                productname=gettext(productname)

                category=input("Enter the category :")
                category=gettext(category)

                supplier=input("Enter the supplier :")
                supplier=gettext(supplier)

                purchaseprice=input("Enter the purchase price :")
                purchaseprice=getprice(purchaseprice)

                sellingprice=input("Enter the selling price :")
                sellingprice=getprice(sellingprice)

                initialstockquantity=input("Enter the initial stock quantity :")
                initialstockquantity=getquantity(initialstockquantity)

                minimumstocklevel=input("Enter the minimum stock level :")
                minimumstocklevel=getquantity(minimumstocklevel)
                database.add_product(productname,category,supplier,purchaseprice,sellingprice,initialstockquantity,minimumstocklevel)

            case 2:
                print("All Infomation")
                database.view_products()

            case 3:
                searchproductname=input("Enter the product name to search :")
                searchproductname=gettext(searchproductname)
                database.search_products(searchproductname)

            case 4:
                updateproductid=input("Enter the product id to update :")
                updateproductid=getnumber(updateproductid)

                if(database.check_productid(updateproductid)==1):
                    updateproductname=input("Enter the new product name :")
                    updateproductname=gettext(updateproductname)

                    updatecategory=input("Enter the new category :")
                    updatecategory=gettext(updatecategory)

                    updatesupplier=input("Enter the new supplier :")
                    updatesupplier=gettext(updatesupplier)

                    updatepurchaseprice=input("Enter the new purchase price :")
                    updatepurchaseprice=getprice(updatepurchaseprice)

                    updatesellingprice=input("Enter the new selling price :")
                    updatesellingprice=getprice(updatesellingprice)

                    updateinitialstockquantity=input("Enter the new initial stock quantity :")
                    updateinitialstockquantity=getquantity(updateinitialstockquantity)

                    updateminimumstocklevel=input("Enter the new minimum stock level :")
                    updateminimumstocklevel=getquantity(updateminimumstocklevel)
                    database.update_products(updateproductname,updatecategory,updatesupplier,updatepurchaseprice,updatesellingprice,updateinitialstockquantity,updateminimumstocklevel,updateproductid)
                    
            case 5:
                deleteproductid=input("Enter the product id to delete :")
                deleteproductid=getnumber(deleteproductid)

                if(database.check_productid(deleteproductid)==1):
                    ch=input("Enter y to continue deletion , n to stop deletion")
                    ch=gettext(ch)

                    if(ch=="y"):
                        database.delete_product(deleteproductid)
                    elif(ch=="n"):
                        print("Deletion stopped")
                    else:
                        print("Choose either y or n")

            case 6:
                break

            case _:
                print("Please enter option from 1 to 6")
