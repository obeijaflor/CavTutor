Project Description
===
CavTutor is a web application for CS 4501: Internet Scale Application meant to illustrate concepts of scalability and best-practice full stack development for Internet-based applications. Our application will provide basic functionality to connect tutors with tutees for courses at any arbitrary instituion.

Authors
===
Rachel Shaw \<rcs8vq@virginia.edu\>

Matthew Schaeffer \<mbs5mz@virginia.edu\>

Daniel Saha \<drs5ma@virginia.edu\>

Description of Docker Containers
===
There are currently 3 docker containers created by running `docker-compose up` on our project, in addition to the pre-requisite MariaDB docker instance named `mysql`; these are

0. `mysql` -- the low-level docker image container for our MariaDB database
1. `api` -- our secondary-level services API that talks to our database directly
2. `ux` -- an abstract tertiary-level user experience layer that communicates
   between our client-facing µ-services (`www`, `ios`, `android`, etc.)
3. `www` -- a client-facing docker image that serves HTML-based content for
   human consumption; aimed at desktop web browsers

User Stories
====
Refer to [doc/user_stories.md](doc/user_stories.md) for documented user stories.

Fixtures
===
We use Django fixtures to prepopulate the given database instance with our test data. A Django superuser is created, with username `root` and password `root`.

API Usage
===
An API services layer is for all models using Django REST framework.

Vist the API docker homepage on port `8003` for details.

http://localhost:8003/

Project Instantiation
===
To run a development instance of this project, spin up your own MySQL/MariaDB container
and call it `mysql`.

Then, clone this repository and start up our docker containers with

    $ docker-compose up

To use the site, simply point your browser (or CLI tool, such as `curl`) to [localhost:8000](http://localhost:8000/).
