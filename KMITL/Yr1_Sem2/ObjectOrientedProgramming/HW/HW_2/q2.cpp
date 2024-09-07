#include "q2.hpp"

using std::cout; using std::cin; using std::endl; using std::string; using std::istream; using std::vector;

struct Scores{
    double score;
    string name;
};

istream& read_hw(istream& in, std::vector<string>& vec){
    if (in){
        vec.clear();

        string x;
        while (in >> x){
            vec.push_back(x);
        }
    }
    return in;
}


int main(){
    vector<string> score;

    cout << "Enter the score:";
    cout << "(End the loop by pressing Ctrl+Z then Enter)";

    // reading input and storing in vector score
    read_hw(cin, score);

    // seperate the name and scores
    vector<vector<double>> scoreD;
    vector<string> scoreN;
    bool nameBool = false;
    for (const auto& h: score){
        try{
            double d = std::stod(h);
            if (nameBool){
                scoreD.push_back(std::vector<double>());
                nameBool = false;
            }
            scoreD.back().push_back(d);
        }
        catch (std::invalid_argument& e){
            scoreN.push_back(h);
            nameBool = true;
        }
    }

    cout << "Name: [";
    for (const auto& h: scoreN){
        cout << h << ", ";
    }
    cout << "]" << endl;

    cout << "Score: [";
    for (const auto& h: scoreD){
        cout << "[";
        for (const auto& i: h){
            cout << i << ", ";
        }
        cout << "], ";
    }
    cout << "]" << endl;

    cout << endl << "Max Score" << endl;
    
    vector<double> maxScore;
    for (const auto& h: scoreD){
        maxScore.push_back(SCORE::max(h));
    }
    vector<Scores> maxScoreRank;
    for (int i = 0; i < maxScore.size(); i++){
        maxScoreRank.push_back(Scores{maxScore[i], scoreN[i]});
    }
    std::stable_sort(maxScoreRank.begin(), maxScoreRank.end(), [](Scores a, Scores b){
        return a.score > b.score;
    });
    for (const auto& h: maxScoreRank){
        cout << h.name << ": " << h.score << endl;
    }

    return 0;
   
}
//Leo 5000 1200 2000 4500 Mike 3800 2400 3200 Raph 1500 2200 1200 4000 4800 Don 5000 1600 3200 4600 May 4400 3300 5800