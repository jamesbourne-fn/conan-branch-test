#include <iostream>
#include "MyTestLibB.h"

int main() 
{
    MyTestLibB::Calculator calc;
	
	std::cout << "MyTestLibB::Calculator: add(4, 5)=" << calc.add(4, 5) << std::endl;
}
