from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author, category, item_type):
        self.title = title
        self.author = author
        self.category = category
        self.item_type = item_type
        self.is_checked_out = False
        self.due_date = None

class Library:
    def __init__(self):
        self.items = []
        self.fines_per_day = 1   

    def add_item(self, title, author, category, item_type):
        new_item = LibraryItem(title, author, category, item_type)
        self.items.append(new_item)
        print(f"Added: {title} ({item_type})")

    def checkout_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if not item.is_checked_out:
                    item.is_checked_out = True
                    item.due_date = datetime.now() + timedelta(days=14)
                    print(f"Checked out: {item.title}. Due date: {item.due_date.strftime('%Y-%m-%d')}")
                    return
                else:
                    print(f"Item '{title}' is already checked out.")
                    return
        print(f"Item '{title}' not found in the library.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                if item.is_checked_out:
                    item.is_checked_out = False
                    overdue_days = (datetime.now() - item.due_date).days
                    fine = max(0, overdue_days * self.fines_per_day)
                    item.due_date = None
                    if fine > 0:
                        print(f"Returned: {item.title}. Overdue fine: {fine} units.")
                    else:
                        print(f"Returned: {item.title}. No fine.")
                    return
                else:
                    print(f"Item '{title}' was not checked out.")
                    return
        print(f"Item '{title}' not found in the library.")

    def search_items(self, keyword, search_type):
        keyword = keyword.lower()
        found_items = []

        for item in self.items:
            if search_type == "title":
                if keyword in item.title.lower():
                    found_items.append(item)
            elif search_type == "author":
                if keyword in item.author.lower():
                    found_items.append(item)
            elif search_type == "category":
                if keyword in item.category.lower():
                    found_items.append(item)

        if len(found_items) > 0:
            print(f"Search results for '{keyword}' in {search_type}:")
            for item in found_items:
                status = "Checked Out" if item.is_checked_out else "Available"
                print(f"- {item.title} by {item.author} ({item.item_type}) [{status}]")
        else:
            print(f"No items found for '{keyword}' in {search_type}.")

    def display_all_items(self):
        if len(self.items) > 0:
            print("Library Inventory:")
            for item in self.items:
                status = "Checked Out" if item.is_checked_out else "Available"
                print(f"- {item.title} by {item.author} ({item.category}, {item.item_type}) [{status}]")
        else:
            print("No items in the library.")

library = Library()
library.add_item("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "Book")
library.add_item("National Geographic", "Various", "Science", "Magazine")
library.add_item("The Avengers", "Joss Whedon", "Action", "DVD")
library.display_all_items()

library.checkout_item("The Great Gatsby")
library.return_item("The Great Gatsby")
library.search_items("Science", "category")

library.display_all_items()
