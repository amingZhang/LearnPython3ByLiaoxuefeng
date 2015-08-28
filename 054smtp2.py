#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#__author__ = 'zhang.c.m'

"""
邮件主题、发件人、收件人等信息并不是通过SMTP协议发给MTA，
而是包含在发给MTA的文本中的，
所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = 'zhang.c.m@3s.com.cn'  # input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = 'aming_zhang@foxmail.com'  # input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.exmail.qq.com'  # input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 发送HTML邮件，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

# 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码
msg['From'] = _format_addr('发送者名字 <%s>' % from_addr)

# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To'] = _format_addr('接受者名字 <%s>' % to_addr)

msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
