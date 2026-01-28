def levenshtein_distasnce(s, t):
    distances = [[0] * (len(t) + 1) for i in range(len(s) + 1)]

    for e in range(len(t) + 1):
        distances[0][e] = e

    for e in range(len(s) + 1):
        distances[e][0] = e

    for e1 in range(1, len(s) + 1):
        for e2 in range(1, len(t) + 1):
            cost = 0 if s[e1 - 1] == t[e2 - 1] else 1
            distances[e1][e2] = min(
                distances[e1 - 1][e2] + 1,
                distances[e1][e2 - 1] + 1,
                distances[e1 - 1][e2 - 1] + cost
            )
    
    return distances[-1][-1]

print(levenshtein_distasnce('hola', 'hello'))