#include "MyTestLibA.h"
#include "MyTestLibB.h"
#include <iostream>

namespace MyTestLibA
{
Printer::Printer(){}
         
void Printer::print()
{
	std::cout << "MyTestLibA says hello!" << std::endl;
		
	MyTestLibB::Calculator calc;
	std::cout << "MyTestLibB::Calculator: add(4, 5)" << calc.add(4, 5) << std::endl;
}
 

}