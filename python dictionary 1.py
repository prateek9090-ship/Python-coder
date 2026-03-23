# Create a dictionary
student = {
    "name": "Rahul",
    "age": 18,
    "marks": 85
}

# Print dictionary
print("Student details:", student)

# Access values
print("Name:", student["name"])
print("Marks:", student["marks"])

# Add new key-value pair
student["grade"] = "A"
print("Updated dictionary:", student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)