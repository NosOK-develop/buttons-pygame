from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='pygame_button',
  version='1.0.0',
  author='NosOK',
  author_email='d877231@gmail.com',
  description='Buttons in pygame',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='home_link',
  packages=find_packages(),
  install_requires=['pygame>=2.6.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='pygame python addons',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)