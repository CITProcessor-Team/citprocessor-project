
# word_frequency.py

# Read the text file
with open("sample_text.txt", "r") as f:
    text = f.read()

# Split into words
words = text.split()

# Count frequencies
counts = {}

for word in words:
    word = word.lower().strip(".,!?;:\"'")
    counts[word] = counts.get(word, 0) + 1

# Sort by frequency (highest first)
top_words = sorted(
    counts.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

# Print results
print("Top 10 Most Common Words")
print("-" * 30)

for word, count in top_words:
    print(f"{word:<15} {count}")
