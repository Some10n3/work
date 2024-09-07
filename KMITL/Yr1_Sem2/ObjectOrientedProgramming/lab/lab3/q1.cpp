#include <iostream>
#include <vector>
#include <list>

using std::vector;
using std::list;

vector<double> lshift(vector<double>& v, int n){
    vector<double> outPut;
    for (int i = 0; i < v.size(); i++){
        if(i > n - 1){
            outPut.push_back(v[i]);
        }
    }
    return outPut;
}

vector<double> rshift(vector<double>& v, int n){
    vector<double> outPut;
    for (int i = 0; i < n; i++){
        outPut.push_back(0);   
    }
    for (int i = 0; i < v.size(); i++){
        outPut.push_back(v[i]);
    }
    return outPut;
}

vector<double> remove_negative(vector<double>& v){
    vector<double> outPut;
    for (int i = 0; i < v.size(); i++){
        if(v[i] > 0){
            outPut.push_back(v[i]);
        }
    }
    return outPut;
}

vector<double> scale(vector<double>& v, auto n){
    vector<double> outPut;
    for (int i = 0; i < v.size(); i++){
        outPut.push_back(v[i] * n);
    }
    return outPut;
}

vector<double> add(vector<double>& v1, vector<double>& v2){
    vector<double> outPut;
    for (int i = 0; i < v1.size(); i++){
        outPut.push_back(v1[i] + v2[i]);
    }
    return outPut;
}

list<double> remove_negative_list(list<double>& v){
    list<double> outPut;
    for (double x : v){
        if(x > 0){
            outPut.push_back(x);
        }
    }
    return outPut;
}

int main(){
    vector<double> v = {2, 1, 4, 3, 7};
    vector<double> v2 = {0.8, -5.1, 1.6, -6.5, 10.5};
    vector<double> v3 = {1, 3, 2, 5};
    list<double> l = {0.8, -5.1, 1.6, -6.5, 10.5};

    //lshift
    std::cout << "lshift" << std::endl;
    vector<double> outPut = lshift(v, 3);
    for(double x : outPut){
        std::cout << x << " ";
    }
    std::cout << std::endl << std::endl;

    //rshift
    std::cout << "rshift" << std::endl;
    outPut = rshift(outPut, 2);
    for(double x : outPut){
        std::cout << x << " ";
    }
    std::cout << std::endl << std::endl;

    //remove_negative
    std::cout << "remove_negative" << std::endl;
    outPut = remove_negative(v2);
    for(double x : outPut){
        std::cout << x << " ";
    }
    std::cout << std::endl << std::endl;

    //scale
    std::cout << "scale" << std::endl;
    outPut = scale(v, 2);
    for(double x : outPut){
        std::cout << x << " ";
    }
    std::cout << std::endl << std::endl;

    //add
    std::cout << "add" << std::endl;
    outPut = add(v, v3);
    for(double x : outPut){
        std::cout << x << " ";
    }
    std::cout << std::endl << std::endl;

    //remove_negative_list
    std::cout << "remove_negative_list" << std::endl;
    list<double> outPut2 = remove_negative_list(l);
    for(double x : outPut2){
        std::cout << x << " ";
    }
    std::cout << std::endl << std::endl;

    return 0;
}