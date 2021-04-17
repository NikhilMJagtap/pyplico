from setuptools import setup, find_packages


setup_args = dict(
    name='pyplico',
    version='0.0.0',
    description='A python port of Xplico to analyse packets.',
    license='MIT',
    packages=find_packages(),
    author='NikhilMJagtap',
    install_requires=[
        'dpkt>=1.9.2',
        'sockets==1.0.0' 
    ]
)

if __name__ == '__main__':
    setup(**setup_args)