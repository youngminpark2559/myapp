# Dependency:
1. pip install json2html==1.2.1

# Support format
1. Space  
<pre><code>
line="""
181031 Wed
09,24 Act1

09,29 Act2

11,53 Act2

12,58 Act3

13,56 Act4

13,56 Act5
"""
</code></pre>

2. Compact  
<pre><code>
line="""
181031 Wed
09,24 Act1
09,29 Act2
11,53 Act2
12,58 Act3
13,56 Act4
13,56 Act5
"""
</code></pre>

3. Mixed  
<pre><code>
line="""
181031 Wed
09,24 Act1
09,29 Act2

11,53 Act2

12,58 Act3

13,56 Act4
13,56 Act5
"""
</code></pre>  

# How to run
1. Open main.py
2. Copy and paste your time to main.py
For example,  
<pre><code>
line="""
181031 Wed
09,24 Act1
09,29 Act2
11,53 Act2
12,58 Act3
13,56 Act4
"""
</code></pre>  

3. Write save place of being created html file to main.py
For example,
sp_hf="/home/young"

4. Run main.py
1) Move to directory where main.py is stored
2) python main.py

# Example
1. Write time text  
![001_line](https://raw.githubusercontent.com/youngminpark2559/myapp/master/manage/myth/pics/001_line.png)
2. Get html table code from above time text  
![002_html_table_code](https://raw.githubusercontent.com/youngminpark2559/myapp/master/manage/myth/pics/002_html_table_code.png)
3. Create html file from above html table code  
![003_html](https://raw.githubusercontent.com/youngminpark2559/myapp/master/manage/myth/pics/003_html.png)
