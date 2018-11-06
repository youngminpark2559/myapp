# Dependency:
1. pip install json2html==1.2.1

# ======================================================================
# Support format
1. Space
line="""
181031 Wed
09,24 Act1

09,29 Act2

11,53 Act2

12,58 Act3

13,56 Act4

13,56 Act5
"""

2. Compact
line="""
181031 Wed
09,24 Act1
09,29 Act2
11,53 Act2
12,58 Act3
13,56 Act4
13,56 Act5
"""

3. Mixed
line="""
181031 Wed
09,24 Act1
09,29 Act2

11,53 Act2

12,58 Act3

13,56 Act4
13,56 Act5
"""

# ======================================================================
# How to run
1. Open main.py
2. Copy and paste your time to main.py
For example,
line="""
181031 Wed
09,24 Act1
09,29 Act2
11,53 Act2
12,58 Act3
13,56 Act4
"""
3. Write save place of being created html file to main.py
For example,
sp_hf="/home/young"

4. Run main.py
1) Move to directory where main.py is stored
2) python main.py
