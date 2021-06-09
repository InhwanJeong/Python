# walrus operator

fruit = {
    'apple': 10,
    'lemon': 0,
    'orange': 5
}
'''
Don't use walrus operator
a = fruit.get('lemon')
if a>5:
'''
if (a := fruit.get('lemon')) > 5:
    print('get item')
else:
    print('out of stock')


# walrus if-else 2
if (a := fruit.get('lemon')) > 1:
    print('get lemon juice')
elif (a := fruit.get('apple')) > 4:
    print('get apple icecream')
elif (a := fruit.get('orange')) > 3:
    print('get orange candy')
else:
    print('out of stock')


# while walrus
while (itemCount := fruit.get(item:='apple')) > 0:
    print(itemCount)
    fruit[item] = itemCount -1