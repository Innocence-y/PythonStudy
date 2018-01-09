#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import  AES
import base64
import requests
import json
import codecs
import time

#头部信息
headers={
    'HOST':"music.163.com",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate, sdch",
    'Content-Type': "application/x-www-form-urlencoded",#text/html;charset=utf8
    'Cookie': "JSESSIONID-WYYY=cd1Rl3VE3QCuWrM1F2p5X2uldz7nID%5CPkiCScp1xwmj%5CQaK1ntkfjHrdsOIPo63qTVSQ%2F31E5R19S8qrlWscJtCZM4fHnp25P%2FHrDweHD91%2FeaFxBD%2Fq6efikdBYg9mDhDAHy0yW23r6iGkCIUE4NGQYNw4oMbmeNiBuf%2BTNfh6MysQ%2B%3A1491229798294; _iuqxldmzr_=32; _ntes_nnid=d805c50ad0597b9a6f15c3a0724ac9f3,1491227998322; _ntes_nuid=d805c50ad0597b9a6f15c3a0724ac9f3; __utma=94650624.196941009.1491227999.1491227999.1491227999.1; __utmb=94650624.8.10.1491227999; __utmc=94650624; __utmz=94650624.1491227999.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; playerid=36222054",
    'Connection': "keep-alive",
    'Referer': 'http://music.163.com/'
}
# 设置代理服务器
proxies = {
    'http:': 'http://121.232.146.184',
    'https:': 'https://144.255.48.197'
}

# offset的取值为:(评论页数-1)*20,total第一页为true，其余页为false
# first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}' # 第一个参数
second_param = "010001"  # 第二个参数
# 第三个参数
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# 第四个参数
forth_param = "0CoJUm6Qyw8W8jud"


# 获取参数
def get_params(page):  # page为传入页数
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    if (page == 1):  # 如果为第一页
        first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        h_encText = AES_encrypt(first_param, first_key, iv)#加密方式是第一个参数和最后一个参数通过固定iv加密
    else:
        offset = str((page - 1) * 20)
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false')
        h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)#第二次加密是上次加密返回值与一个16位的任意字符串加密
    return h_encText


# 获取 encSecKey
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


# 解密过程
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    #print(type(text))
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text).decode()
    return encrypt_text


# 获得评论json数据
def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data, proxies=proxies)
    return response.content



# 抓取某一首歌的全部评论
def get_all_comments(url):
    all_comments_list = []  # 存放所有评论
    all_comments_list.append(u"用户ID 用户昵称 用户头像地址 评论时间 点赞总数 评论内容\n")  # 头部信息
    params = get_params(1)
    encSecKey = get_encSecKey()
    json_text = get_json(url, params, encSecKey).decode()
    json_dict = json.loads(json_text)
    comments_num = int(json_dict['total'])
    if (comments_num % 20 == 0):
        page = int(comments_num / 20)
    else:
        page = int(comments_num / 20) + 1
    print("共有%d页评论!" % page)
    print(type(page))
    for i in range(page):  # 逐页抓取
        params = get_params(i + 1)
        encSecKey = get_encSecKey()
        json_text = get_json(url, params, encSecKey).decode()
        json_dict = json.loads(json_text)
        if i == 0:
            print("共有%d条评论!" % comments_num)  # 全部评论总数
        for item in json_dict['comments']:
            comment = item['content']  # 评论内容
            likedCount = item['likedCount']  # 点赞总数
            comment_time = item['time']  # 评论时间(时间戳)
            userID = item['user']['userId']  # 评论者id
            nickname = item['user']['nickname']  # 昵称
            avatarUrl = item['user']['avatarUrl']  # 头像地址
            comment_info = str(userID) + u" " + nickname + u" " + avatarUrl + u" " + str(
                comment_time) + u" " + str(likedCount) + u" " + comment + u"\n"
            all_comments_list.append(comment_info)
        print("第%d页抓取完毕!" % (i + 1))
    return all_comments_list

# 抓取热门评论，返回热评列表
def get_hot_comments(url):
    hot_comments_list = []
    hot_comments_list.append("用户ID   " + u"\t" + "用户昵称" + u"\t" + "评论时间" + u"\t" + "点赞总数" + u"\t" + "评论内容" + u"\t"  + u"\r\n")
    params = get_params(1)  # 第一页
    encSecKey = get_encSecKey()
    json_text = get_json(url,params,encSecKey).decode()
    json_dict = json.loads(json_text)
    hot_comments = json_dict['hotComments']  # 热门评论
    #print(hot_comments)
    print("共有%d条热门评论!" % len(hot_comments))
    for item in hot_comments:
        comment = item['content']  # 评论内容
        likedCount = item['likedCount']  # 点赞总数
        #comment_time = item['time'] / 1000 # 评论时间(时间戳)除1000转化为10位时间戳
        #print(comment_time)
        # 转换成localtime
        time_local = time.localtime(item['time'] / 1000)
        comment_time = time.strftime("%Y-%m-%d", time_local)
        userId = item['user']['userId']  # 评论者id
        nickname = item['user']['nickname']  # 昵称
        #print(type(comment))
        comment_info = str(userId) + u"\t"  +nickname+u"\t" +str(comment_time)+u"\t" +str(likedCount)   +u"\t\t" +   comment + u"\r\n"
        hot_comments_list.append(comment_info)
    return hot_comments_list

def save_to_file(list, filname):
    with codecs.open(filename, 'a', encoding='utf-8') as f:
        f.writelines(list)
    print("写入文件成功!")


if __name__ == "__main__":
    start_time = time.time()
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_185821?csrf_token"
    filename = "搁浅.txt"
    all_comments_list = get_all_comments(url)
    save_to_file(all_comments_list, filename)
    #hot_comments = get_hot_comments(url)
    #print(hot_comments)
    #save_to_file(hot_comments,filename)
    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))