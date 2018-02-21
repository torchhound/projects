bottles = 99
for x in range(0,98):
    print("{} bottles of beer on the wall, {} bottles of beer \n Take one down pass it around, {} bottles of beer on the wall \n".format(bottles, bottles, bottles - 1))
    bottles -= 1
