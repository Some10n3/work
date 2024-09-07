#include <iostream>
#include <string>
using namespace std;

//// Program 1.2
int main2()
{
int number = 0;
float value = 0; // semicolon here
double bigNumber;
bigNumber = number + value;
cout << number << value << bigNumber << endl;
return 0;
}
//// Program 1.3
int main3()
{
int number = 0;
float value = 0;
double bigNumber;
bigNumber = number + value; // bignumber is spelled wrong
cout << number << value << bigNumber << endl;
return 0;
}
//// Program 1.4
int main4()
{
const string ERROR_MESSAGE = "bad string!"; // missing quote
cout << "Hello!\n"; //missing quote
cout << ERROR_MESSAGE << endl;
return 0;
}
//// Program 1.5
int main5()
{
float firstVal = 0;
float secondVal = 0;
float factor;
factor = 2;
float result = (firstVal - secondVal / factor); // missing ) // factor is not initialized
cout << result << endl;
return 0;
}
//// Program 1.6
int main6()
{
const double x = 2.0;
const double y = 3.1415;
double product;
//x * y = product; //wrong order
product = x * y;
cout << product << endl;
return 0;
}

//// Program 1.1
int main()
{
int number = 0;
float value = 0; // semicolon here
double bigNumber; //bigNumber is not initialized
bigNumber = 1234;
cout << number << endl; 
cout << value << endl;
cout << bigNumber << endl;
main2();
main3();
main4();
main5();
main6();
return 0;
}