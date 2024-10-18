# ''''
# pentru caracterele 'A'-'Z' generati o lista de tuple de genul:
# [('A', 65, 25), ('B', 66, 24), ...., ('Z', 90, 0)]
# unde primul element din tuplu este caracterul in sine, al 2-lea element este codul ascii in baza 10, iar al 3-lea element este un index invers in range-ul (0,..,25)
# Construiti lista cu o singura linie de cod
# '''

# print( [(letter, ord(letter), 25 - index) for index, letter in enumerate('ABCDEFGHIJKLMNOPRQSTUVWXYZ')] )


with open('output.txt', 'r') as f:
    text = f.read()

hex_alphabet = '0123456789ABCDEF'

hex_representation = [[]]
for i in range(0, 16):
    hex_representation[0].append('0' + hex_alphabet[i])

text_length = len(text)

current_index = 0
for i in range(0, len(text) // 16):

    hex_representation.append([hex(ord(text[i * 16 + curr])) for curr in range(16)])

hex_representation.append([hex(ord(text[i * 16 + curr])) for curr in range(16 - len(text) % 16)])


ox_removed = [[f"{elem[2:]:>02}" for elem in ln] for ln in hex_representation] 


final_repr = []

for ln in ox_removed:
    print(' '.join(ln))




