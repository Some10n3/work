#include "q3.hpp"

using std::cout; using std::cin; using std::endl; using std::sort; using std::vector; using std::list; using std::copy; using std::string; using std::istream;

int main(){
    vector<string> head_tag{
        "<body>",
        "<svg width='500' height='500' xmlns='http://www.w3.org/2000/svg'>>",
        "<rect width='100%' height='100%' fill='#EEEEEE' />",
        "<circle cx='250' cy='250' r='250' stroke='black' stroke-width='2' fill='none' />",
        "<circle cx='250' cy='250' r='10' fill='#00FFFF' />",    
    };
    vector<string> tail_tag{
        "</svg>",
        "</body>",
    };

    cout << "Enter the N value: ";
    int N; cin >> N;

    std::mt19937 rng;
    rng.seed(std::random_device()());
    std::uniform_real_distribution<double> dist{-1, 1};
    std::ofstream out("svg.html");
    std::streambuf *coutbuf = std::cout.rdbuf();
    std::cout.rdbuf(out.rdbuf());

    double cenx = 250;
    double ceny = 250;

    SVG::printWords(cout, head_tag);
    for (int i = 0; i < N; i++){
        double distance;
        double cx;
        double cy;
        cx = SVG::map(dist(rng), -1, 1, 0, 500);
        cy = SVG::map(dist(rng), -1, 1, 0, 500);
        distance = sqrt(pow(cx - cenx, 2) + pow(cy - ceny, 2));
        while (distance > 250){
            cx = SVG::map(dist(rng), -1, 1, 0, 500);
            cy = SVG::map(dist(rng), -1, 1, 0, 500);
            distance = sqrt(pow(cx - cenx, 2) + pow(cy - ceny, 2));
        }
        cout << "<circle cx='" << cx << "' cy='" << cy << "' r='10' fill='" + SVG::hexRandomColor() + "' />" << endl;
    }
    SVG::printWords(cout, tail_tag);
    
    return 0;
}