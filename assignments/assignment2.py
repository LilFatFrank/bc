listofNames = ['Max', 'Chris', 'Will', 'John', 'Donald']

def length_of_names():
    for index in range(len(listofNames)):
        print(listofNames[index] + ':' + str(len(listofNames[index])))

def length_more_than_five():
    for name in listofNames:
        if(len(name)>5):
            print(name)

def contains_n():
    for name in (listofNames):
        if ('n' in name) or ('N' in name):
            print(name)

def empty_list():
    while len(listofNames):
        print('before pop(): {}'.format(listofNames))
        listofNames.pop()
        print('after pop(): {}'.format(listofNames))
        print('-' * 20)

def user_choice():
    return input('Your choice:')

user_has_input = True

while user_has_input:
    print('Choose your option-')
    print('1. print length of all names')
    print('2. print names of length more than 5')
    print('3. print names that contain n or N')
    print('4. empty the list and quit')
    user_input = user_choice()
    if user_input == '1':
        length_of_names()
    elif user_input == '2':
        length_more_than_five()
    elif user_input == '3':
        contains_n()
    elif user_input == '4':
        empty_list()
        user_has_input = False
    else:
        print('invalid choice')

print('done, thank you')