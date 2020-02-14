import click
import json
from foundry import Foundry

from joblib import Parallel, delayed
import multiprocessing
num_cores = multiprocessing.cpu_count()

@click.command('install')
@click.option('--file', default="./foundry.json", help='Use which file to create data environment')
def install(file):
    """Simple program that greets NAME for a total of COUNT times."""

    def start_download(dep, interval=3):
        print("=== Fetching Data Package {} ===".format(dep))
        f = Foundry().load(dep)
        f = f.download(interval=interval)
        return {"success":True}

    with open(file, "r") as fp:
        pkg = json.load(fp)
        results = Parallel(n_jobs=num_cores)(delayed(start_download)(dep) for dep in pkg['dependencies'])


if __name__ == '__main__':
    install()

