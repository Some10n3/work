#include <string>
#include <iostream>
#include <memory>

class Hero {
public:
    Hero(std::string name = "Nameless Hero") : name_(name) {}
    std::string name() const { return name_; }
    virtual std::string greetings() const = 0;
    virtual void read(std::istream& is) { is >> name_; }
    virtual void print(std::ostream& os) const { os << name_; }
    virtual ~Hero() {}
protected:
    std::string name_;
};

class Warrior : public Hero {
public:
    Warrior(std::string name = "Nameless Warrior") : Hero(name) {}
    std::string greetings() const override { return "I'm " + name_ + ", I will save the world."; }
    void read(std::istream& is) override { Hero::read(is); }
    void print(std::ostream& os) const override { os << "[Warrior: "; Hero::print(os); os << "]"; }
};

class Fighter : public Hero {
public:
    Fighter(std::string name = "Nameless Fighter") : Hero(name) {}
    std::string greetings() const override { return "I'm " + name_ + ", my fists will crush the evil."; }
    void read(std::istream& is) override { Hero::read(is); }
    void print(std::ostream& os) const override { os << "[Fighter: "; Hero::print(os); os << "]";}
};

class Mage : public Hero {
public:
    Mage(std::string name = "Nameless Mage") : Hero(name) {}
    std::string greetings() const override { return "I'm " + name_ + ", I can cook with fire magic."; }
    void read(std::istream& is) override { Hero::read(is); }
    void print(std::ostream& os) const override { os << "[Mage: "; Hero::print(os); os << "]"; }
};

int main() {
    std::unique_ptr<Hero> w = std::make_unique<Warrior>("Cecil");
    std::cout << w->greetings() << std::endl;

    std::unique_ptr<Hero> f = std::make_unique<Fighter>();
    std::cout << f->greetings() << std::endl;

    std::unique_ptr<Hero> m = std::make_unique<Mage>("Vivi");
    std::cout << m->greetings() << std::endl;

    // Test read() and print() functions
    std::cout << "Enter a name for the Warrior: ";
    w->read(std::cin);
    w->print(std::cout);
    std::cout << std::endl;

    std::cout << "Enter a name for the Fighter: ";
    f->read(std::cin);
    f->print(std::cout);
    std::cout << std::endl;

    std::cout << "Enter a name for the Mage: ";
    m->read(std::cin);
    m->print(std::cout);
    std::cout << std::endl;

    


    return 0;
}


