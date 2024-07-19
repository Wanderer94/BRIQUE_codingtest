import requests
from collections import Counter
import operator

# URL 설정
url = "http://codingtest.brique.kr:8080/random"

# 결과를 저장할 Counter 객체
results_counter = Counter()

# 100번 호출하여 결과 수집
for _ in range(100):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results_counter[str(data)] += 1
    else:
        print("Failed to fetch data from the server")

# 결과를 빈도수에 따라 정렬
sorted_results = sorted(results_counter.items(), key=operator.itemgetter(1), reverse=True)

# 결과 출력
for result, count in sorted_results:
    print(f"count: {count} {result}")

# 총 합 출력
total_count = sum(results_counter.values())
print(f"Total count: {total_count}")
