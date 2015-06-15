def main():
    print "Converter converts to Celsius"
    temp = raw_input("Please input numerical temperature: ")
    sys = raw_input("Please input temperature type: ")
    if sys == 'f' or 'F':
        c = 5/9(float(temp)-32)
        print "C" + c
    elif sys == 'k' or 'K':
        int(temp)
        k = float(temp) - 273.15
        print "C" + k
    elif sys == 'c' or 'C':
        print "C" + temp
    else:
        return False

main()
