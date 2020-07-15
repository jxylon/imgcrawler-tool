import requests
from bs4 import BeautifulSoup
import re
import uuid
from tqdm import tqdm
import time
import shutil
import os

baidu_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&ct=201326592&v=flip&word='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58'}


class Crawler:
    def __init__(self, save_path='./', file_suffix='jpg'):
        self._time_step = 0.1  # 每张图片的下载间隔
        self._save_path = save_path  # 图片保存路径
        self._file_suffix = file_suffix  # 图片重命名后的后缀名
        self._start_page = 1  # 图片爬取起始页数
        self._start_num = 0  # 重命名起始数字
        self._page_num = 1  # 下载页数
        self.default_suffix = ['bmp', 'dib', 'png', 'jpg', 'jpeg', 'pbm', 'pgm', 'ppm', 'tif', 'tiff', 'gif', 'JPG']
        self.flag = 1
        self.root_path = os.path.abspath('./')
        self.signal_page = None
        self.signal_img = None
        self.signal_arrange = None
        self.signal_msg = None
        self.load_parameter()

    def load_parameter(self):
        """
        从settings.txt中加载参数，
        """
        with open(os.path.join(self.root_path, "settings.txt"), "r") as f:  # 打开文件
            lines = f.readlines()  # 按行读取文件
            for line in lines:  # 遍历每一行
                exec('self._' + line)

    def download_img(self, url_list, page_idx=0, page_num=1):
        """
        下载图片函数
        url_list: 待下载图片List
        page_idx: 待下载图片的页数序号
        page_num: 待下载图片的总页数
        """

        print('第{}/{}页正在下载中...'.format(page_idx, page_num))
        n = len(url_list)
        for i in tqdm(range(n)):
            if not self.flag:
                break
            img_url = url_list[i]
            suffix = img_url.split('.')[-1]
            self.signal_img.emit(int((i + 1) / n * 100))
            # 设置时间间隔
            time.sleep(self._time_step)
            try:
                r = requests.get(img_url, timeout=5, headers=headers)
                if r.status_code == 200:
                    with open(self._save_path + str(uuid.uuid1()) + '.' + suffix, 'wb') as f:
                        f.write(r.content)
                        # print('下载图片成功！')
            except Exception as e:
                # print('下载图片失败！')
                continue

    def start_craw(self, pattern, keyword=None, _url=baidu_url):
        """
        爬虫主函数
        pattern: 模式1-下载百度图片，模式2-下载任意网页中的所有图片
        _url: 待下载网页链接
        keyword: 关键词（仅模式1可用）
        start_page: 起始页面
        page_num: 总页数
        """
        if pattern == 1:
            if len(keyword.strip()) == 0:
                self.flag = 3
            for i in range(self._page_num):
                if self.flag != 1:
                    break
                pn = (self._start_page - 1) * 60 + i * 60
                url = _url + keyword + '&pn=' + str(pn)
                r = requests.get(url, headers)
                r.coding = 'utf-8'
                url_list = re.findall('"objURL":"(.*?)",', r.text, re.S)
                self.signal_page.emit({'code': 0, 'val': i + 1})
                self.download_img(url_list, i + 1, self._page_num)
        elif pattern == 2:
            r = requests.get(_url, headers)
            soup = BeautifulSoup(r.content, 'lxml')
            img_list = soup.find_all('img')
            url_list = [tag.get('src') for tag in img_list]
            self.signal_page.emit({'code': 0, 'val': 1})
            self.download_img(url_list)
        if self.flag == 1:
            self.signal_page.emit({'code': 1, 'val': 0})
        elif self.flag == 2:
            self.signal_page.emit({'code': 2, 'val': 0})
        elif self.flag == 3:
            self.signal_msg.emit({'msg': '模式一：关键词不能为空'})

    def arrange_imgname(self, default_path=None):
        """
        重命名图片函数
        default_path: 需要重命名图片的默认目录
        default_num: 默认起始数字
        """
        selected_path = default_path if default_path is not None else self._save_path
        start = self._start_num
        img_list = os.listdir(selected_path)
        n = len(img_list)
        # 创建临时文件夹
        k = 0
        while os.path.exists(selected_path + 'tmp' + str(k)):
            k += 1
        os.mkdir(selected_path + 'tmp' + str(k))
        # 待重命名的图片移动到临时文件夹
        for i in range(n):
            if not os.path.isdir(selected_path + img_list[i]):
                suffix = img_list[i].split('.')[1]  # 后缀
                if suffix in ['bmp', 'dib', 'png', 'jpg', 'jpeg', 'pbm', 'pgm', 'ppm', 'tif', 'tiff', 'gif', 'JPG',
                              'JPEG']:
                    shutil.move(selected_path + img_list[i], selected_path + 'tmp' + str(k) + '/' + img_list[i])
        img_list2 = os.listdir(selected_path + 'tmp' + str(k))
        # 按数字排序
        if self._file_suffix != 'all':
            img_list2.sort(key=lambda x: int(x.split('.')[0]))
        m = len(img_list2)
        # 重命名图片，并移动到原目录下
        print('正在重命名...')
        for i in tqdm(range(m)):
            self.signal_arrange.emit({'code': 0, 'val': (i + 1) / m * 100})
            if self._file_suffix == 'all':  # 重命名不改变后缀
                suffix = img_list2[i].split('.')[1]  # 原后缀
            else:
                suffix = self._file_suffix  # 指定后缀
            shutil.copy2(selected_path + 'tmp' + str(k) + '/' + img_list[i],
                         selected_path + str(start + i) + '.' + suffix)
        shutil.rmtree(selected_path + 'tmp' + str(k))
        print('图片重命名：{} - {}'.format(start, start + m - 1))
        self.signal_arrange.emit({'code': 1, 'val': 100})


if __name__ == '__main__':
    crawler = Crawler(save_path='E:/Document/Datasets/dota2/')
    # crawler.start_craw(1, keyword='快递员')
    # crawler.start_craw(2, _url='https://www.dota2.com.cn/main.htm')
    # crawler.arrange_imgname()
