import click
import time


@click.command()
@click.option("--number", default=1)
def compute(number):
    time.sleep(2)
    print(number ** 2)


if __name__ == "__main__":
    compute()
