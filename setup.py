from setuptools import setup

setup(name='nvidia-docker-compose',
      version='0.0.4',
      description='GPU enabled docker-compose wrapper',
      url='https://github.com/eywalker/nvidia-docker-compose',
      author='Edgar Y. Walker',
      author_email='edgar.walker@gmail.com',
      license='MIT',
      packages=[],
      install_requires=['pyyaml'],
      scripts=['bin/nvidia-docker-compose']
      )
