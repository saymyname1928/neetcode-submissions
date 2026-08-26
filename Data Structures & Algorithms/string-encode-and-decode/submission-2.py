class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        strs = [""] + strs
        return chr(129).join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(chr(129))[1:]
