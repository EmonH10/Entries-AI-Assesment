def frequencyCounter(s):
    s = s.lower()

    d = {}

    n = len(s)

    for i in range(0,n):
        word = ""
        while(s[i]!=" "):
            word = word+s[i]
            i = i+1
        i+=1
        print(word)



s = "the cat and the dog and the bird"
frequencyCounter(s)
            