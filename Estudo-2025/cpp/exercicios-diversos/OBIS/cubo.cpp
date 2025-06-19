// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie();

    int dimensaoCubo;

    cin >> dimensaoCubo;

    if(dimensaoCubo == 2){
        cout << 0 << "\n";
        cout << 0 << "\n";
        cout << 0 << "\n";
        cout << 8 << "\n";
        return 0;
    }

    cout << ((dimensaoCubo - 2) * (dimensaoCubo - 2)) * (dimensaoCubo - 2) << "\n";
    cout << dimensaoCubo * 6 << "\n";
    cout << dimensaoCubo * 6 << "\n";
    cout << 8;


}
