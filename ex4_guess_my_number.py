import random

answer = random.randint(1,100)

# print (answer)

while True:

    user_input = input('enter a number:')
    user_input = int(user_input)

    #  print(user_input)
    print(f'you have entered {user_input}')

    if user_input == answer:
        print ('correct')
        break
    elif user_input > answer: 
        print('too large')
    else:
        print ('too small')