# start developing

def fizzbazz():
    for i in range(1, 100+1):
        if i % 3:
            print("Fizz")
        elif i % 5:
            print("Buzz")
        elif i % 3 and i % 5:
            print("FizzBazz"
        else:
            print(i)


fizzbazz()
