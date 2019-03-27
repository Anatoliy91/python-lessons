import random

def list_random(c1, с2):
    y = random.sample(c1, с2)
    return y

def compare_lists(list1, list2):
    if len(list1) == len(list2):
        return True
    else:
        return False

c1 = list(range(1,5))
c2 = random.randint(1, 5)
print(list_random(c1, c2))

def func():
    for a in range(1000):
        a = compare_lists(list1 = list_random(range(1,100), random.randint(1,10)),
                          list2 = list_random(range(1,100), random.randint(1,10)) )
        print(a)

func()