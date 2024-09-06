# 문제 설명
# 정수 리스트 num_list가 주어질 때, 
# 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 
# 음수가 없다면 -1을 return합니다.

def solution(num_list):
    
    for index, num in enumerate(num_list):
        if num < 0:
            return index
    return -1