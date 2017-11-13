from setuptools import setup

setup(name='nvidia-docker-compose',
      version='0.1.5',
      description='GPU enabled docker-compose wrapper',
      url='https://github.com/eywalker/nvidia-docker-compose',
      author='Edgar Y. Walker',
      author_email='edgar.walker@gmail.com',
      license='MIT',
      packages=[],
      install_requires=['docker-compose', 'pyyaml', 'jinja2'],
      scripts=['bin/nvidia-docker-compose']
      )
