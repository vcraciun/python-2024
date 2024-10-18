with open('olimpice.py', 'r') as f:
    prop = f.read().lower()

# prop = 'Ana are mere'.lower()
f = open('output.txt', 'w') 

freq = {}

for letter in 'abcdefghijklmnopqrstuvwxyz':
    freq[letter] = prop.count(letter)

max_freq = max(freq.values())

m = []
for i in range(26):
    m += ['.' * (max_freq - freq[chr(ord('a') + i)]) + 'o' * freq[chr(ord('a') + i)]]

for j in range(max_freq):
    f.write('\n')
    for i in range(26):
        f.write(m[i][j])

f.write('\n')
f.write(''.join(freq.keys()))
