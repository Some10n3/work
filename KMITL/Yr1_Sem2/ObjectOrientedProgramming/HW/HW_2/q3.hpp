#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <istream>
#include <random>
#include <fstream>
#include <sstream>

using std::cout; using std::cin; using std::endl; using std::sort; using std::vector; using std::list; using std::copy; using std::string; using std::istream;

class SVG{
    public:
        static void printWords(std::ostream& out, const vector<string>& words){
            for (const auto& w: words){
                out << w << endl;
            }
        }
        static double map(double x, double inMin, double inMax, double outMin, double outMax){
            return (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
        }   

        static string hexRandomColor(){
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<> dis(0, 255);
            std::string hex = "#";
            for (int i = 0; i < 3; i++){
                std::stringstream ss;
                ss << std::hex << dis(gen);
                std::string result(ss.str());
                if (result.size() == 1){
                    result = "0" + result;
                }
                hex += result;
            }
            return hex;
        }     
    };