s = "53ddc305))6*;4826)4d.)4d);806*;48c8p60))85;;]8*;:d*8c83(88)5*c;46(;88*96*?;8)*d(;485);5*c2:*d(;4956*2(5*-4)8p8*;4069285);)6c8)4dd;1(d9;48081;8:8d1;48c85;4)485c528806*81(d9;48;(88;4(d?34;48)4d;161;:188;d?;"

# chars = {}
# for char in s:
# 	if char not in chars:
# 		chars[char] = 1
# 	else:
# 		chars[char] += 1


# for key in sorted(chars, key=chars.get, reverse=True):
# 	print key, chars[key]

# digraphs = {}
# for i in range(len(s)-1):
# 	if s[i:i+2] not in digraphs:
# 		digraphs[s[i:i+2]] = 1
# 	else:
# 		digraphs[s[i:i+2]] += 1

# for key in sorted(digraphs, key=digraphs.get, reverse=True):
# 	print key, digraphs[key]

print s.replace("8", "E").replace(";", "T").replace("4", "H").replace(")","S").replace("(", "R").replace("d", "O").replace("*", "N").replace("6","I").replace("5","A") \
.replace("c", "D").replace("]", "W").replace("3", "G").replace(":", "Y").replace("9", "M").replace("?", "U").replace("2", "B").replace("p", "V").replace("-","C") \
.replace("0", "L").replace(".","P").replace("1","F")
# .replace("5","R").replace(")", "A")
