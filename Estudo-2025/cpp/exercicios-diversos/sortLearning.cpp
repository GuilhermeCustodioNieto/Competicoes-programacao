// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie(0);

    int n = 0;
    cin >> n;

    int vetor[n];

    for(int i=0; i<=n-1; i++){
        cin >> vetor[i];
    }

    n = sizeof(vetor) / sizeof(vetor[0]);

    sort(vetor, vetor + n);

    for(int num : vetor){
        cout << num << " ";
    }
}
