import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'beautifulsoup4',
    'lxml'
]

setup(name='cobertura2clover',
      version='0.0',
      description='cobertura2clover',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      long_description=README,
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      install_requires = requires,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      
      entry_points="""\
      [paste.app_factory]
      main = cai:main
      [console_scripts]
      parser = parser:main
      """
      )
