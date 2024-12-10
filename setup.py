import setuptools

setuptools.setup(
    name='certifiable-calib',
    version='0.1.0',
    description='Certifiably globally optimal extrinsic calibration for sensors providing egomotion estimates.',
    author='James Guzman',
    author_email='jamesmguzman94@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['future', 'numpy', 'liegroups', 'scipy', 'matplotlib', 'cvxpy']
)
