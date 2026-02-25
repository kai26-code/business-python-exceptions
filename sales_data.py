def get_valid_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            
            # prevent negative values
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue

            return value
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("=== Retail Sales Data Entry ===")

    # Get validated inputs
    units_sold = get_valid_number("Enter number of units sold: ", int)
    price_per_unit = get_valid_number("Enter price per unit: ", float)

    # Calculate total revenue
    total_revenue = units_sold * price_per_unit

    # Display result formatted as currency
    print(f"\nTotal Revenue: ${total_revenue:,.2f}")


if __name__ == "__main__":
    main()

# validates sales input data (units sold and price per unit) 
# using exception and loops. It prevents invalid or negative entries 
# and calculates total revenue. 