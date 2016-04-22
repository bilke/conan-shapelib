find_path(Shapelib_INCLUDE_DIR NAMES shapefil.h
	PATHS ${CONAN_INCLUDE_DIRS_SHAPELIB}
	NO_DEFAULT_PATH)

find_library(Shapelib_LIBRARY NAMES ${CONAN_LIBS_SHAPELIB}
	PATHS ${CONAN_LIB_DIRS_SHAPELIB}
	NO_DEFAULT_PATH)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Shapelib
	REQUIRED_VARS Shapelib_LIBRARY Shapelib_INCLUDE_DIR
	FOUND_VAR Shapelib_FOUND
)

set(Shapelib_INCLUDE_DIRS ${Shapelib_INCLUDE_DIR})
set(Shapelib_LIBRARIES ${Shapelib_LIBRARY})

mark_as_advanced(Shapelib_INCLUDE_DIR Shapelib_LIBRARY)
