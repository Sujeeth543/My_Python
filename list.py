# List are mutable objects.
# we can add or delete objects in tuples
student_names = ["ramu", "charan", "anil", "mahesh"]
student_names.append("srujan")
print(student_names)
print(len(student_names))
print(student_names[3])
print(student_names[1:4])
print(type(student_names))

# Tuples are immutables objects
# we cannot add or delete objects in tuples
vehicle_names = ("mahindra","tata","bajaj","hundai")
print(type(vehicle_names))
print(vehicle_names)