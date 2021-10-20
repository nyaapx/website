#!/bin/env python3

import os
import sys
import subprocess
import shutil

shutil.rmtree('labelplus_docs', ignore_errors=True)
subprocess.check_call(f"git clone https://github.com/LabelPlus/labelplus_docs", shell=True)
os.chdir('./labelplus_docs')
subprocess.check_call(f"git checkout mkdocs", shell=True)
subprocess.check_call(f"pip install pipenv", shell=True)
subprocess.check_call(f"pipenv install", shell=True)
subprocess.check_call(f"pipenv run mkdocs build", shell=True)
os.chdir('..')

shutil.rmtree('build', ignore_errors=True)
os.mkdir('build')
shutil.copytree('./static', './build', dirs_exist_ok=True)
shutil.copytree('./labelplus_docs/site', './build/labelplus_docs', dirs_exist_ok=True)
