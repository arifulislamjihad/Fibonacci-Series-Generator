def generate_fibonacci_by_terms(n):
    """Generate Fibonacci series for a given number of terms."""
    if n <= 0:
        return []
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[:n]

def generate_fibonacci_by_max_value(max_value):
    """Generate Fibonacci series up to a maximum value."""
    if max_value < 0:
        return []
    fibonacci_series = [0, 1]
    while True:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        if next_term > max_value:
            break
        fibonacci_series.append(next_term)
    return fibonacci_series

def main():
    """Main function to provide user options."""
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                terms = int(input("Enter the number of terms: "))
                if terms < 0:
                    print("Please enter a non-negative integer.")
                else:
                    result = generate_fibonacci_by_terms(terms)
                    print(f"Fibonacci series ({terms} terms): {', '.join(map(str, result))}")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        elif choice == "2":
            try:
                max_value = int(input("Enter the maximum value: "))
                if max_value < 0:
                    print("Please enter a non-negative integer.")
                else:
                    result = generate_fibonacci_by_max_value(max_value)
                    print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, result))}")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
