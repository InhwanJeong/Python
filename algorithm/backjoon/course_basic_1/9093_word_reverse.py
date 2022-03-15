import sys

if __name__ == '__main__':
    wordCount = int(input())

    for i in range(wordCount):
        sentence = sys.stdin.readline().replace("\n", "").split()
        sentence = [word for word in sentence]

        for word in sentence:
            for i in range(len(word)):
                print(word[-1-i], end="")
            print(end=" ")