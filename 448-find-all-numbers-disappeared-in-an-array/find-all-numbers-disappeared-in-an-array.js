/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    let filteredNums = [...(new Set(nums))];
    filteredNums.sort((a, b) => a - b);

    if (filteredNums.length === 1 && filteredNums[0] === 1 && nums.length === 2) {
        return [filteredNums[0] + 1];
    }

    let missingNums = [];
    let i = 0;
    let expectedNum = 1;
    while (i < filteredNums.length) {
        if (expectedNum !== filteredNums[i]) {
            missingNums.push(expectedNum);
        } else {
            i++;
        }
        expectedNum++;
    }
    while((missingNums.length + filteredNums.length) < nums.length){
        missingNums.push(expectedNum++);
    }
    return missingNums;
};
