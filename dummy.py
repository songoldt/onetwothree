import urllib.request as ur,time,requests,grequests,random
from multiprocessing.dummy import Pool as ThreadPool
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

opener = ur.build_opener()
opener.addheaders=[headers]
ur.install_opener(opener)
a = time.time()
urls = ['http://www.qiushibaike.com/8hr/page/{num}'.format(num=i) for i in range(1,21)]
pool = ThreadPool(12)
results = pool.map(requests.get,urls)
print('第一次多线程运行#cost time:{t}s'.format(t=time.time()-a))
pool.close()
pool.join()
time.sleep(random.random()*10)

print('='*30)
b = time.time()
url = 'http://www.qiushibaike.com/8hr/page/{num}'
urls = [url.format(num=i) for i in range(1,21)]
rs = (grequests.get(u) for u in urls)
resps = grequests.map(rs)
print('第二次异步运行#cost time:{q}s'.format(q=time.time()-b))
time.sleep(random.random()*10)

print('—'*30)
c = time.time()
results = []
url = 'http://www.qiushibaike.com/8hr/page/{num}'
for i in range(1,21):
     result = requests.get(url.format(num=i))
     results.append(result)
print('第三次普通运行#cost time:{m}s'.format(m=time.time()-c))









