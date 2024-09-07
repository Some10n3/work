#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

enum class genre {
    fiction, 
    nonfiction, 
    periodical, 
    biography, 
    children,
    null
};

class Book{
    public: 
        string isbn;
        string title;
        string author;
        string year;
        bool checked;
        genre genre;

    Book(string isbn, string title, string author, string year, enum genre genre){
        this->isbn = isbn;
        this->title = title;
        this->author = author;
        this->year = year;
        this->checked = false;
        this->genre = genre;
    }
    string getISBN(){
        return isbn;
    }
    string getTitle(){
        return title;
    }
    string getAuthor(){
        return author;
    }
    string getYear(){
        return year;
    }

    void checkIn(){
        this->checked = true;
    }
    void checkOut(){
        this->checked = false;
    }
    bool check(){
        return (this->checked ? "true" : "false");
    }
    bool compare(Book bookX){
        if (this->isbn == bookX.isbn){
            return true;
        }
        else{
            return false;
        }
    }   

    bool compareISBN(string isbn){
        if (this->isbn == isbn){
            return true;
        }
        else{
            return false;
        }
    }

    string getGenre(){
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
        return "Null";
    }

    string printInfo(){
        return "ISBN : " + this->isbn + "\nTitle: " + this->title + "\nAuthor : " + this->author + "\nYear : " + this->year + "\nGenre : " + getGenre() + "\nChecked : " + (this->checked ? "true" : "false") + "\n\n";
    }
};

genre stringToGenre(string genre){
    if (genre == "fiction"){
        return genre::fiction;
    }
    else if (genre == "nonfiction"){
        return genre::nonfiction;
    }
    else if (genre == "periodical"){
        return genre::periodical;
    }
    else if (genre == "biography"){
        return genre::biography;
    }
    else if (genre == "children"){
        return genre::children;
    }
    else{
        return genre::null;
    }
}

Book findTitle(vector<Book> bookVec, string title){
    for (Book Book : bookVec){
        if (Book.getTitle() == title){
            return Book;
        }
    }
    return Book("Null","Null","Null","Null", genre::fiction);
}


Book findISBN(vector<Book> books, string isbn){
    for (Book Book : books){
        if (Book.compareISBN(isbn)){
            return Book;
        }
    }
    return Book("Null","Null","Null","Null", genre::fiction);
}

vector<Book> genreList(vector<Book> books, genre genre){
    vector<Book> list;
    for (Book book : books){
        if (book.genre == genre){
            list.push_back(book);
        }
    }
    return list;
}

void sortTitle(vector<Book>& books){
    for (int i = 0; i < books.size(); i++){
        for (int j = 0; j < books.size() - 1; j++){
            if (books[j].title > books[j+1].title){
                Book temp = books[j];
                books[j] = books[j+1];
                books[j+1] = temp;
            }
        }
    }
}

void sortISBN(vector<Book>& books){
    for (int i = 0; i < books.size(); i++){
        for (int j = 0; j < books.size() - 1; j++){
            if (books[j].isbn > books[j+1].isbn){
                Book temp = books[j];
                books[j] = books[j+1];
                books[j+1] = temp;
            }
        }
    }
}

int main(){
    cout << "Enter the line in order : \nThe data format will be \"<ISBN>\\n<title>\\n<author>\\n<copyright>\\n<genre>\\n\" , each consumes the whole line of text" << endl;
    vector<string> inp;
    string line;

    while(std::getline(cin , line)){
        if (line.empty()){
            break;
        }
        inp.push_back(line);
    }

    Book book1(inp[0], inp[1], inp[2], inp[3], stringToGenre(inp[4]));
    Book book2("1234567890", "The Lord of the Rings", "J.R.R. Tolkien", "1954", genre::fiction);
    Book book3("1234567891", "The Hobbit", "J.R.R. Tolkien", "1937", genre::fiction);
    Book book4("1234567892", "The Silmarillion", "J.R.R. Tolkien", "1977", genre::fiction);
    Book book5("1234567893", "The Silmarillion", "J.R.R. Tolkien", "1977", genre::children);
    Book book6("1234567894", "The Silmarillion", "J.R.R. Tolkien", "1977", genre::biography);

    vector<Book> books = {book1 , book2 , book3, book4, book5, book6};

    cout << "|-----------------------------------------------------------------------------------------------|\n\n";
    cout << "The list of books is : " << endl;

    for (Book book : books){
        cout << book.printInfo() << "\n\n";
    }

    cout << "|-----------------------------------------------------------------------------------------------|\n\n";

    cout << "The book with ISBN " << inp[0] << " is(findISBN) : " << endl;
    cout << findISBN(books, inp[0]).printInfo();

    cout << "The book with title " << book3.getTitle() << " is(findTitle) : " << endl;
    cout << findTitle(books, book3.getTitle()).printInfo();

    cout << "The list of books with genre " << "fiction" << " is : " << endl;
    vector<Book> list = genreList(books, genre::fiction);
    for (Book book : list){
        cout << book.printInfo();
    }

    cout << "The list of books with genre " << "children" << " is : " << endl;
    vector<Book> list2 = genreList(books, genre::children);
    for (Book book : list2){
        cout << book.printInfo();
    }

    cout << "The list of books with genre " << "biography" << " is : " << endl;
    vector<Book> list3 = genreList(books, genre::biography);
    for (Book book : list3){
        cout << book.printInfo();
    }

    cout << "Sorting the books by title : " << endl;
    sortTitle(books);
    for (Book book : books){
        cout << book.printInfo();
    }

    cout << "Sorting the books by ISBN : " << endl;
    sortISBN(books);
    for (Book book : books){
        cout << book.printInfo();
    }

    
    return 0;
}
