def generate_fibonacci_by_terms(terms):
    """Generate Fibonacci series for a given number of terms."""
    if terms <= 0:
        return []
    series = [0, 1]
    for _ in range(2, terms):
        series.append(series[-1] + series[-2])
    return series[:terms]

def generate_fibonacci_by_value(max_value):
    """Generate Fibonacci series up to a specific maximum value."""
    series = [0, 1]
    while series[-1] + series[-2] <= max_value:
        series.append(series[-1] + series[-2])
    return [num for num in series if num <= max_value]

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
            continue
        
        if choice == 1:
            try:
                terms = int(input("Enter the number of terms: "))
                if terms < 0:
                    print("Number of terms must be a non-negative integer.")
                    continue
                series = generate_fibonacci_by_terms(terms)
                print(f"Fibonacci series ({terms} terms): {', '.join(map(str, series))}")
            except ValueError:
                print("Invalid input! Please enter a non-negative integer.")
        
        elif choice == 2:
            try:
                max_value = int(input("Enter the maximum value: "))
                if max_value < 0:
                    print("Maximum value must be a non-negative integer.")
                    continue
                series = generate_fibonacci_by_value(max_value)
                print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, series))}")
            except ValueError:
                print("Invalid input! Please enter a non-negative integer.")
        
        elif choice == 3:
            print("Goodluck!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
