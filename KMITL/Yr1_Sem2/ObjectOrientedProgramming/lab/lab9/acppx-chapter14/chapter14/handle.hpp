#ifndef ACPP_HANDLE_HPP
#define ACPP_HANDLE_HPP

#include <memory>

template <class T> class Handle {
public:
    Handle(const Handle& s);
    Handle& operator=(const Handle&);
    ~Handle() = default;
    Handle(Handle&&) noexcept = default;
    Handle& operator=(Handle&&) noexcept = default;

    Handle() noexcept = default;
    Handle(T* t) noexcept: p(t) {}

    operator bool() const noexcept { return p.operator bool(); }
    T& operator*() const;
    T* operator->() const;
private:
    std::unique_ptr<T> p;
};

#include <stdexcept>


//clone
template <class T>
Handle<T>::Handle(const Handle& s): p{}
{ if (s.p) p.reset(s.p->clone()); }

template <class T>
Handle<T>& Handle<T>::operator=(const Handle& rhs)
{
    if (&rhs != this) {
        p.reset(rhs.p? rhs.p->clone(): nullptr);
    }
    return *this;
}

template <class T>
T& Handle<T>::operator*() const
{
    if (p) 	
        return *p;
    throw std::runtime_error("unbound Handle");
}

template <class T>
T* Handle<T>::operator->() const
{
    if (p)
        return p.operator->();
    throw std::runtime_error("unbound Handle");
}

#endif /* ACPP_HANDLE_HPP */
