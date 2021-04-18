import random

def rand_quote(type):
    
    dm = ['quote1','quote2','quote3']

    post = ['quote1','quote2','quote3']

    comment = ['quote1','quote2','quote3']

    if type == "dm":
        return random.choice(dm)
    elif type == "post":
        return random.choice(post)
    elif type == "comment":
        return random.choice(comment)