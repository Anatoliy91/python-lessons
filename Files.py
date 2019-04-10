# inputfile = "user_name.txt"
#
# myfile = open(inputfile, mode='r', encoding='utf_8')
# # print(myfile.read())
#
# for num, line in enumerate(myfile, 1):
#     if "sd" in line:
#         print("line № " + str(num) + " " + line.strip())
#

inputfile = "passwords.txt"
outpitfile = "new_passwords.txt"

myfile = open(inputfile, mode='r', encoding='utf_8')
myfile2 = open(outpitfile, mode="a", encoding='utf_8')
# print(myfile.read())

for num, line in enumerate(myfile, 1):
    if "sd" in line:
        print("line № " + str(num) + " " + line.strip())
        myfile2.write('Found password' + line)
sorted(line)


myfile.close()
myfile2.close()