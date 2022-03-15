import sys

if __name__ == '__main__':
    iterNum = int(input())

    stackList = []
    for i in range(iterNum):
        inputData = sys.stdin.readline().replace("\n", "")
        if "push" in inputData:
            stackList.append(inputData.split()[-1])
        if inputData == "pop":
            if stackList:
                print(stackList.pop())
            else:
                print(-1)

        if inputData == "size":
            print(len(stackList))

        if inputData == "empty":
            if stackList:
                print(0)
            else:
                print(1)

        if inputData == "top":
            if stackList:
                print(stackList[-1])
            else:
                print(-1)
