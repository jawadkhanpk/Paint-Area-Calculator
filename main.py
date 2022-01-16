#You're painting a wall the instructions on the paint can says that
# (one can of paint can 5 squares meters) of the wall. Given a random
# height and width of the wall to calculate how many cans of pait you need to buy

import  math

def paint_calc(height, width, cover):
    area = height * width
    num_of_can = math.ceil(area / cover)
    print(f"You'll need {num_of_can} can of paint")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height= test_h, width= test_w, cover= coverage)