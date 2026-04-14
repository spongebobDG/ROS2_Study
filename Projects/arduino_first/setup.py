from setuptools import find_packages, setup

package_name = 'arduino_first'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch.py']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dg',
    maintainer_email='eorjs135795@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'arduino = arduino_first.arduino_node:main',
            'processing = arduino_first.processing_node:main',
            'alert = arduino_first.alert_node:main',
            
        ],
    },
)
