### SETUP

from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as req:
    req_list = req.readlines()
    req_list = [sd.replace('\n', '') for sd in req_list]

requirements = req_list
test_requirements = ['pytest>=3']

setup(
    author="Hu_Hesheng-G5",
    email="",
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Creative image optimization",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts',
    name='scripts',
    packages=find_packages(include=['scripts', 'scripts.*',
                                    'data','tests', 'notebooks']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Hu-Hesheng/creative_image_optimization',
    version='1.0.0',
    zip_safe=False,
)
