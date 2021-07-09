
# DICTIONARIES 

# Dictionary = {Key: Value}

airport = {"IAH": "Intercontinental Airport", "SEATAC": "Seattle Airport"}
#name = airport["HOBBY"]
#print(name) 

cars = [] 

while True:
    make = input("Enter make: ")
    model = input("Enter model: ")

    car = {"make": make, "model": model}
    cars.append(car)

    choice = input("Enter q to quit or any key to continue: ")
    if choice == "q": 
        break 

print(cars)

#car = {"make": make, "model": model, "noOfCylinders": 4, "isElectric": False}

#tweet = {"username": "Vincent", "text": "So what exactly...", 
#    "date_created": "07/09/2021", "hasMedia": True, "likes": 7, "retweets": 2
#}

#print(car)

# EMPTY DICTIONARY 
user = {}

user["first_name"] = "John"
user["last_name"] = "Doe"

#print(user["first_name"] , user["last_name"])

print(f'{user["first_name"]}')

first_name = "John"
last_name = "Doe"

user = {"first_name": first_name, "last_name": last_name}

print(user["first_name"] + " " + user["last_name"])
