function solution(s) {
    const charCounts = {}; 
    for (const char of s) {
        charCounts[char] = (charCounts[char] || 0) + 1;
    }

    const uniqueCharsList = []; 
        for (const char of s) { 
        if (charCounts[char] === 1) { 
            uniqueCharsList.push(char); 
            }
        }
    
    uniqueCharsList.sort(); 
    
    return uniqueCharsList.join(''); 
}