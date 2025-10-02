function solution(order) {
    var answer = 0;
    let list_order = String(order);

    for (let i = 0; i < list_order.length; i++) { 
        if (['3', '6', '9'].includes(list_order[i])) { /* includes 파트에 대해서는 특히 조심! */
            answer += 1;
        }
    }
    
    return answer;
}