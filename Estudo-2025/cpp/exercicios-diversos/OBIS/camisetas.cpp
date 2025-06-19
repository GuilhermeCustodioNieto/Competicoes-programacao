// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie();

	int size;
    cin >> size;

    size--;

    int vector[size + 10];
    for(int i=0; i<=size; i++){
        cin >> vector[i];
    }

    int p, m;
    cin >> p >> m;

    int saidaP = 0, saidaM = 0;

    for(int i = 0; i<=size; i++){
        if(vector[i] == 1){
            saidaP++;

        } else{
            saidaM++;
        }
    }

    if(saidaP == p && saidaM == m){
        cout << "S";
    } else{
        cout << "N";
    }


}
