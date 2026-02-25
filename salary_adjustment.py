def get_valid_float(prompt):
    """
    Repeatedly prompts the user until a valid float is entered.
    """
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=== Employee Salary Adjustment Simulator ===\n")

    # Get current salary
    while True:
        current_salary = get_valid_float("Enter current salary: ")

        if current_salary < 0:
            print("Salary cannot be negative. Please try again.")
        else:
            break

    # Get adjustment percentage
    while True:
        adjustment_percent = get_valid_float(
            "Enter adjustment percentage (0-100): "
        )

        # Custom validation checks
        if adjustment_percent < 0:
            print("Adjustment percentage cannot be negative.")
        elif adjustment_percent > 100:
            print("Adjustment percentage cannot exceed 100.")
        else:
            break

    # Calculate new salary
    adjustment_amount = current_salary * (adjustment_percent / 100)
    new_salary = current_salary + adjustment_amount

    # Display result
    print("\n----- Salary Adjustment Summary -----")
    print(f"Current Salary: ${current_salary:,.2f}")
    print(f"Adjustment: {adjustment_percent:.2f}%")
    print(f"New Salary: ${new_salary:,.2f}")
    print("-------------------------------------")


if __name__ == "__main__":
    main()

# Simulates salary adjustments for employees in an HR setting.
# prompts user to enter an employee's current salary and an adjustment
# percentage. The program validates user input using exception to
# ensure numeric values are entered and that percentages fall within an
# range. Once valid inputs are received, the program calculates
# and displays the employee's new adjusted salary.    