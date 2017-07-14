# First time building a Python App with Django

### I followed this excelent tutorial: https://docs.djangoproject.com/en/1.8/intro/tutorial01/

I choose to learn Python to expand my web development skills. After learning Ruby and JavaScript, I wanted to see how quickly I could learn a new language. I choose to get started with Python and Django because of its similarity to RoR. I first learned about Python after talking to data science professionals about how they are able to leverage the language for data analysis. 

Python is a general-purpose language that can handle a lot of the complexity of programming behind the scenes making it a versatile language for web development, automating workflows, and building desktop applications and games.

Python is beginner friendly language with many resources for learning and is the 4th most used language on GitHub. It is an interpreted language similar to Java, JavaScript, and Perl.

## History
Guido van Rossum released the first version of Python in 1991 with a design that emphasizes code readability. 
The code is open source and has a community based development model and is managed by the non-profit Python Software Foundation.

## Opinion
Setting up models was easy and familiar because of past experience with Rails and Sinatra. I like that Django automatically generates an admin site.

The biggest conceptual hurdle I had while learning is maintaining loose coupling. Starting out, I was hard coding Urls that would create tight coupling. 

What resources do you recommend for interested students?
*For setting up virtual environment: https://virtualenv.pypa.io/en/stable/userguide/
*For installing Django: https://docs.djangoproject.com/en/1.8/topics/install/#installing-official-release
*For installing Python 3: https://www.python.org/downloads/
*Build tutorial: https://docs.djangoproject.com/en/1.8/intro/tutorial01/
    
### What are 3 interview questions one might be asked about this technology?

#### What does it mean that Django apps are “pluggable”? 
You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.

#### Which file do you add URL() calls to? 
urls.py

#### What does the template system use to lookup syntax to access variable attributes?  
dot-lookup

## Requirements
    * Python, Django, Virtualenv
    * The app is set up to run on http://127.0.0.1:8000/ 
    * Admin username: admin
    * email: admin@example.com
    * pwd: firstadmin
    
To activate virtual environment.
```$ source bin/activate```

To run the server.
```$ python3 manage.py runserver```
