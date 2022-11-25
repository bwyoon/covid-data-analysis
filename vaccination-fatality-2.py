#!/usr/bin/python3

# 연령대별 확진자수 초기화 
# 0-9세:10,000명, 10-19세:10,000명, ... 
cases = [[10000 for k in range(8)] for l in range(4)]
print(cases)

# 연령대별 사망자수 (확진자 치명률)
# 70세 이상: 1300명(13%)
# 60 - 69세: 200명(2%)
# 50 - 59세: 70명(0.7%)
# 40 - 49세: 20명(0.2%)
# 30 - 39세: 10명(0.1%)
#  0 - 29세: 0명(0%)
deaths = [[1300, 200, 70, 20, 10, 0, 0, 0] for k in range(4)]
print(deaths)

# 감염예방효과
ip = [0.8, 0.6, 0.4, 0.2]

# 사망예방효과
dp = 0.9

print('백신접종률 확진자치명률80 확진자치명률70 '
      +'확진자치명률60 확진자치명률50 확진자치명률40 '
      +'확진자치명률30 확진자치명률20 확진자치명률10')

# 백신 접종하기 전
# 백신접종률, 확진자수, 사망자수, 확진자 치명률
csum = sum(cases[0])
dsum = sum(deaths[0])
f = dsum/csum
print('{:7.4f} '.format(0.0), end='')
for m in range(len(ip)):
    print('{:.5f} '.format(f), end='')
print()

# 백신 접종한 후
# 백신접종률, 확진자수, 사망자수, 확진자 치명률
for n in range(8):
    # 백신 접종률
    # 11.25%, 22.5%, 33.75%, ...
    v = (n+1)/8*0.9

    print('{:7.4f} '.format(v), end='')

    for m in range(len(ip)): 
        # 백신을 접종을 끝낸 연령대의 확진자수
        # 백신을 접종한 사람(90%)중의 확진자수 
        #   백산 접종 전 확진자수 × 0.9 × (1-감염예방효과) 
        c = cases[m][n]*0.9*(1.0-ip[m]) 
        # 백신을 접종하지 않은 사람(10%)중의 확진자수 
        #   백산 접종 전 확진자수 × 0.1 
        c += cases[m][n]*0.1 
    
        # 백신을 접종을 끝낸 연령대의 사망자수
        # 백신을 접종한 사람(90%)중의 사망자수 
        #   백산 접종 전 확진자수 × 0.9 × (1-사망예방효과) 
        d = deaths[m][n]*0.9*(1.0-dp) 
        # 백신을 접종하지 않은 사람(10%)중의 사망자수 
        #   백산 접종 전 확진자수 × 0.1 
        d += deaths[m][n]*0.1 
    
        cases[m][n] = c
        deaths[m][n] = d
    
        # 백신 접종하기 시작한 후
        # 백신접종률, 확진자수, 사망자수, 확진자 치명률
        csum = sum(cases[m])
        dsum = sum(deaths[m])
        f = dsum/csum
        print('{:.5f} '.format(f), end='')

    print()

