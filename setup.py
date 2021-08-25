from setuptools import setup
long_description = ''
with open('README.md') as longfile:
    long_description=longfile.read()
setup(name='sylvie',
      version='1.0.1',
      description='Sylvie: Enchant your Data',
      author='pspiagicw',
      author_email='pspiagicw@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/pspiagicw/sylvie',
      py_modules=['sylvie'],
      scripts=['sylvie'],
      )
