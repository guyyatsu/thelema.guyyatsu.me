from PIL import Image


def Color_Getter(initial_input):
  def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
  Image_Module=Image
  Color_Pixel=Image_Module.open(initial_input).resize((1, 1)).convert("RGB").getdata()
  for r, g, b, in Color_Pixel:
    return rgb2hex(r, g, b)


def Color_Inverter(color):
  hex_white="FFFFFF"
  hex_one=color.replace('#', '')
  return hex(int(hex_white, 16) - int(hex_one, 16))


def Title_Spacer(title):
  try:
    New_Title=title.replace('Of', ' Of ')
    New_Title=New_Title.replace('The', 'The ')
  except: ...
  return New_Title


def Build_HTML_Index_Page(Header_List, LineItem_List, Reference_Dictionary):
  """  Helper Function that builds a nested unordered list with
       headers and line-items associated with them."""
  ElementObject=""
  _html = []
  _hreflist=[]

  for Link_Header in Header_List:
    for Line_Item in LineItem_List:

      Card_Class=Reference_Dictionary[Line_Item]['class']
      Card_Title=Reference_Dictionary[Line_Item]['title']

      if Reference_Dictionary[Line_Item]['class']==Link_Header:
        _hreflist.append(
          f"<li>"
          f"<a href={{{{ url_for('RenderCard', CARD='{Line_Item}') }}}}>"
          f"{Line_Item}"
          f"</a>"
          f"</li>\n"
        )

    _html.append(
      f"<ul>\n"
      f"<li>"
      f"{Link_Header}"
      f"</li>\n"
      f"<li>\n"
      f"<ul>\n"
    )

    for href in _hreflist: _html.append(href)
    _html.append("</ul>\n</li>\n</ul>\n\n")
    _hreflist.clear()
  for item in _html: ElementObject+=str(item)
  return ElementObject


def HTML_Paragraph_Text_Converter(Text_File):

  HtmlString=''#                               Unified strand of formatted strings.
  StringContainer=[]#                          Container array for individual strings.

  dStart='<p>'
  dEnd='</p>\n'

  with open(str(Text_File), 'r') as TextBlock:

    for line in TextBlock.readlines():
      LetterCount=0; FormattedLine=''#          Set up a register to contain the text.
      StringContainer.append(dStart)#           Begin paragraph.

      LetterList=[char for char in line]#       Create character array for letter counting.

      for letter in LetterList:
        FormattedLine+=letter
        LetterCount+=1#                         Add to register; increment counter.

        if LetterCount == 94:#                  Arbitrary choice; only affects HTML source.
          FormattedLine+='\n'
          LetterCount=0#                        Break line' reset counter

      FormattedLine+=dEnd#                      Close the paragraph.

      StringContainer.append(FormattedLine)#    Append the line to the array.

  for StringElement in StringContainer:
    HtmlString+=StringElement#                  Combine all strings into one.

  return HtmlString