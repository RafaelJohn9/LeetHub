class Solution:
    def countOfAtoms(self, formula: str) -> str:
        import collections
        
        def parse_formula(index):
            stack = [collections.Counter()]
            n = len(formula)
            
            while index < n:
                if formula[index] == '(':
                    stack.append(collections.Counter())
                    index += 1
                elif formula[index] == ')':
                    index += 1
                    start_index = index
                    while index < n and formula[index].isdigit():
                        index += 1
                    multiplier = int(formula[start_index:index] or 1)
                    top = stack.pop()
                    for key in top:
                        stack[-1][key] += top[key] * multiplier
                else:
                    start_index = index
                    index += 1
                    while index < n and formula[index].islower():
                        index += 1
                    atom = formula[start_index:index]
                    start_index = index
                    while index < n and formula[index].isdigit():
                        index += 1
                    count = int(formula[start_index:index] or 1)
                    stack[-1][atom] += count
            
            return stack[-1]
        
        counter = parse_formula(0)
        return ''.join(f"{atom}{(counter[atom] if counter[atom] > 1 else '')}" for atom in sorted(counter))