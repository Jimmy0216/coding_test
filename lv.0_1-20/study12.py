# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
# array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ array의 길이 ≤ 100
# 0 ≤ array의 원소 ≤ 1,000
# 0 ≤ n ≤ 1,000

def solution(array, n):
    if not (1 <= len(array) <= 100 and
            all(0 <= x <= 1000 for x in array) and
            0 <= n <= 1000):
        raise ValueError("입력값이 제한사항을 벗어났습니다.")
    
    # n이 array에 몇 번 나타나는지 계산
    answer = array.count(n)
    
    return answer