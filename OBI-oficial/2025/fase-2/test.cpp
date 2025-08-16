// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie(0);


    // leitura de gols de paulo
    int golsPaulo;
    cin >> golsPaulo;

	set<int> momentosGolsGerais;

    set<int> momentosGols;
    for(int i=0; i<=golsPaulo; i++){
		int momentoGol;
        cin >> momentoGol;
		momentosGols.insert(momentoGol);
		momentosGolsGerais.insert(momentosGols[i]);
    }

    
    // leitura de gols de Camila
    int golsCamila;
    cin >> golsCamila;

    set<int> momentosGolsCamila;
    for(int i=0; i<=golsCamila; i++){
        int momentoGol;
        cin >> momentoGol;
		momentosGolsCamila.insert(momentoGol);
		momentosGolsGerais.insert(momentosGolsCamila[i]);
    }

    cout << "finalizado";

    return 0;

}
