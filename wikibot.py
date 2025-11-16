import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="Web page we want to scrape")
def cli(name):
    # Ensure the name is not None, which can happen if the user runs the CLI without --name
    if name:
        result = scrape(name)
        click.echo(click.style(f"{result}:", fg="blue"))
    else:
        # Handle case where no argument is passed
        click.echo(
            click.style("Please provide a name using the --name option.", fg="red")
        )


if __name__ == "__main__":
    # Using cli.main() is the idiomatic and Pylint-friendly way to run a Click command
    # programmatically, as it correctly initializes the command execution context.
    cli.main()
