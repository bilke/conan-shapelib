import os
from conans import ConanFile, CMake
from conans.tools import download, unzip

class ShapelibConan(ConanFile):
    name = "Shapelib"
    version = "1.3.0"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports = ["CMakeLists.txt", "Shapelib.cmake"]
    url="http://github.com/bilke/conan-shapelib"
    license="http://shapelib.maptools.org/license.html"

    ZIP_FOLDER_NAME = "shapelib-%s" % version
    INSTALL_DIR = "_install"

    def source(self):
        zip_name = self.ZIP_FOLDER_NAME + ".zip"
        download("http://download.osgeo.org/shapelib/%s" % zip_name , zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
        if self.settings.os == "Windows":
            self.run("IF not exist _build mkdir _build")
        else:
            self.run("mkdir _build")
        cd_build = "cd _build"
        self.run("%s && cmake .. -DCMAKE_INSTALL_PREFIX=../%s %s" % (cd_build, self.INSTALL_DIR, cmake.command_line))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))
        self.run("%s && cmake --build . --target install %s" % (cd_build, cmake.build_config))

    def package(self):
        self.copy("*", dst=".", src=self.INSTALL_DIR)

    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["shapelib"]
        else:
            self.cpp_info.libs = ["shp"]
