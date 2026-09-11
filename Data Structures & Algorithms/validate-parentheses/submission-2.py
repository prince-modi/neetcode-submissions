class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol in ("[", "(", "{"):
                stack.append(symbol)
            elif stack and (
                (symbol == "]" and stack[-1] == "[")
                or (symbol == ")" and stack[-1] == "(")
                or (symbol == "}" and stack[-1] == "{")
            ):
                stack.pop()
            else:
                return False
        return not stack