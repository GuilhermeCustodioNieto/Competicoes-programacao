// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
	int n;
    
    cin >> n;

    int numeros[n];
    map<int, int> valoresContados;

    for(int i=0; i<=n - 1; i++){
        cin >> numeros[i];

        valoresContados[numeros[i]]++;
    }

    for(auto [chave, valor] : valoresContados){
        cout << chave << ": " << valor << '\n';
    }
}
