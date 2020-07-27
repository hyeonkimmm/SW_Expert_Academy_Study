for i in range(int(input())):
  N = int(input())
  a = input()
  card_Num = [0]*10
  for j in a:
    card_Num[int(j)] +=1
  reverse_card = list(reversed(card_Num))
  maxNum = 9-reverse_card.index(max(reverse_card))
  maxcnt = max(reverse_card)
  print("#{} {} {}".format(i,maxNum,maxcnt))
