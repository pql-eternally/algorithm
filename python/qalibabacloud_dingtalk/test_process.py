import time
from datetime import datetime
from typing import Dict, List

from alibabacloud_tea_openapi.models import Config
from alibabacloud_dingtalk.workflow_1_0.client import Client as WorkflowClient
from alibabacloud_dingtalk.workflow_1_0 import models as workflow_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

config = Config(
    protocol='https',
    region_id='central',
)
client = WorkflowClient(config=config)


def test_list_user_visible_bpms_processes_with_options():
    """测试获取用户可见的审批流列表

    未携带token时，返回：
    {
        'code': 'AuthenticationFailed.MissingParameter',
        'requestid': '5C152A5C-801C-7041-A495-C830A8C9FB53',
        'message': '缺少参数：x-acs-dingtalk-access-token',
        'statusCode': 400
    }
    """
    request = workflow_models.ListUserVisibleBpmsProcessesRequest(
        max_results=100,
        next_token=0,
        user_id=None
    )
    headers = workflow_models.ListUserVisibleBpmsProcessesHeaders(
        x_acs_dingtalk_access_token='9138f6b2157b325c8ccde568dda816ac'
    )
    try:
        response = client.list_user_visible_bpms_processes_with_options(
            request, headers=headers, runtime=util_models.RuntimeOptions()
        )
    except Exception as e:
        print(e)
        assert False

    response_headers: Dict[str, str] = response.headers
    print(response_headers)

    response_body: workflow_models.ListUserVisibleBpmsProcessesResponseBody = response.body
    assert response_body is not None
    response_body_result: workflow_models.ListUserVisibleBpmsProcessesResponseBodyResult = response_body.result
    # 下一次分页调用的值，当返回结果里没有nextToken时，表示分页结束。
    next_token: int = response_body_result.next_token
    print(next_token)
    # 可见表单列表
    process_list: List[workflow_models.ListUserVisibleBpmsProcessesResponseBodyResultProcessList] = \
        response_body_result.process_list

    # 表单信息
    """
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '供应商合同', 'processCode': 'PROC-380D12E5-78D4-4597-95B0-FC71A76DEE8C', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-380D12E5-78D4-4597-95B0-FC71A76DEE8C#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '通知供应商发货单', 'processCode': 'PROC-9DC3728D-EAC7-43DF-B41F-0B1B249088A0', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-9DC3728D-EAC7-43DF-B41F-0B1B249088A0#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '采购单', 'processCode': 'PROC-77C75508-FDAE-4E38-B607-379BCFF53633', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-77C75508-FDAE-4E38-B607-379BCFF53633#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '访客登记', 'processCode': 'PROC-33212BCC-9891-458E-A5D4-413C2764DA38', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-33212BCC-9891-458E-A5D4-413C2764DA38#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1Yfa0CG6qK1RjSZFmXXX0PFXa-112-112.png', 'name': '请假', 'processCode': 'PROC-585E7B7A-2918-4AD9-B3AC-85CE8535F6DF', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-585E7B7A-2918-4AD9-B3AC-85CE8535F6DF#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1nGe6CIfpK1RjSZFOXXa6nFXa-102-102.png', 'name': '物品领用', 'processCode': 'PROC-0D8A0D97-3D41-4754-B6C0-2915BED91818', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-0D8A0D97-3D41-4754-B6C0-2915BED91818#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1V2S8CHrpK1RjSZTEXXcWAVXa-102-102.png', 'name': '通用审批', 'processCode': 'PROC-C0F8535B-E6AA-4408-8B17-B9749B273EFF', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-C0F8535B-E6AA-4408-8B17-B9749B273EFF#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1JVSVCHPpK1RjSZFFXXa5PpXa-102-102.png', 'name': '绩效自评', 'processCode': 'PROC-31389870-7F78-4F4E-9F27-E94C70D7372E', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-31389870-7F78-4F4E-9F27-E94C70D7372E#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1w.y9CQvoK1RjSZFNXXcxMVXa-112-112.png', 'name': '立项申请', 'processCode': 'PROC-8661AE2F-ACB6-433D-B8C9-B479FA4823D3', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-8661AE2F-ACB6-433D-B8C9-B479FA4823D3#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1uiy8CHvpK1RjSZPiXXbmwXXa-102-102.png', 'name': '招聘', 'processCode': 'PROC-5975B53C-BA5D-4B84-B510-8EA1FBC7B13B', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-5975B53C-BA5D-4B84-B510-8EA1FBC7B13B#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1bHOWCSzqK1RjSZFjXXblCFXa-112-112.png', 'name': '用车申请', 'processCode': 'PROC-3FCAA0E3-0A76-4D08-890B-CD2A6CBC657A', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-3FCAA0E3-0A76-4D08-890B-CD2A6CBC657A#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1V2S8CHrpK1RjSZTEXXcWAVXa-102-102.png', 'name': '用印申请', 'processCode': 'PROC-4B50B989-F6E0-4DFF-996E-DE061EDD7CF4', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-4B50B989-F6E0-4DFF-996E-DE061EDD7CF4#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1.rbgCNjaK1RjSZFAXXbdLFXa-102-102.png', 'name': '售后工单', 'processCode': 'PROC-6AA31189-DE3C-4B0D-9E03-E74ED9D54055', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-6AA31189-DE3C-4B0D-9E03-E74ED9D54055#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB197e_CHrpK1RjSZTEXXcWAVXa-102-102.png', 'name': '设备巡检', 'processCode': 'PROC-117D7772-49DE-4703-9361-66C9E36A4911', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-117D7772-49DE-4703-9361-66C9E36A4911#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1V2S8CHrpK1RjSZTEXXcWAVXa-102-102.png', 'name': '体验极速审批-申请单示例', 'processCode': 'PROC-3AA50DD6-5EDD-4D2D-B939-2C6A0F7ED351', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-3AA50DD6-5EDD-4D2D-B939-2C6A0F7ED351#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1jba9CFzqK1RjSZFoXXbfcXXa-102-102.png', 'name': '进出办公场所申请', 'processCode': 'PROC-CFA2EBA9-847D-4DD1-B0BD-5FD9020499F3', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-CFA2EBA9-847D-4DD1-B0BD-5FD9020499F3#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB15692CRLoK1RjSZFuXXXn0XXa-102-102.png', 'name': '办公场所消毒通风', 'processCode': 'PROC-CD833A6A-DD5E-4294-B681-B3F3D25192F3', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-CD833A6A-DD5E-4294-B681-B3F3D25192F3#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1CODaCFzqK1RjSZFCXXbbxVXa-102-102.png', 'name': '防疫物资申领', 'processCode': 'PROC-B44084F7-ED2D-4122-9A5F-18AA23E3765B', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-B44084F7-ED2D-4122-9A5F-18AA23E3765B#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1ii16CSzqK1RjSZPxXXc4tVXa-102-102.png', 'name': '复工申请单', 'processCode': 'PROC-565CB83C-B790-42DA-9CF6-72530D22DAD9', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-565CB83C-B790-42DA-9CF6-72530D22DAD9#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1r798CFzqK1RjSZSgXXcpAVXa-102-102.png', 'name': '健康承诺书', 'processCode': 'PROC-BA1BB8F3-1825-4A2B-AF97-329195D31877', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-BA1BB8F3-1825-4A2B-AF97-329195D31877#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB11UW.CNTpK1RjSZFMXXbG_VXa-102-102.png', 'name': '状态异常人员报备单', 'processCode': 'PROC-1E26CA66-2178-4917-A3D3-46EF1A8ECA06', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-1E26CA66-2178-4917-A3D3-46EF1A8ECA06#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '客户工单', 'processCode': 'PROC-BE705559-6664-42EC-A181-168EB2E812BB', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-BE705559-6664-42EC-A181-168EB2E812BB#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '客户收货确认单', 'processCode': 'PROC-23C88FEA-942A-4357-9225-F2996E5D2920', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-23C88FEA-942A-4357-9225-F2996E5D2920#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '客户合同', 'processCode': 'PROC-64C03B1A-01C8-4ED6-92D3-566943B4A079', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-64C03B1A-01C8-4ED6-92D3-566943B4A079#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1cbCYCPTpK1RjSZKPXXa3UpXa-112-112.png', 'name': '出差', 'processCode': 'PROC-3ED543B6-140C-4178-B44C-8A4AAF1BA376', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-3ED543B6-140C-4178-B44C-8A4AAF1BA376#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1Y8PlCNjaK1RjSZKzXXXVwXXa-112-112.png', 'name': '加班', 'processCode': 'PROC-0865F7D8-BC12-44C9-B8FE-8E1688642177', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-0865F7D8-BC12-44C9-B8FE-8E1688642177#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1bHOWCSzqK1RjSZFjXXblCFXa-112-112.png', 'name': '外出', 'processCode': 'PROC-272121B8-BBE5-4A01-8BA6-DC433F9C7F36', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-272121B8-BBE5-4A01-8BA6-DC433F9C7F36#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1Qm56CSzqK1RjSZPxXXc4tVXa-102-102.png', 'name': '换班', 'processCode': 'PROC-83DD4C35-E66E-4AEF-A563-E77362B036BC', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-83DD4C35-E66E-4AEF-A563-E77362B036BC#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1Yfa0CG6qK1RjSZFmXXX0PFXa-112-112.png', 'name': '补卡', 'processCode': 'PROC-EA9C19EA-19B7-4772-934A-8AF8BD92B58D', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-EA9C19EA-19B7-4772-934A-8AF8BD92B58D#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1YzS5CNTpK1RjSZFKXXa2wXXa-102-102.png', 'name': '批量付款', 'processCode': 'PROC-80DA7B77-A1C9-4802-8324-4F3058FB2D8C', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-80DA7B77-A1C9-4802-8324-4F3058FB2D8C#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1lkE7NEH1gK0jSZSyXXXtlpXa-120-120.png', 'name': '应收坏账', 'processCode': 'PROC-07E10905-E022-4DE6-BE76-119E7C405BD1', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-07E10905-E022-4DE6-BE76-119E7C405BD1#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1SP_PdfzO3e4jSZFxXXaP_FXa-120-120.png', 'name': '收款单', 'processCode': 'PROC-06D4DDE7-1DFE-4D63-944F-5570BCC6F82B', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-06D4DDE7-1DFE-4D63-944F-5570BCC6F82B#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1fxW7pcKfxu4jSZPfXXb3dXXa-120-120.png', 'name': '开票申请', 'processCode': 'PROC-03C3034A-FB74-4F74-B7DF-51563318E612', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-03C3034A-FB74-4F74-B7DF-51563318E612#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB16l1tX9slXu8jSZFuXXXg7FXa-120-120.png', 'name': '应付免付', 'processCode': 'PROC-A3BCF36C-53AE-4325-84A5-D7B0344BDFAD', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-A3BCF36C-53AE-4325-84A5-D7B0344BDFAD#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB16l1tX9slXu8jSZFuXXXg7FXa-120-120.png', 'name': '应付单', 'processCode': 'PROC-0A6B849A-6194-41CB-AF2D-5326C524EFA4', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-0A6B849A-6194-41CB-AF2D-5326C524EFA4#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB10jxfNRr0gK0jSZFnXXbRRXXa-120-120.png', 'name': '应付实付', 'processCode': 'PROC-A60BCD56-4B38-4A4F-812C-586DE79E6239', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-A60BCD56-4B38-4A4F-812C-586DE79E6239#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB16l1tX9slXu8jSZFuXXXg7FXa-120-120.png', 'name': '付款单', 'processCode': 'PROC-9DCB26C6-74BA-45ED-BF5D-5F55D74F14E6', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-9DCB26C6-74BA-45ED-BF5D-5F55D74F14E6#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1XEdaNNv1gK0jSZFFXXb0sXXa-120-120.png', 'name': '应收单', 'processCode': 'PROC-B251FA77-753E-4AB0-9379-676CFE383284', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-B251FA77-753E-4AB0-9379-676CFE383284#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1t695CFYqK1RjSZLeXXbXppXa-102-102.png', 'name': '日常报销', 'processCode': 'PROC-9AA479A1-3E35-4E7E-B156-7BC3398E42FC', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-9AA479A1-3E35-4E7E-B156-7BC3398E42FC#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1cbCYCPTpK1RjSZKPXXa3UpXa-112-112.png', 'name': '差旅报销', 'processCode': 'PROC-1E2C75A6-CB06-445E-8A6E-A26CC4B594CD', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-1E2C75A6-CB06-445E-8A6E-A26CC4B594CD#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1vYs7NpT7gK0jSZFpXXaTkpXa-120-120.png', 'name': '备用金', 'processCode': 'PROC-AC777407-5267-48A1-A6A6-B4F62082E5BD', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-AC777407-5267-48A1-A6A6-B4F62082E5BD#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB12zo5NuH2gK0jSZJnXXaT1FXa-120-120.png', 'name': '备用金还款', 'processCode': 'PROC-103DAACB-4BE8-4B9A-9D94-03EE33A211F5', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-103DAACB-4BE8-4B9A-9D94-03EE33A211F5#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1cAcScRFR4u4jSZFPXXanzFXa-120-120.png', 'name': '备用金核销', 'processCode': 'PROC-83254F65-681B-49F8-BF8D-47B16D43C6C5', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-83254F65-681B-49F8-BF8D-47B16D43C6C5#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1FHs7NpT7gK0jSZFpXXaTkpXa-120-120.png', 'name': '应收回款', 'processCode': 'PROC-3A5B8AAD-083C-40B0-8715-4B7DF7EA591A', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-3A5B8AAD-083C-40B0-8715-4B7DF7EA591A#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1FHs7NpT7gK0jSZFpXXaTkpXa-120-120.png', 'name': '转账申请', 'processCode': 'PROC-481D96C4-937F-4224-9D54-2BC10973D1E5', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-481D96C4-937F-4224-9D54-2BC10973D1E5#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1e76lCOLaK1RjSZFxXXamPFXa-112-112.png', 'name': '修改个人档案', 'processCode': 'PROC-16E4D3A3-FB91-4192-9020-87E57D4876F3', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-16E4D3A3-FB91-4192-9020-87E57D4876F3#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1nsnvCNnaK1RjSZFBXXcW7VXa-102-102.png', 'name': '入职审批', 'processCode': 'PROC-FE5C5838-88B5-4CCD-8B94-5CFEA749D4EF', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-FE5C5838-88B5-4CCD-8B94-5CFEA749D4EF#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1_YG.COrpK1RjSZFhXXXSdXXa-102-102.png', 'name': '转正', 'processCode': 'PROC-B99331DF-EC2A-470B-8083-8B3F10A4DF56', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-B99331DF-EC2A-470B-8083-8B3F10A4DF56#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1U9iBCSzqK1RjSZPcXXbTepXa-102-102.png', 'name': '离职', 'processCode': 'PROC-93DADD26-40CC-427F-A2C6-513DF18153BF', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-93DADD26-40CC-427F-A2C6-513DF18153BF#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1JKe.CSzqK1RjSZFHXXb3CpXa-102-102.png', 'name': '离职交接', 'processCode': 'PROC-5DFD5DEE-7BA1-44C3-A402-2E43A521D3F5', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-5DFD5DEE-7BA1-44C3-A402-2E43A521D3F5#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1U9iBCSzqK1RjSZPcXXbTepXa-102-102.png', 'name': '离职和交接单', 'processCode': 'PROC-A05936E0-ADB5-43D1-B2F2-A08590EDA4D8', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-A05936E0-ADB5-43D1-B2F2-A08590EDA4D8#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB13ca1CMDqK1RjSZSyXXaxEVXa-102-102.png', 'name': '调岗', 'processCode': 'PROC-68094D0E-F2E1-4F90-AAA0-26ECD23FE196', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-68094D0E-F2E1-4F90-AAA0-26ECD23FE196#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1zzK.CFzqK1RjSZFCXXbbxVXa-102-102.png', 'name': '子管理员权限申请', 'processCode': 'PROC-B821A636-75C9-445A-8703-3A0BB5E76048', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-B821A636-75C9-445A-8703-3A0BB5E76048#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/tfs/TB1oQi.CSzqK1RjSZFpXXakSXXa-112-112.png', 'name': '采购', 'processCode': 'PROC-D807ABBE-A757-47A5-8A58-07BB3F0199AD', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-D807ABBE-A757-47A5-8A58-07BB3F0199AD#/custom'}
    {'iconUrl': 'https://gw.alicdn.com/imgextra/i2/O1CN01FOuyRV1e6WXVKgx25_!!6000000003822-2-tps-112-112.png', 'name': '合同审批', 'processCode': 'PROC-5ED93BB9-B528-44BF-9232-F7D2D12CD0E7', 'url': 'https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?dd_share=false&showmenu=true&back=native&swfrom=corp&corpid=ding2eae0bc70cf61cc3f2c783f7214b6d69&processCode=PROC-5ED93BB9-B528-44BF-9232-F7D2D12CD0E7#/custom'}
    """
    process_info: workflow_models.ListUserVisibleBpmsProcessesResponseBodyResultProcessList
    for process_info in process_list:
        print(process_info)
    assert True


def test_query_schema_by_process_code_with_options():
    """
    获取对应表单的schema信息
    {
        'headers': {
            'server': 'DingTalk/1.0.0',
            'date': 'Tue, 11 Apr 2023 05:01:17 GMT',
            'content-type': 'application/json;charset=utf-8',
            'content-length': '2063',
            'connection': 'keep-alive',
            'vary': 'Accept-Encoding, Accept-Encoding',
            'access-control-allow-origin': '*',
            'x-acs-request-id': '8F76545F-C0C4-7D2D-ABD4-2EB68C71A8BE',
            'x-acs-trace-id': '89dd650d588e44d6a6bebe83e7b3e46d',
            'access-control-allow-headers': 'X-Requested-With, X-Sequence, _aop_secret, _aop_signature, x-acs-dingtalk-access-token',
            'content-security-policy-report-only': "default-src 'self';style-src 'self' 'unsafe-inline' dev.g.alicdn.com g.alicdn.com at.alicdn.com *.test.youku.com *.taobao.net webapi.amap.com;script-src 'report-sample' 'self' 'unsafe-eval' 'unsafe-inline' *.dingtalk.com *.cnzz.com *.alicdn.com market.wapa.taobao.com g.alicdn.com dev.g.alicdn.com ynuf.alipay.com log.mmstat.com s.tbcdn.cn vip.laiwang.com wswukong.laiwang.com local.alipcsec.com:6691 *.taobao.net cfd.aliyun.com restapi.amap.com webapi.amap.com retcode.alicdn.com cfall.aliyun.com gw.alipayobjects.com ynuf.aliapp.org;connect-src 'self' *.dingtalk.com wss://*.dingtalk.com ynuf.alipay.com dev.g.alicdn.com g.alicdn.com retcode.taobao.com dingtalk-cspase-sh.oss-cn-shanghai.aliyuncs.com dingtalk-cspase-sz.oss-cn-shenzhen.aliyuncs.com arms-retcode.aliyuncs.com arms-retcode.aliyuncs.com ynuf.aliapp.org px-intl.ucweb.com px.ucweb.com gm.mmstat.com preview-lippi-space-zjk.oss-accelerate.aliyuncs.com wgo.mmstat.com wss://alidocs-body.oss-accelerate.aliyuncs.com wss://pre-collab.dingtalk.com *.mobgslb.tbcache.com *.mmstat.com px.effirst.com;frame-src 'self' h5.m.taobao.com qiye.aliyun.com log.laiwang.com dev.g.alicdn.com g.alicdn.com login.dingtalk.com login2.dingtalk.com *.dingtalk.com mailsso.mxhichina.com wvjbscheme: alipaybridge: alipaymonitor: mmstat.alicdn.com res.mmstat.com ynuf.aliapp.org alidocs.oss-cn-zhangjiakou.aliyuncs.com;font-src 'self' at.alicdn.com dev.g.alicdn.com g.alicdn.com data: *.taobao.net i.alicdn.com;img-src 'self' data: http: fourier.taobao.com *.dingtalk.com *.aliimg.com *.alicdn.com *.mmstat.com ynuf.alipay.com arms-retcode.aliyuncs.com pin.aliyun.com fourier.alibaba.com retcode.taobao.com *.cnzz.com dingtalk-cspase-sh.oss-cn-shanghai.aliyuncs.com dingtalk-cspase-sz.oss-cn-shenzhen.aliyuncs.com restapi.amap.com kcart.alipay.com preview-lippi-space-zjk.oss-cn-zhangjiakou.aliyuncs.com px-intl.ucweb.com px.ucweb.com alidocs.oss-cn-zhangjiakou.aliyuncs.com;media-src 'self' *.dingtalk.com cloud.video.taobao.com videocdn.taobao.com tbm-auth.alicdn.com dev.g.alicdn.com g.alicdn.com;report-uri https://csp.dingtalk.com/csp;"
        },
        'body': {
            'result': {
                'appType': 0,
                'appUuid': 'ding2eae0bc70cf61cc3f2c783f7214b6d69',
                'creatorUserId': 'bpms_system',
                'engineType': 0,
                'formCode': 'PROC-0865F7D8-BC12-44C9-B8FE-8E1688642177',
                'formUuid': 'FORM-F38AD460-5ACA-41C3-9DDC-B4F94C6BC144',
                'gmtCreate': '2023-04-10T15:39Z',
                'gmtModified': '2023-04-10T15:39Z',
                'listOrder': 4,
                'memo': '适用于加班申请，精确汇总至考勤报表',
                'name': '加班',
                'ownerIdType': 'orgId',
                'schemaContent': {
                    'icon': 'timefades',
                    'items': [{
                        'children': [{
                            'componentName': 'DDSelectField',
                            'props': {
                                'bizAlias': 'type',
                                'id': 'NumberField-OSUCIDP2',
                                'label': '加班类型',
                                'required': True
                            }
                        }, {
                            'componentName': 'InnerContactField',
                            'props': {
                                'bizAlias': 'partner',
                                'id': 'InnerContactField-OSUCIDP3',
                                'label': '加班人',
                                'required': True
                            }
                        }, {
                            'componentName': 'TextNote',
                            'props': {
                                'bizAlias': 'partnerTip',
                                'id': 'TextNote-OSUCIDP4'
                            }
                        }, {
                            'componentName': 'DDDateField',
                            'props': {
                                'bizAlias': 'startTime',
                                'id': 'DDDateField-OSUCIDP5',
                                'label': '开始时间',
                                'required': True
                            }
                        }, {
                            'componentName': 'DDDateField',
                            'props': {
                                'bizAlias': 'finishTime',
                                'id': 'DDDateField-OSUCIDP6',
                                'label': '结束时间',
                                'required': True
                            }
                        }, {
                            'componentName': 'TableField',
                            'props': {
                                'bizAlias': 'everyDayDuration',
                                'id': 'TableField-OSUCIDP7',
                                'label': '明细'
                            }
                        }, {
                            'componentName': 'NumberField',
                            'props': {
                                'bizAlias': 'duration',
                                'id': 'NumberField-OSUCIDP10',
                                'label': '时长',
                                'required': True
                            }
                        }, {
                            'componentName': 'DDSelectField',
                            'props': {
                                'bizAlias': 'compensation',
                                'id': 'DDSelectField-OSUCIDP11',
                                'label': '加班补偿'
                            }
                        }],
                        'componentName': 'DDBizSuite',
                        'props': {
                            'behaviorLinkage': [],
                            'bizAlias': 'overtime',
                            'bizType': 'attendance.batchovertime',
                            'childFieldVisible': {
                                'partner': True,
                                'type': False
                            },
                            'holidayOptions': [],
                            'id': 'DDBizSuite-OSUCIDP1',
                            'label': '加班',
                            'objOptions': [],
                            'push': {
                                'attendanceRule': 3,
                                'pushSwitch': 1,
                                'pushTag': '加班'
                            },
                            'pushToCalendar': 1,
                            'staffStatusEnabled': True,
                            'statField': [],
                            'unit': 'hour',
                            'useCalendar': True
                        }
                    }, {
                        'children': [],
                        'componentName': 'TextField',
                        'props': {
                            'behaviorLinkage': [],
                            'holidayOptions': [],
                            'id': '加班原因',
                            'label': '加班原因',
                            'objOptions': [],
                            'placeholder': '请填写加班原因',
                            'push': {},
                            'staffStatusEnabled': False,
                            'statField': []
                        }
                    }],
                    'title': '加班'
                },
                'status': 'PUBLISHED',
                'visibleRange': 'PRIVATE'
            }
        }
    }
    """
    request = workflow_models.QuerySchemaByProcessCodeRequest(
        # 应用搭建隔离信息
        # app_uuid=100,
        # 表单的唯一码
        process_code='PROC-0865F7D8-BC12-44C9-B8FE-8E1688642177',
    )
    headers = workflow_models.QuerySchemaByProcessCodeHeaders(
        x_acs_dingtalk_access_token='9138f6b2157b325c8ccde568dda816ac'
    )
    try:
        response = client.query_schema_by_process_code_with_options(
            request, headers=headers, runtime=util_models.RuntimeOptions()
        )
    except Exception as e:
        print(e)
        assert False
    print(response)
    assert True


def test_list_process_instance_ids_with_options():
    """
    获取审批实例ID列表
    """
    start_day = 20230401
    end_day = 20230430
    start_time = int(datetime.strptime(str(start_day), '%Y%m%d').timestamp()) * 1000
    end_time = int(datetime.strptime(str(end_day), '%Y%m%d').timestamp()) * 1000

    request = workflow_models.ListProcessInstanceIdsRequest(
        # 审批实例开始时间。Unix时间戳，单位毫秒
        start_time=start_time,
        # 审批实例结束时间，Unix时间戳，单位毫秒
        end_time=end_time,
        # 每页大小，最多传20，由于调用钉钉有频次限制，这里使用最大值
        max_results=20,
        # 分页查询的游标
        next_token=0,
        # 审批流的唯一码
        process_code='PROC-0865F7D8-BC12-44C9-B8FE-8E1688642177',
        # 流程实例状态
        # NEW：新创建
        # RUNNING：审批中
        # TERMINATED：被终止
        # COMPLETED：完成
        # CANCELED：取消
        statuses=None,
        # 发起userid列表
        user_ids=None,
    )
    headers = workflow_models.ListProcessInstanceIdsHeaders(
        x_acs_dingtalk_access_token='9138f6b2157b325c8ccde568dda816ac'
    )
    try:
        response = client.list_process_instance_ids_with_options(
            request, headers=headers, runtime=util_models.RuntimeOptions()
        )
    except Exception as e:
        print(e)
        assert False
    print(response)
    assert True


def test_get_process_instance_with_options():
    """
    获取审批实例
    """
    request = workflow_models.GetProcessInstanceRequest(
        # 审批实例ID
        process_instance_id='xxx',
    )
    headers = workflow_models.GetProcessInstanceHeaders(
        x_acs_dingtalk_access_token='9138f6b2157b325c8ccde568dda816ac'
    )
    try:
        response = client.get_process_instance_with_options(
            request, headers=headers, runtime=util_models.RuntimeOptions()
        )
    except Exception as e:
        print(e)
        assert False
    print(response)
    assert True
