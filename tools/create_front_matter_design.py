"""Original vector cover and monochrome title-page design study (US Letter)."""
from pathlib import Path
import math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf'
OUT.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('BookSerif','C:/Windows/Fonts/georgia.ttf'))
pdfmetrics.registerFont(TTFont('BookSans','C:/Windows/Fonts/arial.ttf'))
W,H=612,792
c=canvas.Canvas(str(OUT/'v1.1-cover-and-title-page.pdf'),pagesize=(W,H),pageCompression=1)
c.setTitle('Introduction to Physics - cover and title page design')
c.setSubject('Version 1.1 front matter design study; original mathematical vector artwork')

def label(text,x,y,color,size=10,spacing=1.6):
    t=c.beginText(x,y); t.setFont('BookSans',size); t.setFillColor(color); t.setCharSpace(spacing); t.textOut(text); c.drawText(t)

def title(color):
    c.setFillColor(color); c.setFont('BookSerif',43)
    c.drawString(62,641,'Introduction')
    c.drawString(62,585,'to Physics')

# Color cover: no logos, external artwork, seals or institutional marks.
navy=HexColor('#102F43'); pale=HexColor('#F5F1E8')
c.setFillColor(navy); c.rect(0,0,W,H,fill=1,stroke=0)
label('VERSION 1.1',64,710,HexColor('#B8CFD6'),9)
title(pale)
c.setStrokeColor(HexColor('#D4B274')); c.setLineWidth(1.5); c.line(64,550,112,550)
# A family of smooth waves: an original, purely geometric motif.
for j in range(13):
    c.setStrokeColor(HexColor('#487E8C') if j!=6 else HexColor('#D4B274'))
    c.setLineWidth(.65 if j!=6 else 1.5)
    path=c.beginPath()
    for k in range(489):
        x=62+k
        u=k/488
        envelope=math.sin(math.pi*u)**1.2
        y=292+(j-6)*9+envelope*(42+3*j)*math.sin(2*math.pi*(1.25*u)+j*.14)
        if k==0:path.moveTo(x,y)
        else:path.lineTo(x,y)
    c.drawPath(path)
label('INTRO.COAPHYS.XYZ',64,63,HexColor('#B8CFD6'),8,1.2)
c.setFillColor(HexColor('#B8CFD6')); c.setFont('BookSans',9); c.drawRightString(548,63,'Park')
c.showPage()
# Matching monochrome title page, low ink coverage.
label('VERSION 1.1',64,710,black,9)
title(black)
c.setStrokeColor(black); c.setLineWidth(.6); c.line(64,550,112,550)
label('INTRO.COAPHYS.XYZ',64,63,black,8,1.2)
c.setFillColor(black); c.setFont('BookSans',9); c.drawRightString(548,63,'Park')
c.showPage(); c.save()
print(OUT/'v1.1-cover-and-title-page.pdf')
