import sys

# Check if numbers are provided
if len(sys.argv) < 2:
    print("Usage: python3 stats.py num1 num2 num3 ...")
    sys.exit()

# Convert command-line arguments to floats
numbers = [float(x) for x in sys.argv[1:]]

# Count
count = len(numbers)

# Sum
total = sum(numbers)

# Mean
mean = total / count

# Median
sorted_numbers = sorted(numbers)

if count % 2 == 1:
    median = sorted_numbers[count // 2]
else:
    median = (
        sorted_numbers[count // 2 - 1]
        + sorted_numbers[count // 2]
    ) / 2

# Mode
freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

max_frequency = max(freq.values())

modes = []

for num, frequency in freq.items():
    if frequency == max_frequency:
        modes.append(num)

# Variance
variance = sum((x - mean) ** 2 for x in numbers) / count

# Standard Deviation
std_dev = variance ** 0.5

# Display Results
print("\n===== STATISTICS REPORT =====")
print(f"Count               : {count}")
print(f"Sum                 : {total}")
print(f"Mean                : {mean:.2f}")
print(f"Median              : {median:.2f}")

if max_frequency == 1:
    print("Mode                : No mode")
else:
    print(f"Mode                : {modes}")

print(f"Variance            : {variance:.2f}")
print(f"Standard Deviation  : {std_dev:.2f}")

# ASCII Bar Chart
print("\n===== ASCII BAR CHART =====")

for num in numbers:
    print(f"{num:>6}: {'#' * int(num)}")
