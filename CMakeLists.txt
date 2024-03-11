cmake_minimum_required(VERSION 3.27)
project(plane-assets VERSION 0.1.1)

include(FetchContent)

set(PLANE_VERSION 0.1.3)
set(PLANE_MD5 101fdffc218e407eb0951a0487a4835d)
set(PLANE_FILE_NAME "plane-${PLANE_VERSION}-Emscripten.zip")

FetchContent_Declare(
  plane_engine_project
  URL "https://github.com/qbki/plane/releases/download/v${PLANE_VERSION}/${PLANE_FILE_NAME}"
  URL_HASH MD5=${PLANE_MD5})
FetchContent_MakeAvailable(plane_engine_project)
FetchContent_GetProperties(plane_engine_project)

install(DIRECTORY ${CMAKE_SOURCE_DIR}/models DESTINATION assets/)
install(DIRECTORY ${CMAKE_SOURCE_DIR}/levels DESTINATION assets/)
install(DIRECTORY ${plane_engine_project_SOURCE_DIR}/ DESTINATION .)
set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY OFF)
set(CPACK_GENERATOR "TGZ")
set(CPACK_OUTPUT_FILE_PREFIX ${CMAKE_SOURCE_DIR}/build/pack)
set(CPACK_PACKAGE_FILE_NAME "dist")
include(CPack)
