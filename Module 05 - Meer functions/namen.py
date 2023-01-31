def get_person_data():
    name = input("Enter name: ")
    age = input("Enter age: ")
    return {'name': name, 'age': age}

person_data_list = []

while True:
    person_data = get_person_data()
    person_data_list.append(person_data)

    stop = input("Toets enter om door te gaan of stop om te printen: ")
    if stop.lower() == 'stop':
        break

for person in person_data_list:
    print(f"{person['name']} is {person['age']} jaar oud")
