class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Price: ${self.price:.2f}"


class Seller:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_book_to_inventory(self, book):
        self.inventory.append(book)

    def list_inventory(self):
        print(f"Inventory of {self.name}:")
        for book in self.inventory:
            print(book)


class Buyer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def buy_book(self, book):
        if self.budget >= book.price:
            self.budget -= book.price
            return True
        else:
            return False


class Marketplace:
    def __init__(self):
        self.sellers = []

    def add_seller(self, seller):
        self.sellers.append(seller)

    def search_books(self, title):
        found_books = []
        for seller in self.sellers:
            for book in seller.inventory:
                if title.lower() in book.title.lower():
                    found_books.append((seller, book))
        return found_books


# Example usage:
if __name__ == "__main__":
    # Creating sellers
    seller1 = Seller("Seller A")
    seller2 = Seller("Seller B")

    # Adding books to seller inventories
    seller1.add_book_to_inventory(Book("Python Programming", "John Smith", 25.99))
    seller1.add_book_to_inventory(Book("Data Structures and Algorithms", "Alice Johnson", 19.99))
    seller2.add_book_to_inventory(Book("Machine Learning Basics", "David Brown", 29.99))
    seller2.add_book_to_inventory(Book("Web Development with Django", "Emily Davis", 22.99))

    # Creating a marketplace and adding sellers
    marketplace = Marketplace()
    marketplace.add_seller(seller1)
    marketplace.add_seller(seller2)

    # Searching for books by title
    search_title = "Python"
    found_books = marketplace.search_books(search_title)
    print(f"Books found matching '{search_title}':")
    for seller, book in found_books:
        print(f"Sold by {seller.name}: {book}")

    # Creating a buyer
    buyer = Buyer("Buyer X", 50)

    # Buying a book
    book_to_buy = found_books[0][1]  # Choosing the first found book
    if buyer.buy_book(book_to_buy):
        print(f"\n{buyer.name} bought '{book_to_buy.title}' for ${book_to_buy.price:.2f}. Remaining budget: ${buyer.budget:.2f}")
    else:
        print(f"\n{buyer.name} cannot afford '{book_to_buy.title}'.")
