[![CircleCI](https://circleci.com/gh/noosenergy/terraform-client.svg?style=svg&circle-token=5d70bf41e76bbad2a187da8db5c0c39f691db452)](https://circleci.com/gh/noosenergy/terraform-client)

# Terraform Client

A Python client wrapping up HashiCorp's Terraform Cloud API.

## Quickstart

Similarly to the rest of the procurement stack, the library must be deployed onto a machine running:

- Python 3.7.6
- a C compiler (either `gcc` via Homebrew, or `xcode` via the App store)


### Local installation

Install [Pyenv](https://github.com/pyenv/pyenv) and [Pipenv](https://docs.pipenv.org/),

    $ brew install pyenv
    $ brew install pipenv

Lock the Python dependencies and build a virtualenv,

    $ make update

To refresh Python dependencies,

    $ make sync


## Development


### Testing

Tests run via `py.test`:

    $ make test

Linting taking care by `flake8` and `mypy`:

    $ make lint

And formatting overviewed by `black` and `isort`:

    $ make format
