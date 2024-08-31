#error handling 1
# while True:
#     try:
#         age = int(input("enter your age"))
#         10/age
#         print(age)
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter age higher than zero')
#     else:
#         print('thank you')
#         break
#error handling 2

# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print('Please enter a number ' + err)
#     finally:
#         print('I\'m done finaly') #This finally block always executes
#
# print(sum(1, 2))

#error handling 3
while True:
    try:
        age = int(input("enter your age"))
        10/age
        print(age)
        raise Exception('hey cut it out')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than zero')
    else:
        print('thank you')
        break