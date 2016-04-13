project(MyShapelib C)
cmake_minimum_required(VERSION 2.8.12)

include(conanbuildinfo.cmake)

conan_basic_setup()

#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY bin)
#message("${CONAN_CMAKE_MODULE_PATH}")
#set(CMAKE_MODULE_PATH ${CONAN_CMAKE_MODULE_PATH} ${CMAKE_MODULE_PATH})
#find_package(Shapelib REQUIRED)

include_directories(${Shapelib_INCLUDE_DIRS})
add_executable(shptest shptest.c)

target_link_libraries(shptest ${CONAN_LIBS})
#target_link_libraries(shptest ${Shapelib_LIBRARIES})
