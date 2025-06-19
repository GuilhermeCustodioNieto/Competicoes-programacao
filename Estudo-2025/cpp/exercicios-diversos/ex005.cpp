// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {

    ios::sync_with_stdio(0);    
    cin.tie();

    int x, resultado = 1;
    cin >> x;
    

    for(int i = 1; i <= x; i++){
        resultado = resultado * i;
        
    }

    cout << resultado;
}
