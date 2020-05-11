#ifndef _MYTESTLIBB_
#define _MYTESTLIBB_
 
namespace MyTestLibB
{
    class Calculator
    {
    public:
        Calculator();
        virtual ~Calculator(){};
        
        /**
         *	Simple add method
         */
        int add(const int lhs, const int rhs);
 
    };
}
 
#endif