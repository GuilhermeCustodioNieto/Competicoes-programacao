#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
    cin.tie(0); 

    int numLojas;
    cin >> numLojas;

    vector<int> lojas;

    
    for(int i=0; i<=numLojas-1; i++){
        int x;
        cin >> x;
        lojas.push_back(x);
        
    }

    sort(lojas.begin(), lojas.end());

    int diasParaBeber;
    cin >> diasParaBeber;

    

    for(int i=0; i<=diasParaBeber - 1; i++){
        int dinheiro;
        cin >> dinheiro;
        auto valorEncontrado = upper_bound(lojas.begin(), lojas.end(), dinheiro);
        cout << valorEncontrado - lojas.begin();
        
        cout << '\n';


    }
}

// 123 168 714 868 987

