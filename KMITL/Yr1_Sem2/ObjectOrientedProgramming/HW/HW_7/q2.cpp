#include <iostream>
#include <string>
#include <tuple>

struct point {
    int x;
    int y;
};

template <class T>
int sizeOfList(T* arr){
    int i = 0;
    while(*arr){
        i++;
        arr++;
    }
    return i;
}

template<class T>
point* combine(T* xList, T* yList, int size){
    point* points = new point[size];
    for (int i = 0; i < size; i++) {
        points[i].x = xList[i];
        points[i].y = yList[i];
    }
    return points;
} 

auto extract (point* p, int size){
    double* xlist = new double[size];
    double* ylist = new double[size];
    for (int i = 0; i < size; i++) {
        xlist[i] = p[i].x;
        ylist[i] = p[i].y;
    }
    return std::make_tuple(xlist, ylist);
}



int main(){
    //create xList and yList
    int xList[] = {3, 56, 7};
    int yList[] = {4235, 56, 33};
    
    int size = sizeOfList(xList);
    point* p = combine(xList, yList, 3);

    auto [xList2, yList2] = extract(p, 3);
    for (int i = 0; i < size; i++) {
        std::cout << xList2[i] << " " << yList2[i] << std::endl;
    }
    return 0;

}