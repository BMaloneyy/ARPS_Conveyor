from setuptools import setup
import os
from glob import glob

package_name = 'conveyor_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[ #(os.path.join("share", package_name), glob("launch/*.launch.py"))
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Brian Maloney',
    maintainer_email='brian.maloney@nist.gov',
    description='Conveyor Package',
    license='Apache 2.0 License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["conveyor_node = conveyor_control.conveyor_node:main",
        ],
    },
)
