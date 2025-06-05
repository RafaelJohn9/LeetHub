function findLHS(nums: number[]): number {
    nums.sort((a, b) => a - b);

    let largest: number = 0;
    let curr_largest: number = 0;


    let i: number = 0;
    let j: number = 0;

    while (j < nums.length){
        if (Math.abs(nums[i] - nums[j]) == 1){
            j += 1;
            curr_largest = Math.abs(j - i);
        }else if (j ==i  || Math.abs(nums[j] - nums[i]) < 1){
            j += 1;
        }else{
            i += 1;
            largest = Math.max(largest, curr_largest);
            curr_largest -= 1;
        }
    }

    return Math.max(largest, curr_largest);
};