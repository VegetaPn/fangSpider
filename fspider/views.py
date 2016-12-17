# encoding: utf-8


from django.shortcuts import render

from models import House, Villa, Shop, Office
from fangSpider import settings
from bs4 import BeautifulSoup
import requests
import logging


# Create your views here.
def spide_house_info():
    house_list = House.objects.all()
    complete_house_info(settings.TYPOS['house'], house_list)
    house_list = Villa.objects.all()
    complete_house_info(settings.TYPOS['villa'], house_list)


def spide_office_info():
    office_list = Shop.objects.all()
    complete_office_info(settings.TYPOS['shop'], office_list)
    office_list = Office.objects.all()
    complete_office_info(settings.TYPOS['office'], office_list)



def complete_office_info(office_type, offices):
    for new_office in offices:
        prefix_url = offices.href
        if not prefix_url.startswith('http'):
            continue

        f_url = prefix_url
        resp = requests.get(f_url)
        resp.encoding = 'gbk'
        soup = BeautifulSoup(resp.text, 'lxml')
        contents = soup.find('div', class_='xiangqing').find_all('dd')
        title = soup.h1.get_text()

        new_office.name = title
        new_office_attr = {}
        for item in contents:
            attr_kv = item.get_text().split(u'：')
            new_office_attr[attr_kv[0]] = attr_kv[1]

        try:
            new_office.category = new_office_attr[u'物业类别']
        except Exception as e:
            print(e)
        try:
            new_office.area = new_office_attr[u'建筑面积']
        except Exception as e:
            print(e)
        try:
            new_office.parking = new_office_attr[u'停 车 位']
        except Exception as e:
            print(e)

        new_office.save()


def complete_house_info(house_type, houses):
    for new_house in houses:
        prefix_url = new_house.href
        if not prefix_url.startswith('http'):
            continue
        if prefix_url[-4:] == 'esf/':
            prefix_url = prefix_url[:-4]
        f_url = prefix_url + settings.URL_POSFIX_DETAIL
        resp = requests.get(f_url)
        resp.encoding = 'gbk'
        soup = BeautifulSoup(resp.text, 'lxml')
        contents = soup.find('div', class_='con_left').contents[3].find('div', class_='inforwrap clearfix').find('dl').find_all('dd')
        title = soup.h1.a.get_text()

        new_house.name = title
        new_house_attr = {}
        for item in contents:
            attr_kv = item.get_text().split(u'：')
            new_house_attr[attr_kv[0]] = attr_kv[1]

        try:
            new_house.area = int(new_house_attr[u'建筑面积'][0:-3])
        except Exception as e:
            print(e)
        try:
            new_house.volume_rate = float(new_house_attr[u'容 积 率'])
        except Exception as e:
            print(e)
        try:
            new_house.greening_rate = float(new_house_attr[u'绿 化 率'][0:-1])
        except Exception as e:
            print(e)
        try:
            new_house.households = int(new_house_attr[u'当期户数'][0:-1])
        except Exception as e:
            print(e)

        new_house.save()


def spide_house(house_type, page_no=1):
    """TODO: Docstring for spide_house.

    :arg1: TODO
    :returns: TODO

    """

    prefix = settings.BASE_URL
    poxfix = ('__%s_0_0_0_%s_0_0/' % (house_type, page_no))
    list_url = prefix + poxfix
    resp = requests.get(list_url)
    resp.encoding = 'gbk'

    soup = BeautifulSoup(resp.text, 'lxml')
    house_list = soup.find('div', class_='houseList').find_all('div', class_='list rel')
    parse_house(house_list, str(house_type))

    logging.info('url collection done..')


    """
    house = House()
    house.name = 'test测试'
    house.area = 10000
    house.households = 400
    house.volume_rate = 2.97
    house.greening_rate = 40
    house.save()
    """


def collect_typo_urls(typo, max_page):
    for i in range(max_page):
        spide_house(typo, str(i))


def collect_all_urls():
    collect_typo_urls(settings.TYPOS['house'], 100)
    collect_typo_urls(settings.TYPOS['villa'], 31)
    collect_typo_urls(settings.TYPOS['shop'], 49)
    collect_typo_urls(settings.TYPOS['office'], 100)

    logging.info('collet all urls success !')


def judge_house(typo):
    if typo == settings.TYPOS['house']:
        new_house = House()

    elif typo == settings.TYPOS['villa']:
        new_house = Villa()

    elif typo == settings.TYPOS['shop']:
        new_house = Shop()

    elif typo == settings.TYPOS['office']:
        new_house = Office()

    else:
        new_house = None
        logging.error('not match')
        logging.error(typo)

    return new_house


def parse_house(house_list, typo):
    for house in house_list:
        new_house = judge_house(typo)
        house_href = house.find('dl').find('dd').find('a', class_='plotTit')['href']
        new_house.href = house_href
        new_house.save()


def test_collect_one():
    spide_house(1, 1)



