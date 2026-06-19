numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

if len(numbers) > 0:
    print("\nStatistics:")
    print("Count   :", len(numbers))
    print("Minimum :", min(numbers))
    print("Maximum :", max(numbers))
    print("Sum     :", sum(numbers))
    print("Average :", sum(numbers) / len(numbers))
else:
    print("No numbers were entered.")
