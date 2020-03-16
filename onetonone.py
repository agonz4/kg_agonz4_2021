import sys

MAX_CHARS = 256
def one_to_one_matching(s1, s2):
    length_s1 = len(s1)
    length_s2 = len(s2)

#Length of both strings must be equal
    if length_s1 != length_s2:
        return False

#Created a boolean list to check characters we have seen
    checked_characters = [False] * MAX_CHARS

#List to mark characters in s2
    maping = [-1] * MAX_CHARS

    #Start processing characters
    for i in range(length_s1):

        #If unicode is first time being seen
        if maping[ord(s1[i])] == -1:

            #If first character of s2 has already been checked, one to one not possible
            if checked_characters[ord(s2[i])]:
                return False

            #Mark character in s2 as checked
            checked_characters[ord(s2[i])]

            #Map the current characters of s1 and s2
            maping[ord(s1[i])] = s2[i]

        #If the current character is not the first appearance in s1
        #see if previous appearance is mapped to same character in s2
        elif maping[ord(s1[i])] != s2[i]:
            return False
    return True
