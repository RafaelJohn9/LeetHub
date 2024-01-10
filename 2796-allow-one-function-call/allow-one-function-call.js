/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    trial = 0;
	return function(...args){
        if (trial === 0)
        {
            trial++;
            result = fn(...args);
            return (result);
        }
        else
        {
            trial++;
            return undefined;
        }
        
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
