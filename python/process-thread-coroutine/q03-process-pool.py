import time
import concurrent.futures


def download_one(url):
    time.sleep(0.02)
    print(f'Url<{url}>下载完成')
    return f'Url<{url}>下载完成'


def download_all(sites):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        result_iterator = executor.map(download_one, sites)
        for result in result_iterator:
            print(result)


def main():
    sites = range(1000)
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    # 下载1000个网站耗时5.888842275秒
    print('下载{}个网站耗时{}秒'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
