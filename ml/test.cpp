# include "soci.h"
# include "mysql/soci-mysql.h"
# include "utils.h"
#include <string>

const std::string test_image_names_concat1 = "99686492_1.png;99686492_2.png;99686492_3.png;99686492_4.png;99686492_5.png;99686492_6.png;99686492_7.png;99686492_8.png;99686492_9.png;99686492_10.png";

int main() {

    
    std::vector<std::string> image_names;

    parse_concat_image_names(test_image_names_concat1, ';', image_names);

    std::cout << "parsed image names:" << std::endl;
    std::cout << image_names << std::endl;

    return 0;
}