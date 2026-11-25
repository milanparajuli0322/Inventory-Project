import database
import products

def getcategoryname(text):
    categorynames=[]
    categorynames=database.getcategorynames()
    while(True):
        while(text.strip()!="" and text.strip() not in categorynames ):
            return text.strip()
        else:
            print("This is mandatory or it already exists")
            text=input("Enter properly :")

def category():
    while(True):
        categorymenu=["Sub Menu","1.Add Category","2.View All Products","3.Search Category","4.Update Category","5.Delete Category","6.Back to main menu"]
        for i in categorymenu:
            print(i)
        categoryoption=input("Enter the operation number :")
        categoryoption=products.getnumber(categoryoption)

        match categoryoption:
            case 1:
                categoryname=input("Enter the category name :")
                categoryname=getcategoryname(categoryname)
                database.add_categories(categoryname)

            case 2:
                print("All Infomation")
                database.view_categories()

            case 3:
                searchcategoryname=input("Enter the category name to search :")
                searchcategoryname=products.gettext(searchcategoryname)
                database.search_categories(searchcategoryname)

            case 4:
                updatecategoryid=input("Enter the category id to update :")
                updatecategoryid=products.getnumber(updatecategoryid)
                if(database.check_categoryid(int(updatecategoryid))==1):
                    newcategoryname=input("Enter the new category name :")
                    newcategoryname=getcategoryname(newcategoryname)
                    database.update_category(newcategoryname,int(updatecategoryid))

            case 5:
                deletecategoryid=input("Enter the category id to delete :")
                deletecategoryid=products.getnumber(deletecategoryid)
                if(database.check_categoryid(int(deletecategoryid))==1):
                    ask=input("Enter y to continue and n to stop deletion")
                    if(ask=="y"):
                        database.delete_category(deletecategoryid)
                    elif(ask=="n"):
                        print("Deletiong stopped")
                    else:
                        print("Enter either y or n")

            case 6:
                break

            case _:
                print("Please enter option from 1 to 6")
