import sqlite3

conn = sqlite3.connect("marketplace.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_seller BOOLEAN DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seller_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image_url TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (seller_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    user_id INTEGER,
    rating INTEGER NOT NULL,
    comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")
conn.commit()

def create_user(username, email, password, is_seller=False):
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password, is_seller) VALUES (?, ?, ?, ?)",
            (username, email, password, is_seller)
        )
        conn.commit()
        print(f"User '{username}' created successfully!")
    except sqlite3.IntegrityError:
        print("Username or email already exists.")


def add_product(seller_id, name, description, price, image_url):
    cursor.execute(
        "INSERT INTO products (seller_id, name, description, price, image_url) VALUES (?, ?, ?, ?, ?)",
        (seller_id, name, description, price, image_url)
    )
    conn.commit()
    print(f"Product '{name}' added successfully!")


def list_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(f"ID: {product[0]}, Name: {product[2]}, Price: ${product[4]}, Description: {product[3]}")


def search_products(keyword):
    cursor.execute("SELECT * FROM products WHERE name LIKE ? OR description LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"ID: {product[0]}, Name: {product[2]}, Price: ${product[4]}, Description: {product[3]}")
    else:
        print("No products found matching your search.")


def add_review(product_id, user_id, rating, comment):
    cursor.execute(
        "INSERT INTO reviews (product_id, user_id, rating, comment) VALUES (?, ?, ?, ?)",
        (product_id, user_id, rating, comment)
    )
    conn.commit()
    print("Review added successfully!")


def view_product_details(product_id):
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    if product:
        print(f"Name: {product[2]}, Price: ${product[4]}, Description: {product[3]}")
        cursor.execute("SELECT * FROM reviews WHERE product_id = ?", (product_id,))
        reviews = cursor.fetchall()
        if reviews:
            print("\nReviews:")
            for review in reviews:
                print(f"Rating: {review[3]}/5, Comment: {review[4]}")
        else:
            print("\nNo reviews for this product.")
    else:
        print("Product not found.")

if __name__ == "__main__":
    create_user("alice", "alice@example.com", "password123", is_seller=True)
    create_user("bob", "bob@example.com", "password456")

    add_product(1, "Laptop", "A high-performance laptop", 1200.99, "image_url_here")
    add_product(1, "Smartphone", "A latest-gen smartphone", 799.99, "image_url_here")
    print("\nAll Products:")
    list_products()
    print("\nSearch Results for 'laptop':")
    search_products("laptop")
    print("\nProduct Details (ID: 1):")
    view_product_details(1)

    add_review(1, 2, 5, "Great product!")
    add_review(1, 2, 4, "Good but a bit expensive.")
    print("\nProduct Details with Reviews (ID: 1):")
    view_product_details(1)
