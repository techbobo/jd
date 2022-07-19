# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    headers = {
        '': 'path: /api?appid=paimai-search-soa&functionId=paimai_unifiedSearch&body={%22apiType%22:2,%22page%22:%221%22,%22pageSize%22:40,%22reqSource%22:0,%22childrenCateId%22:%2213809%22}&loginType=3&jsonp=jQuery426713&_=1638028157549',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'script',
        'referer': 'https://auction.jd.com/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': '3AB9D23F7A4B3C9B=N5LJFBWHEU2JYBOPKSMWMBD5E5LKCHIOGPCE7HKKFPMPOTB6ZZ25SB2Q4JJDFQL4P4R3YMN2Q3BNBBNYXJZ7SHEFLI',
    }

    params = (
        ('appid', 'paimai-search-soa'),
        ('functionId', 'paimai_unifiedSearch'),
        ('body', '{"apiType":2,"page":"1","pageSize":40,"reqSource":0,"childrenCateId":"13809"}'),
        ('loginType', '3'),
        ('jsonp', 'jQuery426713'),
        ('_', '1638028157549'),
    )

    response = requests.get('https://api.m.jd.com/api', headers=headers, params=params)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
