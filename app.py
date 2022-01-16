#!/bin/python3
"""
    Guyyatsu Hikikomori's Occultic Collection.

    Part of the thelema-93.guyyatsu.me sub-domain, which
    diseminates various areas of occultic study.

"""
from flask import Flask, render_template, render_template_string, url_for
from flask_navigation import Navigation
from sys import path
path.append('./static/resources/code')
from tarot import *
from tools import *

app = Flask(__name__, static_url_path='/static')

nav = Navigation(app)
nav.Bar(
  'top', [
    nav.Item('Thoth Home', 'tarot_index'),
    nav.Item('Card List', 'CardIndex'),
    nav.Item('Random Card', 'DrawRandomCard')
  ]
)

@app.route('/')
@app.route('/home')
def thelema_index():
  """ Disambutation page for the whole of the occultic sub-domain of my site."""
  return render_template(
    'layout.html'
    # Should return a general template unique to the whole sub-domain.
    # Refers to a breakdown in areas of study; tarot, goetia, sacred texts, etc.
  )


@app.route('/The_Book_of_Thoth')
def tarot_index():
  """ The initial entrypoint to the whole deck;
  with a bit of exposition by Aleister Crowley himself."""
  return render_template(
    "layout.html",
    PageTitleitle="THOTH",
    description=str("Index of The Book of Thoth by Aleister Crowley."),
    PageHeader="93/93; 93",
    PageContent=HTML_Paragraph_Text_Converter(
      'static/content/articles/The_Book_of_Thoth'
    )
  )


@app.route('/The_Book_of_Thoth/keys')
@app.route('/The_Book_of_Thoth/atu')
def CardIndex():
  """ """
  return render_template(

    "Index.html",

    PageTitle="The ATU",

    description=str(
      'Index page of all the cards of the deck.'
    ),

    PageHeader="The 78 Rays of the Sun",

    PageContent=render_template_string(
      Build_HTML_Index_Page(
        Header_List=TAROT.card_types,
        LineItem_List=TAROT.card_list,
        Reference_Dictionary=TAROT.card_database
      )
    )
  )


@app.route('/The_Book_of_Thoth/keys/<CARD>')
@app.route('/The_Book_of_Thoth/atu/<CARD>')
def RenderCard(CARD):

  return render_template(
    "Card.html",

    PageTitle=Title_Spacer(CARD),

    WorkingTitle=Title_Spacer(CARD),

    description="A card in the deck",

    ImagePath=url_for(
      'static', filename='content/tarot/' + str(
        TAROT.Collect_Card_Data(
          card=CARD,data='picture'
        )
      )
    ),

    CardEssay=HTML_Paragraph_Text_Converter(
      str(
        'static/content/tarot/' + TAROT.Collect_Card_Data(
          card=CARD,data='essay'
        )
      )
    )
  )


@app.route('/The_Book_of_Thoth/keys/draw')
@app.route('/The_Book_of_Thoth/atu/draw')
def DrawRandomCard():
  CARD=str(
    TAROT.Draw_Random_Card()
  )

  return render_template(
    "Card.html",

    PageTitle=Title_Spacer(CARD),

    WorkingTitle=Title_Spacer(CARD),

    description=f"{CARD}",

    ImagePath=url_for(
      'static', filename='content/tarot/' + str(
        TAROT.Collect_Card_Data(
          card=CARD,data='picture'
        )
      )
    ),

    CardEssay=HTML_Paragraph_Text_Converter(
      str(
        'static/content/tarot/' + TAROT.Collect_Card_Data(
          card=CARD,data='essay'
        )
      )
    )
  )

if __name__ == "__main__":
  app.run(
    # My ~personal~ configurations. 
    #host='0.0.0.0',
    #port=10002,
  )