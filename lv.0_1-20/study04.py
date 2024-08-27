# 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# * 0 < num1 ≤ 100
# * 0 < num2 ≤ 100

def solution(num1, num2):
    if not (0 < num1 <= 100 and 0 < num2 <= 100):
        raise ValueError("0부터 100까지의 정수여야 합니다.")
    answer = num1 // num2
    return answer