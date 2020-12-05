from setuptools import setup


setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/jcabrerahi/sklearn_transforms-master/',
      author='Julio Cabrera',
      author_email='jcabrerahi1@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      # install_requires=[
      #    'my_dependency==1.1.0'
      # ],
      zip_safe=False
)
