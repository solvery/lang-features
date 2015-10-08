
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

int func()=delete;

struct NoCopy
{
    NoCopy () = default;
    NoCopy & operator =( const NoCopy & ) = delete;
    NoCopy ( const NoCopy & ) = delete;
};
NoCopy a;
/// NoCopy b(a);

int main(int argc, char** arg) {
}

