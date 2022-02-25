from setuptools import setup, find_packages

meta_data = {}
with open("json-config/meta_data.py") as fp:
    exec(fp.read(), meta_data)

setup(
    name='json-config',
    version=meta_data['__version__'],
    url='https://github.com/iotmaxx/json-config',
    author='Ralf Glaser',
    author_email='glaser@iotmaxx.de',
    description=meta_data['__description__'],
    packages=find_packages(),    
    install_requires=[],
)
