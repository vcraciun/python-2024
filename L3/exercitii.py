import os
# sol = [ (chr(i), i, 25 - (i - 65)) for i in range(65, 91)]
# print(sol)

print(os.getcwd())

def character_freq(r_file,w_file):
    paragraphs = open(r_file,'r').read()
    char_freq = {}
    for char in paragraphs:
        if char.isalnum():
            if char.lower() not in char_freq:
                char_freq[char.lower()] = 0
            char_freq[char.lower()] += 1
    height = max(char_freq.values())
    histogram = []
    for i in range(height):
        line = []
        for value in char_freq.values():
            if value <= i:
                line.append('o')
            else:
                line.append(' ')
        histogram.append(line)
    histogram.append(char_freq.keys())
    open(w_file,'w').write('\n'.join(''.join(line) for line in histogram) )






character_freq('Studenti.txt','Output.txt')