# 1. csv 파일 불러와 셋팅하기
import os, re, usecsv
os.chdir(r'D:\gitPY\0330')
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)
# print(newPop[:4])




# 2. 등록 외국인 비율 계산하기
# i = newPop[1]
# foreign = round(i[2]/ (i[1] + i[2]) * 100,1)
# for i in newPop:
#     foreign = 0
#     try:
#         foreign = round(i[2]/(i[1]+i[2]) * 100,1)
#         print(i[0], foreign)
#     except:
#         pass

# 3. 첫 행 지정하기

new = [['구','한국인','외국인','외국인 비율(%']]
# print(i)
# new.append([i[0],i[1],i[2],foreign])
# print(new)

# 3. 등록 외국인 비율 3% 넘을때만 출력, appen 하기
import re
for i in newPop:
    foreign =  0
    try:
        foreign = round(i[2]/(i[1] + i[2]) * 100,1)
        if foreign > 3:
            print([i[0],i[1],i[2],foreign])
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass

# 4. newPop.csv 파일로 저장하기
usecsv.writecsv('newPop.csv',new)