import random

def get_user_input():
    """
    사용자로부터 입력을 받고 유효성을 검사합니다.
    사용자는 "짝" 또는 숫자를 입력해야 합니다.
    """
    while True:
        user_input = input("당신 차례입니다: (3,6,9면 짝) ")
        if user_input == "짝" or user_input.isdigit():
            return user_input
        else:
            print("잘못된 입력입니다. '짝' 또는 숫자를 입력하세요.")

def check_number(num):
    """
    숫자에 '3', '6', '9'가 포함되어 있는지 확인합니다.
    포함되어 있으면 True를, 아니면 False를 반환합니다.
    """
    num_str = str(num)
    for digit in num_str:
        if digit in ['3', '6', '9']:
            return True
    return False

def user_turn(i):
    """
    사용자의 턴을 처리합니다.
    사용자가 '짝'을 입력하거나 숫자를 입력했을 때의 로직을 구현합니다.
    """
    user_input = get_user_input()
    contains = check_number(i)
    
    if contains and user_input == "짝":
        print("사용자: 짝")
        return True
    elif not contains and user_input.isdigit() and int(user_input) == i:
        print(f"사용자: {i}")
        return True
    else:
        print("패배")
        return False

def computer_turn(i):
    """
    컴퓨터의 턴을 처리합니다.
    숫자에 '3', '6', '9'가 포함되어 있으면 '짝'을 출력하고,
    그렇지 않으면 숫자를 출력합니다.
    """
    if check_number(i):
        print(f"컴퓨터: 짝")
    else:
        print(f"컴퓨터: {i}")

def play_game():
    """
    메인 게임 루프를 실행합니다.
    사용자와 컴퓨터가 번갈아가며 숫자를 외칩니다.
    패배 조건이 발생하면 게임을 종료합니다.
    """
    my_turn = True
    for i in range(1, 100):
        if my_turn:
            if not user_turn(i):
                break
        else:
            computer_turn(i)
        my_turn = not my_turn

if __name__ == "__main__":
    play_game()


# 필요한 라이브러리 임포트
from git import Repo
import os

# 저장소 경로 설정
repo_path = 'path/to/robot-python'  # 로컬 저장소 경로로 변경하세요

# 저장소 열기
repo = Repo(repo_path)

# 변경된 모든 파일 스테이징
repo.git.add('--all')

# 커밋 메시지 작성
commit_message = "수정 사항을 반영합니다."  # 원하는 커밋 메시지로 변경하세요
repo.index.commit(commit_message)

# 원격 저장소 가져오기
origin = repo.remote(name='origin')

# 변경 사항 푸시
origin.push()