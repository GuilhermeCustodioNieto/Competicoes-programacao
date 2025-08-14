// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int calcular(int n, int k)
{
    if (n <= k)
    {
        return 1;
    }

    int segundoCalculo = n;
    if (n % 2 != 0)
    {
        segundoCalculo = (n + 1) / 2;
    }

    int valor = calcular(n / 2, k) + calcular(segundoCalculo, k);
    return valor;
}

// 64 > 32 + 32 > 16 + 16 + 16 + 16 > 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4
// 18 >> 9 + 9 >> 4 + 5 + 4 + 5>>
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int capitalInicial, quantidadeMax;
    cin >> capitalInicial >> quantidadeMax;

    if (capitalInicial < quantidadeMax)
    {
        cout << 1;
        return 0;
    }

    cout << calcular(capitalInicial, quantidadeMax);
}
