import click
import wikipedia


@click.group()
def cli():
    pass


@click.command()
@click.argument("query")
@click.option("--sentences", "-s", default=2, help="Number of sentences to print.")
def summary(query, sentences):
    """Get the summary of any Wikipedia page"""
    print(wikipedia.summary(query, sentences=sentences))


@click.command()
@click.argument("query")
@click.option("--section", "-s", help="Section to get from the article")
def get(query, section):
    """Get any page from Wikipedia"""
    result = wikipedia.page(query)
    if section:
        print(result.section(section))
    else:
        print(result.content)


cli.add_command(get)
cli.add_command(summary)

if __name__ == "__main__":
    cli()
