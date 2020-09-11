def solution(str1, str2):
    if not str1 and not str2:
        return 65536
    str1 = str1.lower()
    str2 = str2.lower()
    str1_dict = {}
    str2_dict = {}
    len_str1 = len(str1)
    len_str2 = len(str2)
    for i in range(1, len_str1):
        str = str1[i-1] + str1[i]
        if str.isalpha():
            str1_dict[str] = str1_dict.get(str, 0) + 1
    for i in range(1, len_str2):
        str = str2[i-1] + str2[i]
        if str.isalpha():
            str2_dict[str] = str2_dict.get(str, 0) + 1
    num = den = 0
    key_set = set(list(str1_dict) + list(str2_dict))
    for key in key_set:
        num += min(str1_dict.get(key, 0), str2_dict.get(key, 0))
        den += max(str1_dict.get(key, 0), str2_dict.get(key, 0))
    if not den:
        return 65536
    answer = int(num / den * 65536)
    return answer

print(solution("FRANCE", "french"))