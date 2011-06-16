# python-sipgate-xmlrpc – Easy to use Python bindings for the sipgate XML-RPC API.

python-sipgate-xmlrpc is a package of Python bindings to simplify and leverage the communication with [the XML-RPC API][] of [Sipgate][].

## Project Information

This software (python-sipgate-xmlrpc) provides an easy way to use the XMLRPC API
offered by Sipgate to its customers. The software consists of a class to leverage
the use of the API and example code to show how to use it.

If you have an idea for the software or want to report a bug, let me know via email!
Or you can use the [issue tracker on GitHub][] to report bugs or request features.

## Required Python modules

The software is tested and known to work well on **Python 2.7.1** on Mac OS X 10.6.7.
<!--
It should, however, work on any operating system that supports python.
I also tested it on **Python 3.2** after converting the files using `2to3-3.2 -w -n *.py`. All examples were tested afterwards and found to be functional. 
Python modules used in this software include the standard modules time, xmlrpclib, hashlib, ConfigParser and sys.
-->

## Installation and Usage

1. Get the source code of the project (via .tar.gz or .zip download or via git).
2. Have a look into the example useage file `example-usage.py` and change the credentials
   or save the credentials in a local settings file `settings.py` (file will be ignored by git).
3. Run the examples to find out if it's working.
4. Have look at the [API documentation PDF][the XML-RPC API] to find out what other calls you send to the API.

<!--
Please refer to my blog post, where I presented the class:
<http://blog.philippklaus.de/... yet to come>
for more information on this class and how you can use it.
-->

## License

> python-sipgate-xmlrpc is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
> 
> python-sipgate-xmlrpc is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
> 
> You should have received a copy of the GNU General Public License
> along with python-sipgate-xmlrpc.  If not, see <http://www.gnu.org/licenses/>.

## Author

* Philipp Klaus
  * Web site: <http://blog.philippklaus.de>
  * Email: philipp.klaus →AT→ gmail.com

[Sipgate]: http://www.sipgate.de
[the XML-RPC API]: http://www.sipgate.de/beta/public/static/downloads/basic/api/sipgate_api_documentation.pdf
[issue tracker on GitHub]: https://github.com/pklaus/python-sipgate-xmlrpc/issues
