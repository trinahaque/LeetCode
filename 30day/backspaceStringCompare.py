# Time Complexity: O(N+M)--> loop through both S and T string
# Space Complexity: O(N+M)--> creating two stack with length S and T

def backspaceCompare(S, T):
    stackS = []
    stackT = []

    # O(N)
    for i in range(len(S)):
        if S[i] != '#':
            stackS.append(S[i])
        elif len(stackS) > 0 and S[i] == '#':
            stackS.pop()
    # O(M)
    for i in range(len(T)):
        if T[i] != '#':
            stackT.append(T[i])
        elif len(stackT) > 0 and T[i] == '#':
            stackT.pop()
    # this is comparing each element inside the array
    # returning true or false based on the comparison
    return stackS == stackT


print(backspaceCompare('a##c#', 'a#c'))