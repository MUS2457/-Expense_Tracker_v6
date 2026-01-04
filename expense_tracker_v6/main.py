import expense_input
import calculations
import storage
import utility


def menu():
    print("\nWelcome to the Expense Tracker v6")
    print("1. Add Expense")
    print("2. Search product based on old data")
    print("3. Load old data")
    print("4. Exit program")


def main():
    while True:
        menu()
        choice = input("Enter your choice (1–4): ").strip()


        if choice == "1":
            expenses = expense_input.get_data()

            if not expenses:
                print("No expenses were added.")
                continue

            total = calculations.total_price(expenses)
            average = calculations.average_price(expenses)

            (
                max_product,
                min_product,
                max_price,
                min_price
            ) = calculations.get_low_high_price(expenses)

            category_prices = calculations.price_per_category(expenses)

            (
                max_category,
                min_category,
                max_category_price,
                min_category_price
            ) = calculations.high_lowest_price_per_category(expenses)

            print("\n--- Shopping Results ---")
            print(f"Total price: {total}")
            print(f"Average price: {average}")

            print(f"Most expensive product: {max_product} ({max_price})")
            print(f"Least expensive product: {min_product} ({min_price})")

            print("\nPrice per category:")
            for category, price in category_prices.items():
                print(f"- {category}: {price}")

            print(
                f"\nHighest spending category: {max_category} ({max_category_price})"
            )
            print(
                f"Lowest spending category: {min_category} ({min_category_price})"
            )

            storage.save_data(expenses)
            print("\nData saved successfully!")


        elif choice == "2":
            results = utility.search_product()

            if not results:
                print("No matching product found.")
                continue

            print("\nSearch results:")
            for time, expense in results:
                print(f"{time} → {expense}")


        elif choice == "3":
            history = storage.load_data()

            if not history:
                print("No saved data found.")
                continue

            print("\nSaved data:")
            print(history)


        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
