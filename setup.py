from setuptools import setup

setup(
   name='ecpkeeper',
   version='0.1',
   description='Something different',
   author='David Southwood',
   author_email='DOS1986@gmail.com',
   packages=['ecpkeeper'],  # would be the same as name
   install_requires=['SQLAlchemy'],  # external packages acting as dependencies
)
