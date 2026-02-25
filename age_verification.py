def get_customer_age():
    """
    Prompt the user until a valid positive integer age is entered.
    """
    while True:
        try:
            age = int(input("Enter customer's age: ").strip())

            if age <= 0:
                print("Age must be a positive number. Please try again.")
                continue

            return age

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=== Customer Age Verification ===\n")

    customer_age = get_customer_age()

    # Simulating a NameError by referencing a variable
    # that was never defined
    try:
        if customer_age >= minimum_age:   # minimum_age not defined yet
            print("Customer is eligible for the promotion.")
        else:
            print("Customer is NOT eligible for the promotion.")

    except NameError:
        print("System error detected: minimum age requirement not defined.")
        print("Defining minimum age requirement now...\n")

        # Now define the missing variable properly
        minimum_age = 18

        # Re-check eligibility after fixing the error
        if customer_age >= minimum_age:
            print("Customer is eligible for the promotion.")
        else:
            print("Customer is NOT eligible for the promotion.")


if __name__ == "__main__":
    main()

# This program validates customer age input using exception handling.
# It determines eligibility for age-restricted promotions and demonstrates
# handling both ValueError and NameError.    