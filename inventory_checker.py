def get_valid_integer(prompt):
    """
    Repeatedly prompts user until a valid integer is entered.
    """
    while True:
        try:
            value = int(input(prompt).strip())

            # Prevent negative inventory levels
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=== Inventory Quantity Checker ===\n")

    # Get validated inputs
    inventory_level = get_valid_integer("Enter current inventory level: ")
    reorder_threshold = get_valid_integer("Enter minimum reorder threshold: ")

    # Check reorder condition
    if inventory_level < reorder_threshold:
        print("\nReorder Alert: Inventory is below the minimum threshold.")
    else:
        print("\nInventory level is sufficient.")

    # Calculate inventory as percentage of threshold
    try:
        percentage = (inventory_level / reorder_threshold) * 100
        print(f"Inventory is {percentage:.2f}% of the reorder threshold.")
    except ZeroDivisionError:
        print("Cannot calculate percentage because the threshold is zero.")


if __name__ == "__main__":
    main()

# Validates inventory inputs using exception.
# It alerts the user when inventory falls below the reorder threshold
# and safely handles division errors.