#include <iostream>
#include<vector>
using namespace std;

int main() {
    vector<int> altitude = {12,42,56,1,14};
    for (const int& value: altitude) {
        cout<<value<<endl;    
    }
}