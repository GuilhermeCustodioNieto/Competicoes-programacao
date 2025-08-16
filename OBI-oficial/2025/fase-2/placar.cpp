// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie(0);


    // leitura de gols de paulo
    int golsPaulo;
    cin >> golsPaulo;

    int[golsPaulo] momentosGols;
    for(int i=0; i<=golsPaulo; i++){
        cin >> momentosGols[i];
    }

    
    // leitura de gols de Camila
    int golsCamila;
    cin >> golsCamila;

    int[golsCamila] momentosGolsCamila;
    for(int i=0; i<=golsCamila; i++){
        cin >> momentosGolsCamila[i];
    }

    
    cout << "finalizado";

    return 0;

}
