def calculate_IC(ciphertext, n):
    list_strs = []
    list_map = dict()
    for i in range(n):
        list_strs.append(ciphertext[i::n])
    for i in list_strs:
        list_map[i] = dict()
        for j in range(26):
            letter = chr(ord('a')+j)
            list_map[i][letter] = i.count(letter)
    IC = 0

    for i in list_map:
        sum_IC = 0
        N = len(i)
        for j in list_map[i]:
            n_i = list_map[i][j] 
            sum_IC += n_i*(n_i-1)
        IC+=(sum_IC/(N*(N-1)))
    IC/=n
    return list_map, IC

def calculate_key_length(ciphertext):
    key_length = 0
    max_IC = 0
    for n in range(3,13):
        _, curr_IC = calculate_IC(ciphertext, n)
        if max_IC < curr_IC:
            max_IC = curr_IC
            key_length = n
    list_map, _ = calculate_IC(ciphertext, key_length)
    return key_length, list_map

def frequency_producer(list_map):
    for i in list_map:
        N = len(i)
        for j in list_map[i]:
            list_map[i][j] /= N
    return list_map

def shift_calculator(frequency_map):
    standard_frequencies = {
        'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0, 'f': 2.2, 'g': 2.0,
        'h': 6.1, 'i': 7.0, 'j': 0.15, 'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7,
        'o': 7.5, 'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8,
        'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0, 'z': 0.074
    }   
    error = 100 
    for j in range(26):
        curr_error = 0
        for i in standard_frequencies:
            k = chr((ord(i)-ord('a')+j)%26 + ord('a'))
            curr_error += (standard_frequencies[i] - frequency_map[k])**2
        curr_error /= 26
        if curr_error < error:
            shift = j
            error = curr_error

    return shift

def merge_list(decoded_list_str, n):
    final_decoded_str = ""
    N = len(decoded_list_str[0])
    for j in range(N):
        for i in decoded_list_str:
            if j < len(i):
                final_decoded_str += i[j]

    return final_decoded_str

def calculate_key(ciphertext):
    n, list_map = calculate_key_length(ciphertext)
    decoded_list_str = []
    frequencies = frequency_producer(list_map)

    key = ""
    for i in list_map:

        shift = shift_calculator(list_map[i])
        key += chr(ord('a')+shift)
        decoded_str = ""
        for j in i:
            k = (ord(j)-ord('a') - shift)%26+ord('a')
            decoded_str += chr(k)
        decoded_list_str.append(decoded_str)
    
    final_decoded_str = merge_list(decoded_list_str, n)

    return key, final_decoded_str
        

with open('input.txt') as f:
    ciphertext = f.read()

updated_text = ""

for i in ciphertext:
    if ord('a') <= ord(i) and ord(i) <= ord('z'):
        updated_text += i

key, final_decoded_str = calculate_key(updated_text)
final_decoded_str_w_punc = ""

cur = 0
for i in ciphertext:
    if ord('a') <= ord(i) and ord('z') >= ord(i):
        final_decoded_str_w_punc += final_decoded_str[cur]
        cur +=1 
    else:
        final_decoded_str_w_punc += i

with open('output.txt', 'w') as f:
    f.write("Plaintext:\n")
    f.write(final_decoded_str_w_punc)
    f.write("\n\nKey:\n")
    f.write(key)
