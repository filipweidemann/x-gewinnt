from setuptools import setup, find_packages
setup(
    name = "x-in-a-row",
    version = "0.1",
    zip_safe = True,
    packages = find_packages(),
    install_requires = ['flask', 'pytest', 'wtforms', 'gevent'],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest', 'wtforms', 'gevent', 'flask'],
    package_data = {},
    author = 'Filip Weidemann',
    author_email = 'filip.weidemann@outlook.de',
    description = 'Basically 4-in-a-row, except x...',
    license = 'Apache License 2.0',
    keywords = 'x-in-a-row',
    url = '',
    entry_points = {'console_scripts': ['x-in-a-row-tty=maintty:main', 'web=webservice_gevent_wsgi:main']})
