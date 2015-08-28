#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#__author__ = 'zhang.c.m'

"""
带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
所以，可以构造一个MIMEMultipart对象代表邮件本身，
然后往里面加上一个MIMEText作为邮件正文，
再继续往里面加上表示附件的MIMEBase对象即可
"""

from email.mime.multipart import MIMEMultipart, MIMEBase
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

# 邮件对象:
# 同时支持HTML和Plain格式
# 如果我们发送HTML邮件，收件人通过浏览器或者Outlook之类的软件是可以正常浏览邮件内容的，
# 但是，如果收件人使用的设备太古老，查看不了HTML邮件怎么办？
# 办法是在发送HTML的同时再附加一个纯文本，
# 如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件。
msg = MIMEMultipart('alternative')  # 指定subtype是alternative

msg['From'] = _format_addr('发送者名字 <%s>' % from_addr)
msg['To'] = _format_addr('接受者名字 <%s>' % to_addr)
msg['Subject'] = Header('有附件的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))  # 包含一个纯文本
"""
把图片嵌入到邮件正文中.
直接在HTML邮件中链接图片地址，大部分邮件服务商都会自动屏蔽带有外链的图片，因为不知道这些链接是否指向恶意网站。

我们需按照发送附件的方式，先把邮件作为附件添加进去，
然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
"""
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))  # 包含一个Html

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
# server.starttls()  # 创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

"""
加密SMTP

使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

某些邮件服务商，例如Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。

必须知道，Gmail的SMTP端口是587，因此，修改代码如下：

smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
...
"""
