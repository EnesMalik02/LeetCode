def isPalindrome(self, x):
    x = str(x)
    num = []
    newNum = []

    for i in range(len(x)):
        num.append(x[i])
    
    for i in reversed(num):
        newNum.append(i)    

    if num == newNum:
        return True
    
print(isPalindrome("self", "1221"))
        