// c++11
// lambda, [capture](parameters)->return-type {body}

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char** arg) {
    vector<int> num {2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8};
    vector<int> p_num;
    copy_if(num.begin(), num.end(), back_inserter(p_num), [](int i){ 
            return (i>0);
            } );
    int average = accumulate(p_num.begin(), p_num.end(), 0) / p_num.size();
    cout << "averge: " << average << endl;

    char s[]="Hello World!";
    int Uppercase = 0; //modified by the lambda
    for_each(s, s+sizeof(s), [&Uppercase] (char c) {
            if (isupper(c))
            Uppercase++;
            });
    cout<< Uppercase<<" uppercase letters in: "<< s<<endl;
}

