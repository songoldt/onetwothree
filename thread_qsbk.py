import requests,re,threading
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#多线程开启
class qsbk_one(threading.Thread):
     def __init__(self):
          threading.Thread.__init__(self)
          self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
     def run(self):
          for i in range(1,6,2):
               url = 'http://www.qiushibaike.com/8hr/page/'+str(i)
               data = requests.get(url,headers=self.headers,timeout=10).content.decode('utf-8','ignore')
               pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
               data_list = re.compile(pat,re.S).findall(data) #re.S表示：.(点)也能匹配换行符
               file = 'qiubai.txt'
               for j in range(len(data_list)):
                    print('\n第'+str(i+1)+'页第'+str(j+1)+'条段子内容是：')
                    print(data_list[j].strip())
                    try:
                         with open(file,'a',encoding='utf-8') as fh:
                              fh.write(data_list[j].lstrip())
                    except  Exception as e:
                         print('意外不：'+str(e))

class qsbk_two(threading.Thread):
     def __init__(self):
          threading.Thread.__init__(self)
          self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
     def run(self):
          for i in range(2,6,2):
               url = 'http://www.qiushibaike.com/8hr/page/'+str(i)
               data = requests.get(url,headers=self.headers,timeout=10).content.decode('utf-8','ignore')
               pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
               data_list = re.compile(pat,re.S).findall(data) #re.S表示：.(点)也能匹配换行符
               file = 'qiubai.txt'
               for j in range(len(data_list)):
                    print('\n第'+str(i+1)+'页第'+str(j+1)+'条段子内容是：')
                    print(data_list[j].strip())
                    try:
                         with open(file,'a',encoding='utf-8') as fh:
                              fh.write(data_list[j].lstrip())
                    except  Exception as e:
                         print('意外不：'+str(e))
if __name__ == '__main__':
     one = qsbk_one()
     two = qsbk_two()
     one.start()
     two.start()
'''
     t1 = qsbk(name='One',area=range(1,6,2))
     t2 = qsbk(name='Two',area=range(2,6,2))
     t1.start()
     t2.start()
     t1.join()
     t2.join()
'''




               
                              
