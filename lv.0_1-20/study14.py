# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# -10,000 ≤ numbers의 원소 ≤ 10,000
# 1 ≤ numbers의 길이 ≤ 1,000

def solution(numbers):
    if not (1 <= len(numbers) <= 1000 and
            all(-10000 <= x <= 10000 for x in numbers)):
        raise ValueError("입력값이 제한사항을 벗어났습니다.")
        
    return [num * 2 for num in numbers]