/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let count = 1;
    let resultIndex = 0;

    for (let i = 0; i < chars.length; i++) {
        if (chars[i] === chars[i + 1]) {
            count++;
        } else {
            chars[resultIndex++] = chars[i];

            if (count > 1) {
                for (let digit of count.toString()) {
                    chars[resultIndex++] = digit;
                }
            }

            count = 1;
        }
    }

    return resultIndex;
};