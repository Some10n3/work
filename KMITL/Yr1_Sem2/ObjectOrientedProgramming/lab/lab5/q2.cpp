#include <iostream>
#include <string>
#include <vector>

using std::cout; using std::endl; using std::string; using std::cin; using std::vector;

class Picture {
    public:
        Picture(vector<string> lines) {
            this->lines = lines;
            this->height = lines.size();
            this->width = lines[0].size();
        }
        Picture(int height, int width) {
            this->height = height;
            this->width = width;
        }
        vector<string> getLines() {
            return lines;
        }
        int getHeight() {
            return height;
        }
        int getWidth() {
            return width;
        }
        void setLines(vector<string> lines) {
            this->lines = lines;
        }
        void addLine(string line) {
            lines.push_back(line);
        }
        void removeLine(int index) {
            lines.erase(lines.begin() + index);
        }
        void setHeight(int height) {
            this->height = height;
        }
        void setWidth(int width) {
            this->width = width;
        }
        void hflip() {
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width / 2; j++) {
                    char temp = lines[i][j];
                    lines[i][j] = lines[i][width - j - 1];
                    lines[i][width - j - 1] = temp;
                }
            }
        }
        void vflip() {
            for (int i = 0; i < height / 2; i++) {
                string temp = lines[i];
                lines[i] = lines[height - i - 1];
                lines[height - i - 1] = temp;
            }
        }
        void hcat(Picture p) {
            for (int i = 0; i < height; i++) {
                lines[i] += p.getLines()[i];
            }
            width += p.getWidth();
        }
        void vcat(Picture p) {
            for (int i = 0; i < p.getHeight(); i++) {
                lines.push_back(p.getLines()[i]);
            }
            height += p.getHeight();
        }
        void resize(int height, int width) {
            this->height = height;
            this->width = width;
            if (this -> height > height) {
                for (int i = 0; i < this->height - height; i++) {
                    removeLine(this->height - i - 1);
                }
            }
            else if (this->height < height) {
                for (int i = 0; i < height - this->height; i++) {
                    addLine("");
                }
            }
            if (this->width > width) {
                for (int i = 0; i < this->height; i++) {
                    for (int j = 0; j < this->width - width; j++) {
                        lines[i].pop_back();
                    }
                }
            }
            else if (this->width < width) {
                for (int i = 0; i < this->height; i++) {
                    for (int j = 0; j < width - this->width; j++) {
                        lines[i] += " ";
                    }
                }
            }
        }
        void print() {
            for (int i = 0; i < height; i++) {
                cout << lines[i] << endl;
            }
        }
    private:
        vector<string> lines;
        int height;
        int width;

};


int main(){
    Picture p(3, 7);
    Picture p2(3, 7);
    p.addLine(" /\\_/\\"); p2.addLine(" /\\_/\\");
    p.addLine("( o.o )"); p2.addLine("( o.o )");
    p.addLine(" > ^ <"); p2.addLine(" > ^ <");
    cout << "p:" << endl; p.print(); cout << endl;
    cout << "p2:" << endl;
    p2.print(); cout << endl;
    cout << "hflip:" << endl;
    p.hflip();
    p.print(); cout << endl;
    cout << "vflip:" << endl;
    p.vflip();
    p.print(); cout << endl;
    cout << "hcat:" << endl;
    p.hcat(p2);
    p.print(); cout << endl;
    cout << "vcat:" << endl;
    p.vcat(p2);
    p.print(); cout << endl;
    cout << "resize:" << endl;
    p.resize(5, 5);
    p.print(); cout << endl;

    return 0;
}