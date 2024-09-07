cmake_minimum_required(VERSION 3.10)
project(example1)
add_executable(q1 q1.cpp)
add_executable(q2 q2.cpp)
add_executable(q2_2 q2_2.cpp)
add_executable(q3 q3.cpp)
# set C++ standard
set_target_properties(
    q1
    q2
    q2_2
    q3
    PROPERTIES
CXX_STANDARD 17
CXX_STANDARD_REQUIRED YES
CXX_EXTENSIONS NO)
# add more warning to the compiler options
if (MSVC)
target_compile_options(q1 PRIVATE /Wall /WX)
target_compile_options(q2 PRIVATE /Wall /WX)
target_compile_options(q2_2 PRIVATE /Wall /WX)
target_compile_options(q3 PRIVATE /Wall /WX)
else()
target_compile_options(q1 PRIVATE -Wall -Wextra)
target_compile_options(q2 PRIVATE -Wall -Wextra)
target_compile_options(q2_2 PRIVATE -Wall -Wextra)
target_compile_options(q3 PRIVATE -Wall -Wextra)
endif()
set(TARGETS q1)
set(TARGETS q2)
set(TARGETS q2_2)
set(TARGETS q3)
set_target_properties(
${TARGETS}
PROPERTIES
CXX_STANDARD 17
CXX_STANDARD_REQUIRED YES
CXX_EXTENSIONS NO)
foreach(T ${TARGETS})
if (MSVC)
target_compile_options(${T} PRIVATE /Wall /WX)
else()
target_compile_options(${T} PRIVATE -Wall -Wextra)
endif()
endforeach()