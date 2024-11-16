 # TASK THREE:INVENTORY MANAGEMENT SYSTEM
print("Inventory Management System")
import tkinter as tk
from tkinter import messagebox, ttk
USERS = {"Shubham": "131003"}
inventory = []

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        self.login_screen()

    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in USERS and USERS[username] == password:
            self.dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Inventory Dashboard", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Manage Inventory", command=self.manage_inventory).pack(pady=10)
        tk.Button(self.root, text="Low Stock Alert", command=self.low_stock_alert).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=10)

    def manage_inventory(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Manage Inventory", font=("Arial", 16)).pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack(pady=10)

        self.load_inventory()

        tk.Button(self.root, text="Add Product", command=self.add_product).pack(pady=5)
        tk.Button(self.root, text="Delete Product", command=self.delete_product).pack(pady=5)
        tk.Button(self.root, text="Back to Dashboard", command=self.dashboard).pack(pady=10)

    def load_inventory(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for idx, product in enumerate(inventory, start=1):
            self.tree.insert("", "end", values=(idx, product["name"], product["quantity"], product["price"]))

    def add_product(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Product")

        tk.Label(self.new_window, text="Product Name").pack()
        self.name_entry = tk.Entry(self.new_window)
        self.name_entry.pack()

        tk.Label(self.new_window, text="Quantity").pack()
        self.quantity_entry = tk.Entry(self.new_window)
        self.quantity_entry.pack()

        tk.Label(self.new_window, text="Price").pack()
        self.price_entry = tk.Entry(self.new_window)
        self.price_entry.pack()

        tk.Button(self.new_window, text="Add", command=self.save_product).pack(pady=10)

    def save_product(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if not name or not quantity.isdigit() or not price.replace(".", "", 1).isdigit():
            messagebox.showerror("Error", "Invalid input. Please check your entries.")
            return

        inventory.append({"name": name, "quantity": int(quantity), "price": float(price)})
        self.new_window.destroy()
        self.load_inventory()
        messagebox.showinfo("Success", "Product added successfully!")

    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a product to delete.")
            return

        item_index = int(self.tree.item(selected_item)["values"][0]) - 1
        inventory.pop(item_index)
        self.load_inventory()
        messagebox.showinfo("Success", "Product deleted successfully!")

    def low_stock_alert(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Low Stock Alert", font=("Arial", 16)).pack(pady=20)

        low_stock_items = [p for p in inventory if p["quantity"] < 5]

        self.alert_tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity"), show="headings")
        self.alert_tree.heading("ID", text="ID")
        self.alert_tree.heading("Name", text="Name")
        self.alert_tree.heading("Quantity", text="Quantity")
        self.alert_tree.pack(pady=10)

        for idx, product in enumerate(low_stock_items, start=1):
            self.alert_tree.insert("", "end", values=(idx, product["name"], product["quantity"]))

        tk.Button(self.root, text="Back to Dashboard", command=self.dashboard).pack(pady=10)
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()