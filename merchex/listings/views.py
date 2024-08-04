from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Announcement


def hello(request):
    bands = Band.objects.all()
    announcements = Announcement.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Mes groupes préférés sont :</p>
        <ul>
            <li>
                <section>
                    {bands[0].name} <br>
                    {announcements[0].title}
                </section>
            </li>
            <li>
                <section>
                    {bands[1].name} <br>
                    {announcements[1].title}
                </section>
            </li>
            <li>
                <section>
                    {bands[2].name} <br>
                    {announcements[2].title}
                </section>
            </li>
            <li>
                <section>
                    {bands[3].name} <br>
                    {announcements[3].title}
                </section>
            </li>
        </ul>
        """)

def about(request):
    return HttpResponse('<h1>About us!</h1> <p>We love merch! </p>')

def contacts(request):
    return HttpResponse('<h1>Contact us</h1>')

def ads(request) :
    return HttpResponse('<h1>Ads available</h1>')
