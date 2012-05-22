from setuptools import setup, find_packages

version = '1.0-rc2'

setup(
    name='gu.js.qtip2',
    version=version,
    description="Plone-ready packaging of qtip2",
    long_description="Plone-ready packaging of qtip2",
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Matthew Trevor',
    author_email='matthew.trevor@griffith.edu.au',
    url='http://www.griffith.edu.au/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gu', 'gu.js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
