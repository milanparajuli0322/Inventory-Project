import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


#Python connecting to database
mydb=mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


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

    sql = """CREATE TABLE IF NOT EXISTS categories (category_id INT AUTO_INCREMENT PRIMARY KEY,category_name VARCHAR(100) NOT NULL UNIQUE)"""
    mycursor.execute(sql)

else:
    print("Server cannot connect")


#Manage Products Functions
def add_product(productname,category,supplier,purchaseprice,sellingprice,initialstockquantity,minimumstocklevel):
    try:
        sql = """INSERT INTO products(product_name, category, supplier, purchase_price, selling_price,
        stock_quantity, minimum_stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val=(productname, category, supplier, purchaseprice,sellingprice, initialstockquantity, minimumstocklevel)
        mycursor.execute(sql,val)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Could not add products :",e)


def getproductnames():
    try:
        lst=[]
        sql="SELECT product_name FROM products"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        for i in myresults:
            lst.extend(i)
        return lst

    except mysql.connector.Error as e:
        print("Could not get product names :",e)
        return []

def view_products():
    try:
        sql="SELECT * FROM products"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for i in myresult:
            print(i)

    except mysql.connector.Error as e:
        print("Could not view products :",e)


def search_products(searchproductname):
    try:
        sql="SELECT * FROM products WHERE product_name LIKE %s"
        val=(f"%{searchproductname}%",)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        if myresult:
            for i in myresult:
                print(i)
        else:
            print("No searching result found")

    except mysql.connector.Error as e:
        print("Could not search products :",e)
    

def check_productid(updateproductid):
    try:
        sql="SELECT * FROM products where product_id=%s"
        val=(updateproductid,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        if(not myresult):
            print("No such product id exists")
            print("Operation cancelled")
        else:
            return 1

    except mysql.connector.Error as e:
        print("Could not check product id :",e)
    

def update_products(updateproductname,updatecategory,updatesupplier,updatepurchaseprice,updatesellingprice,updateinitialstockquantity,updateminimumstocklevel,updateproductid):
    try:
        sql="""UPDATE products SET product_name = %s,category = %s,supplier = %s,purchase_price = %s,selling_price = %s,
        stock_quantity = %s,minimum_stock_level = %s WHERE product_id = %s"""
        val=(updateproductname,updatecategory,updatesupplier,updatepurchaseprice,updatesellingprice,updateinitialstockquantity,updateminimumstocklevel,updateproductid)
        mycursor.execute(sql,val)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Could not update products :",e)


def delete_product(deleteproductid):
    try:
        sql="DELETE FROM products WHERE product_id=%s"
        val=(deleteproductid,)
        mycursor.execute(sql,val)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Could not delete products :",e)


#Manage Category Functions
def add_categories(categoryname):
    try:
        sql="""INSERT INTO categories (category_name) Values (%s)"""
        val=(categoryname,)
        mycursor.execute(sql,val)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Could not add categories :",e)


def getcategorynames():
    try:
        lst=[]
        sql="SELECT category_name FROM categories"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        for i in myresults:
            lst.extend(i)
        return lst

    except mysql.connector.Error as e:
        print("Could not get category names :",e)
        return []


def categoryconnectionvalidation(categoryid):
    connectionlist=[]
    sql="SELECT category FROM products WHERE category = (SELECT category_name FROM categories WHERE category_id=%s)"
    val=(categoryid,)
    mycursor.execute(sql,val)
    myresults=mycursor.fetchall()
    for i in myresults:
        connectionlist.extend(i)
    return connectionlist
    

def view_categories():
    try:
        sql="SELECT * FROM categories"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        for i in myresults:
            print(i)

    except mysql.connector.Error as e:
        print("Could not view categories :",e)


def search_categories(searchcategoryname):
    try:
        sql="SELECT * FROM categories WHERE category_name LIKE %s"
        val=(f"%{searchcategoryname}%",)
        mycursor.execute(sql,val)
        myresults=mycursor.fetchall()
        if(not myresults):
            print("No results found")
        else:
            for i in myresults:
                print(i)

    except mysql.connector.Error as e:
        print("Could not search categories :",e)


def check_categoryid(updatecategoryid):
    try:
        sql="SELECT * FROM categories WHERE category_id=%s"
        val=(updatecategoryid,)
        mycursor.execute(sql,val)
        myresults=mycursor.fetchall()
        if(not myresults):
            print("No result found")
            print("Operation cancelled")
        else:
            return 1

    except mysql.connector.Error as e:
        print("Could not check category id :",e)


def update_category(newcategoryname,updatecategoryid):
    try:
        sql="UPDATE categories SET category_name=%s WHERE category_id=%s"
        val=(newcategoryname,updatecategoryid)
        mycursor.execute(sql,val)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Could not update categories :",e)


def delete_category(deletecategoryid):
    try:
        sql="DELETE FROM categories WHERE category_id=%s"
        val=(deletecategoryid,)
        mycursor.execute(sql,val)
        mydb.commit()

    except mysql.connector.Error as e:
        print("Could not delete categories :",e)


#Database manually closed
import atexit
@atexit.register
def cleanup():
    try:
        mycursor.close()
        mydb.close()
    except:
        pass
