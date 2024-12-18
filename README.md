# django-newsletter

Newsletter application for the Django web framework.
This repo was forked from [django-newsletter](https://github.com/jazzband/django-newsletter) in August 2022 and aims to add more features, and fix bugs.

# Installation

```
pip install git+https://github.com/MecSimCalc/django-newsletter.git@master
```

# Changes

## 1. API endpoint

Django Rest Framework (DRF) API endpoint to `GET` and `POST` user subscriptions

- Related to [Subscribe to newsletters using ajax requests #263](https://github.com/jazzband/django-newsletter/issues/263)

**GET Request:**

Gets the subscription of signed in user to all newsletters.

`GET`: `http://localhost:8000/newsletter/my_subscriptions/`

**Returns:**

```json
[
  {
    "user": "585c0a22-0e70-42f5-afa5-05958a99c149",
    "newsletter": {
      "id": 1,
      "title": "Announcements",
      "slug": "announcements"
    },
    "subscribed": false
  },
  {
    "user": "585c0a22-0e70-42f5-afa5-05958a99c149",
    "newsletter": {
      "id": 2,
      "title": "Blog",
      "slug": "blog"
    },
    "subscribed": false
  }
]
```

**POST Request:**

Sets subscription to newsletters for signed in user.

`POST`: `http://localhost:8000/newsletter/my_subscriptions/`

**Request body:**

```json
[
  {
    "newsletter": 2,
    "subscribed": true
  },
  {
    "newsletter": 3,
    "subscribed": true
  }
]
```

---

## 2. Bug: no emails sent when subscriptions are empty

- Implemented the fix suggested by [Send submission to entire newsletter if subscriptions are empty #110](https://github.com/jazzband/django-newsletter/pull/110)

---

## 3. Added new "Export as CSV" to django admin

- Can export your Users list from Django admin as a csv file

---

## 4. Import CSV file will use ForeignKey

- When importing Users by uploading a CSV file, it will first check to see if the email address exists for a User object. If it does, it will link it by a ForeignKey.

## 5. Added support for attachments in s3 django backends

In [models.py](newsletter/models.py), `attachment.file.path` will throw an error in s3 backends since `.path` is not supported!

```python
for attachment in attachments:
    message.attach_file(attachment.file.path)
```

Error:

```bash
raise NotImplementedError("This backend doesn't support absolute paths.")
NotImplementedError: This backend doesn't support absolute paths.
```

Fix: download file from s3 url into `/tmp` file and use that as the filepath

---

---

# What is it?

Django app for managing multiple mass-mailing lists with both plaintext as
well as HTML templates with rich text widget integration, images and a smart
queueing system all right from the admin interface.

# Status

We are currently using this package in several large to medium scale production
environments, but it should be considered a permanent work in progress.

# Documentation

Extended documentation is available on
[Read the Docs](http://django-newsletter.readthedocs.org/).

# Translations

Strings have been fully translated to a lot of languages with many more on their way.

Contributions to translations are welcome through [Transifex](http://www.transifex.com/projects/p/django-newsletter/). Strings will be included as
soon as near-full coverage is reached.

# Compatibility

Currently, django-newsletter officially supports Django 2.2.x LTS, 3.1.x and 3.2.x and Python 3.7 through 3.10.

# Requirements

Please refer to [requirements.txt](https://github.com/MecSimCalc/django-newsletter/blob/master/docs/requirements.txt)
for an updated list of required packages.

# Tests

Fairly extensive tests are available for internal frameworks, web
(un)subscription and mail sending. Sending a newsletter to large groups of recipients
(+15k) has been confirmed to work in multiple production environments. Tests
for pull req's and the master branch are automatically run through
[GitHub Actions](https://github.com/MecSimCalc/django-newsletter/actions).

# Contributing

Want to contribute, great!

Please refer to the [issues](https://github.com/MecSimCalc/django-newsletter/issues) on
GitHub and read [CONTRIBUTING.rst](https://github.com/MecSimCalc/django-newsletter/blob/master/CONTRIBUTING.rst).

# Feedback

If you find any bugs or have feature request for django-newsletter, don't hesitate to
open up an issue on [GitHub](https://github.com/MecSimCalc/django-newsletter/issues)
(but please make sure your issue hasn't been noticed before, finding duplicates is a
waste of time). When modifying or adding features to django-newsletter in a fork, be
sure to let me know what you're building and how you're building it. That way we can
coordinate whether, when and how it will end up in the main fork and (eventually) an
official release.

In general: thanks for the support, feedback, patches and code that's been flowing in
over the years! Django has a truly great community. <3

# License

This application is released
under the GNU Affero General Public License version 3.

```

```
