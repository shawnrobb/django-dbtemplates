from setuptools import setup, find_packages

setup(
    name='django-dbtemplates',
    version=__import__('dbtemplates').__version__,
    description='Template loader for database stored templates with extensible cache backend',
    long_description=open('docs/overview.txt').read(),
    author='Jannis Leidel',
    author_email='jannis@leidel.info',
    url='http://github.com/jezdez/django-dbtemplates/wikis/',
    download_url='http://cloud.github.com/downloads/jezdez/django-dbtemplates/django-dbtemplates-0.5.5.tar.gz',
    packages=find_packages(),
    zip_safe=False,
    package_data = {
        'dbtemplates': [
            'locale/*/LC_MESSAGES/*',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
