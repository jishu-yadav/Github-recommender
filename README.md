# OpenSourceBuddy : Get personalized recommendation for all your open source needs!

An opensource community is a loosely organized, ad-hoc community of contributors from all over the world 
who share an interest in meeting a common need, ranging from minor projects to huge developments.
The diverse and highly motivated open source community is the harbinger of innovation
and collaboration in today's competitive world.

One of the main hectic things in open source is to find a good repository to contribute especially issues that fall under your skillsets. It becomes more painful with beginners as they go through the process of finding communities and projects to contribute.
The similar issue is faced by maintainers and project-owners who find it laborious to find suitable contributors whose skills align with project requirements. 

A lot of time and energy can be saved if users can get personalized recommendations based on their interests and activities.

Therefore we came with this end-to-end solution for a GitHub recommendation system known as OpenSource Buddy.
It provides personalized recommendations to both the project owners and the contributors alike by
leveraging various AI/ML tools for its purpose.

We have three features on our website :
1) Find projects 
2) Find Contributors
3) Find Organisation

Project and Contributors recommendation use Context-Based recommendation model .

For project recommendation it creates a corpus of description of all 900 repositories which are used to train the model .
Corpus is created using Bag of words concept and then tf-idf is appliend on bag of words to find out the importance of each term in the context.
After that Latent Semantic Indexing is applied to dentify patterns in the relationships between the terms and concepts contained in a corpus. Finally similarity between the user requirement and database repos is calculated using cosine similarity. 

For Organisation recommendation we used user-user collaborative filtering model.

For this we created user profile based on their activity and work done in past. Then we calculated cosine simalirity among all profiles and finally recommended those organisation where similar users are part of it.

##Technology Stack
1) Web framework: Django
2) Database: PostgreSQL
3) Backend : Django
4) Frontend: HTML/CSS/JS
5) Deployed on Heroku
6) Github API for collecting data

# Github-recommender-application
Link : http://github-recommender-hackathon.herokuapp.com/

## How to run 
1. Clone the repo to your local system

    ```git clone https://github.com/Priyanka7011/Github-recommender.git ```
2. Create a virtual environment. You can use this [link](https://docs.python.org/3/library/venv.html) for reference.

    ``` python -m venv myvenv ```
3. Activate your virtual environment using : 
    
    ```myvenv/Scripts/activate``` 
    
    Here venv is the name of virtual environment.

4. Install all the requirements required to run the project : 
    
    ```pip install -r requirements.txt```
5. Go inside Github-Recommender folder:
       ```cd Github-Recommender```
6.  Run the django server
        ```python manage.py runserver```







