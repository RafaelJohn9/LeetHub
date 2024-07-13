class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        # Pairing positions, healths, and directions, then sort by positions
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        # Stack to manage the robots moving to the right
        stack = []
        
        # Result list to track health of robots that survive in the original order
        result = [None] * len(positions)
        
        for pos, health, direction, original_index in robots:
            if direction == 'R':
                # Push right-moving robots onto the stack
                stack.append((health, original_index))
            else:
                # Process left-moving robots
                while stack and health > 0:
                    r_health, r_index = stack[-1]
                    
                    if r_health < health:
                        stack.pop()  # Right-moving robot gets removed
                        health -= 1  # Reduce health of the left-moving robot
                    elif r_health > health:
                        stack[-1] = (r_health - 1, r_index)  # Reduce health of the right-moving robot
                        health = 0  # Left-moving robot gets removed
                    else:
                        stack.pop()  # Both robots have the same health and get removed
                        health = 0  # Left-moving robot gets removed
                
                if health > 0:
                    result[original_index] = health
        
        # Remaining robots in the stack survived without collisions
        for health, original_index in stack:
            result[original_index] = health
        
        # Filter out None values from result to return only surviving robots' healths
        return [h for h in result if h is not None]
