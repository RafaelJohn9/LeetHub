function containsNearbyDuplicate(nums: number[], k: number): boolean {
    let i: number = 0; 
    let j: number = 1;
    let seen = new Set<number>();

    for (let i = 0; i < nums.length; i++){
        if (seen.has(nums[i])){
            return true;
        }

        seen.add(nums[i])

        if (seen.size > k){
            seen.delete(nums[i - k]);
        }
    }

    return false;

};