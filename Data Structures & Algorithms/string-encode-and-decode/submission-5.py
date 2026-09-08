class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded_strs_list = []
        for str_ in strs:
            encoded_str_list = []
            if str_:
                chars = list(str_)
                print(chars)
                for char in chars:
                    print(char)
                    encoded_str_list.append(str(ord(char)))

            encoded_str = "-".join(encoded_str_list)
            encoded_strs_list.append(encoded_str)

        encoded_res = "%".join(encoded_strs_list)
        return "%" + encoded_res + "%"
            

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        res = []
        encoded_strs = s.split("%")
        encoded_strs = encoded_strs[1:-1]
        for encoded_str in encoded_strs:
            str_list = encoded_str.split("-")
            decoded_str_list = []
            for i in range(len(str_list)):
                if str_list[i] == "":
                    decoded_str_list.append("")
                else:
                    ord_ = int(str_list[i])
                    decoded_str_list.append(chr(ord_))
            decoded_str = "".join(decoded_str_list)
            res.append(decoded_str)

        return res


            

