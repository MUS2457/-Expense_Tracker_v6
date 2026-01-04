import storage
def search_product():
    history = storage.load_data()
    if not history:
        return None

    results = []

    while True:
        user = input("Please enter your product name (or 'exit' to quit): ").strip()
        if user.lower() == "exit":
            return None

        user_capitalized = user.capitalize()
        results.clear()  # reset for each search

        for time, expenses in history.items():
            for expense in expenses:
                if user_capitalized == expense["product"]:
                    results.append((time, expense))

        if results:
            return results
        else :
            print("Product not found. Try again.")
            continue

