import urllib.request
import urllib.parse
import json
import jsonpath
import time

# json接口：
# 第一页https://fe-api.zhaopin.com/c/i/sou?kt=3&pageSize=90&cityId=西安&kw=python
# 第二页https://fe-api.zhaopin.com/c/i/sou?kt=3&start=90&pageSize=90&cityId=西安&kw=python
# 第三页https://fe-api.zhaopin.com/c/i/sou?kt=3&start=180&pageSize=90&cityId=西安&kw=python

class ZhiLianSpider(object):
	"""docstring for ZhiLianSpider"""
	url='https://fe-api.zhaopin.com/c/i/sou?kt=3&'
	def __init__(self, cityId,kw,start_page,end_page):
		super(ZhiLianSpider, self).__init__()
		self.cityId = cityId
		self.kw = kw
		self.start_page = start_page
		self.end_page = end_page
		self.jobs_list=[]

	def run(self):
		for page in range(self.start_page,self.end_page+1):
			print('正在爬取第%s页工作信息......' % page)
			url_string=self.get_url(page)
			json_text=self.get_json(url_string)
			self.get_inf(json_text)
			print('成功抓取第%s页工作信息......' % page)
			time.sleep(3)
		self.write_inf()

		print('下载完成............')

	def get_inf(self,json_text):
		#将json文本转换成json对象
		obj=json.loads(json_text)
		jobs=obj['data']['results']
		for job in jobs:
			jobName=jsonpath.jsonpath(job,'$..jobName')[0]
			companyName=jsonpath.jsonpath(job,'$..company.name')[0]
			city=jsonpath.jsonpath(job,'$..city.items..name')[0]
			shuxing=jsonpath.jsonpath(job,'$..company.type.name')[0]
			# start_time=jsonpath.jsonpath(job,'$..createDate')[0]
			# end_time=jsonpath.jsonpath(job,'$..endDate')[0]
			salary=jsonpath.jsonpath(job,'$..salary')[0]
			# recruitCount=job['recruitCount']
			welfare=','.join(job['welfare'])
			item={
				'岗位名称':jobName,
				'工资待遇':salary,
				'工作城市':city,
				# '招聘人数':recruitCount,
				'公司性质':shuxing,
				'公司名称':companyName,
				'福利待遇':welfare,
				# '开始时间':start_time,
				# '结束时间':end_time,
			}
			self.jobs_list.append(item)

	def write_inf(self):
		string=json.dumps(self.jobs_list,ensure_ascii=False)
		with open('jobs.txt','w',encoding='utf8') as fp:
			fp.write(string+"\n")


	def get_json(self,url):
		headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
		}
		request=urllib.request.Request(url=url,headers=headers)
		json_text=urllib.request.urlopen(request).read().decode()
		# json_text=json_text.strip('()\n \t \r')去除json格式字符串两边所有的(,)\n,\t,\r
		return(json_text)

	def get_url(self,page):
		if page==1:
			data = {
				'cityId':self.cityId,
				'kw':self.kw,
				'pageSize':90,
			}
		else:
			data = {
				'cityId':self.cityId,
				'kw':self.kw,
				'pageSize':90,
				'start':(page-1)*90,
			}
		query_string=urllib.parse.urlencode(data)
		url_string = self.url+query_string
		return(url_string)

def main():
	cityId=input('请输入搜索的城市名称：')
	kw=input('请输入搜索的关键字：')
	start_page=int(input('请输入爬取的起始页码：'))
	end_page=int(input('请输入爬取的结束页码：'))

	#创建一个对象
	spider=ZhiLianSpider(cityId,kw,start_page,end_page)
	spider.run()

if __name__ == '__main__':
	main()

