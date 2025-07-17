from setuptools import setup

package_name = 'phantom_hmi'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[('share/' + package_name, ['package.xml'])],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Samuel Cruz',
    maintainer_email='samuel@example.com',
    description='HMI independiente para el Phantom Pincher',
    entry_points={
        'console_scripts': [
            'phantom_hmi = phantom_hmi.hmi_main:main',
        ],
    },
)
