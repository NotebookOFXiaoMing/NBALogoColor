from setuptools import setup

REQUIRED_PACKAGES = ['pyyaml']

with open("README.md",'r') as fh:
      long_description = fh.read()

setup(name="nba_logo_color",
      version='0.0.1',
      description="You can get the nab team logo color",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['NBALogoColor'],
      author_email="mingyan24@126.com",
      author="MingYan",
      install_requires=REQUIRED_PACKAGES,
      scripts=['bin/pick_team_color',
               'bin/load_nbateam_name.py'],
      zip_safe=False)