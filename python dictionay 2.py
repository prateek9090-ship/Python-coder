# Create a dictionary
marks = {
    "Math": 90,
    "Science": 85,
    "English": 88
}

# Print all subjects and marks
print("Marks:", marks)

# Check if a subject exists
if "Math" in marks:
    print("Math marks:", marks["Math"])

# Update a value
marks["Science"] = 89

# Remove an item
marks.pop("English")

# Print updated dictionary
print("Updated Marks:", marks)