from setuptools import setup

package_name = 'rtk'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zj',
    maintainer_email='zj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test=rtk.test1:main",
            "ntripServerByCors=rtk.ntripServerByCors:main",
            "ntripClient=rtk.ntripClient:main",
            "connectSignal=rtk.connectSignal:main",
            "getCoordinatePoint=rtk.getCoordinatePoint:main",

        ],
    },
)
