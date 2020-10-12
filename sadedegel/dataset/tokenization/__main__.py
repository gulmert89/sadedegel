import click
import os.path
from loguru import logger
from pathlib import Path
import boto3
from smart_open import open
import tarfile

from ._core import check_and_display


@click.group(help="Tokenization Dataset Commandline.")
def cli():
    pass


@cli.command()
@click.option("--access-key", help="Access Key ID to download dataset.", prompt=True,
              default=lambda: os.environ.get('sadedegel_access_key', ''))
@click.option("--secret-key", help="Secret Key ID to download dataset.", prompt=True,
              default=lambda: os.environ.get('sadedegel_secret_key', ''))
@click.option("--data_home", '-d', help="Data home directory", default="~/.sadedegel_data")
@click.option("--data-version", "-v", help="Dataset version", default="v2")
def download(access_key, secret_key, data_home, data_version):
    """Download tokenization corpus from cloud with your key."""

    data_home = Path(os.path.expanduser(data_home)) / 'tokenization'
    logger.info(f"Data directory for tokenization data {data_home}")

    data_home.mkdir(parents=True, exist_ok=True)

    transport_params = {
        'session': boto3.Session(aws_access_key_id=access_key,
                                 aws_secret_access_key=secret_key),
        'resource_kwargs': {
            'endpoint_url': 'https://storage.googleapis.com',
        }
    }

    __tarballs__ = ['raw/80M_raw.tar.gz', 'tokenized/80M_tokenized.tar.gz']

    click.echo(click.style(f"\nStarting Download...", fg="yellow"))

    for tarball in __tarballs__:
        url = f"s3://sadedegel/dataset/tokenization/{data_version}/{tarball}"

        with open(url, 'rb', transport_params=transport_params) as fp:
            tf = tarfile.open(fileobj=fp)

            extract_to = (Path(os.path.expanduser(data_home)) / data_version / tarball.split('/')[0])

            tf.extractall(extract_to.absolute())

        click.secho(f".done: {tarball}", fg="green")

    d = check_and_display('~/.sadedegel_data')
    click.secho("Checking download...")
    click.secho("Dataset stats: " + click.style(f"{d}", fg="yellow"), color='white')


if __name__ == "__main__":
    cli()
