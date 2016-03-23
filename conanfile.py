import os
from conans import ConanFile, CMake
from conans.tools import download, unzip

class ShapelibConan(ConanFile):
    name = "Shapelib"
    version = "1.3.0"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    url="http://github.com/bilke/conan-shapelib"
    license="none"

    ZIP_FOLDER_NAME = "shapelib-%s" % version

    def source(self):
        zip_name = self.ZIP_FOLDER_NAME + ".zip"
        download("http://download.osgeo.org/shapelib/%s" % zip_name , zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        if self.settings.arch == "x86":
            self.run("cd %s && make CFLAGS=\"-m32\" LDFLAGS=\"-m32\"" % self.ZIP_FOLDER_NAME)
        else:
            self.run("cd %s && make" % self.ZIP_FOLDER_NAME)

    def package(self):
        self.copy("shapefil.h", dst="include", src=self.ZIP_FOLDER_NAME)
        self.copy("*.lib", dst="lib", src=self.ZIP_FOLDER_NAME)
        self.copy("*.a", dst="lib", src=self.ZIP_FOLDER_NAME)

    def package_info(self):
        self.cpp_info.libs = ["shp"]
