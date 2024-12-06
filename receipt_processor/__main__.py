"""Main entrypoint for the receipt processor"""

import click

from receipt_processor.restapi import flask_app


@click.command()
@click.option('--host', type=str, default='0.0.0.0', help='The host IP to listen on.')
@click.option('--port', type=int, default=8080, help='The host port to listen on.')
@click.option('--debug/--no-debug', type=bool, is_flag=True, default=False, help='Enable debug mode.')
def main(host: str, port: int, debug: bool):
    """Main entrypoint"""
    flask_app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
