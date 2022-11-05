#!/usr/bin/python3

# 입력과 출력 데이터 파일
InFile = 'covid-kor-2020-06.dat'
OutFile = 'covid-kor-2020-06-converted.dat'

# 확진-사망, 확진-격리해제 시차
Days2Death = 17
Days2Recovery = 35

# 입력 데이터 읽기
lines = open(InFile, 'rt').readlines()
data = list(map(lambda x: x.split(), lines[1:]))

# 문자열을 숫자로 변환
for n in range(len(data)):
    for m in range(1, len(data[n])):
        data[n][m] = int(data[n][m])

# '제때 확진되었어야 할 사람수'계산
datalen = len(data)
for n in range(datalen-35):
    # 제때 확진되었어야 할 사람수:
    # 35일 후 격리 해제자수 + 17일 후 사망자수
    TimelyConfirmed = data[n+35][4]+data[n+17][3]
    data[n].append(TimelyConfirmed)
    # 선제적 확진자수:
    # 확진자수 - 제때 확진되었어야 할 사람수
    PreemptiveC = data[n][2]-TimelyConfirmed
    data[n].append(PreemptiveC)

# 데이터 파일에 저장
with open(OutFile, 'wt') as f:
    s = lines[0].rstrip()+' 제때확진자수 선제적확진자수\n'
    f.write(s)
    for d in data:
        s = ''
        for x in d:
            s += f'{x} '
        f.write(s[:-1]+'\n')
