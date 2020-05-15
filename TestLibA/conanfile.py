from conans import ConanFile, CMake, tools

class MytestlibaConan(ConanFile):
    name = "MyTestLibA"
    version = "1.0"
    author = "james.bourne"
    description = "TestLibA to test conan, and cmake, this just prints a message (from the conan-branch-test/foundry branch)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_paths"
    exports_sources = "src/*", "!conanfile.py"
    package_originator = "Foundry"
    package_exportable = False
    
    requires = (
        "MyTestLibB/1.1@common/development",        
    )

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
        self.cpp_info.libs = tools.collect_libs(self)

