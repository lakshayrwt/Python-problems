print('hello,all the beautiful people in the universe')
print("the end or is it? keep watching to learn more about python 3")
print("My hovercraft is full of eels")
print(7*6)
Greeting = "Namaste"
Name = input("Enter your name:")
print(Greeting + ' ' + Name)
print("")
splitscreen =("This string\nhas been\nsplit over\nmultiple times")
print(splitscreen)
print("")
insertion =("There\thave\tbeen\tmany\tinsertions")
print(insertion)
print("")
print("")
Line1 =("S.No.\t\tName\t\t\tType")
print(Line1)
Line2 =("1.\t\tPikachu\t\t\tElectric")
print(Line2)
Line3 =("2.\t\tCharizard\t\tFire")
print(Line3)
Line4 =("2.\t\tBlastoise\t\tWater")
print(Line4)
Line5 =("3.\t\tVenasaur\t\tGrass")
print(Line5)
Line6 =("4\t\tDarkrai\t\t\tDark")
print(Line6)
print()
Table =("Number 1\tThe Larch\nNumber 2\tThe Horse Chestnut")
print(Table)
print()
bun_price = 2.40
money = 15
print(money//bun_price)
print()
a = 12
b = 3
print(a + b / 3 - 4 * 12)
print(((a + b )/ 3 - 4 ) * 12)
print()
#         01234567890123
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[13])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-14])

print()

print(parrot[3-14])
print(parrot[13-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])

print()

print(parrot[0:6])

print()

print(parrot[3:5])

print()

print(parrot[10:14])

print(parrot[:])

print()
        # 0123456789012345678901234567
#letters = "abcdefghijklmnopqrstuvwxyz"

#print(letters[12:13] + letters[24:25]) + (letters) + (letters[13:14] + (letters[0:1]) + letters[12:13] + letters[4:5])  + (letters)+ (letters[8:9] + letters[18:19]) + (letters) + (letters[11:12] + letters[0:1] + letters[10:11] + letters[18:19] + letters[7:8] + letters[0:1] + letters[24:25]) + (letters) + (letters[17:18] + letters[0:1] + letters[22:23] + letters[0:1] + letters[19:20])

print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[-14:-8])

print()

print(parrot[0:6:2])
print(parrot[0:6:3])

print()

number ="9,223,372,036,854,775,807"
print(number[1::4])

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val)for val in values])