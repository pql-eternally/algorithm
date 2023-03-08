import time
import asyncio


async def download_one(url):
    await asyncio.sleep(0.02)
    print(f'Url<{url}>下载完成')


async def download_all(sites):
    await asyncio.gather(*[download_one(site) for site in sites])


def main():
    sites = range(1000)
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    # 下载1000个网站耗时0.047322014999999995秒
    print('下载{}个网站耗时{}秒'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
