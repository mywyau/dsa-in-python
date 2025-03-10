from setuptools import setup, find_packages

setup(
    name='algorithms',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project's dependencies here.
        # For example: 'numpy', 'requests',
    ],
    tests_require=[
        'pytest',  # or 'unittest', if you prefer
        # 'unittest',  # or 'unittest', if you prefer
    ],
    test_suite='test',
    entry_points={
        'console_scripts': [
            # Define command-line scripts here.
            # For example: 'your_script=your_module:main',
        ],
    },
)