#coding:utf-8
import time
def get_url():
    spider_url=[]
    for k in range(1,10000):
        url="https://comp-sync.webapp.163.com/g37/sync_paged_list?per_page=200&page=%s&_=%s"%(k,time.time())
        spider_url.append(url)
    return spider_url

if __name__ == '__main__':
    get_url()
