# include <iostream>
# include <fstream>
# include <string>
# include <vector>
# include "soci.h"
# include "mysql/soci-mysql.h"

using namespace std;
using namespace soci;


int main() {

    const char* db_user = std::getenv("DB_USER");
    const char* db_password = std::getenv("DB_PASSWORD");
    const char* db_name = std::getenv("DB_NAME");
    const char* db_port = std::getenv("DB_PORT");
    const char* db_host = std::getenv("DB_HOST");

    cout << "connect..." << endl;

    session sql;

    if (db_user && db_password && db_name && db_port) {

    

    sql.open(mysql, "db=" + std::string(db_name) + 
                        " user=" + std::string(db_user) + 
                        " password=" + std::string(db_password) + 
                        " port=" + std::string(db_port) +
                        " host=" + std::string(db_host));

    cout << "Successfully connected to db." << endl;
}

    double price;
    string image_name_concat;
    indicator price_i, image_name_i;

    statement st = (sql.prepare << "select overall_price, images from apartment", 
                    into(price, price_i),
                    into(image_name_concat, image_name_i));

    st.execute();

    vector<double> overall_prices;
    vector<string> image_name_concats;
    vector<indicator> price_is, image_name_is;

    while(st.fetch()) {
        overall_prices.push_back(price);
        image_name_concats.push_back(image_name_concat);

        if (price_i != i_null) {
            cout << "Price: " << price << endl;
        }
        cout << endl;

        if (image_name_i != i_null) {
            cout << "Concated image names: " << image_name_concat << endl;
        }
        cout << endl;
    }


    return 0;
}
