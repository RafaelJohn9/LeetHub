/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    const numOfChildren = ratings.length;
    let numOfCandies = Array(numOfChildren).fill(1);

    // Left-to-Right Pass
    for (let i = 1; i < numOfChildren; i++) {
        if (ratings[i] > ratings[i - 1]) {
            numOfCandies[i] = numOfCandies[i - 1] + 1;
        }
    }

    // Right-to-Left Pass
    for (let j = numOfChildren - 2; j >= 0; j--) {
        if (ratings[j] > ratings[j + 1]) {
            numOfCandies[j] = Math.max(numOfCandies[j], numOfCandies[j + 1] + 1);
        }
    }

    // Sum up the candies array
    return numOfCandies.reduce((accumulator, element) => accumulator + element, 0);
}