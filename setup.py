from setuptools import setup, find_packages

version = '0.3.dev0'

setup(name='webtest-casperjs',
      version=version,
      description="Use casperjs with WebTest",
      long_description=open('README.rst').read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Paste",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
      ],
      keywords='wsgi test unit tests web casperjs',
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
