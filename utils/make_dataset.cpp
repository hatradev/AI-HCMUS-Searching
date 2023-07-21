#include <fstream>
#include <iostream>
#include <random>
using namespace std;

int main() {
    srand(time(NULL));
    ofstream fout("../datasets/INPUT_8.txt");
    if (fout.is_open()) {
        short c;
        cout << "Enter small or big (0, 1):";
        cin >> c;
        int m, n;
        if (!c) {
            n = rand() % 31 + 10;
            m = rand() % 4 + 1;
            fout << rand() % 1000 + 1 << endl;
            fout << m << endl;
        } else {
            n = rand() % 100 + 50;
            m = rand() % 6 + 5;
            fout << rand() % 10000 + 1 << endl;
            fout << m << endl;
        }
        cout << "n = " << n << endl;
        int max = 100;
        for (int k = 0; k < 3; k++) {
            if (k == 2) max = m;
            for (int i = 0; i < n; i++) {
                if (i == n - 1) {
                    if (k != 2)
                        fout << rand() % max + 1 << endl;
                    else
                        fout << rand() % max + 1;
                } else
                    fout << rand() % max + 1 << ", ";
            }
        }
    } else
        cout << "Fail to open file";

    fout.close();

    return 0;
}