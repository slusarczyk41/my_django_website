# [Gataguy.pl](http://dataguy.pl/) - first steps in Django

Since I like to learn new things and want to have my own website - some day
I will work as a freelancer - I decided to play with Django framework. 

Besides Django I wanted to get familiar with nginx and docker, so the final
result is a working web page with nginx as a server and it is all in docker
container.

The nice feature worth to mentions is that I connected an email service with
web page, so you can send me a message through the form, and I will get
forwarded email from @dataguy.pl domain.

###### Makefile main commands (it is very likely that most of them will require sudo)
- make install-docker - install docker
- make up-prod - build and initialize website (0.0.0.0)
- make up-dev - for development (0.0.0.0:8000)

The whole thing is live thanks to the free trial on Google Cloud services :)