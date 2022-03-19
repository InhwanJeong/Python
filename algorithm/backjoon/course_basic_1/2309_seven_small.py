import itertools

if __name__ == '__main__':
    inputList = [int(input()) for _ in range(9)]

    sevenList = itertools.combinations(inputList, 7)
    sevenList = list(sevenList)

    getHundred = [index for index, itemList in enumerate(sevenList) if sum(itemList) == 100]
    result = list(sevenList[getHundred[0]])
    result.sort()

    for item in result:
        print(item)
