from json2html import *

line="""
181031 Wed
09,24 Act1

09,29 Act2

11,53 Act2

12,58 Act3

13,56 Act4
"""
# c sp_hf: save place of html file
sp_hf="/home/my_com"

# c li: temp list
li=line.replace("\n","*").replace("**","*").split("*")

# Delete first and last unnecessary character
del li[0]
del li[-1]

# c te_li: temp list2
te_li=[]
for line in li:
    # c time: time part
    time=line[:5]
    # c act: action part
    act=line[6:]
    # c front: front part of string
    front='{ "time": '+'"'+time+'",'
    # c rear: rear part of string
    rear='       "act": ' + '"' + act + '" }'
    # c final: final merged part of string
    final=front+rare
    # Append each one to list
    te_li.append(final)

# c proc1: processed 1
proc1=str(te_li).replace("[\'","").replace("\'","").replace("]","")
# c proc2: processed 2
proc2="["+proc1+"]"

# Process json format string into html markup language
html_mu=json2html.convert(json = proc2)
print(html_mu)

with open(sp_hf+"/manage_your_time_history.html", "a") as f:
    f.write(html_mu)
