class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


a = input().split()
for i in a:
    if hasattr(Person, i.lower()) == True:
        print(i, '-', 'YES', sep='')
    else:
        print(i, '-', 'NO', sep='')
