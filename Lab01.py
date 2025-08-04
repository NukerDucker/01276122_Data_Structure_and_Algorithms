mod = 11
a_values = list(range(1, mod))
inverse_values = [pow(a, -1, mod) for a in a_values]

# Build table strings
header = "| a              | " + " | ".join(f"{a:>2}" for a in a_values) + " |"
separator = "|" + "-" * (len(header) - 2) + "|"
row =    "| Inverse mod 11 | " + " | ".join(f"{inv:>2}" for inv in inverse_values) + " |"

# Print the table
print(header)
print(separator)
print(row)
