// utils.cpp
#include "utils.h"

/**
 * @brief function paarses the concated image names
 * 
 * @param image_concat_names string of concatenated image names, separated by semicolon
 * @param delim delimiter, one char
 * @param image_names: the output vector of parsed image names
 */
void parse_concat_image_names(const std::string &image_concat_names, char delim, std::vector<std::string> &image_names) {
    
    std::istringstream iss(image_concat_names);
    std::string image_name;

    while (std::getline(iss, image_name, delim)) {
        image_names.push_back(image_name);
    }

}


