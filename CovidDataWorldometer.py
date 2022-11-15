#!/usr/bin/python3

import os
import datetime

def GetCovidData(Country):
    URL  = "https://www.worldometers.info/coronavirus/country/"
    URL += f"{Country.lower()}/"
    
    # curl 명령어와 sed 명령어를 사용해 확진자수, 신규확진자수, 
    # 사망자수, 신규사망자수 데이를 읽는다.
    # curl 명령어로 웹페이지 소스를 읽어 pipe로 넘긴다.
    cmd  = f"curl -s '{URL}' | "
    # sed 명령어로 text: categories: data: 가 나오는 줄만 
    # pipe로 넘긴다.
    cmd += r"sed -n -e '/text:/p' -e '/categories:/p' "
    cmd += r"       -e '/data:/p' | "
    # sed 명령어로 필요한 데이터만 골라 pipe로 넘긴다.
    cmd += r"sed -n -e '/Total Cases/{n;n;p;n;n;p;n;n;n;n}' "
    cmd += r"       -e '/Daily New Cases/{n;n;n;n;p;n}' "
    cmd += r"       -e '/Total Deaths/{n;n;n;n;p;n;n;n;n}' "
    cmd += r"       -e '/Daily Deaths/{n;n;n;n;p;n}' | "
    # sed 명령어로 필요없는 문자를 제거하고 pipe로 넘긴다.
    cmd += r"sed -e 's/categories://' -e 's/data://' "
    cmd += r"    -e 's/\[//' -e 's/\]//g' -e 's/\},//g' "
    cmd += r"    -e 's/null/0/g' -e 's/[{}]//g' | "
    # sed 명령어로 날짜 형식 변경
    cmd += r"sed -r 's/(\w{3}) ([0-9]{1,2}), (.{4})/\1-\2-\3/g'"
    # sed 명령어로 공란 제거
    cmd += r" | sed 's/ //g'" 
    
    # popen 으로 cmd를 실행해 출력하는 결과를 읽어 데이터로 변환
    lines = os.popen(cmd).readlines()
    v = lines[0].rstrip().split(',')
    date = list(map(
       lambda x: datetime.datetime.strptime(x, '"%b-%d-%Y"').
                 strftime('%Y-%m-%d'), v))
    cases   = list(map(lambda x: int(x), lines[1].split(',')))
    dcases  = list(map(lambda x: int(x), lines[2].split(',')))
    deaths  = list(map(lambda x: int(x), lines[3].split(',')))
    ddeaths = list(map(lambda x: int(x), lines[4].split(',')))

    return {'date': date, 'cases' : cases, 'dcases': dcases, 
            'deaths':deaths, 'ddeaths': ddeaths}
 
