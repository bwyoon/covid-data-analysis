#!/usr/bin/python3

import sys
import os
from CovidDataWorldometer import GetCovidData
from MovingAverage import MovingAverage

# 영문 국가이름을 입력하지 않으면 멈춤
if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} Country")
    exit(1)

# 영문 국가이름
Country = sys.argv[1]
OutFile = f"covid-{Country.lower()}-st.dat"

data = GetCovidData(Country)

date    = data['date']
cases   = data['cases']
dcases  = data['dcases']
deaths  = data['deaths']
ddeaths = data['ddeaths']

# 7일 이동평균 계산
dc7ma = MovingAverage(dcases, 7)
dd7ma = MovingAverage(ddeaths, 7)

# 데이터 파일에 출력
with open(OutFile, 'wt') as f:
    s  = "날짜 확진자수 신규확진자수 사망자수 신규사망자수 "
    s += "신규확진자수7일이동평균 신규사망자수7일이동평균 "
    s += "단기치명률 단기치명률10 단기치명률14 "
    s += "단기치명률17 단기치명률21\n"
    f.write(s)
    for n in range(len(date)):
        s  = f"{date[n]} {cases[n]} {dcases[n]} "
        s += f"{deaths[n]} {ddeaths[n]} "
        s +=  "{:.3f} {:.3f} ".format(dc7ma[n], dd7ma[n])

        # 단기치명률 계산
        c = int(dc7ma[n])
        d = int(dd7ma[n])
        f0 = 0.0 if c == 0 else d/c
        s += '{:.7} '.format(f0)
        # 단기치명률 (확진-사망 시차 10일) 계산
        c = int(dc7ma[n-10])
        f10 = 0.0 if n < 10 else (0.0 if c == 0 else d/c)
        s += '{:.7} '.format(f10)
        # 단기치명률14 (확진-사망 시차 14일) 계산
        c = int(dc7ma[n-14])
        f14 = 0.0 if n < 14 else (0.0 if c == 0 else d/c)
        s += '{:.7} '.format(f14)
        # 단기치명률 (확진-사망 시차 17일) 계산
        c = int(dc7ma[n-17])
        f17 = 0.0 if n < 17 else (0.0 if c == 0 else d/c)
        s += '{:.7} '.format(f17)
        # 단기치명률 (확진-사망 시차 21일) 계산
        c = int(dc7ma[n-21])
        f21 = 0.0 if n < 21 else (0.0 if c == 0 else d/c)
        s += '{:.7}\n'.format(f21)

        f.write(s)

