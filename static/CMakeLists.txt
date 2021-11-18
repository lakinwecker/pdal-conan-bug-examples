cmake_minimum_required(VERSION 3.15.0)

project(pdal-example)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
include(build/deps/conan/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# Use modern C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(OpenGL_GL_PREFERENCE GLVND)


#-------------------------------------------------------------------------------
set(LIBRARIES CONAN_PKG::pdal)


set(SOURCES src/main.cpp)
set(INCLUDES ${INCLUDES} src)

#------------------------------------------------------------------------------
# The base underlying library.
#------------------------------------------------------------------------------
add_executable(example ${SOURCES})
target_link_libraries(example ${LIBRARIES})
target_include_directories(example PRIVATE ${INCLUDES})
target_compile_definitions(example PRIVATE ${DEFINITIONS})
target_compile_options(example PRIVATE ${DGGS_CMAKE_CXX_FLAGS})


