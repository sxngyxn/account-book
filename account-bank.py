import csv

x1 = []

def f1():
 dat = input("날짜:")
 cat = input("구분:")
 what = input("항목:")
 try:
  val = int(input("금액:"))
 except:
  print("다시 입력")
  return
 x1.append([dat, cat, what, val])
 print("저장됨")

def f2():
 if len(x1)==0:
  print("데이터 없음")
 for r in x1:
  print(r[0], r[1], r[2], r[3])

def f3():
 q = input("검색어:")
 for z in x1:
  if q in z[0] or q in z[2]:
   print(z[0], z[1], z[2], z[3])

def f4():
 a, b = 0, 0
 for t in x1:
  if t[1]=="수입":
   a+=t[3]
  if t[1]=="지출":
   b+=t[3]
 print("수입:",a)
 print("지출:",b)
 print("합:",a-b)

def f5():
 with open("xx.csv","w",newline="",encoding="utf-8") as f:
  w=csv.writer(f)
  w.writerow(["날짜","종류","내용","금액"])
  for d in x1:
   w.writerow(d)
 print("저장완료")

def task_main():
 while True:
  print("1입력 2전체 3찾기 4요약 5끝")
  z = input(":")
  if z=="1":
   f1()
  elif z=="2":
   f2()
  elif z=="3":
   f3()
  elif z=="4":
   f4()
  elif z=="5":
   f5()
   break
  else:
   print("오류")

task_main()
