// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

//Encontrou )( então é YES
// Não encontrou )( então é NO

string validarEntrada(string entrada){
    string saida = "NO";
    if(entrada.find(")(") != string::npos){
        saida = "YES";
        
    }

    while(entrada.length() != 2){
        entrada.erase(0, 1);
        entrada.erase(entrada.length() - 1, 1);

        if(entrada.find(")(") != string::npos){
            saida = "YES";
            
        }
    }

    

    return saida;
}
/*
5
(())
()()()
(())()
()(())
(()())
---
Saída esperada
NO 
YES
YES 
YES
NO
 */

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

	int quantidadeTests;
    cin >> quantidadeTests;

    for(int i=0; i<=quantidadeTests - 1; i++){
        string entrada;

        cin >> entrada;

        string saida = validarEntrada(entrada);
        if(i == quantidadeTests-1){
            cout << saida;
        }else{
            cout << saida << '\n';
        }
        
    }

    return 0;
}
