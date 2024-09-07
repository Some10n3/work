#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Writer;
class Doc_element
{
public:
    explicit Doc_element(const std::string& n) : s(n) {};
    Doc_element(const string& n, const vector<Doc_element>& children);
    static Doc_element text(const std::string& t) {
        return Doc_element(t);
    }
    void write_document(const Writer& w) const;
    void write_to(const Writer& w, int lv) const;

private:
    string s;
    vector<Doc_element> v;
    string tag;
};

class Writer {
public:
    void start_document() const {
        cout << "<!DOCTYPE html>\n<html>\n";
    }

    void end_document() const {
        cout << "</html>\n";
    }

    void start_tag(const string& tag_name) const {
        cout << "<" << tag_name << ">";
    }

    void end_tag(const string& tag_name) const {
    cout << "</" << tag_name << ">";
}
    void write_text(const string& text) const {
        cout << text;
    }

    void write_newline() const {
        cout << "\n";
    }

    void write_indent(int lv) const {
        for (int i = 0; i < lv; ++i) {
            cout << "  ";
        }
    }
};

void Doc_element::write_document(const Writer& w) const {
    w.start_document();
    write_to(w, 0);
    w.end_document();
}

void Doc_element::write_to(const Writer& w, int lv) const {
    w.write_indent(lv);
    if (!tag.empty()) {
        w.start_tag(tag);
        for (const auto& child : v) {
            w.write_newline();
            child.write_to(w, lv + 1);
        }
        w.write_newline();
        w.write_indent(lv);
        w.end_tag(tag);
    } else {
        w.write_text(s);
    }
}

Doc_element::Doc_element(const std::string& n, const std::vector<Doc_element>& children) : tag(n), v(children) {};

int main(){
    auto t = Doc_element::text("Text001");
    auto e = Doc_element("em", {t, Doc_element("p", {t})});

    auto tr = Doc_element(
        "tr",
        {Doc_element("td", {t}), Doc_element("td", {t}),
         Doc_element("td", {t})});
    auto tbl = Doc_element("table", {tr, tr, tr});

    auto t2 = Doc_element::text("Software Engineering");
    auto tr2 = Doc_element(
        "tr",
        {Doc_element("td", {Doc_element::text("SE")}), Doc_element("td", {Doc_element::text("14")})});
    auto tbl2 = Doc_element("table", {tr2});

    Writer writer;
    tbl.write_document(writer);
    e.write_document(writer);
    tbl2.write_document(writer);
    return 0;   
}