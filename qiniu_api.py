import qiniu
import re
import webbrowser
import datetime
import urllib.request as req


def qiniu_upload(a_key, s_key, bucket, prefix, key, local_file):
    q = qiniu.Auth(a_key, s_key)
    # 上传文件到七牛后， 七牛将文件名和文件大小回调给业务服务器。
    policy = {
        'callbackUrl': 'http://your.domain.com/callback.php',
        'callbackBody': 'filename=$(fname)&filesize=$(fsize)'
    }
    if prefix is None or prefix == '':
        upload_key = key
    else:
        upload_key = prefix.rstrip('/') + '/' + key

    token = q.upload_token(bucket, upload_key, 3600, policy)
    ret, info = qiniu.put_file(token, upload_key, local_file)


def qiniu_get_file_list(a_key, s_key, prefix, bucket_name):
    q = qiniu.Auth(a_key, s_key)
    bucket = qiniu.BucketManager(q)
    limit = 255
    delimiter = None
    marker = None
    format_time = []

    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    info_body = info.text_body
    if ret is None:
        return None, None, None

    file_name = re.findall(r'"key":(.+?),', str(info_body))
    file_fsize = re.findall(r'"fsize":(.+?),', str(info_body))
    file_puttime = re.findall(r'"putTime":(.+?),', str(info_body))

    for seconds in file_puttime:
        t = datetime.datetime.fromtimestamp(int(seconds)/10000000).strftime('%Y-%m-%d %H:%M:%S')
        format_time.append(t)

    return file_name, file_fsize, format_time


def qiniu_get_private_url(a_key, s_key, domain, f_name):
    q = qiniu.Auth(a_key, s_key)
    # base_url = 'http://qiniu.leiting6.cn/111.jpg'
    base_url = domain + '/' + f_name
    print('base url: ' + base_url)
    private_url = q.private_download_url(base_url, expires=3600)

    return private_url


'''
七牛云下载文件
先获取私有链接，然后用request.quote进行转换，否则链接含中文会不兼容
'''
def qiniu_download(a_key, s_key, domain, f_name):
    pri_url = qiniu_get_private_url(a_key, s_key, domain, f_name)
    quote_url = req.quote(pri_url, safe=";/?:@&=+$,", encoding="utf-8")
    print('pri url: ' + pri_url)
    print('quote url: ' + quote_url)
    try:
        webbrowser.open_new(quote_url)
    except Exception as e:
        print('open download url in browser error')

