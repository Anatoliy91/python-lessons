import sys

filename = "password.txt"

while True:

    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding='utf_8')
    except Exception:
        print("Inside EXCEPT")
        print("ERROR FOUND")
        print(sys.exc_info()[2])
        filename = input("Correct file name:")

    else:
        print("Inside ELSE")
        print(myfile.read())
    finally:
        print("Inside Finally")
        sys.exit()


print("_________________________________________________END ")