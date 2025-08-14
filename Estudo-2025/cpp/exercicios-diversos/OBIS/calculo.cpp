// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie(0);

    int s, a, b;

    cin >> s >> a >> b;

    set<int> retorno;

    for(int i=a; i<=b; i++){
        string valor = std::to_string(i);
        int soma = 0;
        for(char num : valor){
            soma += (int) num - '0';
        }

        if(soma == s){
            retorno.insert(i);
        }

    }

    cout << retorno.size();
}
