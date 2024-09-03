# 문제 설명
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

def solution(n):
    total = 0
    
    while n > 0:
            total += (n % 10)
            n = n // 10
    return total