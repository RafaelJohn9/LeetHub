/**
 * @param {number} num
 * @return {string}
 */
function intToRoman(num) {
    const val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ];
    const syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ];
    let romanNum = '';
    let i = 0;

    while (num > 0) {
        while (num >= val[i]) {
            romanNum += syb[i];
            num -= val[i];
        }
        i++;
    }

    return romanNum;
}