name = "Umang Ramani"
print(name.capitalize())

print(name.upper())
print(name.lower())

print(name.find("Ramani")) 
print(name.find("Ramani",6,12)) 

print(name.startswith("Umang"))
print(name.startswith("Umang", 0, 5))

print(name.replace("Ramani", "Patel"))

print(name.split(" "))

stringtest = "Hello {name}! , Your are {age} years old."
print(stringtest.format(name="Umang Ramani", age=25))
