import setuptools

setuptools.setup(
    name='certifiable-calib',
    version='0.1.0',
    description='Certifiably globally optimal extrinsic calibration for sensors providing egomotion estimates.',
    author='James Guzman',
    author_email='jamesmguzman94@gmail.com',
    license='MIT',
    # packages=['python', 'python.pose_simulator', 'python.extrinsic_calibration', 'python.extrinsic_calibration.utility', 'python.extrinsic_calibration.solver', 'python.extrinsic_calibration.andreff', 'python.extrinsic_calibration.andreff.liegroups.numpy', 'python.extrinsic_calibration.andreff.liegroups.torch'],
    packages=setuptools.find_packages(),
    install_requires=['future', 'numpy', 'liegroups', 'scipy', 'matplotlib', 'cvxpy']
)
