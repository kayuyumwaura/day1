value = 'abracadabra'

def count_letters(word, char):
    count = 0
    for c in word:
        if char == c:
            count += 1
    return count

x = count_letters(value, 'b')
print (x)