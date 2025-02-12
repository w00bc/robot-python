import random

# 3, 6, 9
#사용자는 input() 함수를 통해 해당 숫자 혹은 3, 6, 9가 들어가는 곳에서는 "짝"을 입력해야 함

value = 1
user = input("해당하는 숫자 입력 : ")

# 무한 반복하게 만들고, 사용자가 틀립 값 입력 시 에러 출력

while value:

    for i in range(len(10)):
        for j in range