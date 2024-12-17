from setuptools import setup, find_packages

setup(
    name='softcommpy',
    version='0.1.0',
    author='Mustafa Eren BAŞOL',
    author_email='merenbasol@gmail.com',
    description='Python iletişim ve servis paketi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kullanici/softcommpy',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
    install_requires=[
        'typing-extensions',  # Tip desteği için
    ],
    extras_require={
        'dev': [
            'pytest',
            'mypy',
        ],
        'test': [
            'pytest',
        ],
    },
    keywords='python communication service messaging',
    project_urls={
        'Source': 'https://github.com/merenbasol42/softcommpy',
    },
)
