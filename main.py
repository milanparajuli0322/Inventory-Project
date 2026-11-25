import products
import categories

myoptions=["Menu","1.Manage Products","2.Manage Category","3.Manage Suppliers","4.Manage Customer",
        "5.Manage Inventory","6.Manage Order","7.Sales Report","8.Exit"]

print("---Inventory Manager---")

while(True):
    for i in myoptions:
        print(i)
    option=input("Enter the operation number :")
    option=products.getnumber(option)

    match option:
        case 1:
            products.product()
            
        case 2:
            categories.category()

        case 3:
            print("Not implemented. Under construction")

        case 4:
            print("Not implemented. Under construction")

        case 5:
            print("Not implemented. Under construction")

        case 6:
            print("Not implemented. Under construction")

        case 7:
            print("Not implemented. Under construction")

        case 8:
            chmain=input("Really want to exit?\nEnter y to exit\nEnter n to go back :").strip().lower()
            if(chmain=="y"):
                break
            elif(chmain=="n"):
                continue
            else:
                print("Enter either y or n")
                continue

        case _:
            print("Please enter option from 1 to 8")

            
#mysql -u root -p
#pip freeze > requirements.txt
