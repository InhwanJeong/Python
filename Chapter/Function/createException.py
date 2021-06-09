item_count = 100
sell_count = 22

# sell_count = 150
# sell_count = 22.2
# sell_count = "22"
# sell_count = [22,22]

def sell_item(item_count: int, sell_count: int) -> int:
    '''item_count(현재 남은 물건 개수)에 sell_count(판매개수)를 뺀다.

    Raises:
        ValueError: 입력값이 int가 아닐때
        ValueError: 현재 남아있는 물건의 개수가 판매될 개수 보다 적을 때
    '''
    if type(item_count) is type(1) and type(sell_count) is type(1):
        if (result := item_count - sell_count)< 0:
            raise ValueError("판매될 개수가 남아 있는 물건 개수보다 많습니다.")
        return result

    else:
        raise ValueError("올바르지 않은 값을 입력하였습니다.")

try:
    item_count = sell_item(item_count, sell_count)
    print(item_count)
except ValueError as e:
    print(e)