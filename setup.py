from setuptools import setup

setup(name='hdoc',
      version='0.1',
      description='Open browser on Hackage documentation',
      url='',
      author='Erik Rantapaa',
      author_email='erantapaa@gmail.com',
      license='MIT',
      packages=[],
      install_requires=[
          'BeautifulSoup4', 'argparse', 'requests'
      ],
      scripts=['bin/hdoc'],
      zip_safe=False)

