# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 0 < n ≤ 1000

def solution(n):
    if not (0 < n <= 1000):
        raise ValueError("0보다 크고 1000 이하의 정수를 입력해주세요.")
    
    answer = sum(i for i in range(2, n+1, 2))
    return answer