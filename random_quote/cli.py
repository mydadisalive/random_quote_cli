# random_quote/cli.py

import click
import requests

API_URL = "https://api.quotable.io/random"

@click.command()
@click.option('--author', help='Filter by author.')
def main(author):
    """
    Fetches a random quote from the API.
    """
    params = {}
    if author:
        params['author'] = author

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        quote = data.get('content')
        author = data.get('author')
        click.echo(f"Random Quote: {quote}")
        if author:
            click.echo(f"- {author}")
    except requests.RequestException as e:
        click.echo(f"Error fetching quote: {e}")

if __name__ == '__main__':
    main()
