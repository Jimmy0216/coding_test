# 문제 설명
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

def solution(price):
    if price >= 500000: 
        discount = 0.2
    elif price >= 300000: 
        discount = 0.1
    elif price >= 100000:
        discount = 0.05
    else: discount = 0.0
    
    final_price = int(price * (1 - discount))
    
    return final_price

# 다른 사람 문제풀이
def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)