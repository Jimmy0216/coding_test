# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    num = 0
    
    for char in my_string:
        if char.isdigit():
            num += int(char)
    
    return num