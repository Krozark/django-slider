from setuptools import setup, find_packages

setup(
    name='django-slider',
    version='0.0.1',
    description='A module for slider',
    long_description=open('README.md').read(),
    author='Maxime Barbier',
    author_email='maxime.barbier1991@gmail.com',
    url='https://github.com/Krozark/django-slider/tree/master/slider',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
