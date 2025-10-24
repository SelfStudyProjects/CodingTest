import numpy as np
import pandas as pd

def solution(score):
    # 1. 각 학생의 평균 점수 계산 (np.mean 활용)
    # score는 2차원 리스트이므로, 각 요소를 numpy 배열로 변환하여 평균을 구합니다.
    # # 첫번째 반복문에서 각 리스트에 접근하여 평균을 구하는 로직
    avg_scores = []
    for s_pair in score: # s_pair는 [영어점수, 수학점수] 형태입니다.
        # # np.mean() 메소드를 활용해서 2개 요소들의 평균을 구합니다.
        avg = np.mean(s_pair)
        avg_scores.append(avg)

    # 2. 평균 점수를 기준으로 등수 매기기 (pandas의 rank() 메소드 활용)
    # # rank() 메소드를 활용해서 순위로 치환하는 방법
    # pandas Series로 변환하여 rank 메소드를 사용합니다.
    # - method='min': 공동 순위가 있을 때 가장 낮은 등수를 부여하고 다음 순위는 건너뜁니다 (예: 2, 2, 4). 문제 요구사항과 일치.
    # - ascending=False: 평균이 높을수록(숫자가 클수록) 등수는 낮게(숫자는 작게) 매겨야 하므로 내림차순 정렬.
    avg_series = pd.Series(avg_scores)
    ranks = avg_series.rank(method='min', ascending=False).astype(int).tolist()
    # .astype(int)로 소수점 제거, .tolist()로 다시 파이썬 리스트로 변환

    return ranks