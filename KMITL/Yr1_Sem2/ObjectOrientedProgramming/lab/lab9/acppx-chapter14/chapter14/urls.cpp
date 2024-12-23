#include "urls.hpp"
#include "str.hpp"
#include "vec.hpp"

#include <algorithm>
#include <cctype>

using std::find;       using std::find_if;

using std::isalnum;    using std::isalpha;    using std::isdigit;

using std::search;

bool not_url_char(char);

Str::const_iterator
    url_end(Str::const_iterator, Str::const_iterator);

Str::const_iterator
    url_beg(Str::const_iterator, Str::const_iterator);

Vec<Str> find_urls(const Str& s)
{
    Vec<Str> ret;
    auto b = s.begin(), e = s.end();

    // look through the entire input
    while (b != e) {
        // look for one or more letters followed by `://'
        b = url_beg(b, e);

        // if we found it
        if (b != e) {
            // get the rest of the URL
            auto after = url_end(b, e);

            // remember the URL
            ret.push_back(Str(b, after));

            // advance `b' and check for more URLs on this line
            b = after;
        }
    }
    return ret;
}

Str::const_iterator
    url_end(Str::const_iterator b, Str::const_iterator e)
{
    return find_if(b, e, not_url_char);
}

bool not_url_char(char c)
{
    // characters, in addition to alphanumerics, that can appear in a URL
    static const Str url_ch = "~;/?:@=&$-_.+!*'(),";

    // see whether `c' can appear in a URL and return the negative
    return !(isalnum(c) ||
             find(url_ch.begin(), url_ch.end(), c) != url_ch.end());
}

Str::const_iterator
    url_beg(Str::const_iterator b, Str::const_iterator e)
{
    static const Str sep = "://";

    // `i' marks where the separator was found
    auto i = b;
    while ((i = search(i, e, sep.begin(), sep.end())) != e) {
        // make sure the separator isn't at the beginning or end of the line
        if (i != b && i + sep.size() != e) {
            // `beg' marks the beginning of the protocol-name
            auto beg = i;
            while (beg != b && isalpha(beg[-1]))
                --beg;

            // is there at least one appropriate character
            // before and after the separator?
            if (beg != i && !not_url_char(i[sep.size()]))
                return beg;
        }

        // the separator we found wasn't part of a URL;
        // advance `i' past this separator
        i += sep.size();
    }
    return e;
}
