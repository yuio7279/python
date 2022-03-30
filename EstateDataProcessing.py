import os, re
os.chdir(r"C:\Users\super\Desktop\2-B_KYS\python_workspace\0330")
import usecsv 
apt = usecsv.switch(usecsv.opencsv('apt_trade.csv'))
print(apt[:3])

#5개 데이터의 시, 군, 구 만 출력하기
# for i in apt[:6]:
#     print(i[0])

#시군구, 아파트 단지명, 거래금액(만원) 출력
# for i in apt[:6]:
#     print(i[0],i[4],i[-7])

#강원도에 120m 이상 3억원 이하 아파트 검색
# for i in apt:
#     try:
#         if i[5] >= 120 and i[-7] <= 30000 and re.match('강원',i[0]):
#             print(i[0],i[4],i[-7])
#     except:pass


#분석결과를 csv 파일로 저장하기
# new_list = []
# for i in apt:
#     try:
#         if i[5] >= 120 and i[-7] <= 30000 and re.match('강원',i[0]):
#             new_list.append([i[0],i[4],i[-7]])
#     except: pass
# usecsv.writecsv('over120_lower3000.csv',new_list)
