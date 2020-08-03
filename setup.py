import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dragonfly',
    version='0.0.1',
    author='Thai Nguyen',
    author_email='nguyenthai2811@gmail.com',
    description='A package to make FlaskRestful easier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thai2811/dragonfly',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
