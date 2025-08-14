// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	set<int> numeros;

    for(int i=0; i<=10; i++){
        int x;
        cin >> x;
        numeros.insert(x);
    }

    for(int num : numeros){
        cout << num << ", ";
    }
}
