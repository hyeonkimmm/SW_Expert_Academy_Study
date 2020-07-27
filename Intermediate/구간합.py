for j in range(int(input())):
  N,M = map(int,input().split())
  num_list = list(map(int,input().split()))
  minsum = 0
  maxsum = 0
  for i in range(N-M+1):
    searchNum = sum(num_list[i:i+M])
    if searchNum<minsum or minsum ==0:
      minsum=searchNum
    if searchNum>maxsum or maxsum ==0:
      maxsum=searchNum
  print("#{} {}".format(j+1,maxsum-minsum))
