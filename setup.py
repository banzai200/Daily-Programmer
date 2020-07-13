from setuptools import setup

setup(
    name='dailyprogrammer',
    version='1.0',
    packages=['dailyprogrammer'],
    url='https://github.com/banzai200/Daily-Programmer',
    license='MIT License',
    author='Wesley',
    author_email='tairoria@gmail.com',
    description='A program to download a challenge from reddit.com/r/dailyprogrammer and then output it to stdout to be used in various editors/ides',
    install_requires=['requests', 'jsonpath_rw_ext'],
    entry_points={
        'console_scripts':[
            'dp = dailyprogrammer.dp:main'
        ]
    },
)
