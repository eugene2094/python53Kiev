import sqlite3
import random


def main():
    conn = sqlite3.connect('db3.sqlite')
    conn.execute('PRAGMA foreign_keys=ON;')
    cursor = conn.cursor()

    cursor.executescript("""
      
       
       CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price NUMERIC NOT NULL CHECK (price >= 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
       );
       
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            total_price NUMERIC NOT NULL,
            order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE            
       );   
           
    """)

    # cursor.executemany("INSERT INTO products (name,price,stock) VALUES (?,?,?)", [
    #     ('iphone 5', 600, 1),
    #     ('iphone 6', 700, 10),
    #     ('iphone 7', 800, 10),
    #     ('samsung galaxy S23', 900, 10)
    # ])
    model_id = random.randint(1, 4)
    cursor.execute(" SELECT price FROM products WHERE id = ?", (model_id,))
    product_price = cursor.fetchone()[0]

    quantity = random.randint(1, 10)
    total_price = product_price * quantity

    cursor.execute("INSERT INTO orders (product_id,quantity,total_price) VALUES (?,?,?)",
                   (model_id, quantity, total_price))

    # cursor.execute("SELECT * FROM products")
    # cursor.execute("SELECT name,price FROM products")

    # cursor.execute("SELECT * FROM products WHERE price > ?;", (700,))

    # cursor.execute("SELECT * FROM products WHERE stock < 2;")

    # cursor.execute("SELECT DISTINCT * FROM orders ORDER BY quantity DESC LIMIT 1;")

    # cursor.execute("SELECT DISTINCT product_id FROM orders;")

    # cursor.execute("SELECT * FROM products WHERE name LIKE '%17'")

    # cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (8, 2))
    # cursor.execute("SELECT * FROM orders;")

    cursor.execute("""
       SELECT products.name, orders.quantity,orders.total_price
       FROM orders
       JOIN products ON orders.product_id = products.id;    
    """)



    for row in cursor.fetchall():
        print(row)

    conn.commit()


if __name__ == "__main__":
    main()
