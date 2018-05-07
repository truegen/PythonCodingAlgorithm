scores = [-1,-1,-1,-1,-1]
max_score = -1

for i in range(0,5):
    while (scores[i] < 0 or scores[i] > 100):
        scores[i] = int(input("(%d) 점수를 입력하세요(0~100): " %(i+1)))
    if(max_score < scores[i]):
        max_score = scores[i]

print("최고 점수는 %d점입니다." %max_score)