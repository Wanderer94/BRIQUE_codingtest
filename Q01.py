import pandas as pd
import numpy as np

# CSV 파일 읽기
sample1 = pd.read_csv('sample.csv')

# 필요한 계산 결과를 담을 리스트 초기화
calculated_lines = []

# 숫자가 아닌 값들을 담을 리스트 초기화
error_values = []

# 각 라인별로 계산
for index, row in sample1.iterrows():
    
    # 각 행의 모든 값을 숫자로 변환하여 계산
    numeric_values = pd.to_numeric(row, errors='coerce')
    
    # 만약 숫자가 아닌 값이 하나라도 존재하면 해당 행은 계산하지 않음
    # 숫자가 아닌 값만 추출하여 리스트에 추가
    non_numeric_values = row[numeric_values.isnull()]
    if not non_numeric_values.empty:
        error_values.append(f'Line {index}: {non_numeric_values.to_string(index=False)}')

    # 최소값
    min_value = np.nanmin(numeric_values)
    # 최대값
    max_value = np.nanmax(numeric_values)
    # 합계
    sum_value = np.nansum(numeric_values)
    # 평균
    mean_value = np.nanmean(numeric_values)
    # 표준편차
    std_value = np.nanstd(numeric_values)
    # 중간값
    median_value = np.nanmedian(numeric_values)
    
    # 계산 결과를 리스트에 추가
    calculated_lines.append(f'{min_value} {max_value} {sum_value} {mean_value} {std_value} {median_value}')

# 결과 출력
print("The calculated lines:")
for line in calculated_lines:
    print(line)
print("The total number of lines:", len(sample1))

print("The error values:")
for error in error_values:
    print(error)
