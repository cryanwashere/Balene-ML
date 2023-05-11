import parse
import multiprocessing

with open("urls.txt", "r") as f:
    urls = f.read().split("\n")

from joblib import Parallel, delayed

def download_url(i):
    parse.process_page(urls[i], "data")

if __name__ == "__main__":
    # Run the loop in parallel.
    results = Parallel(n_jobs=4)(delayed(download_url)(i) for i in range(0, len(urls)))