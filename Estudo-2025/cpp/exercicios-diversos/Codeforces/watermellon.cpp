// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    float x;
    cin >> x;

    if(x == 2){
        cout << "NO";        
        return 0;
    }

    while(x > 2){
        x -= 2;
    }

    if(x == 2){
        cout << "YES";
    } else {
        cout << "NO";        
    }
}
