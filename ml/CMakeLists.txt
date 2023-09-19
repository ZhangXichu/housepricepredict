cmake_minimum_required(VERSION 3.20)

project(housingprice)

add_executable(training training.cpp)

set(SOCI_DIR /mnt/c/worksspace/housepricepredict/ml/soci/include/soci)

target_include_directories(training
    PUBLIC
    ${SOCI_DIR}
)
