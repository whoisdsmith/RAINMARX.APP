from setuptools import setup, find_packages

setup(
    name='RAINMARX',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'aiodns',
        'beautifulsoup4',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'run_nested=scripts.run_nested:main',
            'run_collectid=scripts.run_collectid:main',
            'run_updatr=scripts.run_updatr:main',
        ],
    },
)
