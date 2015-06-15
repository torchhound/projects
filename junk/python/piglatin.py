def main(string):
    string = raw_input('Pig Latinify: ")
    string.split()
    for x in string:
        if x == 'a','e','i','o','u':
            return True
        else:
            if x != 'a','e','i','o','u':
                string.insert(len(string),x)
                return False
    string.append('ay')
main()
