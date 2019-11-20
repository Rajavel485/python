def cab(num):
    return
def auto(num):
    return
def bike(num):
    return
name = input("Enter your name: ")
print(name)
num = input("Enter your number: ")
print(num)
print("please select -\n"\
      "1. cab \n" \
      "2. auto \n" \
      "3. bike \n")
select = int(input("select 1, 2, 3, 4: "))

src = input("enter your location")
dst = input("enter your drop location")

if select == '1':
         print("Rs 20 for 1km")
elif select == '2':
         print("Rs 15 for 1km")
elif select == '3':
         print("Rs 10 for 1km")
else:
    print("invalid input")

