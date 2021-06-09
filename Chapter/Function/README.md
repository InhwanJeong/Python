# 함수
파이썬은 프로그래머들이 처음으로 사용하는 정리 도구이다.
- 가독성을 높힐 수 있다.
- 코드에 더 쉽게 접근 가능하다.
- 재사용과 리펙토링이 쉬워진다.

## 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹하지 말라
- 함수가 여러값을 반환하기 위해서는 튜플에 넣어서 반환, 호출하는 쪽에서는 파이썬 언패킹 구문을 쓸 수 있다.
  
    ~~~python3    
    def temp() -> tuple:
        # 튜플에 넣어서 반환
        return (10, 20)
    # 언패킹
    a, b = temp()
    ~~~
- 언패킹 구문에 변수가 네 개 이상 나오면 실수하기 쉽다. 대신 작은 클래스를 반환하거나 namedtuple 인스턴스를 반환

## None을 반환하기 보다 예외를 발생
None은 false가 아니라 true를 반환한다. 따라서 None을 반환하면 오류를 야기하기 좋다.
~~~ python3
def sell_item(item_count: int, sell_count: int) -> int:
    '''
    
    '''
    result = item_count - sell_count
    
    if type(result) == type(int): 
    
~~~
