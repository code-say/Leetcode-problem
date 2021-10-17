first_name = "sayan"
list_of_things = ['running', 'mayonaise', 'purple']
age = 24

#for i in range(5):
#    print('whats up')

#for i in range(len(first_name)):
#    print(first_name[i])

#for char in first_name:
#    print(char)


#for thing in list_of_things:
#    print(thing)


#while age < 30:
#    print('not 30 yet')
#    age += 1

#def add_nums(a,b):
#    return a + b
#print(add_nums(10,5))

#if age < 30:
#    print('age is less than 30')
#else:
#    print('age is 30 or higher')

class Person:
    def __init__(self):
        self.age = 0

    def increase_age(self):
        self.age += 1

    def birthday(self):
        self.increase_age()
        print("sayan is now" + str(self.age) + 'years old')  