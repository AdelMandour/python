import webbrowser;
import random;
class randomWebsite:
    def __init__(self,website):
        webbrowser.open(website, new=2);
web=['http://www.google.com','http://www.yahoo.com','http://www.youtube.com','http://www.msn.com','http://www.iti.gov.eg'];
randomWebsite(random.choice(web));