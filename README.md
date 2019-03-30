# two-eyes-out
___
![Homepage Image](designs/landing.png?raw=true "Landing Page")

If a class is full at UBC, students cannot register until a seat opens in their desired sections. 

Since there is no officially offered solution other than checking the webpage regularly, 3rd party tools have been created to watch lecture web pages for openings and alert the students when a seat opens up.

*__two-eyes-out__* or _2eo_ is my solution to this problem. The current 3rd party options work very well, but lack some quality of life features that makes the experiance un-necessarily stressful

This product is still in early stages of development and there is no available version for the public yet

Tech Stack: Django REST API and React + Redux frontend


### Status:
___
**Backend:** 
```
    [x] PostgreSQL database setup and configuration
    [x] Django setup and initial migration
    [x] Django-rest-framework setup and configuration
    [x] Django auth overriding / custom user model
    [x] Web scraping function for checking open seats
    [x] JSON web token configuration and end point setup
    [x] Celery and Redis for task management setup
    [x] Celery tasks for seat monitering and communicating with user
    [x] Docker setup and image creation
    [x] Deployment on DigitalOcean droplet and Docker autobuild
    [] Endpoint for registered section population
    [] Email API implementation
```
**Frontend:**
```
    [x] UI/UX Designs
    [x] React app configuration
    [x] Redux reducers/actions for token and section list
    [x] Auth utils with Axios and Lodash
    [x] Components: Login, Nav, Landing page
    [] Components: Section list,  Section form, Section page, User settings
```

Once basic functionality is completed for both back and front end, both will be deployed to a DigitalOcean droplet with Docker and published to liam-armstrong.com/2eo

