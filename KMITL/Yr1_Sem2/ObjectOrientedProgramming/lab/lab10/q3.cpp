/*
#include <iostream>
#include <string>

using namespace std;

class raggedArray{
    // array made from with 3, 2, 4 columns and 3 rows separated with ;
    public:
        raggedArray(string array){
            int rowElements = 0;
            int rows = 1;
            bool valid = true;
            //check if array is valid
            for (int i = 0; i < array.length(); i++){
                cout << rowElements << endl;
                if (array[i] != ','){
                    rowElements++;
                }
                switch (rows)
                {
                case 1:
                    if (rowElements > 3){
                        cout << "Invalid array" << endl;
                        valid = false;
                        break;
                    }
                    break;
                case 2:
                    if (rowElements > 2){
                        cout << "Invalid array" << endl;
                        valid = false;
                        break;
                    }
                    break;
                case 3:
                    if (rowElements > 4){
                        cout << "Invalid array" << endl;
                        valid = false;
                        break;
                    }
                    break;
                default:
                    break;
                }
                if (array[i] == ';'){
                    rows++;
                    rowElements = 0;
                }
            }
            if (valid){
                this->array = array;
            } 
        }
        void print(){
            cout << array << endl;
        }
    string array;
};

int main(){
    raggedArray array("1,2,3;4,5;6,7,8,9");
    array.print();

    
    return 0;
}
*/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class RaggedArray {
public:
    RaggedArray(string input) {
        parseInput(input);
    }

    string toString() {
        string result = "Array(";
        for (int i = 0; i < rows.size(); i++) {
            result += "[";
            for (int j = 0; j < rows[i].size(); j++) {
                result += to_string(rows[i][j]);
                if (j < rows[i].size() - 1) {
                    result += ", ";
                }
            }
            result += "]";
            if (i < rows.size() - 1) {
                result += ", ";
            }
        }
        result += ")";
        return result;
    }

private:
    vector<vector<int>> rows;

    void parseInput(string input) {
        int i = 1;
        while (i < input.length() - 1) {
            int j = i;
            while (input[j] != ';' && input[j] != ']') {
                j++;
            }
            string rowString = input.substr(i, j - i);
            vector<int> row;
            int k = 0;
            while (k < rowString.length()) {
                if (isdigit(rowString[k])) {
                    int number = rowString[k] - '0';
                    k++;
                    while (isdigit(rowString[k])) {
                        number = number * 10 + (rowString[k] - '0');
                        k++;
                    }
                    row.push_back(number);
                } else {
                    k++;
                }
            }
            rows.push_back(row);
            i = j + 1;
        }
    }
};

int main() {
    string input;
    cout << "Enter ragged array: ";
    getline(cin, input);
    RaggedArray arr = RaggedArray(input);
    cout << arr.toString() << endl;
    return 0;
}