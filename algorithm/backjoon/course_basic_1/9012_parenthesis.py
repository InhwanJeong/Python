import sys

if __name__ == '__main__':
    wordCount = int(input())

    for i in range(wordCount):
        word = sys.stdin.readline().replace("\n", "")
        stackList = []
        for j in range(len(word)):
            if word[j] == "(":
                stackList.append("(")
            elif word[j] == ")":
                if stackList:
                    stackList.pop()
                    if j == len(word)-1 and not stackList:
                        print("YES")
                else:
                    print("NO")
                    break
        if stackList:
            print("NO")