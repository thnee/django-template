
# django-template

This Django project template is not only strongly opinionated,
but also contains a lot of scaffold code
to provide examples of the patterns that I enjoy using.

### Quick rundown of framework level features

- Code is developed using Debian 8, Python 3 and PostgreSQL 9.5.
- Ability to run project in docker containers in dev with ansible-container.
- Project installation is automated with ansible.
- Support for multiple sites/domains, referred to as `apps`.
- Code is shared between apps via shared libraries in `libs`.
- Support for different target environments, referred to as `envs`.
- Settings are broken up into a matrix, where apps are on side and envs are one side.
- Support for multiple distinct user types, as separate models and database tables.
- Different types of users are able to log in on the different apps.

### Scaffolding that is included

**Envs**

- `dev`
- `stage`
- `prod`

**Apps**

- `admin_site` is the standard django admin.
- `backoffice` is a custom app that can be developed to contain for example internal administration panels.
- `frontoffice` is a custom app that can be developed to contain for example a public facing end user site.
- `system` is intended for running management commands.

**Libs**

- `core` contains all the core models, managers, factories, migrations.
- `dbtools` contains some commands used to build the database in dev and stage.

**User models**

- `AdminUser` can log in on the admin_site and backoffice apps.
- `DudeUser` can log in on the frontoffice app.

## Quickstart

The following commands are known to work on Debian Testing:

```
$ sudo apt-get install python python-pip python-virtualenv docker-engine

$ virtualenv venv

$ ./venv/bin/activate

$ pip install django

$ django-admin startproject \
--template https://github.com/thnee/django-template/zipball/master \
-n container.yml \
-n django_project.yml \
myproject

$ cd myproject

$ pip install -r requirements.txt

$ ansible-container build

$ ansible-container run
```

The following ports are exposed:

| App | Port | Protocol |
| --- | --- | --- |
| PostgreSQL | 5500 | psql |
| Admin | 5501 | HTTP / HTML |
| Backoffice | 5502 | HTTP / API |
| Frontoffice | 5503 | HTTP / API |

Navigate a browser to http://127.0.0.1:5501/
and login with `admin@example.com` / `password`.


## Technical overview

#### Django folder structure

The standard django startproject creates a redundant folder structure such as
`project_name/project_name/` to contain `wsgi.py`, `urls.py`, and `settings.py`.

This project template instead chooses to lift those files up one level,
and have them directly under `project_name/`.
The end result is not cluttered at all,
since all other code is neatly organized under `apps/` and `libs/`.

The file `wsgi.py` is now parallel to `manage.py`,
which I think makes a lot of sense since these are
the two entry points for calling into the project.

The `settings.py` is made into a package
to contain the complexities of envs and apps.
To see how settings are loaded for an env and app,
have a look at `project_name/settings/__init__.py`.

And `urls.py` is moved into each app that has a set of urls.
Since there is support for multiple domains / sites,
each app can have it's own url conf.


#### Containers

By using ansible-container / docker,
it should be possible to run this on virtually any distro,
as long as it has a recent docker available.
(However, as soon as ansible-container gains support for `lxd`,
I will probably use that instead).
The definition of the dev environment is also reproducable / scripted,
so that a developer does not have to configure any networking or packages.

To see the defintion of the containers, have a look at `ansible/container.yml`.

Since the code is mounted as a volume and gunicorn is being run with `--reload`,
code changes are detected and loaded ASAP while running.

To run a management command,
use the following while the system container is running:

```
$ docker exec ansible_system_1 /var/opt/myproject/venv/bin/python /opt/myproject/manage.py check
```
