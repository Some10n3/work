#ifndef ACPP_PTR_HPP
#define ACPP_PTR_HPP

#include <memory>

template <class T> class Ptr {
public:
    // new member to copy the object conditionally when needed
    void make_unique()
    {
        if (p.use_count() > 1) {
            p.reset( clone(p.get()) );
        }
    }

    // the rest of the class looks like `Ref_handle' except for its name
    Ptr() noexcept = default;
    explicit Ptr(T* t): p(t) {}

    Ptr(const Ptr& h) noexcept = default;
    // implemented analogously to 14.2/261
    Ptr& operator=(const Ptr&) noexcept = default;
    ~Ptr() = default;              // implemented analogously to 14.2/262
    Ptr(Ptr&& h) noexcept = default;
    Ptr& operator=(Ptr&&) noexcept = default;

    operator bool() const noexcept { return p.operator bool(); }
    T& operator*() const;          // implemented analogously to 14.2/261
    T* operator->() const;         // implemented analogously to 14.2/261
private:
    std::shared_ptr<T> p;
};







#include <stdexcept>

template <class T> T* clone(const T* tp)
{
    return tp->clone();
}

template<class T>
T& Ptr<T>::operator*() const
{
    if (p)
        return *p;
    throw std::runtime_error("unbound Ptr");
}

template<class T>
T* Ptr<T>::operator->() const
{
    if (p)
        return p.operator->();
    throw std::runtime_error("unbound Ptr");
}

#endif /* ACPP_PTR_HPP */
