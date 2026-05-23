def checkPalindrom(s):

    s = s.lower()
    s = s.replace(" ","")

    if s == s[::-1]:
        return True
    else:
        return False
    

s = "No lemon, no melon"

print(checkPalindrom(s))