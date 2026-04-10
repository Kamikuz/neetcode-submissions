class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        # count + 'delimiter' + content
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        res = []
        pointer = 0
        while pointer < len(s):
            count = ''
            while s[pointer] != '#':
                count += s[pointer]
                pointer += 1
            count = int(count)
            pointer += 1
            res.append(s[pointer:pointer+count])
            pointer += count

        return res