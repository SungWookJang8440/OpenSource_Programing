import os
import sys
# 추가됨: Sphinx가 상위 폴더에 있는 app.py와 validator.py를 찾을 수 있도록 경로를 설정합니다.
sys.path.insert(0, os.path.abspath('../..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My profile API'
copyright = '2026, 장성욱'
author = '장성욱'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#  수정됨: 파이썬 코드와 독스트링을 자동으로 읽어오기 위한 확장 프로그램들 [cite: 838, 839]
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#  수정됨: 기본 테마(alabaster) 대신 훨씬 깔끔하고 전문적인 ReadTheDocs 테마로 변경 [cite: 851]
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']