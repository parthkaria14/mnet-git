import sqlite3

# Connect (creates the file if it doesn't exist)
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
""")

# Insert data
cursor.executescript("""
INSERT OR IGNORE INTO users (name, email) VALUES
    ('Parth', 'parth@example.com'),
    ('Rohit', 'rohit@example.com');

INSERT OR IGNORE INTO products (name, price) VALUES
    ('Laptop', 75000),
    ('Phone', 30000),
    ('Headphones', 5000);

INSERT OR IGNORE INTO orders (user_id, product_id, quantity) VALUES
    (1, 1, 1),
    (1, 3, 2),
    (2, 2, 1);
""")

conn.commit()

# SELECT — fetch all users
print("=== Users ===")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# SELECT with WHERE
print("\n=== Products under ₹50,000 ===")
cursor.execute("SELECT name, price FROM products WHERE price < 50000")
for row in cursor.fetchall():
    print(row)

# JOIN — orders with user and product names
print("\n=== Orders with Details ===")
cursor.execute("""
    SELECT users.name, products.name, orders.quantity
    FROM orders
    JOIN users ON orders.user_id = users.id
    JOIN products ON orders.product_id = products.id
""")
for row in cursor.fetchall():
    print(row)

conn.close()