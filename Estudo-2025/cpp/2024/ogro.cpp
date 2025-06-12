#include <iostream>
using namespace std;

int main()
{
    int esquerda, direita;
    cin >> esquerda >> direita;

    if (esquerda > direita)
    {
        cout << esquerda + direita;
    }
    else
    {
        cout << 2 * (direita - esquerda);
    }

    return 0;
}