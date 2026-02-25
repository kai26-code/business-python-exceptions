def main():
    print("=== Profit Margin Ratio Calculator ===\n")

    while True:
        try:
            profit = float(input("Enter total profit: ").strip())
            revenue = float(input("Enter total revenue: ").strip())

            # ratio calculation (may raise ZeroDivisionError)
            ratio = profit / revenue

        except ValueError:
            # Silent reprompt for invalid numeric input
            pass

        except ZeroDivisionError:
            print("Revenue cannot be zero. Please try again.\n")

        else:
            # Runs only if no exceptions occurred
            percentage = ratio * 100
            print(f"\nProfit Margin Ratio: {percentage:.2f}%")
            break  # Exit loop once successful


if __name__ == "__main__":
    main()

# calculates profit margin (profit / revenue).
# It demonstrates defensive programming using try-except-else,
# handling ValueError and ZeroDivisionError.    