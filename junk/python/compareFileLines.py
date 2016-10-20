import sys

def compareFile(): #(txtFile1, txtFile2):
    overlap = []
    txt1 = open("primenumbers.txt", "r") #open(txtFile1, "r")
    txt2 = open("happynumbers.txt", "r") #open(txtFile2, "r")
    print(txt1, txt2)
    for line in txt1:
        for line1 in txt2:
            if line == line1:
                overlap.append(line)
    print(overlap)

def main():
    #compareFile(sys.argv[1], sys.argv[2])
    compareFile()

if __name__ == "__main__":
    main()
