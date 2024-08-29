# 문제 설명
# 정수 배열 array가 매개변수로 주어질 때, 
# 가장 큰 수와 그 수의 인덱스를 담은 배열을 
# return 하도록 solution 함수를 완성해보세요.

def solution(array):
    max_value = max(array)
    max_index = array.index(max_value)
    return [max_value, max_index]

# 다른 사람 문제풀이
def solution(array):
    return [max(array), array.index(max(array))]