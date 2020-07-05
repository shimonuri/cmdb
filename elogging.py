import logging_wrapper
import click

from logging_filter import LoggingFilter


@click.command()
@click.option("--script", default=None, help="Python script path")
@click.option("--function", default=None, help="The function name to filter.")
def main(script, function):
    if not script or not function:
        return

    logging_wrapper.wrap_logging((LoggingFilter(functions=[function]),))
    exec(open(script, "rt").read(), globals())


if __name__ == "__main__":
    main()
