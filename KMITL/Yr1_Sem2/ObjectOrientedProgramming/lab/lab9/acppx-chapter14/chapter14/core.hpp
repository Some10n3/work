#ifndef ACPP_CORE_HPP
#define ACPP_CORE_HPP

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

class Core {
public:
    Core(): midterm(0), final(0) {}
    Core(std::istream& is) { read(is); }

    std::string name() const;

    // as defined in 13.1.2/230
    virtual std::istream& read(std::istream&);
    virtual double grade() const;

    virtual ~Core() {}

protected:
    // accessible to derived classes
    std::istream& read_common(std::istream&);
    double midterm, final;
    std::vector<double> homework;

public:
    virtual Core* clone() const { return new Core(*this); }

private:
    // accessible only to `Core'
    std::string n;
    friend class Student_info;
};

class Grad: public Core {
public:
    Grad(): thesis(0) {}
    Grad(std::istream& is) { read(is); }

    // as defined in 13.1.2/230;
    // Note: `grade' and `read' are `virtual' by inheritance
    double grade() const override;
    std::istream& read(std::istream&) override;
private:
    double thesis;
    Grad* clone() const override { return new Grad(*this); }
};

bool compare(const Core&, const Core&);
bool compare_Core_ptrs(const Core* cp1, const Core* cp2);

#endif /* ACPP_CORE_HPP */
