from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='steering_reasoning_models',
    version='0.9.0',
    packages=find_packages(),
    install_requires=requirements,
    author='Rauno Arike',
    author_email='rauno.arike@gmail.com',
    description='Steering the chain of thought of reasoning LLMs',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.10',
)
