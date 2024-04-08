arr = [4,2,0,3]

def goldtest(arr):
    ataques = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                ataques += 2
            elif abs(i - j) == abs(arr[i] - arr[j]):
                ataques += 2
    return ataques

resultado = goldtest(arr)
print("Número de ataques:", resultado)

               
