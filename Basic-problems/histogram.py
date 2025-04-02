#Print histogram of all characters in file word.txt

def hist(word,myhist):  
    for ch in word:
        if ch not in myhist:
            myhist[ch] = 1
        else:
            myhist[ch] += 1
    return (myhist)
  
file = open("words.txt")
myhist = {}

for line in file:   
    word = line.strip()
    myhist = hist(word,myhist)

print(myhist)
