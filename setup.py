from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup(
  name = 'Genetic Algorithm',
  version = '0.0.1',
  author = 'mayo-ya',
  author_email = 'mayo.yamasaki[at]gmail.com',
  cmdclass = {'build_ext': build_ext},
  ext_modules = [Extension("genetic_optimization", ["src/genetic_optimization.pyx"])],
  package_dir = {'': 'libs'}
)
