import sqlite3
import datetime
conn = sqlite3.connect("social_network.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS friends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    friend_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER,
    receiver_id INTEGER,
    message TEXT,
    sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users(id),
    FOREIGN KEY (receiver_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    message TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")
conn.commit()

def create_user(username, email, password):
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        print(f"User '{username}' created successfully!")
    except sqlite3.IntegrityError:
        print("Username or email already exists.")


def add_friend(user_id, friend_id):
    cursor.execute("INSERT INTO friends (user_id, friend_id) VALUES (?, ?)", (user_id, friend_id))
    conn.commit()
    print(f"Friend added between user {user_id} and user {friend_id}!")


def post_content(user_id, content):
    cursor.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (user_id, content))
    conn.commit()
    print(f"User {user_id} posted: {content}")


def send_message(sender_id, receiver_id, message):
    cursor.execute("INSERT INTO messages (sender_id, receiver_id, message) VALUES (?, ?, ?)", (sender_id, receiver_id, message))
    conn.commit()
    print(f"Message sent from user {sender_id} to user {receiver_id}.")


def get_news_feed(user_id):
    cursor.execute("""
    SELECT users.username, posts.content, posts.created_at 
    FROM posts 
    JOIN users ON posts.user_id = users.id 
    WHERE posts.user_id = ? OR posts.user_id IN (
        SELECT friend_id FROM friends WHERE user_id = ?
    )
    ORDER BY posts.created_at DESC
    """, (user_id, user_id))
    posts = cursor.fetchall()
    for post in posts:
        print(f"[{post[2]}] {post[0]}: {post[1]}")


def get_notifications(user_id):
    cursor.execute("SELECT message, created_at FROM notifications WHERE user_id = ? ORDER BY created_at DESC", (user_id,))
    notifications = cursor.fetchall()
    for notification in notifications:
        print(f"[{notification[1]}] {notification[0]}")

if __name__ == "__main__":
    create_user("alice", "alice@example.com", "password123")
    create_user("bob", "bob@example.com", "password456")
    
    add_friend(1, 2)

    post_content(1, "Hello, world!")
    post_content(2, "This is my first post!")
    
    send_message(1, 2, "Hey Bob, how's it going?")
    send_message(2, 1, "All good, Alice! You?")
    
    print("\nNews Feed for Alice:")
    get_news_feed(1)
    
    print("\nNotifications for Alice:")
    get_notifications(1)
