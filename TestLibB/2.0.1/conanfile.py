from conans import ConanFile, CMake


class MytestlibbConan(ConanFile):
    name = "MyTestLibB"
    author = "james.bourne"
    description = "TestLibB to test conan, and cmake (from the conan-branch-test/development branch)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_paths"
    exports_sources = "*"
    package_originator = "Foundry"
    package_exportable = False

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = "conan_paths.cmake"
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["MyTestLibB"]
