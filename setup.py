# ==============================================================================#
#                                                                               #
#                                  Fraunhofer FOKUS                             #
#                                                                               #
#                                                                               #
#    All rights reserved. Distribution or duplication without previous          #
#    written agreement of the owner prohibited.                                 #
#                                                                               #
# ===============================================================================
# ===============================================================================
# -*-coding:utf-8-*-
# : $  wang_library
# : $  Ya Wang
# : $  19.04.2023
# ===============================================================================
from setuptools import setup, find_packages

setup(
    name='wang_library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your library dependencies here, for example:
        'matplotlib',
    ],
    # Add more package metadata as needed, e.g., author, description, etc.
)