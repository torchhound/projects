def answer(area):
    final = []
    if area == 0:
        return final
    else:
        if area % 2 == 0:
            final.append(area)
        else:
            answer(area - 1)

def main():
    print(answer(12))
    print(answer(15324))

if __name__ == "__main__":
    main()
