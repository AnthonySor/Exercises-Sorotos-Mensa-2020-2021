#Exercise 1

#name = input('What is your name?')
#age = int(input('How old are you?'))
#currentage = 100 - age
#yearof100 = 2020 + (currentage)
#print(f'{name}, you will be 100 in the year {yearof100}')

#Exercise 2

#number1 = int(input('give me a number'))
#number2 = int(input('give me another number'))
#maximum = max(number1, number2)
#print(f'the maximum number is {maximum}')

##Exercise 3

#num1 = 10
#num2 = 14
#num3 = 12

## uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

#if (num1 >= num2) and (num1 >= num3):
#   largest = num1
#elif (num2 >= num1) and (num2 >= num3):
#   largest = num2
#else:
#   largest = num3

#   print(largest)

#|Exercise 4

#Speed = int(input('How fast do you want your driver to go?'))

#morekmph = Speed - 70
#points = morekmph / 5

#if (Speed < 70):
#    print('ok')
#print(f'you have got {points} bad points')
#if (points > 12):
#    print('licence suspended')

#Exercise 5
#max=int(input("Please enter the maximum number: "));
#for number in range(1,max+1):
#    if(number%2 !=0):
#        print(number,"ODD")
#    else:
#        print(number,"EVEN",)


#Exercise 6

#number = int(input('tell me a number'))
#if (number % 3 ==0):
#   print('fizz')
#if (number % 5==0):
#   print('fuzz')
#else:
#    print(number)

#Exercise 7

#limit = int(input('give a limit'))
#for i in range(0,limit,3):
#    print(i)

#for i in range(0,limit,5):
#    print(i)

#Exercise 8

#num = int(input('enter the number of rows'))
#for i in range(1,num+1):
#    for j in range(1,i+1):
#        print("*",end = " ")
#    print()

#Exercise 9

#lower = int(input('tell me the first number'))
#upper = int(input('tell me the second number'))

#print("Prime numbers between", lower, "and", upper, "are:")

#for num in range(lower, upper + 1):
#   # all prime numbers are greater than 1
#   if num > 1:
#       for i in range(2, num):
#           if (num % i) == 0:
#               break
#       else:
#           print(num)

#Exercise 1 a listes

# vowels list
#vowels = ['a', 'e', 'i', 'o', 'i', 'u']


#index = vowels.index('e')
#print('The index of e:', index)


#index = vowels.index('i')

#print('The index of i:', index)

#Exercise 1 b listes

#listof10 = [0,1,2,3,4,5,6,7,8,9]

#Exercise 1 c listes

#listof500andhalf = [500, 250, 125, 62.5, 31.25, 15.625, 7.8125, 3.90625, 1.953125, 0.9765625, 0.48828125]

#Exercise 2

#num1 = int(input('tell me the first number of the list'))
#num2 = int(input('tell me the second number of the list'))
#num3 = int(input('tell me the third number of the list'))
#num4 = int(input('tell me the fourth number of the list'))
#num5 = int(input('tell me the fifth number of the list'))
#num6 = int(input('tell me the sixth number of the list'))
#num7 = int(input('tell me the seventh number of the list'))
#num8 = int(input('tell me the eighth number of the list'))
#num9 = int(input('tell me the ninth number of the list'))
#num10 = int(input('tell me the tenth number of the list'))
#listof10withuser = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
#print(listof10withuser)

#Exercises 3

#list1 = list(input('give me a list'))
#if 0 in list1 in all_text:
#            print ('ok')

#Exarcise 4

#list1 = list(input('tell me a list of strings'))
#if 'end' in list1 in all_text:
#    print('ok')

#Exexercise 5

#num1 = int(input('tell me a number'))
#num2 = int(input('tell me a number'))
#num3 = int(input('tell me a number'))
#num4 = int(input('tell me a number'))
#num5 = int(input('tell me a number'))
#num6 = int(input('tell me a number'))
#num7 = int(input('tell me a number'))
#num8 = int(input('tell me a number'))
#num9 = int(input('tell me a number'))
#num10 = int(input('tell me a number'))

#print(((num1+num2+num3+num4+num5+num6+num7+num8+num9+num10) / 10))

#Exercise 6

#num1 = int(input('tell me a number'))
#num2 = int(input('tell me a number'))
#num3 = int(input('tell me a number'))

#minimum = min(num1,num2,num3)
#print(minimum)

#Exercise 7

#list1 = list(input('tell me a list of numbers'))

#print(min(list1))

#Exercise 8

#list1 = ['egg' , 'sifteocubes' , 'goateggnogoftornadoesandgoatlandianlanguage' , 'a' ]
#print('goateggnogoftornadoesandgoatlandianlanguage')

#Exercise 10

#list1 = list(input('tell me a list'))
#num1 = int(input('tell me a number'))

#count = list1.count(num1)
#print(count)

#Exercise 11

#list1 = list(input('tell me a list'))

#length = len(list1)
#print(length)

#Exercises pack2 exercise 1

#name = input('tell me your name')
#print(name * 10)

#Exercise 2

#name = input('tell me your name')
#print(f'Welcome {name} !')

#Exercise 3

#name = input('tell me your name')
#name3 = (name * 3)
#print(name3)
#name6 = (name3 * 6)
#print(name6)

#Exercise 4

#name = input('tell me your name')
#times = int(input('tell me how many times'))
#print((name) * (times))

#Exercise 5

#num = int(input('tell me a number'))
#print((num) * (num))

#Exercise 6

#length = int(input('tell me the length'))
#width = int(input('tell me the width'))
#print((length) * (width))

#Exercise 7

#height = int(input('tell me the height'))
#base = int(input('tell me the base'))
#print(height * (base/2))

#Exercise 8

#price = float(input('tell me a price'))
#print((price) / 100 * 24)


#Exercise 9

#children = int(input('how many children'))

#if(children < 3):
#    print('3%')
#if(children > 3):
#    print('5%')

