class Library:
    """A simple library management system"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        """Add a book to the library"""
        book = {"title": title, "author": author, "available": True}
        self.books.append(book)
        return f"Book '{title}' by {author} added to library"
    
    def register_member(self, member_name):
        """Register a new member"""
        if member_name not in self.members:
            self.members.append(member_name)
            return f"Member '{member_name}' registered successfully"
        else:
            return f"Member '{member_name}' already registered"
    
    def borrow_book(self, member_name, book_title):
        """Allow member to borrow a book"""
        if member_name not in self.members:
            return "Member not registered"
        
        for book in self.books:
            if book["title"] == book_title and book["available"]:
                book["available"] = False
                return f"Book '{book_title}' borrowed by {member_name}"
        
        return "Book not available or not found"
    
    def return_book(self, book_title):
        """Return a book to the library"""
        for book in self.books:
            if book["title"] == book_title and not book["available"]:
                book["available"] = True
                return f"Book '{book_title}' returned successfully"
        
        return "Book not found or already available"
    
    def show_available_books(self):
        """Display all available books"""
        available = [book for book in self.books if book["available"]]
        if available:
            result = "Available Books:\n"
            for book in available:
                result += f"- {book['title']} by {book['author']}\n"
            return result
        else:
            return "No books available"

# Example usage
library = Library("City Library")
print(library.add_book("Python Crash Course", "Eric Matthes"))
print(library.add_book("Clean Code", "Robert Martin"))
print(library.register_member("Alice"))
print(library.borrow_book("Alice", "Python Crash Course"))
print(library.show_available_books())