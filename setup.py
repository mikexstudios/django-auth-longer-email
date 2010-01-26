from distutils.core import setup

setup(
    name = 'django_auth_longer_email',
    packages = ['django_auth_longer_email'],
    version = '1.0.0',
    description = "Simple django app that patches auth.User's email field to 254 char.",
    author='Michael Huynh',
    author_email='mike@mikexstudios.com',
    url='http://github.com/mikexstudios/django_auth_longer_email',
    classifiers=[
        'Programming Language :: Python', 
        'Framework :: Django', 
        'License :: OSI Approved :: MIT License',
    ]
)

