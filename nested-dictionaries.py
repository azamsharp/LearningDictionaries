
user = {"first_name": "John", "last_name": "Doe"}

address1 = {"street": "1200 Richmond", "city": "Houston", "state": "TX"}
address2 = {"street": "1200 Harvin", "city": "Austin", "state": "TX"}

user["addresses"] = [address1, address2]

print(user)

addresses = user["addresses"]

numbers = [11,32,43,54,5]

for index in range(0, len(numbers)): 
    print(number[index])

for number in numbers: 
    print(number)

# print all addresses 
for address in addresses:
    print(address["street"] + " " + address["city"])



#employee = {name: "John Doe", badgeNumber: "1234", "employer_name": "HEB", "employer_title": "Supervisor",
#    "employer_location": "Houston"
#}

name = employee["employer_name"]
title = employee["employer_title"]
location = employee["location"]

employer = {"name": "HEB", "title": "Supervisor", "location": "Houston"}

employee = {"name": "John Doe", "badgeNumber": "4567", 
            "employer": employer
}

employer = employee["employer"]


