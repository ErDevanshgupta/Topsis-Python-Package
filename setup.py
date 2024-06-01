

from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)'
LONG_DESCRIPTION = 'TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method that helps identify the best solution from a set of alternatives. The core idea is to choose the alternative that is closest to the positive ideal solution (PIS) and farthest from the negative ideal solution (NIS). The process begins with constructing a decision matrix that lists all alternatives and criteria. This matrix is then normalized to make the criteria comparable. Next, the normalized matrix is weighted according to the importance of each criterion. The PIS and NIS are identified by selecting the best and worst values for each criterion. The Euclidean distance of each alternative from the PIS and NIS is calculated, which helps determine the relative closeness of each alternative to the ideal solutions. The alternative with the highest relative closeness value is considered the best choice. TOPSIS is advantageous due to its simplicity, ease of understanding, and flexibility in handling various criteria and alternatives. It is widely used across fields such as engineering, business, healthcare, and environmental management for tasks like material selection, project management, supplier evaluation, and sustainability assessments. However, the methods effectiveness can be influenced by the subjective assignment of weights to criteria and the choice of normalization technique. Despite these limitations, TOPSIS remains a powerful tool for decision-makers, offering clear and logical solutions based on a well-defined process.'

# Setting up
setup(
    name="Devansh_Topsis_Package",
    version=VERSION,
    author="Devansh Gupta",
    author_email="<guptadevanshof2003@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
) 