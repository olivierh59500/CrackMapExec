from setuptools import setup, find_packages

setup(name='crackmapexec',
    version='3.1.5dev',
    description='A swiss army knife for pentesting Windows/Active Directory environments',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
    keywords='pentesting security windows smb active-directory networks',
    url='http://github.com/byt3bl33d3r/CrackMapExec',
    author='byt3bl33d3r',
    author_email='byt3bl33d3r@gmail.com',
    license='BSD',
    packages=find_packages(include=[
        "cme", "cme.*"
    ]),
    install_requires=[
        'impacket>=0.9.15',
        'gevent>=1.2.0',
        'netaddr',
        'pyOpenSSL',
        'pycrypto',
        'pyasn1',
        'termcolor',
        'requests',
        'msgpack-python'
    ],
    entry_points = {
        'console_scripts': ['crackmapexec=cme.crackmapexec:main', 'cme=cme.crackmapexec:main', 'cmedb=cme.cmedb:main'],
    },
    include_package_data=True,
    zip_safe=False)
