// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie();

    int numAlfabeto, numMensagem;
    cin >> numAlfabeto >> numMensagem;

    char alfabeto[numAlfabeto], mensagem[numMensagem];

    for(int i = 0; i<=numAlfabeto - 1; i++){
        cin >> alfabeto[i];
    }

    for(int i = 0; i<=numMensagem - 1; i++){
        cin >> mensagem[i];
    }

    

    for(char codigo : mensagem){
        char output = 'S';
        for(char letra : alfabeto){
            if(codigo != letra){
                output = 'N';
            } else{
                output = 'S';
                break;
            }
        }

        if(output != 'S'){
            cout << output;
            return 0;
        } 
    }

    cout << 'S';

}
