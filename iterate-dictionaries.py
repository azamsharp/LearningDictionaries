
# ITERATING THROUGH DICTIONARY 

 # "address": {"street": "1200 Richmond", "city": "Houston", "state": "TX"}

user = {"first_name": "John", "last_name": "Doe", "middle_name": "Steven"}

print("OPTION 1")
for key in user: 
    print(user[key])

print("OPTION 2")
for item in user.values(): 
    print(item)

print("OPTION 3")
# (key, value) is called Tuple 
# When a function returns a pair of values it is called Tuple
for key, value in user.items():  
    print(key)
    print(value)
    print(f"{key} with {value}")

# DELETING FROM A DICTIONARY 
electric_car = {"make": "TESLA", "model": "Model S"}

del electric_car["model"]
print(electric_car)
print("Hello World")