name = ''
age = ''

def your_data():
    global name
    global age
    name = input('Your name: ')
    age = input('Your age: ')
    print("Hi, Your entered data: Name- " + name + " and age- " + age)

def your_arguments():
    print('We will now add two numbers')
    arg1= input('please enter a number: ')
    arg2= input('please enter another number: ')
    sum = float(arg1) + float(arg2)
    print('the sum of ' + arg1 + ' and ' + arg2 + ' is ' + str(sum))

def num_of_decades():
    decades = int(age)//10
    print('according to your age, you\'ve lived ' + str(decades) + ' decades')

your_data()
your_arguments()
num_of_decades()