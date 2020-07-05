import click

import logging_wrapper
from logging_filter import LoggingFilter


@click.command()
@click.argument("script", default=None)
@click.option("--function", default=".*", help="The function name to filter.")
def main(script, function):
    if not script:
        return

    logging_wrapper.wrap_logging((LoggingFilter(function_patterns=[function]),))
    exec(open(script, "rt").read(), globals())


if __name__ == "__main__":
    main()
