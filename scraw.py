from pyquery import PyQuery as pyq

html = ''' 
<html>
    <title>这是标题</title>
<body>
    <p id="hi">Hello</p>
    <ul>
        <li>list1</li>
        <li>list2</li>
    </ul>
</body>
</html>
'''
jq = pyq(html)
#print(jq('title'))
#print(jq('title').text())
#print(jq('#hi').text())
li = jq('li')
html = pyq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'}).html()
html = html.replace("&#13;", "")
print(html)

