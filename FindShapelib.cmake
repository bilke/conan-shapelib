find_path(Shapelib_INCLUDE_DIR NAMES shapefil.h
	PATHS ${CONAN_INCLUDE_DIRS_SHAPELIB})

find_library(Shapelib_LIBRARY NAMES ${CONAN_LIBS_SHAPELIB}
	PATHS ${CONAN_LIB_DIRS_SHAPELIB})

set(Shapelib_FOUND TRUE)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Shapelib DEFAULT_MSG
	Shapelib_FOUND
	Shapelib_INCLUDE_DIR
	Shapelib_LIBRARY
)

set(Shapelib_INCLUDE_DIRS ${Shapelib_INCLUDE_DIR})
set(Shapelib_LIBRARIES ${Shapelib_LIBRARY})

mark_as_advanced(Shapelib_INCLUDE_DIR Shapelib_LIBRARY Shapelib_DIR)
