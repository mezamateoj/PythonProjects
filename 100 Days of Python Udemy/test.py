import time
import datetime
# def add(*args):
#     arguments_list = [x for x in args]
#     return sum(arguments_list)

# class Model:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get('make')  # Use get so if argument does not exist returns none.
#         self.model = kwargs.get('model')

# new_car = Model(make='Nissan')
# print(new_car.model) 
def timer():
    total_seconds = 5 * 60 + 0
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer)
        # Prints the time left on the timer
        # self.time.append(timer)
        # print(timer, end="\r")
        # Delays the program one second

        time.sleep(1)
        # Reduces total time by one second
        total_seconds -= 1
        
print(timer())

