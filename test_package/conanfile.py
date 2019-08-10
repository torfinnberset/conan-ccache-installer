import os

from conans import ConanFile
from six import StringIO


class CcacheTestConan(ConanFile):
    def test(self):
        output = StringIO()
        ccache_path = os.path.join(self.deps_cpp_info["ccache_installer"].rootpath, "bin", "ccache")
        self.run("{} --version".format(ccache_path), output=output, run_environment=True)
        self.output.info("Installed: %s" % str(output.getvalue()))
        ver = str(self.requires["ccache_installer"].ref.version)

        value = str(output.getvalue())
        ccache_version = value.split('\n')[0]
        self.output.info("Expected value: {}".format(ver))
        self.output.info("Detected value: {}".format(ccache_version))
        assert (ver in ccache_version)
