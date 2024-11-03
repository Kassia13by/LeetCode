class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = []
        current_substr = ""

        for st in s:
            if st not in current_substr:
                current_substr = current_substr + st
            else:        
                s_list.append(current_substr)
                current_substr = current_substr[current_substr.index(st) + 1:]+ st

        s_list.append(current_substr)

        current_len = 0
        for i in s_list:
            if len(i) > current_len:
                current_len = len(i)
        return(current_len)
  
        