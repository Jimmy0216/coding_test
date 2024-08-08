# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 1,000
# 1 ≤ numbers의 길이 ≤ 100
# 정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.


def solution(numbers):
    if not all(0 <= num <= 1000 for num in numbers) or not (1 <= len(numbers) <= 100):
        raise ValueError("입력값이 제한사항을 벗어났습니다.")
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    answer = round(average, 1)
    
    return answer

# 다른 사람의 풀이
# def solution(numbers):
#     return sum(numbers) / len(numbers)