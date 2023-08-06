from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='QoolTabs',
    version='1.0.1',
    description='PyQt6 QTabWidget with drag and drop',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rohankishore/QoolTabs/',
    author='Rohan Kishore',
    author_email='rohankishore746@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['pyqt6', 'qtabwidget', 'modern', 'pyqt6 widgets'],
    packages=find_packages(),
    install_requires=['pyqt6']
)