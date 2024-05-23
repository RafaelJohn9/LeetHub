class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the versions into parts by '.'
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        # Determine the length of the longer version
        max_length = max(len(v1_parts), len(v2_parts))
        
        # Compare each part
        for i in range(max_length):
            # Get the current part for each version, or 0 if this version is shorter
            v1_part = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2_part = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            # Compare the current parts
            if v1_part < v2_part:
                return -1
            elif v1_part > v2_part:
                return 1
        
        # If all parts are equal, the versions are equal
        return 0