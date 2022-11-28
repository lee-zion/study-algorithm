import sys, time

# A, B = map(int, sys.stdin.readline().split())
A, B = 2, 100000
start = time.perf_counter()

# 1. 소수를 판별 & 소인수의 수 저장
dp = [1]*100001                           
dp[0], dp[1] = 0, 0                       

# 2. 소수판별, 에라토스테네스의 체
for i in range(2, 100001):
    n = 2
    while i*n < 100001:
        dp[i*n] = 0
        n += 1

# 3. 소인수분해를 위햔 소수리스트 생성
prime_lst = []                              # 소수를 저장할 리스트
for idx, val in enumerate(dp):
    if val == 1:
        prime_lst.append(idx)

end = time.perf_counter()
print(f"Time elapsed: {(end - start)*10**3} ms")

# 4. 소인수의 수 계산
result = 0
for num in range(A, B+1):
    temp = num
    temp_lst = []                           # 모든 약수에 대한 소인수의 수를 계산하기 위한 임시저장 리스트
    cnt, n = 0, 0                           # 소인수 개수 / 소수인덱스

    if dp[temp] == 1:                      # 현재 수가 소수일 경우, 소인수의 수 == 1이므로 계산하지 않음
        continue

    # 5. 소인수 분해
    while temp > 1:
        if dp[temp]:                       # memoization 활용
            cnt += dp[temp]                # 소인수의 수 저장 리스트에 값이 있을 경우 값을 불러와 활용
            temp = 1                        # 반복문 바로 탈출
        else:
            if temp % prime_lst[n]:         # 안나눠질 경우 다음 소수로 이동
                n += 1                      
            else:                           # 나눠지는 경우
                temp_lst.append(temp)       # 모든 약수에 대한 소인수의 수를 계산하기 위해 임시저장
                temp //= prime_lst[n]
                cnt += 1                    # 나눠질 때마다 소인수 개수 +1

    # 6. lst에 값 저장
    for idx, val in enumerate(temp_lst):    # 계산과정에서의 모든 약수에 대한 소인수의 수 저장
        dp[val] = cnt - idx                # 계산순서대로, 큰수 -> 작은수로 저장

    # 7. 결과 카운트
    if dp[cnt] == 1:                       # 소인수의 수가 소수일 경우, 결과값 추가
        result += 1
print(result)


# import sys, time
# from math import isqrt

# def main():
#     def num_prime(n):
#         ans = 0
#         div = 3
#         while (n >= div):
#             if n % div == 0:
#                 ans += 1
#                 n = n // div
#             else:
#                 div += 2
#         return ans
#     def find_divider(n):
#         for i in range(1, n // 2 + 1):
#             if (n % (i*2 + 1)) == 0:
#                 return i
#     def is_prime(n):
#         if n < 2 or n % 2 == 0:
#             return False
#         for i in range(3, max(2, isqrt(n) + 1), 2):
#             if (n % i) == 0:
#                 return False
#         return True
    
#     # a, b = map(int, sys.stdin.readline().split())
#     a, b = 2, 100000
#     start = time.perf_counter()
#     answer = 0
#     dp = [0] * (b + 1)

#     for num in range(2, b+1):
#         if dp[num] == 0:
#             if is_prime(num):
#                 dp[num] = 1
#                 cnt = 1
#                 while 1:
#                     temp = pow(num, cnt + 1)
#                     if temp > b:
#                         break
#                     dp[temp] = min(dp[temp], dp[num] + cnt) if dp[temp] else dp[num] + cnt
#                     cnt += 1
#             else:
#                 if num%2 == 0:
#                     dp[num] = dp[num // 2] + 1
#                 else:
#                     # divider = find_divider(num)
#                     # dp[num] = dp[num // divider] + dp[divider]
#                     dp[num] = num_prime(num)
#     for num in dp[a:b+1]:
#         if is_prime(num):
#             answer += 1
#     print(answer)
#     end = time.perf_counter()
#     print(f"Time elapsed: {(end - start)*10**3} ms")
# if __name__ == "__main__":
#     main()