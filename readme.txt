=== FoxyFlask


Foxycart + Flask integration 

Based on Django code (python integration) 
https://github.com/electricjay/django-foxycart

The idea is *NOT* to use request.forms["FoxyData"] (that implicitly parses the data, as utf-8 and not as 1251)

but to parse it manually using the request.get_data()  function (Thanks to the green man that pointed that out)



Enjoy,
Guy Laybovitz
