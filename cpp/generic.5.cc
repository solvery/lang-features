// 类模板的静态成员：

#include <iostream>

using namespace std;

template <class T> 
class A
{
public:
    void m1();
    static T v1;
private:
    static T v2;
};

template <class T> 
void A<T>::m1()
{
    cout << v2++ << endl;
}

// 静态成员初始化:
template <class T> T A<T>::v1 = 1;
template <class T> T A<T>::v2 = 1.2;

main()
{
    A<int> oa1;
    A<float> oa2;

    oa1.m1();
    cout << oa1.v1 << endl;
    oa2.m1();
}
