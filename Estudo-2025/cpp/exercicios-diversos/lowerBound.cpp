// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
using namespace std;

int main() {
	vector<int> vetor = {1,2,3,4,5,6,7,8,9};

    auto iterador = lower_bound(vetor.begin(), vetor.end(), 5);
    cout << *iterador;
}
