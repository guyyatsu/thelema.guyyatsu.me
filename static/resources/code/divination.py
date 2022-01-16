class DIVINATION

  from random import choice
  from sys import path
  path.append('./777')
  from keyscale import *


  def iChing():
    """ An ancient Chinese system of divination."""

    Bagua = {
      'Qian': {
        'trigram': Table_of_Correspondence['2']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading': 
      },
      'Dui': {
        'trigram': Table_of_Correspondence['14']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      },
      'Li': {
        'trigram': Table_of_Correspondence['6']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      },
      'Zhen': {
        'trigram': Table_of_Correspondence['27']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      },
      'Xun': {
        'trigram': Table_of_Correspondence['11']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      },
      'Kan': {
        'trigram': Table_of_Correspondence['10']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      },
      'Gen': {
        'trigram': Table_of_Correspondence['32-bis']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      },
      'Kun': {
        'trigram': Table_of_Correspondence['3']['XIII']['Eastern Mysticism']['Taoist System'][2],
        'reading':
      }
    }

    def Generate_Triagram():
      possibilities=['yin', 'yang']

      line1=choice(possibilities)
      line2=choice(possibilities)
      line3=choice(possibilities)

      if line1 == 'yang':
        if line2 == 'yang':
          if line3 == 'yang':
            return 'Qian'# yang yang yang
          else: return 'Xun'# yang yang yin
        else:
          if line3 == 'yang':
            return 'Li'# yang yin yang
          else: return 'Gen'# yang yin yin
      else:
        if line2 == 'yang':
          if line3 == 'yang':
            return 'Dui'# yin yang yang
          else: return 'Kan'# yin yang yin
        else:
          if line3 == 'yang':
            return 'Zhen'# yin yin yang
          else: return 'Kun'# yin yin yin

    def Generate_Hexagram():

      First_Trigram = Generate_Hexagram()
      Second_Trigram = Generate_Hexagram()

      if First_Trigram == 'Qian':
        if Second_Trigram == 'Qian': return 'Khien'
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      elif First_Trigram == 'Dui':
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      elif First_Trigram == 'Li':
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      elif First_Trigram == 'Zhen':
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      elif First_Trigram == 'Xun':
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      elif First_Trigram == 'Kan':
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen': return 'Kun'
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      elif First_Trigram == 'Gen':
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else:

      else:
        if Second_Trigram == 'Qian':
        elif Second_Trigram == 'Dui':
        elif Second_Trigram == 'Li':
        elif Second_Trigram == 'Zhen':
        elif Second_Trigram == 'Xun':
        elif Second_Trigram == 'Kan':
        elif Second_Trigram == 'Gen':
        else: return 'Khwan'