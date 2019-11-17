
while True:
    #making sure the entered number is a number
    try:
        end = int(input("Please select a number between 1 and 100: "))

    except ValueError:
        print("You have to enter a number.")
        break

    #making sure the entered number is between 1 and 100
    if end + 1 <= 100 and end + 1 >= 0:
        pass
    else:
        print("You must enter a number between 1 and 100!")
        break

    #FizzBuzz operation
    for num in range(1, end+1):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
    break
