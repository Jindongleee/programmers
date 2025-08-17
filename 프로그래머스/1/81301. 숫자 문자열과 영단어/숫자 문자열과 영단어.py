def solution(s):
    
    answer = []
    # 한글자씩 조사 -> 아스키코드 값이 65 이상이다. 그러면 문자
    # 또는 isdigit 모두 숫자라면 -> True, 아니면 False
    str = []
    
    # 1. 노가다 방식
    # for i in range(len(s)):
    #     if s[i].isdigit():
    #         if len(str) != 0:
    #             if ''.join(str) == "zero":
    #                 answer.append("0")
    #                 str = []
    #             elif ''.join(str) == "one":
    #                 answer.append("1")
    #                 str = []
    #             elif ''.join(str) == "two":
    #                 answer.append("2")
    #                 str = []
    #             elif ''.join(str) == "three":
    #                 answer.append("3")
    #                 str = []
    #             elif ''.join(str) == "four":
    #                 answer.append("4")
    #                 str = []
    #             elif ''.join(str) == "five":
    #                 answer.append("5")
    #                 str = []
    #             elif ''.join(str) == "six":
    #                 answer.append("6")
    #                 str = []
    #             elif ''.join(str) == "seven":
    #                 answer.append("7")
    #                 str = []
    #             elif ''.join(str) == "eight":
    #                 answer.append("8")
    #                 str = []
    #             elif ''.join(str) == "nine":
    #                 answer.append("9")
    #                 str = []
    #         answer.append(s[i]) # 숫자 담기
    #     else:
    #         str.append(s[i]) 
    #         if ''.join(str) == "zero":
    #             answer.append("0")
    #             str = []
    #         elif ''.join(str) == "one":
    #             answer.append("1")
    #             str = []
    #         elif ''.join(str) == "two":
    #             answer.append("2")
    #             str = []
    #         elif ''.join(str) == "three":
    #             answer.append("3")
    #             str = []
    #         elif ''.join(str) == "four":
    #             answer.append("4")
    #             str = []
    #         elif ''.join(str) == "five":
    #             answer.append("5")
    #             str = []
    #         elif ''.join(str) == "six":
    #             answer.append("6")
    #             str = []
    #         elif ''.join(str) == "seven":
    #             answer.append("7")
    #             str = []
    #         elif ''.join(str) == "eight":
    #             answer.append("8")
    #             str = []
    #         elif ''.join(str) == "nine":
    #             answer.append("9")
    #             str = []
    #   return int(''.join(answer))
            
    # 2. 분기 방식
    if 'one' in s:
        s= s.replace('one', '1')
    if 'zero' in s:
        s= s.replace('zero', '0')
    if 'two' in s:
        s= s.replace('two', '2')
    if 'three' in s:
        s= s.replace('three', '3')
    if 'four' in s:
        s= s.replace('four', '4')
    if 'five' in s:
        s= s.replace('five', '5')
    if 'six' in s:
        s= s.replace('six', '6')
    if 'seven' in s:
        s= s.replace('seven', '7')
    if 'eight' in s:
        s= s.replace('eight', '8')
    if 'nine' in s:
        s= s.replace('nine', '9')

    return int(s)