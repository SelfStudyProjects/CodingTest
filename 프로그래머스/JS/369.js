function solution(order) {
    var answer = 0;
    let list_order = String(order);

    for (let i = 0; i < list_order.length; i++) { 
        if (['3', '6', '9'].includes(list_order[i])) { 
            answer += 1;
        }
    }
    
    return answer;
}