class solution:
    def removeduplicates(self,s):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

solution = solution()
s = "abbaca"
result = solution.removeduplicates(s)
print("Input:", s)
print("Output after removing adjacent duplicates:", result)
