# datastore-git

## datastore implementation for git

See [datastore](https://github.com/datastore/datastore).


### Install

From pypi (using pip):

    sudo pip install datastore.git

From pypi (using setuptools):

    sudo easy_install datastore.git

From source:

    git clone https://github.com/datastore/datastore.git/
    cd datastore.git
    sudo python setup.py install


### License

datastore.git is under the MIT License.

### Contact

datastore.git is written by [Juan Batiz-Benet](https://github.com/jbenet).
It was extracted from [datastore](https://github.com/datastore/datastore)
in Feb 2013.

Project Homepage:
[https://github.com/datastore/datastore.git](https://github.com/datastore/datastore.git)

Feel free to contact me. But please file issues in github first. Cheers!


### Hello World

    >>> import datastore.git
    >>>
    >>> ds = datastore.git.GitDatastore('.datastore')
    >>>
    >>> hello = datastore.Key('hello')
    >>> ds.put(hello, 'world')
    >>> ds.contains(hello)
    True
    >>> ds.get(hello)
    'world'
    >>> ds.delete(hello)
    >>> ds.get(hello)
    None
