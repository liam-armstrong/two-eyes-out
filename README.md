# two-eyes-out
![Homepage Image](designs/landing-actual.png?raw=true "Landing Page")

### Closed Beta now open at [2eo.xyz](https://2eo.xyz). Contact me (liam at liam-armstrong.com) for access!

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
    [x] Celery Queue and worker configuration
    [x] Docker setup and image creation
    [x] REST endpoint for sections: get, add, remove and update
    [x] AWS EC2 setup and deployment
    [] AWS SES setup and API calls from Celery tasks
    [] User registration
    [] Forgot password functionality
    [] Postman scripting automated API endpoint testing 
```
**Frontend:**
```
    [x] UI/UX Designs
    [x] React app configuration
    [x] Redux reducers/actions for token and section list
    [x] Auth utils with Axios and Lodash
    [x] Section utils for getting, adding, removing and updating
    [x] Components: Login, Nav, Landing page, Section form, Section page, Section list
    [] Components: Loading, Alert, Registration form, Forgot Password form
```

Once basic functionality is completed for both back and front end, both will be deployed to an AWS EC2 instance with Docker and published to 2eo.xyz

You can view the KanBan boards and feature pipeline on Notion [here](https://www.notion.so/Two-Eyes-Out-cf165d78af3f4a7ca896b5ca39d7032f)
