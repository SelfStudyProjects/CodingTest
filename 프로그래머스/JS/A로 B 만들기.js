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