try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A template to use for creating packages',
    'author': 'Karl Martino',
    'url': 'https://github.com/kmartino/py-package-template',
    'download_url': 'https://github.com/kmartino/py-package-template',
    'author_email': 'kmartino@gmail.com',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['packagetemplate'],
    'name': 'packagetemplate',
    entry_points={
        'console_scripts': [
            'pt = packagetemplate.sample:main',
        ]
    },
}

setup(**config)
