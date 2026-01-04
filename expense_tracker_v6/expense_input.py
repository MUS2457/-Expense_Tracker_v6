def validation_input(name):
    name = name.lower()
    if name == "exit":
        return "exit"
    if name.lower() == "done":
        return "done"
    if name == "" or any(char.isdigit() for char in name):
        return "invalid"
    return name.capitalize()

def get_product():
    while True:
        user = input("Enter the product name ,'done' to finish or 'exit' to quit : ")
        product = validation_input(user)

        if product in ("exit", "done"):
            return product
        if product == "invalid":
            print("Invalid product name. Try again (no numbers or empty names).")
            continue
        return product


def get_category(product):
    categories = [
        "Food",
        "Beverages",
        "Cleaning",
        "Clothing",
        "Electronics",
        "School Supplies",
        "Home",
        "Health",
        "Transport",
        "Other"
    ]
    while True:
         category = input(f"Enter a category of the {product}  from the following list : {categories} or 'done' to finish: ").strip()
         if category.lower() == "done" :
             return 'done'
         if category.capitalize() in categories:
             return category.capitalize()
         print("Invalid category name. Try again (no numbers or empty names).")
         continue


def get_amount(product,category):
    while True:
        try :
            amount = float(input(f"Enter the price of {product} from the category {category} : "))
            if amount < 0:
                print("Enter a valid price")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Try again (no letters or empty input).")
            continue

def get_data() :
    expenses = []
    while True:

        product = get_product()
        if product == "exit":
            print("Exit the program")
            break
        if product == "done":
            break
        category = get_category(product)
        if category == 'done' :
            break
        price = get_amount(product,category)

        expenses.append({"product":product,"category":category,"amount":price})
    return expenses

