#include <iostream>
using namespace std;
int main()
{
    int horas, minutos, segundos, adiamento;
    cin >> horas >> minutos >> segundos >> adiamento;

    segundos += adiamento % 60;

    if (segundos >= 60)
    {
        segundos -= 60;
        minutos += 1;
    }
    adiamento = adiamento / 60;
    minutos += adiamento % 60;
    if (minutos >= 60)
    {
        minutos -= 60;
        horas += 1;
    }

    adiamento = adiamento / 60;
    horas += adiamento % 24;

    cout << horas << endl;
    cout << minutos << endl;
    cout << segundos << endl;

    return 0;
}

/*
3
14
15
1
 */