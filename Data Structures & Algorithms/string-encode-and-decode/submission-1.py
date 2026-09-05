class Solution:

    def encode(self, strs: List[str]) -> str:
        hex_code = ''
        for s in strs:
            if len(s) == 0:
                hex_code = hex_code +'0x000xffff'
                continue
            chars = list(s)
            for c in chars:
                hex_code = hex_code + f"0x{ord(c):02x}"
            hex_code = hex_code + '0xffff'
        # print(hex_code)
        return hex_code
    def decode(self, s: str) -> List[str]:
        hex_words = s.split("0xffff")
        string_list = []
        for hex_word in hex_words[:-1]:
            word = "".join((hex_word.split("0x"))[1:])
            if word == '00':
                string_list.append('')
                continue
            byte_data = bytes.fromhex(word)
            text_string = byte_data.decode('utf-8')
            string_list.append(text_string)
        return string_list