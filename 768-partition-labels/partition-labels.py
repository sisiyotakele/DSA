class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance=[0]*26
        for i ,char in enumerate(s):
            last_occurance[ord(char)-ord('a')]=i
        result=[]
        start =0
        end=0
        for i,char in enumerate(s):
            end =max(end,last_occurance[ord(char)-ord('a')])
            if i == end:
                result.append (end-start+1)
                start=end+1
        return result