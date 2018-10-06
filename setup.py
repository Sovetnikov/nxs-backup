from setuptools import setup

setup(name='nxs-backup',
      version='0.1',
      description='nxs-backup',
      url='https://github.com/nixys/nxs-backup',
      author='nixys',
      author_email='',
      packages=['nxsbackup', ],
      package_dir={'nxsbackup': 'src'},
      entry_points={
          'console_scripts': [
              'nxs-backup=nxsbackup.main:main',
          ],
      },
      install_requires=[
          'mysqlclient',
          'pymongo',
          'psutil',
          'psycopg2-binary',
          'redis',
          'pyyaml',
      ],
      zip_safe=False)
