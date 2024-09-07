#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

istream& read_input(istream& in, vector<string>& vec){

    if (in){
        vec.clear();

        string x;
        while (in >> x){
            vec.push_back(x);
        }
    }
    return in;
}



enum class genre {fiction, nonfiction, periodical, biography, children};

class book{
    public: 
        string isbn;
        string title;
        string author;
        string year;
        bool checked;
        genre genre;

    book(string isbn, string title, string author, string year, enum genre genre){
        this->isbn = isbn;
        this->title = title;
        this->author = author;
        this->year = year;
        this->checked = false;
        this->genre = genre;
    }

    string get_isbn(){
        return isbn;
    }

    string get_title(){
        return title;
    }

    string get_author(){
        return author;
    }

    string get_year(){
        return year;
    }
    
    void checked_in(){
        this->checked = true;
    }

    void checked_out(){
        this->checked = false;
    }

    bool is_checked(){
        return (this->checked ? "true" : "false");
    }

    bool compare(book book1){
        if (this->isbn == book1.isbn){
            return true;
        }
        else{
            return false;
        }
    }   

    string get_genre(){
        switch (this->genre){
            case genre::fiction:
                return "fiction";
            case genre::nonfiction:
                return "nonfiction";
            case genre::periodical:
                return "periodical";
            case genre::biography:
                return "biography";
            case genre::children:
                return "children";
        }
    }

    string print_book(){
        return "ISBN: " + this->isbn + "\nTitle: " + this->title + "\nAuthor: " + this->author + "\nYear: " + this->year + "\nGenre: " + get_genre() + "\nChecked: " + (this->checked ? "true" : "false");
    }
};

int main(){
    string isbn;
    
    cout << "Enter the line in order (ISBN , Title , Author , Copyright year , Genre) then Find ISBN" << endl;
    vector<string> inp;
    string line;

    while(std::getline(cin , line)){
        if (line.empty()){
            break;
        }
        inp.push_back(line);
    }
    isbn = inp[5];
    
    
    book book4 = book(inp[0], inp[1], inp[2], inp[3], (inp[4] == "fiction" ? genre::fiction : (inp[4] == "nonfiction" ? genre::nonfiction : (inp[4] == "periodical" ? genre::periodical : (inp[4] == "biography" ? genre::biography : genre::children)))));    
    book book1 = book("123B", "The Hobbit", "J.R.R. Tolkien", "1937" , genre::fiction);
    book book2 = book("123B", "The Lord of the Rings", "J.R.R. Tolkien", "1954" , genre::nonfiction);
    book book3 = book("789D", "The Silmarillion", "J.R.R. Tolkien", "1977" , genre::periodical);
    
    cout << endl;
    cout << book1.get_isbn() << book1.get_title() << book1.get_author() << book1.get_year() << endl;
    cout << "compare book1 and book2: \n";
    cout << book1.compare(book2) << endl;
    cout << "\nprint_book function: \n";
    cout << book1.print_book() << endl << endl;
    cout << book4.print_book() << endl << endl;

    book2.checked_in();
    cout << "book2 is availble: " << book2.is_checked() << endl << endl;


    vector<book> books = {book1 , book2 , book3, book4};

    bool founnd = false;
    for (auto& book : books){
        if (book.get_isbn() == isbn){
            cout << book.print_book() << endl;
            founnd = true;
            break;
        }
    }
    if (!founnd){
        cout << "Book not found" << endl;
    }

    
    return 0;
}
