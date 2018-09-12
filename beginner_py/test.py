name = input('Your name is: ')
age = input('Your age is: ')

def my_info():
    print(name + ' ' + age)


my_info()

def decades():
    timeframe = int(age) // 10
    return timeframe


print(decades())
