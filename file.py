num1 = 42 #varaible declaration, numbers
num2 = 2.3 #varaible declaration, numbers
boolean = True #varaible declaration, boolean
string = 'Hello World' #varaible declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #varaible declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #varaible declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') #varaible declaration, tuples,
print(type(fruit)) #function log, printing fruit
print(pizza_toppings[1]) #function log, printing index 1 of pizza_toppings
pizza_toppings.append('Mushrooms')# function, appending mushrooms to list of pizaa_toppings
print(person['name']) #function log, printing name key in dictionary of person
person['name'] = 'George'# changing value of name in person dictionary
person['eye_color'] = 'blue' # adding key eye_color and also value of eye color to dictionary
print(fruit[2]) #function log, printing index 2 of list

if num1 > 45:
    print("It's greater")#conditional, if else, printing string based off num1s value
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:              #condtional if elif and else printing a string based off the length, len(), of string
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):# for loop with a stop of 5 and pringting value of x
    print(x)
for x in range(2,5): # for loop with a stop of 5 and start of 2 and pringting value of x
    print(x)
for x in range(2,10,3):# for loop with a stop of 10 and start of 2 and and incremting by 3 pringting value of x
    print(x)
x = 0
while(x < 5): # while loop, pringting x in each iteration, with x starting at 0 and going up 1 in each step
    print(x)
    x += 1

pizza_toppings.pop() # function, pop, and removing last index in pizza_topping list
pizza_toppings.pop(1) # function, pop, and removing second index in pizza_topping list

print(person) #function, printing person
person.pop('eye_color')#function, pop(),removing eye_color in person
print(person)#function, printing person

for topping in pizza_toppings:  #for loop, looping through list pizza_toppings, with a print, and breaking the loop when olives is found
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function named print_hello_ten_times, having a for loop within it, with a print statement printing out hello
    for num in range(10):
        print('Hello')

print_hello_ten_times() # calling the print_hello_ten_times function

def print_hello_x_times(x):# function named print_hello_x_times with a parameter of x, and a for loop within it thatll run till the value of x and each step it will print out hello
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # calling function with argument of 4

def print_hello_x_or_ten_times(x = 10): # function with a deafualt parameter of 10 and a for loop thatll run till the value of x, loop will print out hello each time
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()# calling function with no arguement, so it will default to 10
print_hello_x_or_ten_times(4)# calling function with arguement of 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)