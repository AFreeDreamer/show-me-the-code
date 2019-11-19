# -*- coding: utf-8 -*-
# 一个HTML文件，找出里面的**正文**。

from bs4 import BeautifulSoup

html = """
<html> <head >< title > The  Dormouse ’ s  story</title></head>
<body >
<p  class =" title"  name="dromouse ”>< b> The  Dormouse  ’ s story</b></p>
<p  class =” story ’'> Once  upon  a time  there  were  three  little  s isters;  and  their  names  were
<a  href =” http://example.com/elsie " class= "  sister " id =” linkl ”><  ! - Elsie … >< la>,
<a  href =” http://example.com/lacie " class =” sister " id =” link2 ”> Lacie</a>  and
<a  href="http://example.com/tillie "  class =” sister " id =” li nk3 ”> T illie</a> ;
and  they  lived  at  the  bottom  of  a well. </p>
<p  class =” story ”>  ...  </p>
"""

soup = BeautifulSoup(html,'lxml')
soup.prettify()
print(soup.body)