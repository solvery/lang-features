// 模板无类型参数
#include <iostream>
using namespace std;

template <typename T, int count>
void loopIt(T x)
{
   T val[count];

   for(int ii=0; ii<count; ii++)
   { 
       val[ii] = x++;
       cout <<  val[ii] << endl;
   }
};

template <typename T=float, int count=3>
T multIt(T x)
{
   for(int ii=0; ii<count; ii++)
   {
       x = x * x;
   }
   return x;
};

main()
{
   float xx = 2.1;

   loopIt<float,3>(xx);

   cout << xx << ": " << multIt<>(xx) << endl;;
}


