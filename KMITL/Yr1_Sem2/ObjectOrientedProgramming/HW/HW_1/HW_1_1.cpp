#include <iostream>
#include <string>
using std::cout, std::cin, std::endl, std::string;

void addChar(int amt, string str){
    for(int i = 0; i < amt; i++){
        cout << str;
    }
}

int main(){
    string warrior;
    string mage;
    string ninja;
    string fighter;

    cout << "Enter warrior name: ";
    cin >> warrior;
    cout << "Enter mage name: ";
    cin >> mage;
    cout << "Enter ninja name: ";
    cin >> ninja;
    cout << "Enter fighter name: ";
    cin >> fighter;
    cout << endl;

    warrior = "Warrior: " + warrior;
    mage = "Mage: " + mage;
    ninja = "Ninja: " + ninja;
    fighter = "Fighter: " + fighter;
    
    const int pad = 1;
    const string::size_type max = std::max(std::max(std::max(warrior.size(), mage.size()), ninja.size()), fighter.size());
    const string::size_type col = max * 2 + pad * 4 + 2;
    const int row = pad * 4 + 5;

    for(int r = 0; r != row; r++){

        string::size_type c = 0;

        while(c <= col){

            if(r == 2){
                if(c == pad + 1){
                    cout << warrior;
                    c += warrior.size();
                    if (warrior.size() - max > 0){
                        addChar(warrior.size() - max, " ");
                        c += warrior.size() - max + 2;
                    }
                }
                else if(c == pad + 3 + max + pad){
                    cout << mage;
                    c += mage.size();
                    if (mage.size() - max > 0){
                        addChar(mage.size() - max, " ");
                        c += mage.size() - max + 3;
                    }
                }
                else if(c == 0 || c == col - 1 || c == pad + 2 + max){
                    cout << "|";
                    c++;
                }
                else{
                    cout << " ";
                    c++;
                }
            }
            else if(r == 6){
                if(c == pad + 1){
                    cout << ninja;
                    c += ninja.size();
                    if (ninja.size() - max > 0){
                        addChar(ninja.size() - max, " ");
                        c += ninja.size() - max + 1;
                    }
                }
                else if(c == pad + 3 + max + pad){
                    cout << fighter;
                    c += fighter.size();
                    if (fighter.size() - max > 0){
                        addChar(fighter.size() - max, " ");
                        c += fighter.size() - max + 2;
                    }
                }
                else if(c == 0 || c == col || c == pad + 2 + max){
                    cout << "|";
                    c++;
                }
                else{
                    cout << " ";
                    c++;
                }
            }
            else if(r == 0 || r == row - 1 || c == 0 || c == col || r == 4 || c == pad + 2 + max){
                if ((c == 0 && r == 0) || (c == 0 && r == 4) || (c == 0 && r == row - 1) || (c == col && r == 0) || (c == col && r == 4) || (c == col && r == row - 1) || (c == pad + 2 + max && r == 0) || (c == pad + 2 + max && r == 4) || (c == pad + 2 + max && r == row - 1)){
                    cout << "+";
                    c++;
                }else if(c == 0 || c == col || c == pad + 2 + max){
                    cout << "|";
                    c++;
                }
                else if(r == 4){
                    cout << "-";
                    c++;
                }
                else{
                    cout << "=";
                    c++;
                }
            }
            else{
                cout << " ";
                c++;
            }
        }
        cout << endl;
    }

    return 0;
}