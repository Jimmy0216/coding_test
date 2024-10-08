# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
# 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 
# 중앙값을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# array의 길이는 홀수입니다.
# 0 < array의 길이 < 100
# -1,000 < array의 원소 < 1,000

def solution(array):
    # 제한사항 검사
    if not (0 < len(array) < 100 and 
            len(array) % 2 == 1 and 
            all(-1000 < x < 1000 for x in array)):
        raise ValueError("입력값이 제한사항을 벗어났습니다.")
        
    return sorted(array)[len(array) // 2]