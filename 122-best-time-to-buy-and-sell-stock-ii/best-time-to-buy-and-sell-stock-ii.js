/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let i = 1;
    let j = i - 1;
    while (i < prices.length){
        if (prices[i] - prices[j] > 0){
            profit += prices[i] - prices[j];
        }
        i++;
        j++;
    }
    return (profit);
};