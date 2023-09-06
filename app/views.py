from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <h2>Hello my name is Vikash Sharma</h2>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)