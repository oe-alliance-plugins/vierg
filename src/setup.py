from setuptools import setup
import setup_translate

pkg = 'Extensions.vierg'
setup(name='enigma2-plugin-extensions-vierg',
       version='3.0',
       description='Four wins game',
       package_dir={pkg: 'vierg'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
