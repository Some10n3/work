#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <ostream>

using std::cin; using std::cout; using std::endl; using std::string; using std::vector; using std::pair;

struct Point{
    double x;
    double y;
};

class PolyLine{
    public:
        PolyLine(vector<Point> points){
            this->points = points;
        }

        vector<Point> getPoints(){
            return points;
        }

    private:
        vector<Point> points;
};

void print(Point segs, std::ostream os){
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
    <polyline fill="none" stroke="black"
    points="10, 10 190, 20 180, 180 80, 110 10, 10"
    />
    </svg>
}