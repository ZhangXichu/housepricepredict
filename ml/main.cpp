# include <fstream>
# include "utils.h"
# include "soci.h"
# include "mysql/soci-mysql.h"


int main() {

    const char* db_user = std::getenv("DB_USER");
    const char* db_password = std::getenv("DB_PASSWORD");
    const char* db_name = std::getenv("DB_NAME");
    const char* db_port = std::getenv("DB_PORT");
    const char* db_host = std::getenv("DB_HOST");

    std::cout << "connect..." << std::endl;

    soci::session sql;

    if (db_user && db_password && db_name && db_port) {

    

    sql.open(soci::mysql, "db=" + std::string(db_name) + 
                        " user=" + std::string(db_user) + 
                        " password=" + std::string(db_password) + 
                        " port=" + std::string(db_port) +
                        " host=" + std::string(db_host));

    std::cout << "Successfully connected to db." << std::endl;
}

    double price;
    std::string image_name_concat;
    soci::indicator price_i, image_name_i;

    soci::statement st = (sql.prepare << "select overall_price, images from apartment", 
                    soci::into(price, price_i),
                    soci::into(image_name_concat, image_name_i));

    st.execute();

    std::vector<double> overall_prices;
    std::vector<std::string> image_name_concats;

    while(st.fetch()) {
        overall_prices.push_back(price);
        image_name_concats.push_back(image_name_concat);

        if (price_i != soci::i_null) {
            std::cout << "Price: " << price << std::endl;
        }
        std::cout << std::endl;

        if (image_name_i != soci::i_null) {
            std::cout << "Concated image names: " << image_name_concat << std::endl;
        }
        std::cout << std::endl;
    }

    std::vector<std::string> image_names;


    return 0;
}
