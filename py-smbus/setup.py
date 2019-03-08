#!/usr/bin/env python

# from distutils.core import setup, Extension
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import subprocess
import os

class BuildI2CLibrary(build_ext):
    """Customized install to run library Makefile"""
    def run(self):
        print("building 'i2c' library")
        os.environ['CFLAGS'] = '-fPIC'
        proc = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(proc.stderr.read())
        build_ext.run(self)

setup(	name="smbus",
	version="1.1.post2",
	description="Python bindings for Linux SMBus access through i2c-dev",
	author="Mark M. Hoffman",
	author_email="mhoffman@lightlink.com",
	maintainer="Mark M. Hoffman",
	maintainer_email="linux-i2c@vger.kernel.org",
	license="GPLv2",
	url="https://i2c.wiki.kernel.org/index.php/I2C_Tools",
    cmdclass = {'build_ext':BuildI2CLibrary},
	ext_modules=[Extension(
		"smbus",
		["smbusmodule.c"],
		extra_compile_args=['-Iinclude'],
		extra_link_args=['-Llib'],
        extra_objects=['lib/libi2c.a']
    )]
)
