from setuptools import find_packages, setup

package_name = 'face_display'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'pygame'],
    zip_safe=True,
    maintainer='autobeton1',
    maintainer_email='ahmedamoussaoui@gmail.com',
    description='TODO: Package description',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'eyes = face_display.eyes:main'
        ],
    },
)
