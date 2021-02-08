# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
#爬取页面数据
def get_url_content(url):
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}
    response = requests.get(url, headers=header)
    url_content = response.text
    soup_url_content = BeautifulSoup(url_content,'html.parser', from_encoding='utf-8')
    return soup_url_content
#分析页面结构
def page_parse(soup_url_content):
    body = soup_url_content.find('div', class_='tslb_b')
    df = pd.DataFrame(columns=['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态'])
    tr_list = body.find_all('tr')
    for tr in tr_list:
        body = {}
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            投诉编号, 投诉品牌, 投诉车系, 投诉车型, 问题简述, 典型问题, 投诉时间, 投诉状态 = \
                td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            body['投诉编号'], body['投诉品牌'], body['投诉车系'], body['投诉车型'], body['问题简述'], body['典型问题'], body['投诉时间'], body[
                '投诉状态'] = 投诉编号, 投诉品牌, 投诉车系, 投诉车型, 问题简述, 典型问题, 投诉时间, 投诉状态
            df = df.append(body, ignore_index=True)
    return df

#主函数
if __name__ == '__main__':
    pages = 20
    base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
    result = pd.DataFrame(columns=['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态'])
    for i in range(pages):
        request_url = base_url + str(i + 1) + '.shtml'
        soup = get_url_content(request_url)
        df = page_parse(soup)
        print(df)
        result = result.append(df)
    result.to_csv('12365auto.csv', index=False)
