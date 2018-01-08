'''
zhibo8 api module
'''

import json
from datetime import datetime

import requests

from .. import const
from ..model.match import Match
from ..model.text_living import TextLiving

const.LIVING_MATCHES_URL = 'http://bifen4m.qiumibao.com/json/list.htm'
const.MATCH_MAX_SID_URL = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/max_sid/{0}/0.htm'
const.MATCH_LIVING_TEXT_URL = 'http://dingshi4pc.qiumibao.com/livetext/data/cache/livetext/{0}/0/lit_page_2/{1}.htm'
const.MATCH_INFO_URL = 'http://bifen4pc2.qiumibao.com/json/{0}/{1}.htm'


def get_living_matches():
    response = requests.get(const.LIVING_MATCHES_URL)
    result = json.loads(response.text)
    matches = [
        Match(**match) for match in result['list']
        if match['type'] == 'basketball' and match['period_cn'] != '完赛'
    ]
    return matches


def get_match_max_sid(match_id):
    response = requests.get(const.MATCH_MAX_SID_URL.format(match_id))
    if response.status_code == requests.codes.OK:
        return int(response.text)


def get_match_living(match_id, max_sid):
    match_info = get_match_info(match_id)

    response = requests.get(const.MATCH_LIVING_TEXT_URL.format(match_id, max_sid))

    texts = []
    if response.status_code == requests.codes.OK:
        result = json.loads(response.text)
        texts = [TextLiving(match_info, **living) for living in result]
    return texts


def get_match_info(match_id):
    today = datetime.now().strftime('%Y-%m-%d')
    response = requests.get(const.MATCH_INFO_URL.format(today, match_id))
    match_info = json.loads(response.text)
    return match_info
