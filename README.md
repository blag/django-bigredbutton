# Big Red Button

### For Django

[![pypi](https://img.shields.io/pypi/v/django-bigredbutton.svg)](https://pypi.python.org/pypi/django-bigredbutton/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/blag/django-bigredbutton/main.svg)](https://results.pre-commit.ci/latest/github/blag/django-bigredbutton/main)
[![tests ci](https://github.com/blag/django-bigredbutton/workflows/tests/badge.svg)](https://github.com/blag/django-bigredbutton/actions)

**django-bigredbutton** provides a big red "End All Other Sessions" button in a list of a user's current sessions.

Rendered with a light theme:

![light_bg](https://github.com/blag/django-bigredbutton/assets/597113/3504d235-3750-4354-a35c-78e628a3e248)

Rendered with a dark theme:

![dark_bg](https://github.com/blag/django-bigredbutton/assets/597113/33f8405d-4b24-4f96-b1a5-e028de0abf84)

It can work with multiple session backends, and includes built-in templates for both [django-qsessions](https://pypi.org/project/django-qsessions) and [django-user-sessions](https://pypi.org/project/django-user-sessions), and dynamically switches between them depending on which one is identified in `settings.SESSION_ENGINE`.

## Compatibility

- Python: >= **3.11**
- Django: >= **4.0**

## Installation

1. Install the latest version:

   ```sh
   pip install django-bigredbutton
   ```

   ```sh
   poetry add django-bigredbutton
   ```

2. Add a session backend, like django-qsessions or django-user-sessions. You can
   use the optional packaging shortcuts:

   ```sh
   pip install 'django-bigredbutton[qsessions]'
   ```

   ```sh
   poetry add 'django-bigredbutton[qsessions]'
   ```

   ```sh
   pip install 'django-bigredbutton[user-sessions]'
   ```

   ```sh
   poetry add 'django-bigredbutton[user-sessions]'
   ```

   But there may be additional steps required for each session backend. Refer
   to the documentation for your session backend package for their installation
   instructions.

3. Add `bigredbutton` to `INSTALLED_APPS` in your project's `settings.py`, and
   optionally set `BIGREDBUTTON_DELETE_SUCCESS_URL_NAME` to the URL name of
   your choice (default: `list_sessions`).

4. Register `bigredbutton` in your projects root URLConf:

   ```python
   urlpatterns = [
       ...
       path("account/sessions/", include("bigredbutton.urls")),
       ...
   ]
   ```

## Usage

Run Django's development server and navigate to the configured root for
`bigredbutton`. The URL in these instructions will be
`http://localhost:8000/account/sessions/`.

You will see a list of all of your current sessions. If you have more than one
session (eg: you are signed in on more than one browser or device), you will
see a big red "End All Other Sessions" button. That button will sign you out of
all of your other sessions.

## TODO

I have intentionally kept this app very small to minimize the maintenance
burden. But contributions are very welcome!

## License

MIT
