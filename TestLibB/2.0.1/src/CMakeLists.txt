cmake_minimum_required(VERSION 3.13)

set(MYLIBRARY_TARGET_NAME 			MyTestLibB)
set(MYLIBRARY_TARGETS_NAME 			${MYLIBRARY_TARGET_NAME}Targets)
set(MYLIBRARY_CONFIG_NAME  			${MYLIBRARY_TARGET_NAME}Config)
set(MYLIBRARY_CONFIG_VERSION_NAME   ${MYLIBRARY_TARGET_NAME}ConfigVersion)

project(MyTestLibB VERSION 1.0 LANGUAGES CXX)

add_library(MyTestLibB MyTestLibB.cpp)

#add the header files to the public properties
set_target_properties(
	MyTestLibB PROPERTIES
    PUBLIC_HEADER MyTestLibB.h
)

#Export library as target (Create's the <name>Targets.cmake)
install(
    TARGETS
		${MYLIBRARY_TARGET_NAME}
	EXPORT
		${MYLIBRARY_TARGETS_NAME} 
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
	PUBLIC_HEADER DESTINATION include
)

install(EXPORT 
	${MYLIBRARY_TARGETS_NAME} 
	NAMESPACE ${MYLIBRARY_TARGET_NAME}:: 
	DESTINATION cmake
)

export(EXPORT 
	${MYLIBRARY_TARGETS_NAME} 
	NAMESPACE ${MYLIBRARY_TARGET_NAME}:: 
	FILE ${CMAKE_BINARY_DIR}/cmake/${MYLIBRARY_TARGETS_NAME}.cmake
)

#Export library as target (Create's the <name>Config.cmake)
include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/cmake/${MYLIBRARY_CONFIG_NAME}.cmake
    INSTALL_DESTINATION cmake
)

install(
    FILES
      ${CMAKE_CURRENT_BINARY_DIR}/cmake/${MYLIBRARY_CONFIG_NAME}.cmake
    DESTINATION cmake
)

#Export library as target (Create's the <name>ConfigVersion.cmake)
write_basic_package_version_file(
	${CMAKE_CURRENT_BINARY_DIR}/cmake/${MYLIBRARY_CONFIG_VERSION_NAME}.cmake 
	COMPATIBILITY SameMinorVersion
) 

install(
    FILES
      ${CMAKE_CURRENT_BINARY_DIR}/cmake/${MYLIBRARY_CONFIG_VERSION_NAME}.cmake
    DESTINATION cmake
)