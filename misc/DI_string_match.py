def diStringMatch(S):
    result = []
    N = len(S)
    remaining = [x for x in range(0, N+1)]
    for i in range(0, N):
        if S[i] == 'I':
            result.append(remaining[0])
            del remaining[0]
        else: 
            result.append(remaining[-1])
            del remaining[-1]
    result.append(remaining.pop())
    return result
diStringMatch('IDID')
diStringMatch('III')
diStringMatch('DDI')