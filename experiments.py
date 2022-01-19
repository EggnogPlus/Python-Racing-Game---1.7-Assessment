"""
91883: Develop a computer program
This standard requires that the learner’s
program uses data stored in collections or
 uses user-defined methods, functions or
 procedures (or possibly uses both).
The terms ‘collections’ and ‘user-defined methods, functions or procedures’ are all plural,
so more than one collection or more than one user-defined method, function or procedure must be used.
For example, a program with two functions and one list meets the requirements, but a program with one
list and one function does not.

The learner is required to test and debug their program. Testing should be clearly documented. In particular,
the tests that the program has passed should be made clear.

For Merit, the learner needs to follow conventions for the programming language.
Most languages have well-established conventions, particularly relating to naming and code layout.
There are automated tools to check conventions available for many popular languages.


"""
# make car distance like car_distance and if that number is rolled do the +=1 thing to make the carmove
import random

# write an intro to the game asking for a car number
import cars as cars

print("Hello and welcome to my car game ( ✧≖ ͜ʖ≖)")
print("_______________________________________")


# check the car number
def car_check(low_boundary, high_boundary, amount_initial):
    valid = False
    while not valid:
        try:
            amount_initial = int(input("which car would you like to play with? (1-6)? "))
            if low_boundary <= amount_initial <= high_boundary:
                print("you have entered as car - {}".format(amount_initial))
                return amount_initial
            else:
                print('you need a number between 1 and 6! try again!')
                continue
        except ValueError:
            print('you need a number between 1 and 6! try again!')
    return amount_initial


car_c = car_check(1, 6, 0)


# keeping this just in case
# track_number = int(input('now select a track length: 10 or 15?'))
# if 1<= track_number <=6:
# print("good luck")
# else:
# print("That's not an option, try again")
# ask and check track

# track_number = 0
def track_check(low_boundary, high_boundary, track_number):
    valid = False

    while not valid:

        try:
            track_number = int(input('now select a track length between: 5 & 15?'))
            if low_boundary <= track_number <= high_boundary:
                print("you have selected track number - {}. Good luck racing!".format(track_number))
                # break
                return track_number
            else:
                print('sorry, you need a track number between 5 & 15')
                continue
        except ValueError:
            print('you need a track number between 5 & 15, try again.')

    return track_number


# store the result
# print the result
track_number = track_check(5, 15, 0)  # setting track_number to 0
# check
# print(track_number)


# somehow this makes a nill value... lol?
# track_number = intcheck("now select a track length", 5, 15, track_number)
times = (90)
winner = 0
car1 = 0
car2 = 0
car3 = 0
car4 = 0
car5 = 0
car6 = 0
# if I remove the commas then winner is not defined??
# cars = ["car 1", "car 2", "car 3", "car 4", "car 5", "car 6"]
cars = list(range(7))
print(cars)
for i in range(times):
    number = random.choice(cars)
    # print(number)
    if number == 1:
        car1 = car1 + 1
    elif car1 == track_number:
        print('Car 1 has won!')
        winner = 1
        break
    elif number == 2:
        car2 = car2 + 1
    elif car2 == track_number:
        print('Car 2 has won!')
        winner = 2
        break
    elif number == 3:
        car3 = car3 + 1
    elif car3 == track_number:
        print('Car 3 has won!')
        winner = 3
        break
    elif number == 4:
        car4 = car4 + 1
    elif car4 == track_number:
        print('Car 4 has won!')
        winner = 4
        break
    elif number == 5:
        car5 = car5 + 1
    elif car5 == track_number:
        print('Car 5 has won!')
        winner = 5
        break
    elif number == 6:
        car6 = car6 + 1
    elif car6 == track_number:
        print('Car 6 has won!')
        winner = 6
        break

if winner == car_c:
    print('You were car {}, You won! ( ͡^ ͜ʖ ͡^)'.format(car_c))
else:
    print('You were car {}, You lost ( ཀ ʖ̯ ཀ)'.format(car_c))

print(
    'here are the placings for the race (Length:{})- Car 1: {}, Car 2: {}, Car 3: {}, Car 4: {}, Car 5: {}, Car 6: {},'.format(
        track_number, car1, car2, car3, car4, car5, car6, ))
# print(car_c)
# elif cars == 'car2':


'''
#winner of race
print(winner)
#player car
print(car_c)
#track number
print(track_number)
'''
