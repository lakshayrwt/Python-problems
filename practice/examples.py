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

print()
         #0123456789012345678901234567
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-11]
print(backwards)

print()

QPO = letters[16:13:-1]
EDCBA = letters[4::-1]
REVERSO = letters[:-9:-1]
print()

print(QPO)
print(EDCBA)
print(REVERSO)
print(letters[-4:])
print(letters[0:-25])

print()

string1 = "he's "
string2 = "probably "
string3 = "an "
string4 = "anime "
string5 = "watcher "
print(string1 +   string2   + string3   + string4   + string5)

print()

print("hello " * 5)
print("hello " * (5 + 4))
print("hello " * 5 + "4")

today = "friday"
print("fri" in today)
print("day" in today)
print("thur" in today)
print("Norwegian Blue" in parrot)

age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print()

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "jan", "march", "may", "july", "aug", "oct", "dec"))

print("there are {0} days in Jan, Mar, May, July, Aug, Oct, Dec".format(31))

print("jan:{1}, feb:{0},march:{1}, april:{2},may:{1}, june:{2},july:{1}, august:{1},September:{2}, october:{1},november:{2}, december:{1},".format(28, 31,30))
print()
print("""
jan:{1}
feb:{0}
mar:{1}
apr:{2}
may:{1},
jun:{2}
jul:{1}
aug:{1}
Sep:{2}
oct:{1}
nov:{2}
dec:{1}
""".format(28,31,30))

print()

for i in range(1, 13):
    print("No. {0:2} squared {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:15}".format(22 / 7))

name = "lakshay"
age = 19
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:<12.50f}")
Pi = 22 / 7
print(f"pi is approximately {Pi:<12.50f}")
print("PI is approximately %60.50f"% (22 / 7))

meal1 = "spam" + "eggs" + "beans"
meal3 = "spam, eggs, beans"
meal2 = "spam\neggs\nbeans"
print(meal2)
print(meal1)
print(meal3)

print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")

#first_name = "John"
#last_name = "Cleese"
#age = 78
 
#print(first_name + last_name + age)

a = 45
b = 15
c = 3
 
print(a - b / c)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)
#      01234567890123456789012345678901234   
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
      # .    .    .    .    .    .    .    .
      #0123456789012345678901234567890123456789 
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[1:5])

flower = "blue violet"
print('blue'in flower)
