def create_record(name, telephone, address):
    record = {
        "name" : name,
        "phone" : telephone,
        "address" : address
    }
    return record

user1 = create_record("vasya", "123122321321", "tunissia")
user2 = create_record("petya", "456456546", "dfgdfg")
user3 = create_record("griha", "345345", "tunisfsdfsdfsia")
user4 = create_record("kolya", "76878678", "trty")
user5 = create_record("tolya", "345345345", "tuniryfghssia")

print(user1)
print(user2)

def give_award(medal, *persons):
    for person in persons:
        print("tov " + person.title() + " nagragdayetsya " + medal)

give_award("Za berlin", "Vasya", "Petya")
give_award("Za lenina", "Grisha", "Vasya", "Petya")

