cmake_minimum_required(VERSION 3.10)

project(simple_calculator)

add_subdirectory(nse)

add_executable(q1 q1.cpp)
add_executable(q12 q12.cpp)
add_executable(q2 q2.cpp)

target_link_libraries(q12 PRIVATE nse_html)

set(TARGETS q1 q2 q12)

#set(DATA_FILES "")

set_target_properties(
    ${TARGETS}
    PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO)

foreach(T IN LISTS TARGETS)
    if (MSVC)
        target_compile_options(${T} PRIVATE /Wall /WX)
    else()
        target_compile_options(${T} PRIVATE -Wall -Wextra)
    endif()
endforeach()

#[[
foreach(FN IN LISTS DATA_FILES)
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
]]