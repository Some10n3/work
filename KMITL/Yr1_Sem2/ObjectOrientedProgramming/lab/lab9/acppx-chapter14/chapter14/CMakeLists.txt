cmake_minimum_required(VERSION 3.10)

project(acppx_ch14)

add_executable(
    std_main1
    std_main1.cpp student_info.cpp
    grade.cpp read_hw.cpp core.cpp)

add_executable(
    std_main2
    std_main2.cpp student_info.cpp
    grade.cpp read_hw.cpp core.cpp)

add_executable(
    std_main3
    std_main3.cpp student_info.cpp
    grade.cpp read_hw.cpp core.cpp)

add_executable(urls_main urls_main.cpp urls.cpp vec_clone.cpp str.cpp)

set(TARGETS std_main1 std_main2 std_main3 urls_main)

set(DATA_FILES mixed_grades urls.htm)

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

foreach(FN ${DATA_FILES})
    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${FN}
        COMMAND ${CMAKE_COMMAND} -E copy
            ${CMAKE_CURRENT_SOURCE_DIR}/${FN}
            ${CMAKE_CURRENT_BINARY_DIR}/${FN}
        DEPENDS ${FN})

    add_custom_target(
        data-${FN} ALL DEPENDS
        ${CMAKE_CURRENT_BINARY_DIR}/${FN})
endforeach()
