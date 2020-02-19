from setuptools import setup, find_packages
setup(
    name='Team_4_Package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Analyse - Predict. Functions use Eskom data/variables.',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/Ron-AllanYisa/Team-4',
    author='Team 5: [Allan Yisa],[Lee-Roy Yonga],[Orifha Singo],[Clarencia Mondlana],[Duduzile Ngwenya]',
    author_email='allanyisa@gmail.com'
)
