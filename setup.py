from setuptools import setup, find_packages, Command
import sys
import os


if sys.version_info < (3, 4):
    raise Exception('This package requires Python 3.4 or higher.')


VERSION_FILENAME = "VERSION"
SOURCE_DIR_NAME = "src"


def readme():
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()


def read_version_file():
    try:
        with open(VERSION_FILENAME, "rb") as f:
            release_version = f.readlines()[0].decode().strip()
            return release_version
    except IOError:
        return None


def write_version_file(version):
    with open(VERSION_FILENAME, 'w') as f:
        f.write(version + "\n")


def add_src_to_syspath():
    currentdir = os.path.dirname(os.path.realpath(__file__))
    pkg_source_dir = os.path.join(currentdir, SOURCE_DIR_NAME)
    sys.path.insert(0, pkg_source_dir)


def get_version():

    # Read in the version that's currently in VERSION file.
    saved_version = read_version_file()

    # Get version from app
    add_src_to_syspath()
    try:
        from aiohttp_autoreload import __version__
        app_version = __version__
    except ImportError:
        app_version = saved_version

    # If we still don't have anything, that's an error.
    if app_version is None:
        raise ValueError("Cannot find the version number!")

    # If the current version is different from what's in the
    # VERSION file, update the file to be current.
    if app_version != saved_version:
        write_version_file(app_version)

    # Finally, return the complete version.
    return app_version


class GenVersionCommand(Command):
    description = "Generate VERSION file if not exist, or update it."
    user_options = []

    def run(self):
        version = get_version()
        print(version)

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


setup(
    name='aiohttp_autoreload',
    version=get_version(),
    description='Makes aiohttp server autoreload on source code change',
    author="Dmitry Litvinenko",
    author_email="anti1869@gmail.com",
    long_description=readme(),
    url="https://github.com/anti1869/aiohttp_autoreload",
    package_dir={'': SOURCE_DIR_NAME},
    packages=find_packages(SOURCE_DIR_NAME, exclude=('*.tests',)),
    py_modules=["aiohttp_autoreload"],
    include_package_data=True,
    zip_safe=False,
    package_data={},
    license='Apache 2',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[],
    cmdclass={
        "gen_version": GenVersionCommand,
    },
)
