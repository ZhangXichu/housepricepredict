#ifndef UTILS_H
#define UTILS_H

# include <string>
# include <vector>
# include <iostream>
# include <sstream>


template <typename S>
std::ostream& operator<< (std::ostream& os, const std::vector<S> &vector) {
    for (auto element : vector) {
        os << element << "\n";
    }
    return os;
}

void parse_concat_image_names(const std::string&, char, std::vector<std::string>&);


#endif // UTILS_H