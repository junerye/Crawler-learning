
#!/usr/local/bin/python3
#encoding:utf8

'''
    作用:爬取京东商城手机分类下的的所有手机商品的展示图片。
    url:为需要爬取的网址
    page：页数
'''

import re  
import urllib.request  
  
def  getimage(url, page):  
    html = urllib.request.urlopen(url).read();  
    html = str(html);  
    pattern1 = '<div id="plist".+? <div class="page clearfix">';  
    rst1 = re.compile(pattern1).findall(html);  
    rst1 = rst1[0];  
    pattern2 = '<img width="220" height="220" .+?//.+?\.jpg';  
    imagelist = re.compile(pattern2).findall(rst1);  
  
    x = 1;  
    for imageurl in imagelist:  
        imagename = "Desktop/jd/"+str(page)+"-"+str(x)+".jpg";  
        pattern3 = '//.+?\.jpg';  
        imageurl = re.compile(pattern3).findall(imageurl);  
        imageurl = "http:"+imageurl[0];  
        try:  
            urllib.request.urlretrieve(imageurl, filename=imagename);  
        except urllib.error.URLError as e:  
            if hasattr(e, 'code'):  
                x+=1;  
            if hasattr(e, 'reason'):  
                x+=1;  
        x+=1;  
  
for i in range(1, 2):  
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i);  
    getimage(url, i);  
