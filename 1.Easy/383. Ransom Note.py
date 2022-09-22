
from operator import le


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    rnsm = {}
    mgzn = {}

    for letter in ransomNote:
        if letter not in rnsm:
            rnsm[letter] = 1
        else:
            rnsm[letter] += 1

    for letter in magazine:
        if letter not in mgzn:
            mgzn[letter] = 1
        else:
            mgzn[letter] += 1

    if not set(rnsm.keys()).issubset(set(mgzn.keys())):
        return False
    
    for letter in rnsm:
        if rnsm[letter] > mgzn[letter]:
            return False
    
    return True

print(canConstruct("aab", "aab"))