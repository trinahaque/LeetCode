# Given an input string, reverse the string word by word.
# Input: "the sky is blue"
# Output: "blue is sky the"

def reverseWordsInString(s):
    if len(s) < 1:
        return ""
    elif len(s) < 2:
        if s.isalnum() == True:
            return s
    result = ""
    # splits the words into an array
    strArr = s.split(" ")


    # reverses the array
    for i in range(int(len(strArr)/2)):
        if strArr[i].isalnum() == False or strArr[len(strArr) - 1 - i].isalnum() == False:
            break
        strArr[i], strArr[len(strArr) - 1 - i] = strArr[len(strArr) - 1 - i], strArr[i]
    
    # puts each word from the reversed array into result string except for the last one
    for i in range(len(strArr) - 1):
        if strArr[i].isalnum() == False:
            break
        result += strArr[i] + " "
    result += strArr[len(strArr) - 1]
    return result

input = "the sky blue"
print (reverseWordsInString("1 "))

    

