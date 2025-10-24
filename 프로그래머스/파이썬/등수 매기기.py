# 1. 각 학생의 평균 점수 계산 (np.mean 활용)
# score는 2차원 리스트이므로, 각 요소를 numpy 배열로 변환하여 평균을 구합니다.
# # 첫번째 반복문에서 각 리스트에 접근하여 평균을 구하는 로직
# s_pair는 [영어점수, 수학점수] 형태입니다.
# # np.mean() 메소드를 활용해서 2개 요소들의 평균을 구합니다.
# 2. 평균 점수를 기준으로 등수 매기기 (pandas의 rank() 메소드 활용)
# # rank() 메소드를 활용해서 순위로 치환하는 방법
# pandas Series로 변환하여 rank 메소드를 사용합니다.
# - method='min': 공동 순위가 있을 때 '가장 낮은 등수'를 부여하고 다음 순위는 건너뜁니다 (예: 2, 2, 4). 문제 요구사항과 일치.
# - ascending=False: 평균이 높을수록(숫자가 클수록) 등수는 낮게(숫자는 작게) 매겨야 하므로 '내림차순' 정렬.
# .astype(int)로 소수점 제거, .tolist()로 다시 파이썬 리스트로 변환

'''
Series 객체: Pandas 라이브러리에서 제공하는 1차원 레이블링된 배열 형태로,
인덱스(Index)와 값(Values)으로 구성됩니다. 이는 다양한 데이터 타입을 저장할 수 있으며,
인덱스를 통해 값에 접근하는 기능을 제공하여 표 형태 데이터 처리의 기본 구성 요소로 활용됩니다.

배열 (Array): Numpy 라이브러리에서 주로 사용되는 다차원 데이터를 효율적으로 저장하고 처리하는 자료구조입니다.
모든 요소가 동일한 데이터 타입을 가지며, 수학적 연산에 최적화되어 고성능 과학 계산 및 데이터 분석에 기초적인 역할을 합니다.
'''


import numpy as np
import pandas as pd

def solution(score):
    avg_scores = []
    for s_pair in score:
        avg = np.mean(s_pair)
        avg_scores.append(avg)
    avg_series = pd.Series(avg_scores)
    ranks = avg_series.rank(method='min', ascending=False).astype(int).tolist()
    return ranks