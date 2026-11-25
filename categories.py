import database
import validator


def category():
    while(True):
        categorymenu=["Sub Menu","1.Add Categories","2.View All Categories","3.Search Categories","4.Update Categories","5.Delete Categories","6.Back to main menu"]
        for i in categorymenu:
            print(i)
        categoryoption=input("Enter the operation number :")
        categoryoption=validator.getnumber(categoryoption)

        match categoryoption:
            case 1:
                categoryname=input("Enter then category name :").strip().lower()
                categoryname=validator.getcategoryname(categoryname)
                database.add_categories(categoryname)

            case 2:
                print("All Information")
                database.view_categories()

            case 3:
                searchcategoryname=input("Enter the category name to search :").strip().lower()
                searchcategoryname=validator.gettext(searchcategoryname)
                database.search_categories(searchcategoryname)

            case 4:
                updatecategoryid=input("Enter the category id to update :")
                updatecategoryid=validator.getnumber(updatecategoryid)

                if(database.check_categoryid(updatecategoryid)==1):
                    newcategoryname=input("Enter the new category name :").strip().lower()
                    updatecategoryconnectionvalidation=[]
                    updatecategoryconnectionvalidation=database.categoryconnectionvalidation(updatecategoryid)

                    if(updatecategoryconnectionvalidation):
                        print("Product exists for this category so cannot update its name")
                        continue

                    newcategoryname=validator.getcategoryname(newcategoryname)
                    database.update_category(newcategoryname,updatecategoryid)

            case 5:
                deletecategoryid=input("Enter the category id to delete :")
                deletecategoryid=validator.getnumber(deletecategoryid)

                if(database.check_categoryid(deletecategoryid)==1):
                    deletecategoryconnectionvalidation=[]
                    deletecategoryconnectionvalidation=database.categoryconnectionvalidation(deletecategoryid)

                    if(deletecategoryconnectionvalidation):
                        print("Product exists for this category so cannot delete its name")
                        continue

                    ask=input("Enter y to continue and n to stop deletion :").strip().lower()
                    ask=validator.gettext(ask)

                    if(ask=="y"):
                        database.delete_category(deletecategoryid)
                    elif(ask=="n"):
                        print("Deletion stopped")
                    else:
                        print("Enter either y or n")

            case 6:
                chcategories=input("Really want to exit?\nEnter y to exit\nEnter n to go back :").strip().lower()
                if(chcategories=="y"):
                    break
                elif(chcategories=="n"):
                    continue
                else:
                    print("Enter either y or n")

            case _:
                print("Please enter option from 1 to 6")
