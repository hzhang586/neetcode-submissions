class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str += str(len(s))+'#'+ s
        
        return encode_str

    def decode(self, s: str) -> List[str]:

        decode_str_lst = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] == '#':
                str_len = int(s[i:j])
                decode_str_lst.append(s[j+1:j+1+str_len])
                i = j+1+str_len
                j = i
            else:
                j += 1

        return decode_str_lst



