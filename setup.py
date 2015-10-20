from distutils.core import setup

setup(name='kao_factory',
      version='0.5.1',
      description='Python Factory Library',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_factory',
                'kao_factory.Exception',
                'kao_factory.Args',
                'kao_factory.Source',
                'kao_factory.Factory'],
     )