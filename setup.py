from distutils.core import setup

setup(
    name='packagetemplate',
    version='0.1.0',
    author='Karl Martino',
    author_email='kmartino@gmail.com.com',
    packages=['packatetemplate', 'packagetemplate.test'],
    #scripts=['if you have a bin dir and scripts that can be called,
    #specify them here']
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='A template to use for creating packages.',
    long_description=open('README.txt').read(),
    install_requires=[
        "nose >= 1.2.1",
    ],
)
