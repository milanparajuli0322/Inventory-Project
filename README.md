# Inventory Management System

A command-line inventory management system built with Python and MySQL. This application allows users to manage products and categories with strict input validation and relational database constraints.

## Features
- **Product Management:** Full CRUD operations (Add, View, Search, Update, Delete) for products.
- **Category Management:** Full CRUD operations for categories.
- **Relational Integrity:** Prevents the deletion of a category if there are existing products assigned to it.
- **Validation:** Strict input validation for text, integers, and decimal prices (prevents negative numbers, empty fields, and duplicates).
- **Partial Search:** Search functionality using SQL `LIKE` queries.

## Tech Stack
- **Language:** Python 3
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`, `python-dotenv`

## Setup & Installation

1. **Clone the repository and navigate into the folder:**
   git clone https://github.com/milanparajuli0322/Inventory-Project.git
   cd Inventory-Project

2. **Create and activate a virtual environment:**
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate

3. **Install the required dependencies:**
   pip install -r requirements.txt

4. **Set up environment variables:**
   Create a .env file in the root directory and add your MySQL credentials:
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password

5. **Run the application:**
   python3 main.py

## Notes
- The database (inventory_db) and the required tables are created automatically on the first run if they do not exist.
- This is currently a backend CLI (Command Line Interface) application. Web frontend and user authentication are not implemented yet.
