import click
from mylib.bot import scrape


@click.command()
@click.option("--name", prompt="Wikipedia page to scrape", help="Web page to scrape")
@click.option(
    "--sentences",
    prompt="The number of sentence you want to extract",
    help="It extracts the n first sentences.",
)
def cli(name="Microsoft", sentences=1):
    result = scrape(name, sentences=sentences)
    click.echo(click.style(f"{result}:", fg="red", bg="black"))


if __name__ == "__main__":
    cli()
