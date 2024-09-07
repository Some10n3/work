#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <memory>

class Shape {
public:
    virtual double area() const = 0;
    virtual void read(std::istream& is) = 0;
    virtual void print(std::ostream& os) const = 0;
    virtual ~Shape() {}
};

class Circle : public Shape {
public:
    Circle(double x = 50, double y = 50, double r = 10) : x_(x), y_(y), r_(r) {}
    double area() const override {
        return M_PI * r_ * r_;
    }
    void read(std::istream& is) override {
        is >> x_ >> y_ >> r_;
    }
    void print(std::ostream& os) const override {
        os << "[Circle: (" << x_ << ", " << y_ << ", " << r_ << ")]";
    }
private:
    double x_;
    double y_;
    double r_;
};

class Rectangle : public Shape {
public:
    Rectangle(double x = 0, double y = 0, double w = 0, double h = 0) : x_(x), y_(y), w_(w), h_(h) {}
    double area() const override {
        return w_ * h_;
    }
    void read(std::istream& is) override {
        is >> x_ >> y_ >> w_ >> h_;
    }
    void print(std::ostream& os) const override {
        os << "[Rectangle: (" << x_ << ", " << y_ << ", " << w_ << ", " << h_ << ")]";
    }
private:
    double x_;
    double y_;
    double w_;
    double h_;
};

void read_shapes(std::istream& is, std::vector<std::unique_ptr<Shape>>& shapes) {
    char shape_type;
    while (is >> shape_type) {
        if (shape_type == 'C') {
            double x, y, r;
            is >> x >> y >> r;
            shapes.emplace_back(std::make_unique<Circle>(x, y, r));
        }
        else if (shape_type == 'R') {
            double x, y, w, h;
            is >> x >> y >> w >> h;
            shapes.emplace_back(std::make_unique<Rectangle>(x, y, w, h));
        }
    }
}

int main() {
    std::istringstream iss("C 50 50 15 R 40 40 20 20");
    std::vector<std::unique_ptr<Shape>> shapes;
    read_shapes(iss, shapes);
    
    std::sort(shapes.begin(), shapes.end(), [](const auto& a, const auto& b) {
        return a->area() < b->area();
    });
    
    for (const auto& shape : shapes) {
        shape->print(std::cout);
        std::cout << " area: " << shape->area() << std::endl;
    }
    
    return 0;
}