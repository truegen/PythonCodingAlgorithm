# 1~20의 값을 log X로 출력 + 별 문자 그래프

import math
for i in range(1,21):
    print("log(%i) = %f" %(i, math.log(i)))

for i in range(1,21):
    k = math.log(i)*25.0
    print("%s*" %(" "*int(k)))

# 다른 방식 : 속도 느림
# for i in range(1,21):
#     k = int(math.log(i)*25.0)
#     for j in range(k):
#         print(" ", end="")
#     print("*")