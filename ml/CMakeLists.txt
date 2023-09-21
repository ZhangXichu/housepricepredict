cmake_minimum_required(VERSION 3.20)

project(housingprice)

# use Findmysql.cmake to find mysql
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}")
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

find_package(MySQL REQUIRED)

message(STATUS "CMAKE_SOURCE_DIR = ${CMAKE_SOURCE_DIR}")

set(SOCI_DIR ~/workspace/housing-price-predict/ml/soci/include/soci)
set(SOURCES  utils.cpp ${SOCI_DIR}/soci.h ${SOCI_DIR}/mysql/soci-mysql.h utils.h)

link_directories(${CMAKE_SOURCE_DIR}/soci/build/lib)

add_executable(main main.cpp ${SOURCES})

add_executable(test test.cpp ${SOURCES})

target_include_directories(main
    PUBLIC
    ${SOCI_DIR}
)

target_include_directories(test
    PUBLIC
    ${SOCI_DIR}
)

include_directories(${MySQL_INCLUDE_DIRS})
target_link_libraries(main ${MySQL_LIBRARIES} soci_core soci_mysql)
target_link_libraries(test ${MySQL_LIBRARIES} soci_core soci_mysql)
