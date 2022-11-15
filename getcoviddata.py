#!/usr/bin/python3

import sys
import os
from CovidDataWorldometer import GetCovidData

# 영문 국가이름을 입력하지 않으면 멈춤
if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} Country")
    exit(1)

Country = sys.argv[1]
OutFile = f"covid-{Country.lower()}.dat"

data = GetCovidData(Country)

date    = data['date']
cases   = data['cases']
dcases  = data['dcases']
deaths  = data['deaths']
ddeaths = data['ddeaths']

# 데이터 파일에 출력
with open(OutFile, 'wt') as f:
    s  = "날짜 확진자수 신규확진자수 사망자수 신규사망자수 "
    s += "치명률 치명률10 치명률14 치명률17 치명률21\n"
    f.write(s)
    for n in range(len(date)):
        s  = f"{date[n]} {cases[n]} {dcases[n]} "
        s += f"{deaths[n]} {ddeaths[n]} "

        # 치명률 계산
        c = int(cases[n])
        d = int(deaths[n])
        f0 = 0.0 if c == 0 else d/c
        s += '{:.7} '.format(f0)
        # 치명률10 계산
        c = int(cases[n-10])
        f10 = 0.0 if n < 10 else (0.0 if c == 0 else d/c)
        s += '{:.7} '.format(f10)
        # 치명률14 계산
        c = int(cases[n-14])
        f14 = 0.0 if n < 14 else (0.0 if c == 0 else d/c)
        s += '{:.7} '.format(f14)
        # 치명률17 계산
        c = int(cases[n-17])
        f17 = 0.0 if n < 17 else (0.0 if c == 0 else d/c)
        s += '{:.7} '.format(f17)
        # 치명률21 계산
        c = int(cases[n-21])
        f21 = 0.0 if n < 21 else (0.0 if c == 0 else d/c)
        s += '{:.7}\n'.format(f21)

        f.write(s)

