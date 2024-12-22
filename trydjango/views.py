"""
To render html web pages
"""
import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    name = "Safi"
    random_id = random.randint(1,4) # API call

    # from database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    my_list = [101,102,103,104,105]
    context = {
        "object_list" : article_queryset,
        "object" : article_obj,
        "title" : article_obj.title,
        "id" : article_obj.id,
        "content" : article_obj.content
    }

    #Django TEmplates
    
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """ 
    # <h1> {title} (id: {id}) !</h1>
    # <p> {content}! </p>""".format(**context)
    
    return HttpResponse(HTML_STRING)