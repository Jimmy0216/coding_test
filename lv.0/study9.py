# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
# 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

# 예각 : 0 < angle < 90
# 직각 : angle = 90
# 둔각 : 90 < angle < 180
# 평각 : angle = 180

# 제한사항
# 0 < angle ≤ 180
# angle은 정수입니다.

def solution(angle):
    if not (0 < angle <= 180):
        raise ValueError("각도는 0보다 크고 180 이하의 정수여야 합니다.")
    
    if 0 < angle < 90:
        answer = 1  # 예각
    elif angle == 90:
        answer = 2  # 직각
    elif 90 < angle < 180:
        answer = 3  # 둔각
    else:  # angle == 180
        answer = 4  # 평각
    
    return answer

# 다른 사람 풀이
# def solution(angle):
#     return 2 if angle==90 else 1 if angle<90 else 4 if angle==180 else 3
