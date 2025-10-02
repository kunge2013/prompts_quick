from setuptools import setup, find_packages

setup(
    name='prompt-tool',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for quickly invoking prompt templates based on keyboard shortcuts.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'prompt-tool=main:main',  # Adjust this based on your main function location
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)