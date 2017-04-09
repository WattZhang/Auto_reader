#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
import random
import time


def get_web(ip_list, url_str):
    if ip_list != []:
        for ip_one in ip_list:
            # 访问
            driver = webdriver.PhantomJS()
            proxy = webdriver.Proxy()
            proxy.proxy_type = 'ProxyType.MANUAL'
            proxy.http_proxy = ip_one
            proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
            driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
            try:
                driver.get(url_str)
            except Exception as e:
                print 'bad ip' + str(e)
                driver.quit()
                continue
            web_scrolltop_number = 0
            for auto_read_times in xrange(0, 5):
                web_scrolltop_number += random.uniform(300, 600)
                time.sleep(random.uniform(2, 3))
                js = "var q=document.documentElement.scrollTop=" + str(web_scrolltop_number)
                driver.execute_script(js)
            time.sleep(random.uniform(2, 4))
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            time.sleep(random.uniform(2, 4))
            js = "var q=document.documentElement.scrollTop=0"
            driver.execute_script(js)
            time.sleep(random.uniform(3, 4))
            driver.quit()
            print "success!"
        else:
            print 'ip_list is null!'
