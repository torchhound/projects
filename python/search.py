def search(ordered, check):
    if check in ordered:
        print("True")
    else:
        print("False")

def main():
    searchList = [1,2,3,4,5]
    trueCheck = 1
    falseCheck = 6
    search(searchList, trueCheck)
    search(searchList, falseCheck)

if __name__ == '__main__':
    main()
