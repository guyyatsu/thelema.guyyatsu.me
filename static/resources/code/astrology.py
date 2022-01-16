class ASTROLOGY:
  import re
  import json
  import urllib
  from datetime import datetime

  def Collect_Local_Data():
    url='http://ipinfo.io/json'
    response=urllib.request.urlopen(url)
    return json.load(response)


  def Generate_Chart_Boiler():
    # Formats an astrolog chart based on current settings.

    data=ASTROLOGY.Collect_Local_Data()
    now=datetime.now()

    nearest_city=data['city']
    location=data['loc'].split(',')
    latitude=location[0][:-2].replace('.', 'N')
    longitude=location[1][:-2].replace('.','W')

    month=now.strftime('%b')
    day=now.strftime('%-d')
    year=now.strftime('%Y')
    time=now.strftime('%-I:%-M%p').lower()

    chart_data_string=(
      f"@AI730  ; Astrolog chart info.\n"
      f"-qb {month} {day} {year}  {time} DT 5W  {longitude} {latitude}\n"
      f"-zi \"{month}, {day} {year}\" \"{nearest_city}\""
    )


  Planetary_Hours_Chart={

    'Sunday': {
      'day': {
        1: '☉',
        2: '♀',
        3: '☿',
        4: '☽',
        5: '♄',
        6: '♃',
        7: '♂',
        8: '☉',
        9: '♀',
        10: '☿',
        11: '☽',
        12: '♄',
      },
      'night': {
        1: '♃',
        2: '♂',
        3: '☉',
        4: '♀',
        5: '☿',
        6: '☽',
        7: '♄',
        8: '♃',
        9: '♂',
        10: '☉',
        11: '♀',
        12: '☿',
      }
    },
  
    'Monday': {
      'day': {
        1: '☽',
        2: '♄',
        3: '♃',
        4: '♂',
        5: '☉',
        6: '♀',
        7: '☿',
        8: '☽',
        9: '♄',
        10: '♃',
        11: '♂',
        12: '☉',
      },
      'night':{
        1: '♀',
        2: '☿',
        3: '☽',
        4: '♄',
        5: '♃',
        6: '♂',
        7: '☉',
        8: '♀',
        9: '☿',
        10: '☽',
        11: '♄',
        12: '♃',
      }
    },
  
    'Tuesday': {
      'day': {
        1: '♂',
        2: '☉',
        3: '♀',
        4: '☿',
        5: '☽',
        6: '♄',
        7: '♃',
        8: '♂',
        9: '☉',
        10: '♀',
        11: '☿',
        12: '☽',
      },
      'night': {
        1: '♄',
        2: '♃',
        3: '♂',
        4: '☉',
        5: '♀',
        6: '☿',
        7: '☽',
        8: '♄',
        9: '♃',
        10: '♂',
        11: '☉',
        12: '♀',
      }
    },

    'Wednesday': {
      'day': {
        1: '☿',
        2: '☽',
        3: '♄',
        4: '♃',
        5: '♂',
        6: '☉',
        7: '♀',
        8: '☿',
        9: '☽',
        10: '♄',
        11: '♃',
        12: '♂',
      },
      'night': {
        1: '☉',
        2: '♀',
        3: '☿',
        4: '☽',
        5: '♄',
        6: '♃',
        7: '♂',
        8: '☉',
        9: '♀',
        10: '☿',
        11: '☽',
        12: '♄',
      }
    },
  
    'Thursday': {
      'day': {
        1: '♃',
        2: '♂',
        3: '☉',
        4: '♀',
        5: '☿',
        6: '☽',
        7: '♄',
        8: '♃',
        9: '♂',
        10: '☉',
        11: '♀',
        12: '☿',
      },
      'night': {
        1: '☽',
        2: '♄',
        3: '♃',
        4: '♂',
        5: '☉',
        6: '♀',
        7: '☿',
        8: '☽',
        9: '♄',
        10: '♃',
        11: '♂',
        12: '☉',
      }
    },

    'Friday': {
      'day': {
        1: '♀',
        2: '☿',
        3: '☽',
        4: '♄',
        5: '♃',
        6: '♂',
        7: '☉',
        8: '♀',
        9: '☿',
        10: '☽',
        11: '♄',
        12: '♃',
      },
      'night': {
        1: '♂',
        2: '☉',
        3: '♀',
        4: '☿',
        5: '☽',
        6: '♄',
        7: '♂',
        8: '☉',
        9: '♀',
        10: '☿',
        11: '☽',
        12: '♄',
      }
    },

    'Saturday': {
      'day': {
        1: '♄',
        2: '♂',
        3: '☉',
        4: '♀',
        5: '☿',
        6: '☽',
        7: '♄',
        8: '♂',
        9: '☉',
        10: '♀',
        11: '☿',
        12: '☽',
      },
      'night': {
        1: '☽',
        2: '♄',
        3: '♂',
        4: '☉',
        5: '♀',
        6: '☿',
        7: '☽',
        8: '♄',
        9: '♂',
        10: '☉',
        11: '♀',
        12: '☿',
      }
    }
  }