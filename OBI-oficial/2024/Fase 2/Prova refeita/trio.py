import sys

def contador_valid_trios(a, N):
    a.sort()
    contador = 0

    for i in range(N - 2):
        k = i + 2

        for j in range(i+1, N - 1):
            while k < N and a[i] + a[j] > a[k]:
                k += 1

            contador += k - j - 1

    return contador

if __name__ == "__main__":
    entrada = sys.stdin.read
    data = entrada().split()

    N = int(data[0])

    a = list(map(int, data[1:N+1]))

    result = contador_valid_trios(a, N)
    print(result)