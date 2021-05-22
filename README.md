# swift-lang-packaging-fedora
All the files necessary to package Apple's Swift Programming language for Fedora

# Setup for building RPM files
I use [this guide](https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/) for setting up my machine for building Swift. The shell scripts (e.g., `justbuild.sh`) assume the RPM packaging tools are already installed.

# Warning!
This is very much a working directory; some of the patches are unfinished or temporary. The file to "trust" is `swift-lang.spec`.
