def isNumStr(s):    # 정수인지 검사
    try:
        int(s)
        return True
    except ValueError:
        return False

num1 = input("정수 숫자를 입력하세요: ")
num2 = input("다음 정수를 입력하세요: ")

if isNumStr(num1) and isNumStr(num2):
    print(int(num1)-int(num2))
else:
    print("정수가 아닌 것이 포함되어 있습니다.")

def isNumber(s):    # 숫자인지 검사
    try:
        float(s)
        return True
    except ValueError:
        return False
