// Source: https://usaco.guide/general/io

#include <algorithm>
#include <bits/stdc++.h>
#include <string>
#include <unordered_set>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie();

    int n;
    string cadeia;

    unordered_set<string> saida;
    string saidaString = "";

    cin >> n >> cadeia;

    for (int i = 0; i < n; i++)
    {
        i = 0;
        std::string valor(1, cadeia.at(i));

        cout << (saida.count(valor)) << endl;

        if (saida.count(valor) > 0)
        {
            continue;
        }

        int contagem = 0;

        if (cadeia.at(i) == valor.at(0))
        {
            n = (int)cadeia.size();

            cadeia.replace(i, 1, "");
            contagem++;
            saidaString += valor.append(" " + contagem);
            saida.insert(saidaString);
        }

        // n = (int)cadeia.size();
    }

    cout << saidaString;
}
