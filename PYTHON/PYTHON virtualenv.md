#PYTHON VIRTUALENV



## OVERALL

[Tool Description](https://virtualenv.pypa.io/en/stable/)


`virtualenv` is a tool to create isolated Python environments. It creates isolated Python environments to avoid problems caused by conflicting dependencies and differing versions.

The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? If you install everything into `/usr/lib/python2.7/site-packages` (or whatever your platform’s standard location is), it’s easy to end up in a situation where you unintentionally upgrade an application that shouldn’t be upgraded.

Or more generally, what if you want to install an APP and leave it be? If an APP works, any change in its libraries or the versions of those libraries can break the APP.

Also, what if you can’t install packages into the global site-packages directory? For instance, on a shared host.

In all these cases, `virtualenv` can help you. It creates an environment that has its own installation directories, that doesn’t share libraries with other virtualenv environments (and optionally doesn’t access the globally installed libraries either).



## INSTALLATION

[Install steps](https://virtualenv.pypa.io/en/stable/installation/)


To install globally with pip (if you have pip 1.3 or greater installed globally):
```
sudo pip install virtualenv
```


## USAGE

[Usage](https://virtualenv.pypa.io/en/stable/userguide/)


Place the new virtual env to the `env1` dir

**Option1**

Via `virtualenv` tool itself
```
virtualenv /Users/sbur/overall/test/env1

      New python executable in /Users/sbur/overall/test/env1/bin/python
      Installing setuptools, pip, wheel...done.
```

**Option2**

Via `python` installed, with appropriate key `-m`
```
python3 -m venv /Users/sbur/overall/test/env1
```




## REMOVING ENV

```
deactivate
rm -r /path/to/ENV
```















