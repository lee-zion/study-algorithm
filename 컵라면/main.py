import sys
input = sys.stdin.readline
import heapq

re=0
c=1#현 시간
mins =[]
s = []

n = int(input())
for i in range(n):
    dl_curr, reward = map(int, input().split())
    heapq.heappush(s, (dl_curr, -reward))
while s:
    t = heapq.heappop(s)
    re-=t[1]#우선 데드라인 안쪽이니 더해줌
    heapq.heappush(mins,-t[1])#더한 값들을 다 저장해줌
    if s and c ==s[0][0]:#현재 시간과 같은 데드라인을 가지고 있는 문제들을 발견하면 다 빼내야함 
        while s and t[0] == s[0][0]:#계속 빼내는 과정
            w =heapq.heappop(s)#여기서 데드라인이 긴 경우가 더 많은 라면을 얻을 수 있는 경우를 찾아냄
            if -w[1]>mins[0]:#데드라인이 긴 경우가 라면 획득량 > 획득했던 라면량중에 가장 적은 획득량
                re-=heapq.heappop(mins)#가장 적은 획득량을 빼고
                re-=w[1]#지금 라면 획득량을 더해줌
                heapq.heappush(mins,-w[1])#이건 다시 이때까지 획득했던 라면량으로 넣어줌
    c+=1#시간 +1

if re >=2**31:# 컵라면 수와 최대로 받을 수 있는 컵라면 수는 모두 2**31보다 작거나 같은 자연수인데 넘을 수 있으니 저렇게 해줌.
    print(2**31)
else:
    print(re)