list_gif1 = ["?'labaf_haf" ,"6'leddbf",  "4'lbgfaegf"]
list_gif2 = ["?al''hfd_c_b", "6aladf", "4aldgd'hhce"]

def ascii_list(str1):
	return [ord(k) for k in str1]

list1 = ascii_list(list_gif1[1])
list2 = ascii_list(list_gif2[1])

def func(n):
	for j in range(n):
		str2 = ""
		str3 = ""
		for k in list1:
			str2 += chr(k+j)
		for l in list2:
			str3 += chr(l+j)
		print(str2, str3)

func(2)