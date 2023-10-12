cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD 20)

project(housingprice)

# use Findmysql.cmake to find mysql
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}")
message(STATUS "CMAKE_MODULE_PATH = ${CMAKE_MODULE_PATH}")


list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

find_package(MySQL REQUIRED)

# Add find_package for Caffe
find_package(Caffe REQUIRED)

message(STATUS "CMAKE_SOURCE_DIR = ${CMAKE_SOURCE_DIR}")
message(STATUS "Caffe_INCLUDE_DIRS = ${Caffe_INCLUDE_DIRS}")

set(SOCI_DIR /soci/include/soci)
set(SOURCES  utils.cpp ${SOCI_DIR}/soci.h ${SOCI_DIR}/mysql/soci-mysql.h utils.h)

link_directories(/soci/build/lib)

add_executable(main main.cpp ${SOURCES})

add_executable(test test.cpp ${SOURCES})

target_include_directories(main
    PUBLIC
    ${SOCI_DIR}
    ${Caffe_INCLUDE_DIRS} # Add this for Caffe
)

target_include_directories(test
    PUBLIC
    ${SOCI_DIR}
    ${Caffe_INCLUDE_DIRS} # Add this for Caffe
)

include_directories(${MySQL_INCLUDE_DIRS})
target_link_libraries(main ${MySQL_LIBRARIES} soci_core soci_mysql ${Caffe_LIBRARIES})
target_link_libraries(test ${MySQL_LIBRARIES} soci_core soci_mysql ${Caffe_LIBRARIES})
