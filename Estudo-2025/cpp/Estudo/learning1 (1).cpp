// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
    
    int a, b;
    cin >> a >> b;
    cout << "A Soma de A + B = " << a + b << "\n";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');


    string x;
    getline(cin, x);

    cout << "Seu teste deu: " << x;

    while(cin >> x){
        cout << "valor digitado: " << x << "\n";
    }



    return 0;
}
