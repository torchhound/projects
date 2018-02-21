def listCompEven(listN):
    return [x for x in listN if x != 0 and x % 2 == 0 and listN.index(x) % 2 == 0]

def main():
    print(listCompEven([1,2,3,4,5,6,7,8,9,10]))
    print(listCompEven([0,2,2,2,4,5,6,8,2,4,1,6,9]))

if __name__ == "__main__":
	main()
