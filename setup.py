from setuptools import setup

setup(
    name="redfish_hp_ilo",
    version="0.0.1",
    description="Redfish API implementation on HPE servers with iLO RESTful API,",
    keywords="python, hp ilo, rest api, hp, ipmi",
    author="Kalinin Dmitry <kalinin.mitko@gmail.com>",
    url="https://github.com/null-none/redfish-hp-ilo",
    license="MIT",
    packages=["redfish_hp_ilo"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["redfish==3.1.9",],
)