/*
dic의 각 요소들을 하나씩 끌고 온다, 이때는 for 반복문을 쓴다.
각 요소가 문자열이기에 이거를 반복 가능한 배열(list)(이거를 d로 명명)로 바꾼다
참고로 이때는 split() 메서드를 사용
spell을 기준으로 각 요소를 하나씩 끌고 온다, 이때는 for 반복문을 쓴다. 결국 이중 for 반복문 사용
이 과정에서 spell의 요소들이 d에 다 있는지 판단해야 함, 이때는 includes() 메서드를 사용
이 과정에서 includes 메서드에 하나라도 속하는 게 있으면 return 1 하고 break
이 과정에서 includes 메서드에 하나라도 속하는 게 없으면 return 2 하고 break
*/

function solution(spell, dic) {
    // spell 배열을 미리 정렬하고 문자열로 합쳐둡니다.
    // 이렇게 하면 나중에 dicWord와 비교할 때 효율적입니다.
    // spell.sort()는 spell 배열 자체를 변경합니다.
    const sortedSpellStr = [...spell].sort().join(''); // spell 복사본을 정렬 후 문자열로

    // dic의 각 단어를 순회합니다.
    for (const dicWord of dic) {
        // 1. dicWord의 길이를 먼저 확인하여 spell의 길이와 일치하는지 봅니다.
        //    (spell의 모든 원소를 "한번씩만" 사용해야 하므로 길이가 다르면 바로 불일치)
        if (dicWord.length !== spell.length) {
            continue; // 길이가 다르면 다음 dic 단어로 넘어갑니다.
        }

        // 2. dicWord를 문자 배열로 쪼갠 후 정렬하고 문자열로 합칩니다.
        const sortedDicWordStr = [...dicWord].sort().join('');
        //   예: dicWord가 "dzx" 이면 -> ["d", "z", "x"] -> ["d", "x", "z"] -> "dxz"

        // 3. 정렬된 spell 문자열과 정렬된 dic 단어 문자열이 정확히 일치하는지 확인합니다.
        //    이것이 spell의 모든 알파벳을 '한 번씩만' 사용했는지 확인하는 가장 정확한 방법입니다.
        if (sortedSpellStr === sortedDicWordStr) {
            return 1; // 일치하는 단어를 찾았으므로 즉시 1을 반환하고 함수 종료
        }
    }

    // dic의 모든 단어를 확인했지만, 일치하는 단어를 찾지 못했습니다.
    return 2; // 따라서 2를 반환
} 