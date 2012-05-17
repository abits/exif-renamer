from distutils.core import setup
import glob
from DistUtilsExtra.command import *
from DistUtilsExtra.auto import *

setup(
    name='exif-renamer',
    version='0.1',
    packages=['exif_renamer'],
    url='https://abits@github.com/abits/exif-renamer.git',
    license='LICENSE.txt',
    author='Chris Martel',
    author_email='chris@codeways.org',
    description='Rename photos from exif data.',
    long_description=open('README.txt').read(),
    install_requires=[
        "PIL>=1.1.7"
    ],
    include_package_data=True,
    data_files=[
        ('share/exif-renamer/ui',
         glob.glob("data/ui/*.ui")
        ),
        ("share/applications",
         glob.glob("data/desktop/*.desktop")),
    ],
    scripts=['bin/exif-renamer'],
    cmdclass = { "build" : build_extra.build_extra,
                 "build_icons" :  build_icons.build_icons }
)
