#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using std::cin; using std::cout; using std::endl; using std::string; using std::vector;

class Picture{
    public:
        vector<string> pic;
        int width;
        int height = pic.size();

        Picture(vector<string> pic){
            this->pic = pic;
            this->width = 0;
            for(auto& x : pic){
                if(x.size() > this->width){
                    this->width = x.size();
                }
            }
            this->height = pic.size();
        }

        int get_width(){
            return width;
        }

        int get_height(){
            return height;
        }

        auto getdata(){
            return pic;
        }

        Picture hcat(Picture& p){
            for(auto& x : pic){
                if(x.size() < width){
                    x.insert(x.end(), width - x.size(), '`');
                }
            }
            vector<string> newPic;
            std::copy(pic.begin(), pic.end(), std::back_inserter(newPic));
            vector<string> p2 = p.getdata(); 
            for(auto& x : p2){
                if(x.size() < width){
                    x.insert(x.end(), width - x.size(), '`');
                }
            }
            for (auto& h: p2){
                newPic.push_back(h);
            }
            return Picture(newPic);
        }

        Picture vcat(Picture& p){
            for(auto& x : pic){
                if(x.size() < width){
                    x.insert(x.end(), width - x.size(), '`');
                }
            }
            vector<string> newPic;
            std::copy(pic.begin(), pic.end(), std::back_inserter(newPic));
            vector<string> p2 = p.getdata(); 
            if (p2.size() - height > 0){
                for (int i = 0; i < p2.size() - height; i++){
                    newPic.push_back(string(width, '`'));
                }
            }
            else if (p2.size() - height < 0){
                for (int i = 0; i < height - p2.size(); i++){
                    p2.push_back(string(width, '`'));
                }
            }
            for (int i = 0; i < p2.size(); i++){
                newPic[i] += p2[i];
            }
            return Picture(newPic);
        }

        void resize(double newHeight, double newWidth){
            if(newHeight < height){
                pic.resize(newHeight);
            }
            else if (newHeight > height){
                for (int i = 0; i < newHeight - height; i++){
                    pic.push_back(string(width, '`'));
                }
            }

            if(newWidth < width){
                for (auto& x : pic){
                    x.resize(newWidth);
                }
            }
            else if (newWidth > width){
                for (auto& x : pic){
                    x.insert(x.end(), newWidth - x.size(), '`');
                }
            }
        }

        void print(){
            cout << endl;
            cout << endl;
            for (auto& h: pic){
                cout << h << endl;
            }
        }
};

int main(){
    vector<string> pic = {
      "—–-—▒▒▒▒▒▒▒▒▒▒",
"—–-▒███████████▒",
"—▒████▒▒▒▒▒▒▒███▒",
"-▒████▒▒▒▒▒▒▒▒▒███▒……………….▒▒▒▒▒▒",
"-▒███▒▒▒▒▒███▒▒▒███▒…………..▒██████▒",
"-▒███▒▒▒▒██████▒▒███▒……….▒██▒▒▒▒██▒",
"—▒███▒▒▒███████▒▒██▒…….▒███▒▒█▒▒██▒",
"—–▒███▒▒████████▒██▒…▒███▒▒███▒▒██▒",
"——–▒██▒▒██████████▒▒███▒▒████▒▒██▒",
"———▒██▒▒██████████████▒████▒▒██▒",
"———-▒██▒▒█████████████████▒▒██▒",
"————▒██▒▒██████████████▒▒██▒",
"————–▒██▒▒████████████▒▒██▒",
"—————-▒██▒▒██████████▒▒██▒",
"—————–▒██▒▒████████▒▒██▒",
"——————-▒██▒▒██████▒▒██▒",
"———————▒██▒▒████▒▒██▒",
"———————-▒██▒▒███▒▒█▒",
"————————▒██▒▒█▒▒█▒",
"————————-▒██▒▒▒█▒",
"—————————▒██▒█▒",
"—————————♥♥♥♥♥♥",
"—————————-♥♥♥♥♥",
"——————————♥♥♥",
"—————————-—♥♥",
"———————————♥",
    };

    vector<string> pic2 = {
"        ┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌",
"┌┘┌┘┌█████┌┘█████┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘",
"┘┌┘┌██████████████┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌",
"┌┘┌████┘┌████┘┌┘███┘┌┘┌┘┌┘┌┘┌┘███████┘┌┘",
"┘┌┘███┘┌┘┌██┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘████████┌┘┌",
"┌┘┌██┘┌┘┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌┘┌┘┌┘█████┘┌┘",
"┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌┘┌┘┌┘███┘██┌┘┌",
"┌┘┌██┘┌┘┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘███┘┌██┘┌┘",
"┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘███┘┌┘┌┘┌┘┌┘███┘┌┘┘┌┌┘┌",
"┌┘┌███┌┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌┘┌┘███┘┌┘┌┘┌┘┌┘",
"┘┌┘┌██┘┌┘┌┘┌┘┌┘┌███┌███┌┘┌┘███┘┌┘┌┘┌┘┌┘┌",
"┌┘┌┘███┘┌┘┌┘┌┘┌███┘█████┌┘█████┘┌┘┌┘┌┘┌┘",
"┘┌┘┌┘███┘┌┘┌┘┌███┌███┌█████┌┘███┘┌┘┌┘┌┘┌",
"┌┘┌┘┌┘███┘┌┘┌███┌██┘┌┘┌███┌┘┌┘██┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘███┘┌███┌┘██┌┘┌┘┌█┌┘┌┘┌███┌┘┌┘┌┘┌",
"┌┘┌┘┌┘┌┘██████┌┘██┌┘┌┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌███┌┘┌██┘┌┘┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌┘┌",
"┌┘┌┘┌┘┌┘┌┘██┌┘┌┘██┌┘┌┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘┌███┌┘┌┘┌┘┌",
"┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌██┘┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌██┘┌┘┌┘┌┘┌┘███┘┌┘┌┘┌┘┌",
"┌┘┌┘┌┘██████████┌┘███┘┌┘┌┘┌┘███┘┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌██████████┘┌┘███┘┌┘┌┘███┘┌┘┌┘┌┘┌┘┌",
"┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌┘┌┘███┘┌┘███┘┌┘┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌┘┌┘███┘███┘┌┘┌┘┌┘┌┘┌┘┌",
"┌┘┌┘┌┘┌┘┌┘██┌┘┌┘┌┘┌┘┌┘█████┘┌┘┌┘┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌██┘┌┘┌┘┌┘┌┘┌┘███┘┌┘┌┘┌┘┌┘┌┘┌┘┌",
"┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘",
"┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌",
    };

    Picture p1 = Picture(pic);
    Picture p2 = Picture(pic2);

    Picture p3 = p2.hcat(p1);
    p3.print();

    Picture p4 = p1.vcat(p2);
    p4.print();

    p4.resize(20, 60);
    p4.print();

    p1.resize(20, 60);
    p1.print();

    return 0;
}