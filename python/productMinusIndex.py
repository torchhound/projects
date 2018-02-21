from functools import reduce

def productMinusIndex(integers):
    for x in integers:
        print(reduce(lambda x, y: x * y, integers[:integers.index(x)] + integers[integers.index(x) + 1 :]))

def main():
    productMinusIndex([1,2,3])
    productMinusIndex([50,90,20])

if __name__ == "__main__":
    main()
