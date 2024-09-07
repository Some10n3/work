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

    cout << "Min Score" << endl;

    vector<double> minScore;
    for (const auto& h: scoreD){
        minScore.push_back(SCORE::min(h));
    }

    vector<Scores> minScoreRank;
    for (int i = 0; i < minScore.size(); i++){
        minScoreRank.push_back(Scores{minScore[i], scoreN[i]});
    }

    std::stable_sort(minScoreRank.begin(), minScoreRank.end(), [](Scores a, Scores b){
        return a.score > b.score;
    });

    for (const auto& h: minScoreRank){
        cout << h.name << ": " << h.score << endl;
    }

    cout << endl;
    cout << "Average Score" << endl;

    std::vector<double> averageScore;
    for (const auto& h: scoreD){
        averageScore.push_back(SCORE::avg(h));
    }
    std::vector<Scores> averageScoreRank;
    for (int i = 0; i < averageScore.size(); i++){
        averageScoreRank.push_back(Scores{averageScore[i], scoreN[i]});
    }
    std::stable_sort(averageScoreRank.begin(), averageScoreRank.end(), [](Scores a, Scores b){
        return a.score > b.score;
    });
    for (const auto& h: averageScoreRank){
        cout << h.name << ": " << h.score << endl;
    }

    return 0;
   
}