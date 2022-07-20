alphabet_list = list(str(input()))

def alphabet_code(alphabet):
    return ord(alphabet)-64

alphabet_ascii = list(map(alphabet_code, alphabet_list))

print(*alphabet_ascii)