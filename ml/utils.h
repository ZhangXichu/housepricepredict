#ifndef UTILS_H
#define UTILS_H

# include <string>
# include <vector>
# include <iostream>
# include <sstream>

/**
 * @brief overriden operator << to print content of a vector
 * 
 * @tparam S class of the elements in the vector
 * @param os output stream
 * @param vector the input vector
 * @return std::ostream& 
 */
template <typename S>
std::ostream& operator<< (std::ostream& os, const std::vector<S> &vector) {
    for (auto element : vector) {
        os << element << "\n";
    }
    return os;
}

void parse_concat_image_names(const std::string&, char, std::vector<std::string>&);


#endif // UTILS_H