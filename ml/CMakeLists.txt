cmake_minimum_required(VERSION 3.20)

project(housingprice)

# use Findmysql.cmake to find mysql
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}")
find_package(MySQL REQUIRED)

set(SOCI_DIR /mnt/c/worksspace/housepricepredict/ml/soci/include/soci)
set(SOURCES training.cpp ${SOCI_DIR}/soci.h ${SOCI_DIR}/mysql/soci-mysql.h)

add_executable(training ${SOURCES})

target_include_directories(training
    PUBLIC
    ${SOCI_DIR}
)

include_directories(${MySQL_INCLUDE_DIRS})
target_link_libraries(training ${MySQL_LIBRARIES} soci_core soci_mysql)
