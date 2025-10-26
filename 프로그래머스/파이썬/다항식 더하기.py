# 다ㅅ ㄱㄱ

# polynomial 문자열을 공백(' ') 기준으로 분리하여 항들의 리스트를 얻는다.
# x 항의 계수 합산 변수
# 상수항 합산 변수
# 분리된 항들(item)을 하나씩 순회한다.
# '+'는 단순히 구분자이므로 무시하고 넘어간다.
# 항이 'x'를 포함한다면 (x 항이라면)
# 'x' 단독 항 (계수 1 생략된 경우)
# 'x' 앞에 숫자가 있는 항 (예: "3x")
# 'x'를 제외한 앞부분을 숫자로 변환하여 계수에 더한다.
# term[:-1]은 'x'를 제외한 문자열 부분 (예: "3x"에서 "3")
# 항이 'x'를 포함하지 않는다면 (상수항이라면)
# 숫자로 변환하여 상수항 합산 변수에 더한다.
# x_coeff_sum과 const_sum을 바탕으로 최종 결과 문자열을 구성한다.
# 최종 결과의 각 부분을 담을 리스트
# x 항 처리
# 계수가 1일 경우 "1x"가 아닌 "x"
# 계수와 함께 "Cx" 형태
# 상수항 처리
# 상수항은 문자열로 변환하여 추가


def solution(polynomial):
    terms = polynomial.split(' ')

    x_coeff_sum = 0
    const_sum = 0

    for term in terms:
        if term == '+':
            continue
        elif 'x' in term:
            if term == 'x':
                x_coeff_sum += 1
            else:
                x_coeff_sum += int(term[:-1]) 
        else:
            const_sum += int(term)

    result_parts = []
    if x_coeff_sum > 0:
        if x_coeff_sum == 1:
            result_parts.append("x")
        else:
            result_parts.append(f"{x_coeff_sum}x")

    if const_sum > 0:
        result_parts.append(str(const_sum))
    return " + ".join(result_parts)