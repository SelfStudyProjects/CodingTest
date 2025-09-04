def solution(s1, s2):
    answer = 0;
    i = 0
    j = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                   answer += 1
    return answer;

'''
js 코드로 작성(동일한 로직)
    function solution(s1, s2) {
    var answer = 0;
    for(i = 0; i < s1.length; i++) {
        for(j = 0; j < s2.length; j++) {
            if(s1[i] === s2[j]) {
                answer += 1
            }
        }
    }
    return answer;
}

'''