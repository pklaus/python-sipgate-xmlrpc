# python-sipgate-xmlrpc – Easy to use Python bindings for the sipgate XML-RPC API.

python-sipgate-xmlrpc is a package of Python bindings to simplify and 
leverage the communication with [the XML-RPC API][] of the [Sipgate][] products *sipgate basic* and *sipgate plus*.

## Project Information

This software (python-sipgate-xmlrpc) provides an easy way to use the XMLRPC API
offered by Sipgate to its customers. The software consists of a class to leverage
the use of the API and example code to show how to use it.

If you have an idea for the software or want to report a bug, let me know via email!
Or you can use the [issue tracker on GitHub][] to report bugs or request features.

### About the API.

Nowadays, Sipgate also offers a more modern [RESTful web API][] the documentation 
of which can be found on <http://www.live.sipgate.de/api/rest>.
But [users with a Basic Account can't use it][RESTful API only for Sipgate one and team].
Only customers with a Sipgate one or Sipgate team account may use the RESTful API.

On the [end user information site for the API][the XML-RPC API], the user is being 
displayed version of the API documentation file: 
[XML-RPC API documentation v1.06 2007-08-21][].  
And on the [Sipgate team API help site][] they link a more up-to-date version 1.09
of the document: [XML-RPC API documentation v1.09 2009-06-22][] which seems to be
availbale only for Sipgate one and Sipgate team customers with the newer URL
<https://api.sipgate.net/RPC2> as indicated 
[in a post on the API discussion][new api only on new url].  
As this Python module is intended primarily for basic / plus customers at the moment,
the API version is still at 1.06.

## Requirements

The software is tested and known to work well on **Python 2.7.x** on Mac OS X 10.6, 10.7 and 10.8.
<!--
It should, however, work on any operating system that supports python.
I also tested it on **Python 3.2** after converting the files using `2to3-3.2 -w -n *.py`.
All examples were tested afterwards and found to be functional. 
-->

This module uses the standard Python module `xmlrpclib` that should come with any Python installation.

## Installation and Usage

1. Get the source code of the project (via .tar.gz or .zip download or via git).
2. Have a look into the example useage file `example-usage.py` and change the credentials
   or save the credentials in a local settings file `settings.py` (file will be ignored by git).
3. Run the examples to find out if it's working.
4. Have look at the [API documentation PDF][XML-RPC API documentation v1.09 2009-06-22]
   to find out what other calls you send to the API.

You may also have a look at my blog post, where I presented the class:  
[`python-sipgate-xmlrpc` – Easy to use Python bindings for the Sipgate XML-RPC API](http://blog.philippklaus.de/2011/06/python-sipgate-xmlrpc_easy-to-use-python-bindings-for-the-sipgate-xml-rpc-api/).

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
[the XML-RPC API]: http://www.sipgate.de/basic/api
[XML-RPC API documentation v1.06 2007-08-21]: http://www.sipgate.de/beta/public/static/downloads/basic/api/sipgate_api_documentation.pdf
[XML-RPC API documentation v1.09 2009-06-22]: http://www.live.sipgate.de/static/sipgate.de/downloads/api/sipgate_API.pdf
[issue tracker on GitHub]: https://github.com/pklaus/python-sipgate-xmlrpc/issues
[RESTful web API]: http://en.wikipedia.org/wiki/Representational_State_Transfer
[RESTful API only for Sipgate one and team]: http://groups.google.com/group/sipgate-api/browse_thread/thread/bdee9a2712e2a4d6
[Restful API buggy]: https://twitter.com/#!/sipgateDE/status/77744407687856128
[Sipgate team API help site]: http://www.sipgate.de/team/faq/article/446/Technische_Spezifikationen_zur_sipgate_API
[new api only on new url]: http://groups.google.com/group/sipgate-api/msg/51a3535b6d61241f
