"""
Open Source Electronic Component Inventory Management.
Copyright (C) 2022 DOS1986

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
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
