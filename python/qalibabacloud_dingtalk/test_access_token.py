from alibabacloud_tea_openapi.models import Config
from alibabacloud_dingtalk.oauth2_1_0.client import Client
from alibabacloud_dingtalk.oauth2_1_0.models import GetAccessTokenRequest

config = Config(
    protocol='https',
    region_id='central',
)
client = Client(config=config)


def test_get_access_token():
    """
    获取access_token
    {
        'headers': {
            'server': 'DingTalk/1.0.0',
            'date': 'Tue, 11 Apr 2023 03:04:31 GMT',
            'content-type': 'application/json;charset=utf-8',
            'content-length': '66',
            'connection': 'keep-alive',
            'access-control-allow-origin': '*',
            'x-acs-request-id': '69FF832F-0AEE-710E-A94F-617077C8D913',
            'x-acs-trace-id': 'bb7cd87f0d806ebaaec8617b64feb8e4',
            'access-control-allow-headers': 'X-Requested-With, X-Sequence, _aop_secret, _aop_signature, x-acs-dingtalk-access-token',
            'content-security-policy-report-only': "default-src 'self';style-src 'self' 'unsafe-inline' dev.g.alicdn.com g.alicdn.com at.alicdn.com *.test.youku.com *.taobao.net webapi.amap.com;script-src 'report-sample' 'self' 'unsafe-eval' 'unsafe-inline' *.dingtalk.com *.cnzz.com *.alicdn.com market.wapa.taobao.com g.alicdn.com dev.g.alicdn.com ynuf.alipay.com log.mmstat.com s.tbcdn.cn vip.laiwang.com wswukong.laiwang.com local.alipcsec.com:6691 *.taobao.net cfd.aliyun.com restapi.amap.com webapi.amap.com retcode.alicdn.com cfall.aliyun.com gw.alipayobjects.com ynuf.aliapp.org;connect-src 'self' *.dingtalk.com wss://*.dingtalk.com ynuf.alipay.com dev.g.alicdn.com g.alicdn.com retcode.taobao.com dingtalk-cspase-sh.oss-cn-shanghai.aliyuncs.com dingtalk-cspase-sz.oss-cn-shenzhen.aliyuncs.com arms-retcode.aliyuncs.com arms-retcode.aliyuncs.com ynuf.aliapp.org px-intl.ucweb.com px.ucweb.com gm.mmstat.com preview-lippi-space-zjk.oss-accelerate.aliyuncs.com wgo.mmstat.com wss://alidocs-body.oss-accelerate.aliyuncs.com wss://pre-collab.dingtalk.com *.mobgslb.tbcache.com *.mmstat.com px.effirst.com;frame-src 'self' h5.m.taobao.com qiye.aliyun.com log.laiwang.com dev.g.alicdn.com g.alicdn.com login.dingtalk.com login2.dingtalk.com *.dingtalk.com mailsso.mxhichina.com wvjbscheme: alipaybridge: alipaymonitor: mmstat.alicdn.com res.mmstat.com ynuf.aliapp.org alidocs.oss-cn-zhangjiakou.aliyuncs.com;font-src 'self' at.alicdn.com dev.g.alicdn.com g.alicdn.com data: *.taobao.net i.alicdn.com;img-src 'self' data: http: fourier.taobao.com *.dingtalk.com *.aliimg.com *.alicdn.com *.mmstat.com ynuf.alipay.com arms-retcode.aliyuncs.com pin.aliyun.com fourier.alibaba.com retcode.taobao.com *.cnzz.com dingtalk-cspase-sh.oss-cn-shanghai.aliyuncs.com dingtalk-cspase-sz.oss-cn-shenzhen.aliyuncs.com restapi.amap.com kcart.alipay.com preview-lippi-space-zjk.oss-cn-zhangjiakou.aliyuncs.com px-intl.ucweb.com px.ucweb.com alidocs.oss-cn-zhangjiakou.aliyuncs.com;media-src 'self' *.dingtalk.com cloud.video.taobao.com videocdn.taobao.com tbm-auth.alicdn.com dev.g.alicdn.com g.alicdn.com;report-uri https://csp.dingtalk.com/csp;"
        },
        'body': {
            'accessToken': '9138f6b2157b325c8ccde568dda816ac',
            'expireIn': 7200
        }
    }
    """
    request = GetAccessTokenRequest(
        app_key='dingb7m909kvmh08ghfv',
        app_secret='5Kx6B37d_qfdKISCjfZ0HLazci1h3GwhuccLxlx9TmwAMigIdg9PFN97Bdxe6Ir5',
    )
    result = client.get_access_token(request)
    print(result)

    body = result.body
    access_token = body.access_token
    expire_in = body.expire_in
    print(f'Access token: {access_token}, expire in: {expire_in}')
    assert True
