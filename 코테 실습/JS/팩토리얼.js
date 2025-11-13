/* 숫자 n이 있다고 하자. n을 1부터 ++1을 하는 와중에, n!를 하자.
그리고 처음으로 n보다 클 때 바로 return 0를 해서 멈추게끔 하자.
*/

function solution(n) {
    let i = 1;
    let factorial = 1;

    while (true) { 
        factorial *= i;
        if (factorial > n) {
            return i - 1; 
        }
        i++;
    }
}