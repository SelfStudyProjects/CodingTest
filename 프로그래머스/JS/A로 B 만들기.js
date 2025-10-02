/*
splice() 메소드의 기본적인 형태는 배열.splice(startIndex, deleteCount, item1, item2, ...) 이렇게 돼.
startIndex: 작업을 시작할 배열의 인덱스.
deleteCount: startIndex부터 몇 개의 요소를 제거할지 지정. (0이면 제거하지 않음)
item1, item2, ...: (선택 사항) 제거된 요소 자리에 추가할 요소들.
*/

function solution(before, after) {
    answer = 0;

    let afterArray = after.split(''); 
    for (let i = 0; i < before.length; i++) {
        const char_b = before[i];
        const indexInAfter = afterArray.indexOf(char_b);

        if (indexInAfter !== -1) {
            afterArray.splice(indexInAfter, 1);
        } else {
            return 0; 
        }
    }

    if (afterArray.length === 0) {
        return 1;
    } else {
        return 0;
    }
}