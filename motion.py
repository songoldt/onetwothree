import urllib.request as ur
import re
import urllib.error as ue

#伪装成浏览器
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
opener=ur.build_opener()
opener.addheaders=[headers]
ur.install_opener(opener)

comid ="6332961593869642524"
# 报错如果是证书有误（SSL error）此时网址需要注意，是http协议，不是https
def get_cmt(url):
     for i in range(0,2) :
          data = ur.urlopen(url).read().decode('utf-8','ignore')
          patnext = '"last":"(.*?)"'
          nextid = re.compile(patnext).findall(data)[0] #列表里面去第一个元素
          patcom = '"content":"(.*?)",'
          comdata = re.compile(patcom).findall(data)
          tlabels = []
          for j in range(0,len(comdata)):
               print('第'+str(i)+str(j)+"条评论内容是：")
               print(eval('u"'+comdata[j]+'"')) #常规：u'content' 或者u"content"，转码，用eval（）函数把content转换数据格式
               thislabel = input("请输入评论【0-负向 1-正向 2-中兴】感情类别: ")
               tlabels.append(thislabel)
          
               if len(tlabels)>8 :
                    break 
               
     url = "http://video.coral.qq.com/filmreviewr/c/upcomment/i5w51tl7vbl5mid?commentid="+nextid+"&reqnum=3&callback=jQuery1124011741735606122239_1510208126058&_=1510208126063"
     get_cmt(url) #强行添加退出递归的条件
     
url="http://video.coral.qq.com/filmreviewr/c/upcomment/i5w51tl7vbl5mid?commentid="+comid+"&reqnum=3&callback=jQuery1124011741735606122239_1510208126058&_=1510208126063"
get_cmt(url)
