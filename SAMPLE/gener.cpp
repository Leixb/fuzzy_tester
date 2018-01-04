#include <bits/stdc++.h>
#include <sys/time.h>
using namespace std;

int main () {
    ios_base::sync_with_stdio(false);
    struct timeval t1;
    gettimeofday(&t1, NULL);
    srand(t1.tv_usec * t1.tv_sec);

    int rounds = rand()%10 + 2;

    while(rounds--) {

        string v = "AKQJTN";

        for (int i = 0; i < 11; ++i) {
            if (i == 5) cout << ' ';
            else cout << v[rand()%6];
        }
        cout << endl;
    }
}

