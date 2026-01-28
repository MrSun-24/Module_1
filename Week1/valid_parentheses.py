# def shrink_once(s: str):
#     def is_pair(a, b):
#         return (a == '(' and b == ')') or \
#                (a == '[' and b == ']') or \
#                (a == '{' and b == '}')
#     out = []
#     skip = 0
#     changed = False
#     for i in range(len(s)):
#         if skip:
#             skip = 0
#             continue
#         if i + 1 < len(s) and is_pair(s[i], s[i + 1]):
#             skip = 1          # bỏ qua cặp liền kề hợp lệ
#             changed = True
#         else:
#             out.append(s[i])  # giữ lại ký tự chưa ghép được
#     return ''.join(out), changed

# def is_valid_no_stack(s: str) -> bool:
#     if len(s) % 2 == 1:
#         return False
#     changed = True
# #     while changed:
# #         s, changed = shrink_once(s)
# #     return s == "" # nếu s == "" thì true còn lại là False
# print(is_valid_no_stack("()[]{}"))        # True
# print(is_valid_no_stack("()[]{}("))       # False
# print(is_valid_no_stack("([{}])[]{}"))    # True
# print(is_valid_no_stack("([)]"))          # False


def isValid(s):
    if len(s) % 2 == 1:
        return False
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack:
                return False
            if (ch == ')' and stack[-1] != '(') or \
               (ch == ']' and stack[-1] != '[') or \
               (ch == '}' and stack[-1] != '{'):
                return False
            stack.pop()
    return stack == []

print(isValid("([{}])[]{}")) 