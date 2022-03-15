if __name__ == '__main__':
    cookTimeInSeconds = int(input())

    result = []
    buttonList = [300, 60, 10]

    for button in buttonList:
        if (cookTimeInSeconds // button) > 0:
            result.append(cookTimeInSeconds // button)
            cookTimeInSeconds %= button
        else:
            result.append(0)

    if cookTimeInSeconds > 0:
        print(-1)
    else:
        for item in result:
            print(item, end=' ')
