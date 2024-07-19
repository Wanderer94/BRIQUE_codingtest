def longest_valid_parentheses(str):
    max_length = 0
    stack = [-1]  # 스택에 초기값 -1을 추가하여 계산의 편의를 도모

    for i, char in enumerate(str):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

def main():
    user_input = input("괄호 문자열을 입력하세요: ")

    # 유효성 검사: 입력 문자열이 '('와 ')'로만 구성되어 있는지 확인
    valid = True
    for char in user_input:
        if char not in ('(', ')'):
            valid = False
            break

    if not valid:
        print("잘못된 값을 입력하셨습니다.")
        return

    result = longest_valid_parentheses(user_input)
    print(f"result: {result}")

if __name__ == "__main__":
    main()