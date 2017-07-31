#coding:utf-8
import requests,time,pymysql
def main():
    for k in range(1,2):#19000
        url="https://comp-sync.webapp.163.com/g37/sync_paged_list?per_page=200&page=%s&_=%s"%(k,time.time())
        response=requests.get(url)
        result=response.json()
        # print (result['data'])
        values=[]
        for j in result['data']:
            value=(
                j['req_id'],
                j['get_time'],
                j['prop_info']['from'],
                j['prop_info']['prop_name'].split("式神")[0],
                j['prop_info']['prop_name'].split("式神")[-1],
                j['user_info']['nick'],
                j['user_info']['server'],
                j['user_info']['uid'])
            values.append(value)
        print (values)
        return values

def mysql(value):
    connect=pymysql.connect(host='localhost',db='for_fun',user='root',passwd='',port=3306,charset='utf8')
    cursor=connect.cursor()
    sql="insert into yys VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,value)
    connect.commit()

if __name__ == '__main__':
    values=main()
    for i in values:
        mysql(i)
