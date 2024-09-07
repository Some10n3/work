#include <algorithm>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <typeinfo>

using namespace std;

class SCORE{
    public:
        static double max(const vector<double>& vec){
            double max = 0;
            for (const auto& v: vec){
                if (v > max){
                    max = v;
                }
            }
            return max;
        }

        static double min(const vector<double>& vec){
            double min = 10000;
            for (const auto& v: vec){
                if (v < min){
                    min = v;
                }
            }
            return min;
        }

        static double avg(const vector<double>& vec){
            double sum = 0;
            for (const auto& v: vec){
                sum += v;
            }
            return sum / vec.size();
        }
};