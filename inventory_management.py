import json

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"

class Inventory:
    def __init__(self, filename='inventory.json'):
        self.products = {}  # Dictionary to store products, where key is productID
        self.filename = filename  # File to store inventory data
        self.load_from_file()  # Load existing inventory from file when initializing

    def add_product(self, id, name, price, quantity):
        """Add a new product to inventory """
        if not id or not isinstance(id, str):
            print("Invalid product ID. It must be a non-empty string.")
            return
        if id in self.products:
            print(f"Product with ID {id} already exists.")
        else:
            try:
                price = float(price)
                quantity = int(quantity)
                if price < 0 or quantity < 0:
                    raise ValueError("Price and quantity must be non-negative.")
                self.products[id] = Product(id, name, price, quantity)  # create new Product object and add to dictionary
                print(f"Product {name} added.")
            except ValueError as e:
                print(f"Invalid input: {e}")

    def update_product(self, id, name=None, price=None, quantity=None):
        """Update an existing product in inventory"""
        if not id or not isinstance(id, str):
            print("Invalid product ID. It must be a non-empty string.")
            return
        if id in self.products:
            try:
                if name is not None:
                    self.products[id].name = name
                if price is not None:
                    price = float(price)
                    if price < 0:
                        raise ValueError("Price must be non-negative.")
                    self.products[id].price = price
                if quantity is not None:
                    quantity = int(quantity)
                    if quantity < 0:
                        raise ValueError("Quantity must be non-negative.")
                    self.products[id].quantity = quantity
                print(f"Product {id} updated.")
            except ValueError as e:
                print(f"Invalid input: {e}")
        else:
            print(f"Product with ID {id} not found.")

    def delete_product(self, id):
        """Delete a product from inventory"""
        if not id or not isinstance(id, str):
            print("Invalid product ID. It must be a non-empty string.")
            return
        if id in self.products:
            del self.products[id]
            print(f"Product {id} deleted.")
        else:
            print(f"Product with ID {id} not found.")

    def view_product(self, id):
        """View details of a specific product"""
        if not id or not isinstance(id, str):
            print("Invalid product ID. It must be a non-empty string.")
            return
        if id in self.products:
            print(self.products[id])
        else:
            print(f"Product with ID {id} not found.")

    def list_all_products(self):
        """List all products in inventory"""
        if self.products:
            for product in self.products.values():
                print(product)
        else:
            print("No products in inventory.")

    def low_stock_alert(self, threshold):
        """Display products with quantity below a specified threshold"""
        try:
            threshold = int(threshold)
            if threshold < 0:
                raise ValueError("Threshold must be non-negative")
            low_stock_products = [product for product in self.products.values() if product.quantity < threshold]
            if low_stock_products:
                for product in low_stock_products:
                    print(product)
            else:
                print("No products below the stock threshold")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def total_inventory_value(self):
        """Calculate and display the total value of inventory"""
        total_value = sum(product.price * product.quantity for product in self.products.values())
        print(f"Total inventory value: ${total_value:.2f}")

    def load_from_file(self):
        """Load inventory data from a JSON file"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for id, details in data.items():
                    self.products[id] = Product(id, details['name'], details['price'], details['quantity'])
            print("Inventory loaded from file")
        except FileNotFoundError:
            print("Inventory file not found. Starting with an empty inventory")
        except json.JSONDecodeError:
            print("Error reading the inventory file. Starting with an empty inventory.")

    def save_to_file(self):
        """Save current inventory data to a JSON file """

        with open(self.filename, 'w') as f:
            data = {id: vars(product) for id, product in self.products.items()}
            json.dump(data, f, indent=4)
        print("Inventory saved to file.")

def main():
    inventory = Inventory()

    menu = """
    1. Add Product
    2. Update Product
    3. Delete Product
    4. View Product
    5. List All Products
    6. Low-Stock Alert
    7. Total Inventory Value
    8. Exit
    """


    while True:
        print(menu)
        choice = input("Select an option: ")

        if choice == '1':
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            quantity = input("Enter product quantity: ")
            inventory.add_product(id, name, price, quantity)

        elif choice == '2':
            id = input("Enter product ID to update: ")
            name = input("Enter new product name (leave blank to keep current): ") or None
            price = input("Enter new product price (leave blank to keep current): ")
            price = price if price else None
            quantity = input("Enter new product quantity (leave blank to keep current): ")
            quantity = quantity if quantity else None
            inventory.update_product(id, name, price, quantity)

        elif choice == '3':
            id = input("Enter product ID to delete: ")
            inventory.delete_product(id)

        elif choice == '4':
            id = input("Enter product ID to view: ")
            inventory.view_product(id)

        elif choice == '5':
            inventory.list_all_products()

        elif choice == '6':
            threshold = input("Enter stock threshold: ")
            inventory.low_stock_alert(threshold)

        elif choice == '7':
            inventory.total_inventory_value()

        elif choice == '8':
            inventory.save_to_file()
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
