#ifndef ACPP_REF_HANDLE_HPP
#define ACPP_REF_HANDLE_HPP

#include <memory>
#include <stdexcept>

template <class T> class Ref_handle {
public:
    // manage reference count as well as pointer
    Ref_handle() noexcept = default;
    Ref_handle(T* t): p(t) {}

    Ref_handle(const Ref_handle& h) noexcept = default;
    Ref_handle& operator=(const Ref_handle&) noexcept = default;
    ~Ref_handle() = default;
    Ref_handle(Ref_handle&& h) noexcept = default;
    Ref_handle& operator=(Ref_handle&&) noexcept = default;

    // as before
    operator bool() const noexcept { return p.operator bool(); }
    T& operator*() const
    {
        if (p)
            return *p;
        throw std::runtime_error("unbound Ref_handle");
    }
    T* operator->() const
    {
        if (p)
            return p.operator->();
        throw std::runtime_error("unbound Ref_handle");
    }
private:
    std::shared_ptr<T> p;
};

#endif /* ACPP_REF_HANDLE_HPP */
