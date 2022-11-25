def MovingAverage(data, interval):
    # 입력 데이터 길이
    datalen = len(data)
    # 출력 데이터 초기화
    data_ma = [0.0]*datalen
    data_sum = 0 
    for n in range(datalen):
        data_sum += data[n]
        # 계산할 데이터 갯수가 충분하지 않은 앞부분
        if n < interval:
            data_ma[n] = data_sum/(n+1)
        # 계산할 데이터가 충분한 나머지 부분
        else:
            data_sum -= data[n-interval]
            data_ma[n] = data_sum/interval

    return data_ma 

