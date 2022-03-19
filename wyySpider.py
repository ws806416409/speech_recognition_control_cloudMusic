"""
@Time       ：2022/3/19 20:49 
@File       ：wyySpider.py 
@Author     ：DizzyLime 
@Blog       ：https://lemonws.top
@Annotation : " "
"""
import json
import requests

global song

headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_user(user_id):
    """
    获取用户注册时间
    """
    data = {}
    url = 'https://music.163.com/api/v1/user/detail/' + str(user_id)
    response = requests.get(url=url, headers=headers)
    # 将字符串转为json格式
    js = json.loads(response.text)
    if js['code'] == 200:
        # 性别
        data['gender'] = js['profile']['gender']
        # 年龄
        if int(js['profile']['birthday']) < 0:
            data['age'] = 0
        else:
            data['age'] = (2022 - 1970) - (int(js['profile']['birthday']) // (1000 * 365 * 24 * 3600))
        if int(data['age']) < 0:
            data['age'] = 0
        # 城市
        data['city'] = js['profile']['city']
        # 个人介绍
        data['sign'] = js['profile']['signature']
    else:
        data['gender'] = '无'
        data['age'] = '无'
        data['city'] = '无'
        data['sign'] = '无'
    return data


def get_comment(sid, page):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(sid) + '?limit=20&offset=' + str(page)
    response = requests.get(url, headers)
    result = response.json()
    items = result['comments']
    for item in items:
        comment = item['content']
        user_id = str(item['user']['userId'])
        user_msg = get_user(user_id)
        user_age = str(user_msg['age'])
        user_gender = str(user_msg['gender'])
        user_city = str(user_msg['city'])

        with open('music_comments.csv', 'a', encoding='utf-8-sig') as f:
            f.write(
                user_id + ',' + user_age + ',' + user_gender + ',' + user_city + ',' + comment + '\n')
        f.close()


def main(sid):
    for i in range(0, 1000, 20):
        get_comment(sid, i)


if __name__ == '__main__':
    main()
