/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    let greedFactor = g.sort((a, b) => a - b);
    let sizeFactor = s.sort((a,b) => a - b);
    let satisfiedChildren = 0;

    let i = 0;
    for(let j = 0; i < g.length && j < s.length; j++){
        if(sizeFactor[j] >= greedFactor[i]){
            satisfiedChildren++;
            i++;
        }
    }
    return satisfiedChildren;
};