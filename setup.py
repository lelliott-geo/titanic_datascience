from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/lelliott-geo/titanic_datascience',
    author='Laura Elliott',  # Substitute your name
    author_email='lauraelliott8671@comcast.net',  # Substitute your email
    license='MIT',
    packages=['titanic'],
    install_requires=[
        'pytest>=4.3.1',
        'pytest-runner>=4.4',
        'click>=7.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    ini
    [aliases]
    test=pytest
    entry_points=
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis)
