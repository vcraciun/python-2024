
with open("alte_date/input.txt",'r') as f:
    text = f.read()

with open("alte_date/words.txt",'r') as f:
    search_words = f.read().splitlines()

for i in search_words:
    first, last = -1, -1
    try:
        first = text.index(i)
    except Exception:
        pass
    try:
        last = text.rindex(i)
    except Exception:
        pass
    print(i, first, last)

        
