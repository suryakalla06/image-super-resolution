map ={ 
"A": '00000',
"B": '00001',
"C": '00010',
"D": '00011',
'E': '00100',
'F': '00101',
'G': '00110',
'H': '00111',
'I': '01000',
'J': '01001',
'K': '01010',
'L': '01011',
'M': '01100',
'N': '01101',
'O': '01110',
'P': '01111',
'Q': '10000',
'R': '10001',
'S': '10010',
'T': '10011',
'U': '10100',
'V': '10101',
'W': '10110',
'X': '10111',
'Y': '11000',
'Z': '11001',
'2': '11010',
'3': '11011',
'4': '11100',
'5': '11101',
'6': '11110',
'7': '11111'}
content = "JI2UQRSVKNBUMR2NLJLEGVCTJNGEUTCWJ5LUUVCMIZEUKQ2QJI2UQVJWKQZFASJ5"
bin_str=""
for i in content:
	bin_str += map[i]
bin_str+="00000"

def str_to_dec(s):
	add = 0
	prod = 1
	for i in s[::-1]:
		add += int(i)*prod
		prod*=2
	return add
ans = ""
for i in range(len(bin_str)):
	if i % 8 == 0 and i!=0:
		ans += chr(str_to_dec(bin_str[i-8:i]))
print(ans)
