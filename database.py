#mysql -u root -p
#pip freeze > requirements.txt

import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


mydb=mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

#Manage Products functions
def add_product(productname,category,supplier,purchaseprice,sellingprice,initialstockquantity,minimumstocklevel):
    sql = """INSERT INTO products(product_name, category, supplier, purchase_price, selling_price,
    stock_quantity, minimum_stock_level)VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    val=(productname, category, supplier, purchaseprice,sellingprice, initialstockquantity, minimumstocklevel)
    mycursor.execute(sql,val)
    mydb.commit()

def view_products():
    sql="SELECT * FROM products"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)

def search_products(searchproductname):
    sql="SELECT * FROM products WHERE product_name=%s"
    val=(searchproductname,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()
    if myresult:
        for i in myresult:
            print(i)
    else:
        print("No searching result found")

def check_productid(updateproductid):
    sql="SELECT * FROM products where product_id=%s"
    val=(updateproductid,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()
    if(not myresult):
        print("No such product id exists")
    else:
        return 1

def update_products(updateproductname,updatecategory,updatesupplier,updatepurchaseprice,updatesellingprice,updateinitialstockquantity,updateminimumstocklevel,updateproductid):
    sql="""UPDATE products SET product_name = %s,category = %s,supplier = %s,purchase_price = %s,selling_price = %s,
    stock_quantity = %s,minimum_stock_level = %s WHERE product_id = %s"""
    val=(updateproductname,updatecategory,updatesupplier,updatepurchaseprice,updatesellingprice,updateinitialstockquantity,updateminimumstocklevel,updateproductid)
    mycursor.execute(sql,val)
    mydb.commit()

def delete_product(deleteproductid):
    sql="DELETE FROM products WHERE product_id=%s"
    val=(deleteproductid,)
    mycursor.execute(sql,val)
    mydb.commit()
    
if(mydb.is_connected()):
    mycursor=mydb.cursor()
    sql="CREATE DATABASE IF NOT EXISTS inventory_db"
    mycursor.execute(sql)
    sql="USE inventory_db"
    mycursor.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS products (product_id INT AUTO_INCREMENT PRIMARY KEY,product_name VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,supplier VARCHAR(100),purchase_price DECIMAL(10,2) NOT NULL,selling_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,minimum_stock_level INT NOT NULL DEFAULT 0)"""
    mycursor.execute(sql)
else:
    print("Server cannot connect")

