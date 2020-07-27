#https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
for i in range(int(input())):
  K,N,M = map(int,input().split())
  # K 이동할 수 있는 정류장 수
  # N 종점 정류장
  # M 정류장 개수
  bus = list(map(int,input().split()))
  start = 0
  cnt =0
  end = K
  while True:
    if start+K >=N:
      break
    for a in range(K,0,-1):
      if start+a in bus:
        start +=a
        cnt+=1
        break
    else:
      cnt=0
      break
  print("#{} {}".format(i+1,cnt))
