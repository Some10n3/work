
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

class Graph {
public:
  Graph(){};
  void add_value(double d) { this->values.push_back(d); }
  void set_header(string s) { this->header = s; }

  string get_header() { return this->header; }

  vector<double> get_values() { return this->values; }

  void generatePiechart() {
    ofstream ofs("pie_chart.html");
    ofs << "<html><body><svg width='1000' height='1000'>" << endl;
    double sum = 0;
    for (int i = 0; i < values.size(); i++) {
        sum += values[i];
    }
    double start = 0;
    double end = 0;
    for (int i = 0; i < values.size(); i++) {
        double percentage = (values[i] / sum) * 100;
        end = start + (values[i] / sum) * 2 * M_PI;
        ofs << "<path d='M 500 500 L " << 500 + 500 * cos(start) << " " << 500 + 500 * sin(start) << " A 500 500 0 0 1 "
            << 500 + 500 * cos(end) << " " << 500 + 500 * sin(end) << " Z' style='fill:rgb(" << rand() % 255 + 1 << ","
            << rand() % 255 + 1 << "," << rand() % 255 + 1
            << ");stroke-width:3;stroke:rgb(0,0,0)'/>" << endl;
        double middle = start + (end - start) / 2;
        ofs << "<text x='" << 500 + 400 * cos(middle) << "' y='" << 500 + 400 * sin(middle) << "' fill='black' font-size='20' text-anchor='middle' style='dominant-baseline: middle' >" << percentage << "%</text>"<<endl;
        start = end;
    }
    ofs << "</svg></body></html>" << endl;
}

  void generateBarChart() {
    std::ofstream outputFile("bar_chart.html");
    if (!outputFile.is_open()) {
      std::cout << "Failed to create the HTML file." << std::endl;
      return;
    }

    int numBars = this->values.size();
    double maxnum = 0;
    for (int i = 0; i < numBars; ++i) {
        if (this->values[i] > maxnum) {
            maxnum = this->values[i];
        }  
    }

    outputFile << "<!DOCTYPE html>\n";
    outputFile << "<html>\n";
    outputFile << "<head>\n";
    outputFile << "<header style=\"text-align:center\">" <<this->header<< "</header>\n";
    outputFile << "<title>Bar Chart</title>\n";
    outputFile << "<style>\n";
    outputFile << "#chart {\n";
    outputFile << "background-color: #f1f1;\n";
    outputFile << "width: " << (numBars * 80) << "px;\n";
    outputFile << "height: " <<(maxnum * 30) << "px;\n";
    outputFile << "margin: 30px auto;\n";
    outputFile << "padding: 20px;\n";
    outputFile << "box-sizing: border-box;\n";
    outputFile << "border-radius: 5px;\n";
    outputFile << "}\n";
    outputFile << "#chart .bar {\n";
    outputFile << "width: 45px;\n";
    outputFile << "margin-right: 20px;\n";
    outputFile << "display: inline-block;\n";
    outputFile << "background-color: #0099ff;\n";
    outputFile << "border-radius: 5px 5px 0 0;\n";
    outputFile << "transition: height 1s ease;\n";
    outputFile << "}\n";
    outputFile << "#chart .bar-label {\n";
    outputFile << "display: inline-block;\n";
    outputFile << "margin-top: 10px;\n";
    outputFile << "font-size: 16px;\n";
    outputFile << "font-weight: bold;\n";
    outputFile << "text-align: center;\n";
    outputFile << "width: 60px;\n";
    outputFile << "}\n";
    outputFile << "#chart.loaded";

    for (int i = 0; i < numBars; ++i) {
      outputFile << " .bar:nth-child(" << (i + 1) << ") {\n";
      outputFile << "height: " << this->values[i] * 20<< "px;\n";
      outputFile << "}\n";
    }

    outputFile << "</style>\n";
    outputFile << "</head>\n";
    outputFile << "<body>\n";
    outputFile << "<div id=\"chart\">\n";

    for (int i = 0; i < numBars; ++i) {
      outputFile << "<div class=\"bar\"></div>\n";
    }

    for (int i = 0; i < numBars; ++i) {
      outputFile << "<div class=\"bar-label\">" << this->values[i]
                 << "</div>\n";
    }

    outputFile << "</div>\n";
    outputFile << "<script>\n";
    outputFile << "window.addEventListener('load', function() {\n";
    outputFile << "document.getElementById('chart').classList.add('loaded');\n";
    outputFile << "});\n";
    outputFile << "</script>\n";
    outputFile << "</body>\n";
    outputFile << "</html>\n";

    outputFile.close();
    std::cout << "HTML file generated successfully." << std::endl;
  }

private:
  vector<double> values;
  string header;
};

void test_case(Graph& g1){
  vector<double> d1 = {20,12,13,14,30,35};
  assert(g1.get_values()  == d1);
  cout << "READ FROM TEXT: PASSED" << endl;
  assert(g1.get_header() == "My Graph");
  cout << "HEADER: PASSED" << endl;
   
};

void readfile(ifstream& file, Graph& g1){
  int NumberOfData;
  string line;
  getline(file, line);

  stringstream ss;
  ss.str(line);
  ss >> NumberOfData;
  

  double temp;
  while (getline(file, line)) {
    temp = stod(line);
    cout << temp << endl;
    g1.add_value(temp);
  }
}

int main() {
  
  std::ifstream file("value.txt");
  
  Graph g1;
  g1.set_header("My Graph");
  readfile(file, g1);

  test_case(g1);

  g1.generatePiechart();
  g1.generateBarChart();

  return 0;
}
