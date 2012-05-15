from distutils.core import setup

setup(
    name='exif-renamer',
    version='0.1',
    packages=[''],
    url='https://abits@github.com/abits/exif-renamer.git',
    license='LICENSE.txt',
    author='Chris Martel',
    author_email='chris@codeways.org',
    description='Rename photos from exif data.',
    long_description=open('README.txt').read(),
    install_requires=[
        "PIL==1.1.7"
    ]
)
