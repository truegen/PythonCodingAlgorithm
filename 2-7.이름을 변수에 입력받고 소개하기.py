name = input("이름을 입력하세요: ")
n = name.strip()    # 이름 앞뒤 공백 제거

if(n != ""):    # 입력된 이름이 있으면
    print("입력한 이름은 %s입니다." %n)
else:
    print("입력한 이름이 없습니다.")