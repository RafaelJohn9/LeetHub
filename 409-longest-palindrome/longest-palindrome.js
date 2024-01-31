/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    if (s.length === 1){
        return 1;
    }
    let letterOccurrence = {};
    for (let letter of s){
        if (letter in letterOccurrence){
            letterOccurrence[letter]++;
        }
        else{
            letterOccurrence[letter] = 1;
        }
    }
    let palindrome = 0;
    for (key of Object.keys(letterOccurrence)){
        if (letterOccurrence[key] > 1){
            if (letterOccurrence[key] % 2 === 0){
                palindrome += letterOccurrence[key]
            }
            else{
                palindrome += letterOccurrence[key] - 1;
            }
        }
    }
    if (s.length > palindrome){
        palindrome++;
    }
    return palindrome;
};