import random

# 3, 6, 9
#사용자는 input() 함수를 통해 해당 숫자 혹은 3, 6, 9가 들어가는 곳에서는 "짝"을 입력해야 함

# 무한 반복하게 만들고, 사용자가 틀립 값 입력 시 에러 출력

my_turn = True
for i in range(1, 100):
  if my_turn == True:
    user = input("당신 차례입니다: (3,6,9면 짝)")
    #사용자가 3,6,9라고 판단한 경우
    if user == "짝":
      # if i가, 3 6, 9인가?
      i = str(i)
      for j in range(len(i)):
        # 3,6,9면
        if i[j] == "3" or i[j] == "6" or i[j] == "9":
          break
        else:
          print("패배")

    #사용자가 3,6,9가 아니라고 판단한 경우
    else:
      i = str(i)
      for j in range(len(i)):
      # 3,6,9가 맞는데, 아니라고 판단.
        if i[j] == "3" or i[j] == "6" or i[j] == "9":
          print("패배")
          break

    my_turn = False

  # 컴퓨터 차례
  else:
    i = str(i)
    박수 = False

    for j in range(len(i)):
      if i[j] == "3" or i[j] == "6" or i[j] == "9":
        print("컴퓨터 : ", "짝")
        박수 = True
        break

      else:
        박수 = False
        break
    my_turn = True