from distutils.core import setup
setup(
  name = 'pyCS',         # How you named your package folder (MyLib)
  packages = ['pyCS'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Helps solve CS problems with python',   # Give a short description about your library
  author = 'Ilya Hajiaghayi',                   # Type in your name
  author_email = 'ihajiaghayi@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Ilya28410/pyCS',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Ilya28410/pyCS/archive/refs/tags/v_011.zip',    # I explain this later on
  keywords = ['CODE','COMPUTER', 'CS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'hopcroftkarp'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3'      #Specify which pyhton versions that you want to support
  ],
)
