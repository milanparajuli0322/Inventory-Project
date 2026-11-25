import database
import validator


def product():
    while(True):
        productsmenu=["Sub Menu","1.Add Products","2.View All Products","3.Search Products","4.Update Product","5.Delete Product","6.Back to main menu"]
        for i in productsmenu:
            print(i)
        productoption=input("Enter the operation number :")
        productoption=validator.getnumber(productoption)

        match productoption:
            case 1:
                productname=input("Enter the product name :").strip().lower()
                productname=validator.getproductnames(productname)

                categorynames=[]
                categorynames=database.getcategorynames()
                for i in categorynames:
                    print(i)
                category=input("Enter the category :").strip().lower()
                category=validator.getcategoryproductconnectionvalidation(category)

                supplier=input("Enter the supplier :").strip().lower()
                supplier=validator.gettext(supplier)

                purchaseprice=input("Enter the purchase price :")
                purchaseprice=validator.getprice(purchaseprice)

                sellingprice=input("Enter the selling price :")
                sellingprice=validator.getprice(sellingprice)

                initialstockquantity=input("Enter the initial stock quantity :")
                initialstockquantity=validator.getquantity(initialstockquantity)

                minimumstocklevel=input("Enter the minimum stock level :")
                minimumstocklevel=validator.getquantity(minimumstocklevel)
                database.add_product(productname,category,supplier,purchaseprice,sellingprice,initialstockquantity,minimumstocklevel)

            case 2:
                print("All Information")
                database.view_products()

            case 3:
                searchproductname=input("Enter the product name to search :").strip().lower()
                searchproductname=validator.gettext(searchproductname)
                database.search_products(searchproductname)

            case 4:
                updateproductid=input("Enter the product id to update :")
                updateproductid=validator.getnumber(updateproductid)

                if(database.check_productid(updateproductid)==1):
                    updateproductname=input("Enter the new product name :").strip().lower()
                    updateproductname=validator.getproductnames(updateproductname)

                    categorynames=[]
                    categorynames=database.getcategorynames()
                    for i in categorynames:
                        print(i)
                    updatecategory=input("Enter the new category :").strip().lower()
                    updatecategory=validator.getcategoryproductconnectionvalidation(updatecategory)

                    updatesupplier=input("Enter the new supplier :").strip().lower()
                    updatesupplier=validator.gettext(updatesupplier)

                    updatepurchaseprice=input("Enter the new purchase price :")
                    updatepurchaseprice=validator.getprice(updatepurchaseprice)

                    updatesellingprice=input("Enter the new selling price :")
                    updatesellingprice=validator.getprice(updatesellingprice)

                    updateinitialstockquantity=input("Enter the new initial stock quantity :")
                    updateinitialstockquantity=validator.getquantity(updateinitialstockquantity)

                    updateminimumstocklevel=input("Enter the new minimum stock level :")
                    updateminimumstocklevel=validator.getquantity(updateminimumstocklevel)
                    database.update_products(updateproductname,updatecategory,updatesupplier,updatepurchaseprice,updatesellingprice,updateinitialstockquantity,updateminimumstocklevel,updateproductid)
                    
            case 5:
                deleteproductid=input("Enter the product id to delete :")
                deleteproductid=validator.getnumber(deleteproductid)

                if(database.check_productid(deleteproductid)==1):
                    ch=input("Enter y to continue deletion , n to stop deletion :").strip().lower()
                    ch=validator.gettext(ch)

                    if(ch=="y"):
                        database.delete_product(deleteproductid)
                    elif(ch=="n"):
                        print("Deletion stopped")
                    else:
                        print("Choose either y or n")

            case 6:
                chproducts=input("Really want to exit?\nEnter y to exit\nEnter n to go back :").strip().lower()
                if(chproducts=="y"):
                    break
                elif(chproducts=="n"):
                    continue
                else:
                    print("Enter either y or n")

            case _:
                print("Please enter option from 1 to 6")
