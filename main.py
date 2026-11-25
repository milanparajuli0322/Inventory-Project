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

        case 8:
            break

        case _:
            print("Please enter option from 1 to 8")
