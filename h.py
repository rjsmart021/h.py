class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self._allocated_budget = allocated_budget
        self._expenses = 0
    # Getter and setter for category name
    def get_category_name(self):
        return self._category_name

    def set_category_name(self, new_name):
        self._category_name = new_name

    # Getter and setter for allocated budget
    def get_allocated_budget(self):
        return self._allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self._allocated_budget = new_budget
        else:
            print("Invalid budget amount. Budget should be a positive number.")
    # Getter for expenses
    def get_expenses(self):
        return self._expenses

    # Setter for expenses (optional, since expenses are managed internally)
    def set_expenses(self, amount):
        self._expenses = amount

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount >= 0:
            self._expenses += amount
        else:
            print("Invalid expense amount. Expense should be a positive number.")
    # Method to calculate remaining budget
    def remaining_budget(self):
        return self._allocated_budget - self._expenses
    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self._category_name}")
        print(f"Allocated Budget: ${self._allocated_budget}")
        print(f"Expenses: ${self._expenses}")
        print(f"Remaining Budget: ${self.remaining_budget()}")


# Example usage
if __name__ == "__main__":
    food_category = BudgetCategory("Food", 500)
    food_category.add_expense(100)
    food_category.display_category_summary()

    # Test setters
    food_category.set_category_name("Groceries")
    food_category.set_allocated_budget(600)
    food_category.add_expense(50)

    food_category.display_category_summary()


class Product:
    # Constructor and common attributes
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        
    def display_info(self):
        # General method to display product info
        print("The product Id is: ", self.product_id)
        print("The product name is: ", self.name)
        print("The price of the product is: ", self.price)

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print("the author of the book is:", self.author)

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print("The specs of the Electronic are:", self.specs)

# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()
my_book2 = Book("349", "sqL is great", 30.0, "Johny Apple")
my_book2.display_info()

my_electronic = Electronic("552", "smartphone", 60.99, "4gig RAM, 2 core precessor")
my_electronic.display_info()
my_electronic2 = Electronic("643","computer", 60.99, "4gig RAM, 1 core precessor")
my_electronic2.display_info()

class (Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print("The specs of the Electronic are:", self.specs)

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs
    def display_info(self):
        super().display_info()
        print("The specs of the Electronic are:", self.specs)

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self, product_id, name, price, size):
        super().display_info()
        print("The size of the Clothing are:", self.size)
my_Clothing = Clothing("123", "Tang top", 29.99, "7")
my_Clothing.display_info()
my_Clothing2 = Clothing("349", "apple bottom Jeans", 30.0, "15")
my_Clothing2.display_info()

#Task 3: Override Display Method in Subclasses
class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self, product_id, name, price, size):
        super().display_info()
        print("The size of the Clothing are:", self.size)
my_Clothing = Clothing("123", "Tang top", 29.99, "7")
my_Clothing.display_info()
my_Clothing2 = Clothing("349", "apple bottom Jeans", 30.0, "15")
my_Clothing2.display_info()