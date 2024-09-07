cmake_minimum_required(VERSION 3.10)

project(using_libs)

find_package(range-v3 CONFIG REQUIRED)
find_package(fmt CONFIG REQUIRED)
find_package(scn CONFIG REQUIRED)

add_executable(range_ex1 range_ex1.cpp)
add_executable(scn_ex1 scn_ex1.cpp)

target_link_libraries(range_ex1 PRIVATE range-v3::range-v3)
target_link_libraries(
    scn_ex1 PRIVATE scn::scn-header-only fmt::fmt-header-only)

set(TARGETS range_ex1 scn_ex1)

#set(DATA_FILES split_cpp grades palins_input urls.htm)

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

#[[
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
#]]
