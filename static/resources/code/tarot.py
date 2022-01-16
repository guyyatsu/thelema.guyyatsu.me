#!/bin/python3
""" Functional back end for the flask instance.

The Thoth class contains a couple preleminary variables common to all functionality;
    A list of all the cards in the deck taken from the dictionary,
    The ability to randomly pull a card from that list.

DrawCard takes a card and gives back either it's text or it's image as a file path.

BuildIndex generates a useable html pattern with proper headings and classification of it's members.

    It achieves this by first accepting one of three classes: 'TRUMPS', 'COURTS', or 'MINORS', then comparing
members of the ATU list against values within same-named sub-dictionaries that match the given class.

    The resulting list is iterated over to be wrapped within an html string after first printing the structural
html headings."""


class TAROT:
  """
    Header class for tarot sub-section.


    Core functionality includes:

      TAROT.Draw_Random_Card
        -Generates a random card by selecting from
         a list of keys from TAROT.card_database.

      TAROT.Collect_Card_Data
        -Flask utility for populating routes by way
         of a pseudo-database containing metadata
         enabling ease of indexing a given card's
         image and essay data.
  """





  card_database = {
    'Adjustment': {
      'title': 'Adjustment',
      'class': 'TRUMPS',
    },
    'Art': {
      'title': 'Art',
      'class': 'TRUMPS',
    },
    'Death': {
      'title': 'Death',
      'class': 'TRUMPS',
    },
    'Fortune': {
      'title': 'Fortune',
      'class': 'TRUMPS',
    },
    'Lust': {
      'title': 'Lust',
      'class': 'TRUMPS',
    },
    'TheAeon': {
      'title': 'TheAeon',
      'class': 'TRUMPS',
    },
    'TheChariot': {
      'title': 'TheChariot',
      'class': 'TRUMPS',
    },
    'TheDevil': {
      'title': 'TheDevil',
      'class': 'TRUMPS',
    },
    'TheEmperor': {
      'title': 'TheEmperor',
      'class': 'TRUMPS',
    },
    'TheEmpress': {
      'title': 'TheEmpress',
      'class': 'TRUMPS',
    },
    'TheFool': {
      'title': 'TheFool',
      'class': 'TRUMPS',
    },
    'TheHangedMan': {
      'title': 'TheHangedMan',
      'class': 'TRUMPS',
    },
    'TheHermit': {
      'title': 'TheHermit',
      'class': 'TRUMPS',
    },
    'TheHierophant': {
      'title': 'TheHierophant',
      'class': 'TRUMPS',
    },
    'TheLovers': {
      'title': 'TheLovers',
      'class': 'TRUMPS',
    },
    'TheMagus': {
      'title': 'TheMagus',
      'class': 'TRUMPS',
    },
    'TheMoon': {
      'title': 'TheMoon',
      'class': 'TRUMPS',
    },
    'ThePriestess': {
      'title': 'ThePriestess',
      'class': 'TRUMPS',
    },
    'TheStar': {
      'title': 'TheStar',
      'class': 'TRUMPS',
    },
    'TheSun': {
      'title': 'TheSun',
      'class': 'TRUMPS',
    },
    'TheTower': {
      'title': 'TheTower',
      'class': 'TRUMPS',
    },
    'TheUniverse': {
      'title': 'TheUniverse',
      'class': 'TRUMPS',
    },
    'KnightOfWands': {
      'title': 'KnightOfWands',
      'class': 'COURTS',
      'order': 'KNIGHT',
      'suit': 'WANDS',
    },
    'QueenOfWands': {
      'title': 'QueenOfWands',
      'class': 'COURTS',
      'order': 'QUEEN',
      'suit': 'WANDS',
    },
    'PrinceOfWands': {
      'title': 'PrinceOfWands',
      'class': 'COURTS',
      'order': 'PRINCE',
      'suit': 'WANDS',
    },
    'PrincessOfWands': {
      'title': 'PrincessOfWands',
      'class': 'COURTS',
      'order': 'PRINCESS',
      'suit': 'WANDS',
    },
    'KnightOfCups': {
      'title': 'KnightOfCups',
      'class': 'COURTS',
      'order': 'KNIGHT',
      'suit': 'CUPS',
    },
    'QueenOfCups': {
      'title': 'QueenOfCups',
      'class': 'COURTS',
      'order': 'QUEEN',
      'suit': 'CUPS',
    },
    'PrinceOfCups': {
      'title': 'PrinceOfCups',
      'class': 'COURTS',
      'order': 'PRINCE',
      'suit': 'CUPS',
    },
    'PrincessOfCups': {
      'title': 'PrincessOfCups',
      'class': 'COURTS',
      'order': 'PRINCESS',
      'suit': 'CUPS',
    },
    'KnightOfSwords': {
      'title': 'KnightOfSwords',
      'class': 'COURTS',
      'order': 'KNIGHT',
      'suit': 'SWORDS',
    },
    'QueenOfSwords': {
      'title': 'QueenOfSwords',
      'class': 'COURTS',
      'order': 'QUEEN',
      'suit': 'SWORDS',
    },
    'PrinceOfSwords': {
      'title': 'PrinceOfSwords',
      'class': 'COURTS',
      'order': 'PRINCE',
      'suit': 'SWORDS',
    },
    'PrincessOfSwords': {
      'title': 'PrincessOfSwords',
      'class': 'COURTS',
      'order': 'PRINCESS',
      'suit': 'SWORDS',
    },
    'KnightOfDisks': {
      'title': 'KnightOfDisks',
      'class': 'COURTS',
      'order': 'KNIGHT',
      'suit': 'DISKS',
    },
    'QueenOfDisks': {
      'title': 'QueenOfDisks',
      'class': 'COURTS',
      'order': 'QUEEN',
      'suit': 'DISKS',
    },
    'PrinceOfDisks': {
      'title': 'PrinceOfDisks',
      'class': 'COURTS',
      'order': 'PRINCE',
      'suit': 'DISKS',
    },
    'PrincessOfDisks': {
      'title': 'PrincessOfDisks',
      'class': 'COURTS',
      'order': 'PRINCESS',
      'suit': 'DISKS',
    },
    'AceOfWands': {
      'title': 'AceOfWands',
      'class': 'MINORS',
      'order': 'ACES',
      'suit': 'WANDS',
    },
    'TwoOfWands': {
      'title': 'Dominion',
      'class': 'MINORS',
      'order': 'TWOS',
      'suit': 'WANDS',
    },
    'ThreeOfWands': {
      'title': 'Virtue',
      'class': 'MINORS',
      'order': 'THREES',
      'suit': 'WANDS',
    },
    'FourOfWands': {
      'title': 'Completion',
      'class': 'MINORS',
      'order': 'FOURS',
      'suit': 'WANDS',
    },
    'FiveOfWands': {
      'title': 'Strife',
      'class': 'MINORS',
      'order': 'FIVES',
      'suit': 'WANDS',
    },
    'SixOfWands': {
      'title': 'Victory',
      'class': 'MINORS',
      'order': 'SIXES',
      'suit': 'WANDS',
    },
    'SevenOfWands': {
      'title': 'Valour',
      'class': 'MINORS',
      'order': 'SEVENS',
      'suit': 'WANDS',
    },
    'EightOfWands': {
      'title': 'Swiftness',
      'class': 'MINORS',
      'order': 'EIGHTS',
      'suit': 'WANDS',
    },
    'NineOfWands': {
      'title': 'Strength',
      'class': 'MINORS',
      'order': 'NINES',
      'suit': 'WANDS',
    },
    'TenOfWands': {
      'title': 'Oppression',
      'class': 'MINORS',
      'order': 'TENS',
      'suit': 'WANDS',
    },
    'AceOfCups': {
      'title': 'AceOfCups',
      'class': 'MINORS',
      'order': 'ACES',
      'suit': 'CUPS',
    },
    'TwoOfCups': {
      'title': 'Love',
      'class': 'MINORS',
      'order': 'TWOS',
      'suit': 'CUPS',
    },
    'ThreeOfCups': {
      'title': 'Abundance',
      'class': 'MINORS',
      'order': 'THREES',
      'suit': 'CUPS',
    },
    'FourOfCups': {
      'title': 'Luxury',
      'class': 'MINORS',
      'order': 'FOURS',
      'suit': 'CUPS',
    },
    'FiveOfCups': {
      'title': 'Disappointment',
      'class': 'MINORS',
      'order': 'FIVES',
      'suit': 'CUPS',
    },
    'SixOfCups': {
      'title': 'Pleasure',
      'class': 'MINORS',
      'order': 'SIXES',
      'suit': 'CUPS',
    },
    'SevenOfCups': {
      'title': 'Debauch',
      'class': 'MINORS',
      'order': 'SEVENS',
      'suit': 'CUPS',
    },
    'EightOfCups': {
      'title': 'Indolence',
      'class': 'MINORS',
      'order': 'EIGHTS',
      'suit': 'CUPS',
    },
    'NineOfCups': {
      'title': 'Happiness',
      'class': 'MINORS',
      'order': 'NINES',
      'suit': 'CUPS',
    },
    'TenOfCups': {
      'title': 'Satiety',
      'class': 'MINORS',
      'order': 'TENS',
      'suit': 'CUPS',
    },
    'AceOfSwords': {
      'title': 'AceOfSwords',
      'class': 'MINORS',
      'order': 'ACES',
      'suit': 'SWORDS',
    },
    'TwoOfSwords': {
      'title': 'Peace',
      'class': 'MINORS',
      'order': 'TWOS',
      'suit': 'SWORDS',
    },
    'ThreeOfSwords': {
      'title': 'Sorrow',
      'class': 'MINORS',
      'order': 'THREES',
      'suit': 'SWORDS',
    },
    'FourOfSwords': {
      'title': 'Truce',
      'class': 'MINORS',
      'order': 'FOURS',
      'suit': 'SWORDS',
    },
    'FiveOfSwords': {
      'title': 'Defeat',
      'class': 'MINORS',
      'order': 'FIVES',
      'suit': 'SWORDS',
    },
    'SixOfSwords': {
      'title': 'Science',
      'class': 'MINORS',
      'order': 'SIXES',
      'suit': 'SWORDS',
    },
    'SevenOfSwords': {
      'title': 'Futility',
      'class': 'MINORS',
      'order': 'SEVENS',
      'suit': 'SWORDS',
    },
    'EightOfSwords': {
      'title': 'Interference',
      'class': 'MINORS',
      'order': 'EIGHTS',
      'suit': 'SWORDS',
    },
    'NineOfSwords': {
      'title': 'Cruelty',
      'class': 'MINORS',
      'order': 'NINES',
      'suit': 'SWORDS',
    },
    'TenOfSwords': {
      'title': 'Ruin',
      'class': 'MINORS',
      'order': 'TENS',
      'suit': 'SWORDS',
    },
    'AceOfDisks': {
      'title': 'AceOfDisks',
      'class': 'MINORS',
      'order': 'ACES',
      'suit': 'DISKS',
    },
    'TwoOfDisks': {
      'title': 'Change',
      'class': 'MINORS',
      'order': 'TWOS',
      'suit': 'DISKS',
    },
    'ThreeOfDisks': {
      'title': 'Works',
      'class': 'MINORS',
      'order': 'THREES',
      'suit': 'DISKS',
    },
    'FourOfDisks': {
      'title': 'Power',
      'class': 'MINORS',
      'order': 'FOURS',
      'suit': 'DISKS',
    },
    'FiveOfDisks': {
      'title': 'Worry',
      'class': 'MINORS',
      'order': 'FIVES',
      'suit': 'DISKS',
    },
    'SixOfDisks': {
      'title': 'Success',
      'class': 'MINORS',
      'order': 'SIXES',
      'suit': 'DISKS',
    },
    'SevenOfDisks': {
      'title': 'Failure',
      'class': 'MINORS',
      'order': 'SEVENS',
      'suit': 'DISKS',
    },
    'EightOfDisks': {
      'title': 'Prudence',
      'class': 'MINORS',
      'order': 'EIGHTS',
      'suit': 'DISKS',
    },
    'NineOfDisks': {
      'title': 'Gain',
      'class': 'MINORS',
      'order': 'NINES',
      'suit': 'DISKS',
    },
    'TenOfDisks': {
      'title': 'Wealth',
      'class': 'MINORS',
      'order': 'TENS',
      'suit': 'DISKS',
    }
  }

  card_list=list(card_database.keys())

  def Collect_Card_Data(card, data):
    """ Returns the url path for a given card's picture or text.
    Accepts a card title, and either 'essay' or 'jpg'."""

    if data=='picture': ext='jpg'
    elif data=='essay': ext=str(data)
    else: ext='jpg'

    CardObject=TAROT.card_database[card]
    cTitle=CardObject['title']
    cClass=CardObject['class']

    if cClass=='TRUMPS': return str(f"{cClass}/{cTitle}/{cTitle}.{ext}") 
    else:
      cOrder=CardObject['order']; cSuit=CardObject['suit']
      return str(f"{cClass}/{cOrder}/{cSuit}/{cTitle}.{ext}")


  card_types=['TRUMPS', 'COURTS', 'MINORS']


  def Draw_Random_Card(): from random import choice; return choice(TAROT.card_list)