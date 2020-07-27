#https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
#List1문제
for i in range(int(input())):
  N = int(input())
  a = list(map(int,input().split()))
  print("#{} {}".format(i+1,max(a)-min(a)))
