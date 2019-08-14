import hug

@hug.get('/echo')
def echo(text):
    return text
