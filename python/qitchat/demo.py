import os
import json
import time
import requests


def send_wechat(agent_id, secret, company_id, message):
    """
    :param agent_id: 应用ID
    :param secret: 应用Secret
    :param company_id: 企业ID
    """
    # 通行密钥
    access_token = None
    # 如果本地保存的有通行密钥且时间不超过两小时，就用本地的通行密钥
    if os.path.exists('ACCESS_TOKEN.txt'):
        txt_last_edit_time = os.stat('ACCESS_TOKEN.txt').st_mtime
        now_time = time.time()
        print('ACCESS_TOKEN_time:', int(now_time - txt_last_edit_time))
        if now_time - txt_last_edit_time < 7200:  # 官方说通行密钥2小时刷新
            with open('ACCESS_TOKEN.txt', 'r') as f:
                access_token = f.read()
                # print(ACCESS_TOKEN)

    # 如果不存在本地通行密钥，通过企业ID和应用Secret获取
    if not access_token:
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={company_id}&corpsecret={secret}').json()
        access_token = r["access_token"]
        # print(ACCESS_TOKEN)
        # 保存通行密钥到本地ACCESS_TOKEN.txt
        with open('ACCESS_TOKEN.txt', 'w', encoding='utf-8') as f:
            f.write(access_token)

    # 要发送的信息格式
    data = {
        "touser": "WeiXunSenLin",
        # "touser": "PangQiLong",
        "msgtype": "text",
        "agentid": f"{agent_id}",
        "text": {"content": f"{message}"}
    }
    # 字典转成json，不然会报错
    data = json.dumps(data)
    # 发送消息
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}', data=data)
    print(r.json())


if __name__ == '__main__':
    # 应用ID
    agent_id = '1000002'
    # 应用Secret
    app_secret = 'Bd5IXppPJxBBtvBLmvImPX-BJecLR-_G3qXG6nrXtdk'
    # 企业ID
    company_id = 'wwe8e74a41f78abd5b'
    # 发送的消息
    message = '等一一增加一个自动回复功能，我们就可以聊天了！'
    send_wechat(agent_id, app_secret, company_id, message)
