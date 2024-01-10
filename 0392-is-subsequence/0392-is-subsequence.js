/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    if (s.length === 0){
        return true;
    }
    for (let i = 0; i < t.length; i++){
        let j = 0;
        if (t[i] === s[j]){
            let k = i + 1;
            j++;
            while (k < t.length && j < s.length){
                if (s[j] === t[k]){
                    j++;
                }
                k++;
            }
            if (j >= s.length){
                return true;
            }
        }
    }
    return false;
};