#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;
using std::string;

  
vector<string> splitString(const string& str)
{
    vector<string> tokens;
 
    std::stringstream ss(str);
    string token;
    while (std::getline(ss, token, '\n')) {
        tokens.push_back(token);
    }
 
    return tokens;
}

void reverseStr(string& str)
{
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
        swap(str[i], str[n - i - 1]);
}

class Picture {

public:
int width;
int height;
vector<string> pic;

Picture(vector<string> pic) {
    this->pic = pic;
    this->width = pic[0].length();
    this->height = pic.size();
}

void getPic() {
    for (int i = 0; i < pic.size(); i++) {
        cout << pic[i] << endl;
    }
}

void hflip() {
    for (int i = 0; i < pic.size(); i++) {
        reverseStr(pic[i]);
        cout << pic[i] << endl;
    }
}

void vflip() {
    reverse(pic.begin(), pic.end());
    for (int i = 0; i < pic.size(); i++) {
        cout << pic[i] << endl;
    }
}

void hcat(Picture p) {
    for (int i = 0; i < pic.size(); i++) {
        pic[i] += p.pic[i];
        cout << pic[i] << endl;
    }
}

void vcat(Picture p) {
    for (int i = 0; i < pic.size(); i++) {
        cout << pic[i] << endl;
    }
    for (int i = 0; i < p.pic.size(); i++) {
        cout << p.pic[i] << endl;
    }
}

void resize(int w , int h){
        if(w > width){
            for(auto& x : pic){
                x += string(w - x.size(), '.');
            }
        }
        else{
            for(auto& x : pic){
                x = x.substr(0, w);
            }
        }
        if(h > height){
            for(int i = 0; i < h - height; i++){
                pic.push_back(string(w, '.'));
            }

        }
        else{
            pic = vector<string>(pic.begin(), pic.begin() + h);
        }
        width = w;
        height = h;
    }

};



int main() {
    vector<string> pic ={

    
    "_____/XXXXXXXXX________/XXXXXXXXXXX__________/XXXXXXXXX__/XXXXXXXXXXX__/XXXXXXXXXXX_________",
    "____/XXXXXXXXXXXXX____/XXX/////////XXX_____/XXX////////__X/////XXX///__X/////XXX///_________",
    "____/XXX/////////XXX__X//XXX______X///____/XXX/_______________X/XXX_________X/XXX___________",
    "____X/XXX_______X/XXX___X////XXX__________/XXX_________________X/XXX_________X/XXX__________",
    "_____X/XXXXXXXXXXXXXXX______X////XXX______X/XXX_________________X/XXX_________X/XXX_________",
    "______X/XXX/////////XXX_________X////XXX___X//XXX________________X/XXX_________X/XXX________",
    "_______X/XXX_______X/XXX__/XXX______X//XXX___X///XXX______________X/XXX_________X/XXX_______",
    "________X/XXX_______X/XXX_X///XXXXXXXXXXX/______X////XXXXXXXXX__/XXXXXXXXXXX__/XXXXXXXXXXX__",
    "_________X///________X///____X///////////___________X/////////__X///////////__X///////////__", 
    };

    vector<string> pic2 = {
        "XXXXXXXXXXXX_______________________",
        "X//////////X_______________________",
        "X_________X________________________",
        "X_________X________________________",
        "X_________X________________________",
        "X_________X________________________",
        "X_________X________________________",
        "X_________X________________________",
        };



Picture p1(pic);
Picture p2(pic2);



// p1.resize(100,100);


ofstream MyFile("lab5-3.svg");

     
MyFile << "<svg width=\"100\" height=\"100\" xmlns=\"http://www.w3.org/2000/svg\">\n";
    MyFile << "<rect width=\"100\" height=\"100\" fill=\"white\" />\n";
    for (int i = 0; i < p1.pic.size(); i++) {
        for (int j = 0; j < p1.pic[i].length(); j++) {
            if (p1.pic[i][j] == '_') {
                MyFile << "<rect x=\"_" << j << "\" y=\"" << i << "\" width=\"5\" height=\"5\" fill=\"grey\" />\n";
            }
            else if (p1.pic[i][j] == '/') {
                MyFile << "<rect x=\"" << j << "\" y=\"" << i << "\" width=\"5\" height=\"5\" fill=\"yellow\" />\n";
            }
            else if (p1.pic[i][j] == 'X') {
                MyFile << "<rect x=\"" << j << "\" y=\"" << i << "\" width=\"5\" height=\"5\" fill=\"red\" />\n";
            }
        }
    }

    MyFile << "</svg>";


  MyFile.close();
}