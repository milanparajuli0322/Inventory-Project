# Inventory

A Python command-line inventory management system with MySQL, supporting add, view, search, update and delete for products.

## Setup

1. Clone the repo and create a virtual environment: `python3 -m venv venv` then `source venv/bin/activate` (on Windows: `.\venv\Scripts\activate`)

2. Install dependencies: `pip install -r requirements.txt`

3. Make sure MySQL is installed and running.

4. Create a `.env` file in the project folder with your MySQL details: `DB_HOST`, `DB_USER` and `DB_PASSWORD`

5. Run the app: `python3 main.py`

## Notes

- The `inventory_db` database and `products` table are created automatically on first run.
- Search matches the exact product name.
- Only product management is working for now.
