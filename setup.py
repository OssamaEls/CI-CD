from setuptools import setup, find_namespace_packages

if __name__ == "__main__":
    setup(
        name='ossama_simple_package',
        version='0.1.0',
        description='A simple package',
        packages=find_namespace_packages(where='src'),
        install_requires='requests>1',
        extras_require={'tests': ['pytest']}
    )
