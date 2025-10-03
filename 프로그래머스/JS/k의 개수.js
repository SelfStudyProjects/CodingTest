/* i부터 j까지 1씩 증가, string으로 바꾸고, 1개씩 보면서
k에 해당하면 result를 ++1을 해주는 형식 */

function solution(i, j, k) {
    var answer = 0;
    const k_str = String(k);

    for (let y = i; y <= j; y++) {
        let string_y = y.toString(); 

        for (let z = 0; z < string_y.length; z++) {
            const char_z = string_y[z]; 

            if (char_z === k_str) {
                answer += 1;
            }
        }
    }
    
    return answer; 
}