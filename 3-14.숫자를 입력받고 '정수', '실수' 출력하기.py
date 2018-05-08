def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    num = input("정수 또는 실수를 입력하세요: ")
    if isNumber(num) == False:
        continue

    num = float(num)
    num2 = int(num)
    print("num = {}, num2 = {}".format(num,num2))

    if -9999 == num2:
        break
    elif num - num2 == 0.0:
        print("정수입니다.")
    else:
        print("실수입니다.")