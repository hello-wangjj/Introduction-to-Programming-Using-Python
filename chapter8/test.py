d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    return '<tr><td style="color:red">%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
html='<table border="1">'+'<tr><th>Name</th><th>Score</th><tr>'+'\n'.join(tds)+'</table>'
with open('test.html','w') as f:
	f.write(html)
	f.close()

def isPlalindrome(s):
    s=str(s)
    low=0
    high=len(s)-1
    if s[low]!=s[high]:
        return False
    else:
        low+=1
        high-=1
    return True
print [x for x in range(1,1001) if isPlalindrome(x)]

