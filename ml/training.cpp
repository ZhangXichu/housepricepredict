# include <iostream>
# include <fstream>
# include <string>
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

    if (db_user && db_password && db_name && db_port) {
    session sql(mysql, "db=" + std::string(db_name) + 
                        " user=" + std::string(db_user) + 
                        " password=" + std::string(db_password) + 
                        " port=" + std::string(db_port) +
                        " host=" + std::string(db_host));
}

    string id = "1004246348";
    double area;

    // session sql(mysql, "db=estate user=root password=Zxc_19960209 port=3306");


    return 0;
}
