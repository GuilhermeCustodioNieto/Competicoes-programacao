// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie(0);

    int partidas;
    cin >> partidas;

    for(int i=0; i < partidas; i++){
        int valorMaxCaixinha, minimo, maximo;
        cin >> valorMaxCaixinha >> minimo >> maximo;
        
        int caixinha = 0;
        int contagemBombons = 0;

        for(int j = minimo; j < maximo + 1; j++){
            if(caixinha >= valorMaxCaixinha) break;

            contagemBombons++;
            caixinha += j;
        }
        
        cout << contagemBombons << '\n';
    }


    return 0;

}
