import os
import shutil
import requests
import urllib.parse
from time import time
import concurrent.futures
from pathlib import Path

from tqdm import tqdm

MAX_WORKERS = 8

BASE_URL = 'https://s3.amazonaws.com/ava-dataset/trainval/'
TEST_VIDEOS_LIST = 'https://s3.amazonaws.com/ava-dataset/annotations/ava_file_names_test_v2.1.txt'
TRAIN_VAL_VIDEOS_LIST = 'https://s3.amazonaws.com/ava-dataset/annotations/ava_file_names_trainval_v2.1.txt'

def parse_args():
    """
    Usage: python download_ava.py ./data/ava/videos 
    """
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('out_path', type=str, help='Directory path')
        
    return parser.parse_args()

def download_file(out, url):
    with requests.get(url, stream=True) as r:
        with open(out, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return out

def main(args):
    out_path = Path(args.out_path)
    out_path.mkdir(exist_ok=True, parents=True)
    start_time = time()
    for split_vid_lst_url in [TEST_VIDEOS_LIST, TRAIN_VAL_VIDEOS_LIST]:
        # get vid_list
        vid_lst = requests.get(split_vid_lst_url).text.splitlines()
        vid_lst = [(os.path.join(str(out_path), v), urllib.parse.urljoin(BASE_URL, v)) for v in vid_lst]
        # download videos in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_url = {executor.submit(download_file, out, url): url for out, url in vid_lst}
            for future in tqdm(concurrent.futures.as_completed(future_to_url), total=len(future_to_url)):
                url = future_to_url[future]
                try:
                    data = future.result()
                except Exception as e:
                    print('%r generated an exception: %s' % (url, e))

    split_time = time() - start_time
    print(f'Successfully completed download in: {(split_time / 60):.3f} mins')

if __name__ == '__main__':
    args = parse_args()
    main(args)
