def add(num1, num2):
    return(num1 + num2)
def sub(num1, num2):
    return(num1 - num2)
def mul(num1, num2):
    return(num1 * num2)
def div(num1, num2):
    return(num1 / num2)
print("please select operations -\n"\
      "1. add \n" \
      "2. sub \n" \
      "3. mul \n" \
      "4. div \n")

select=int(input("select operations form 1, 2, 3, 4: ")
num1 = int(input("Enter first number: ")
num2 = int(input("Enter second number: ")

if select == '1':
         print(num1, "+", num2, "="
                               add(num1, num2))

elif select == '2':
         print(num1, "-", num2, "="
                               add(num1, num2))

elif select == '3':
         print(num1, "*", num2, "="
                               add(num1, num2))

elif select == '4':
         print(num1, "/", num2, "="
                               add(num1, num2))
else:
    print("invalid input")
