import time
import concurrent.futures


def download_one(url):
    time.sleep(0.02)
    print(f'Url<{url}>下载完成')


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)


def main():
    sites = range(1000)
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    # 下载1000个网站耗时4.748322858秒
    print('下载{}个网站耗时{}秒'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
