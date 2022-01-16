from flask import render_template, url_for, render_template_string
from tools import *
from sys import path
path.append('./static/resources/code')
from tarot import *
from __main__ import app


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
    "thoth-index.html",
    PageTitleitle="THOTH",
    description=str("Index of The Book of Thoth by Aleister Crowley."),
    PageHeader="93/93; 93",
    PageContent=HTML_Paragraph_Text_Converter(
      'static/resources/articles/The_Book_of_Thoth'
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

    PageTitle=CARD,

    WorkingTitle=CARD,

    description="A card in the deck",

    ImagePath=url_for(
      'static', filename='content/' + str(
        DrawCard(
          card=CARD,data='picture'
        )
      )
    ),

    CardEssay=HTML_Paragraph_Text_Converter(
      str(
        'static/content/' + TAROT.Collect_Card_Data(
          card=CARD,data='essay'
        )
      )
    )
  )


@app.route('/The_Book_of_Thoth/keys/draw')
@app.route('/The_Book_of_Thoth/atu/draw')
def DrawRandomCard():
  CARD=str(
    THOTH.Draw_Random_Card()
  )# Here's the fucker!

  return render_template(
    "Card.html",

    PageTitle=CARD,

    WorkingTitle=CARD,

    description=f"{CARD}",

    ImagePath=url_for(
      'static', filename='content/' + str(
        THOTH.Collect_Card_Data(
          card=CARD,data='picture'
        )
      )
    ),

    CardEssay=HTML_Paragraph_Text_Converter(
      str(
        'static/content/' + THOTH.Collect_Card_Data(
          card=CARD,data='essay'
        )
      )
    )
  )