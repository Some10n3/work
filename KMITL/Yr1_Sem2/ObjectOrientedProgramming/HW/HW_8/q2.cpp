#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Text_base{
    public:
        Text_base(string str, string open):Text_base(str){
            this->opening = open;
        }
        Text_base(string str){this->texts = str;};
        virtual string text() const{
            return texts;
        }

        Text_base& operator=(const Text_base& rhs){
            this->texts = rhs.texts;
            return *this;
        }

    protected:
        string texts;
        string opening;
};

class Quoted_text : public Text_base{
    public:
        Quoted_text(string str, string open):Text_base(str){
            this->opening = open;
            this->closing = open;
        }
        Quoted_text(string str, string open, string close):Text_base(str){
            this->opening = open;
            this->closing = close;
        }
        string text() const override{
            return opening + texts + closing;
        }

    private:
        string opening;
        string closing;

};

class Crypted_text : public Text_base{
    public:
        Crypted_text(string str):Text_base(str){};
        char invert_char(char c) const
        {
            char x = c;
            if (x >= 'a' && x <= 'z')
                return char('a' -x + 'z');
            if (x >= 'A' && x <= 'Z')
                return char('A' -x + 'Z');

            return x;
        }

        string invert_string(string str) const
        {
            string str2 = str;
            for (auto& c: str2)
                c = invert_char(c);
            return str2;
        }

        string text() const override{
            return invert_string(this->texts);
        }
};

class Text{
    public:
        Text(Text_base* t):texts(t){};
        Text(string str, string open):Text(new Quoted_text(str, open)){};
        Text(string str, string open, string close):Text(new Quoted_text(str, open, close)){};
        Text(string str):Text(new Crypted_text(str)){};

        string text() const{
            return texts->text();
        }
        Text& operator=(const Text& rhs){
            this->texts = rhs.texts;
            return *this;
        }
    private:
        Text_base* texts;
};




int main(){
    Text_base q0("Python", "*"); 
    auto text = q0.text(); // "Python"
    cout << text << endl;
    Quoted_text q("Python", "*"); 
    const Text_base& rq = q; 
    text = q.text(); // "*Python*" 
    cout << text << endl;
    text = rq.text(); // "*Python*"
    cout << text << endl;
    q = Quoted_text("Python", "<em>", "</em>"); 
    text = q.text(); // "<em>Python</em>" 
    cout << text << endl;
    text = rq.text(); // "<em>Python</em>"
    cout << text << endl;
    Crypted_text ct("Abc101"); 
    const Text_base& rct = ct; 
    text = ct.text(); // "Zyx101" 
    cout << text << endl;
    text = rct.text(); // "Zyx101"
    cout << text << endl;
    ct = Crypted_text{"PYthoN101"};
    text = ct.text();    // "KBgslM101" 
    cout << text << endl;
    text = rct.text();// "KBgslM101"
    cout << text << endl;

    vector<Text> words{ 
        Text("C++", "<i>", "</i>"), 
        Text("Zidane"),
        Text("Rust", "*"),
        Text("Python", "[[", "]]"), 
        Text("Vivi")
    };
    for (const auto& w: words) { 
        std::cout << w.text() << std::endl;
    }

}