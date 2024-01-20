def plusOne(self, digits):
    index = len(digits) - 1
    digits[index] += 1
    if digits[len(digits) - 1] > 9:
        lastNum = str(digits[len(digits) - 1])
        digits[len(digits) - 1] = int(lastNum[0])
        digits.append(int(lastNum[1]))

    return digits

print(plusOne("self", [4,3,2,1]))
