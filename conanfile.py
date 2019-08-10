import os

from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LcovConan(ConanFile):
    name = "ccache_installer"
    version = "3.7.2"
    license = "GPL3"
    author = "Torfinn Berset <torfinn@bloomlife.com>"
    url = "https://github.com/torfinnberset/conan-ccache-installer"
    homepage = "https://ccache.dev"
    description = "ccache speeds up recompilation by caching previous compilations and detecting when the same compilation is being done again"
    topics = ("compilation", "cache", "build", "tool")
    settings = ()  # written in perl

    _filename = F"ccache-{version}"

    _version_sha256 = {
        "3.7.2": "a5da0008512ff9e882097acaffb3616fae98ec25827167bb4bd1e4acf0b66793"
    }

    def source(self):
        url = F"https://github.com/ccache/ccache/releases/download/" \
              F"v{self.version}/ccache-{self.version}.tar.xz"
        tools.get(url, sha256=self._version_sha256[self.version])

    def package(self):
        with tools.chdir(self._filename):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure()
            env_build.install()

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.output.success("Added ccache to $PATH")