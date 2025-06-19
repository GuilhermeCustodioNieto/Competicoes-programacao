// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

struct Hero {
    string nome;
    int forca;
    int vida;
};

int main() {
	ios::sync_with_stdio(0);
    cin.tie();

    int quantidadeHerois;
    cin >> quantidadeHerois;

    string nomeMaisForte, nomeComMaisVida;
    int maisForte = 0, maisVida = 0;
    double mediaForca = 0;



    for(int i=0; i<=quantidadeHerois-1; i++){
        Hero heroi;
        cin >> heroi.nome >> heroi.forca >> heroi.vida;

        if(heroi.forca > maisForte){
            nomeMaisForte = heroi.nome;
            maisForte = heroi.forca;
        }

        if(heroi.vida > maisVida){
            nomeComMaisVida = heroi.nome;
            maisVida = heroi.vida;
        }

        mediaForca += heroi.forca;
    }

    mediaForca = mediaForca / quantidadeHerois;

    cout << "Herói com maior força: " << nomeMaisForte << '\n';
    cout << "Herói com maior vida: " << nomeComMaisVida << '\n';
    cout << fixed <<  setprecision(2);
    cout << "Média de força: " << mediaForca;

    return 0;
}
