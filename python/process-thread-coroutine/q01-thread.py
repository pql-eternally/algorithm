import time


def download_one(url):
    time.sleep(0.02)
    print(f'Url<{url}>下载完成')


def download_all(sites):
    for site in sites:
        download_one(site)


def main():
    sites = range(1000)
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    # 下载1000个网站耗时23.3050418070000003秒
    print('下载{}个网站耗时{}秒'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
