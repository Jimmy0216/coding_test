# 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.

# 제한사항
# -50000 ≤ num1 ≤ 50000
# -50000 ≤ num2 ≤ 50000

def solution(num1, num2):
    # 입력값 검증
    if not (-50000 <= num1 <= 50000 and -50000 <= num2 <= 50000):
        raise ValueError("입력값은 -50000 이상 50000 이하의 정수여야 합니다.")
    
    # 계산 수행
    answer = num1 - num2
    return answer