def stringPermutations(string):
    count = 1
    index = count
    while index <= len(string):
        for x in string:
            addendum = ""
            addendum += x
            index -= 1
        print(addendum)
        index = count
        count += 1

def main():
    stringPermutations("Hello")
    stringPermutations("World")
    stringPermutations("foo")

if __name__ == "__main__":
    main()
