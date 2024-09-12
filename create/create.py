import os

# 폴더 생성 (이미 존재하지 않는 경우)
folder_path = 'lv0_41-60'
os.makedirs(folder_path, exist_ok=True)

# 파일 생성
for i in range(41, 61):
    file_name = f'study{i}.py'
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'w') as file:
        file.write(f'# This is study{i}.py\n')

print("파일 생성이 완료되었습니다.")