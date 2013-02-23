from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='webtest-casperjs',
      version=version,
      description="Use casperjs with WebTest",
      long_description="""\
""",
      classifiers=[],
      keywords='wsgi test webtest',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='https://github.com/gawel/webtest-casperjs',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'WebTest',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
