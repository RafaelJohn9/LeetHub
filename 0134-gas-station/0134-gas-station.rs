impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let (mut total_tank, mut curr_tank, mut start) = (0, 0, 0);

        for i in 0..gas.len(){
            let net = gas[i] - cost[i];
            total_tank += net;
            curr_tank  += net;

            if curr_tank < 0{
                start = i + 1;
                curr_tank = 0;
            }
        }

        if total_tank >= 0 {start as i32} else { -1}
    }
}