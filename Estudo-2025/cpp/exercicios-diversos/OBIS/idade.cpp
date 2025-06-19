// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie();

    int a, b, c;

    cin >> a >> b >> c;

    vector<int> idades = {a, b, c};

    sort(idades.begin(), idades.end());

    cout << idades[1];

}
