# Inventory Management System

This Python program allows you to manage your product inventory. It provides functionalities to add, update, delete, view, and list all products. Additionally, you can check for low-stock items and calculate the total inventory value.

## Run Locally

Clone the project

Go to the project directory on your device

Run the program

```bash
  python3 inventory_management.py
```

## Usage

The program will display a menu with various options. You can choose the desired action by entering the corresponding number:

1. Add Product: Enter product details like ID, name, price, and quantity to add a new item.
2. Update Product: Provide the ID of the product you want to modify. You can then update its name, price, or quantity (or leave fields blank to keep them unchanged).
3. Delete Product: Enter the ID of the product to remove it from the inventory.
4. View Product: Enter the ID of the product to view its details.
5. List All Products: This will display a list of all products currently in the inventory.
6. Low-Stock Alert: Specify a stock threshold. The program will then list products with quantities below the specified level.
7. Total Inventory Value: This option calculates and displays the total value of your inventory based on product prices and quantities.
8. Exit: Saves the current inventory data to a file and exits the program.
   Note: The program validates user input and provides informative messages for errors or invalid selections.

## Design Choices and Assumptions

- The program stores inventory data in a JSON file named 'inventory.json' by default. This file is automatically loaded when you launch the program and saved when you exit.
- Product IDs are assumed to be unique strings.
- Prices and quantities must be non-negative numbers. The program performs validation to ensure this.
- You can modify the filename for storing inventory data by changing the filename parameter in the Inventory class constructor within the code.
