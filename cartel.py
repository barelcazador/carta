from PIL import Image,ImageDraw,ImageFont
import cv2,numpy as np
W,H=1240,1748;BR=(43,29,20);OR=(217,130,43);GR=(122,122,122)
c=Image.new("RGB",(W,H),"white");d=ImageDraw.Draw(c)
SF="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf";SS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf";F=ImageFont.truetype
def ct(x,w,y,t,f,col): d.text((x+(w-d.textlength(t,font=f))/2,y),t,font=f,fill=col)
lg=Image.open("site/logo.png").convert("RGBA");lg.thumbnail((500,440));c.paste(lg,((W-lg.width)//2,80),lg)
y=80+lg.height+40
ct(0,W,y,"Escanea y mira",F(SF,70),BR);ct(0,W,y+85,"nuestra carta",F(SF,70),BR)
y+=195;d.line((W//2-60,y,W//2+60,y),fill=OR,width=4);y+=45
q=Image.open("qr_carta.png").resize((540,540),Image.NEAREST);g=Image.open("qr_instagram.png").resize((380,380),Image.NEAREST)
c.paste(q,(120,y));c.paste(g,(W-120-380,y+80))
ct(120,540,y+545,"Carta",F(SS,46),BR);ct(W-500,380,y+470,"Instagram",F(SS,40),BR);ct(W-500,380,y+522,"@barelcazadorvillel",F(SS,28),OR)
y+=630;d.line((120,y,W-120,y),fill=(230,225,214),width=2)
ct(0,W,y+30,"Reservas: 978 09 25 31",F(SS,54),BR);ct(0,W,y+105,"Villel · Teruel",F(SS,32),GR)
print("bottom",y+150)
c.save("cartel_qr.png",dpi=(300,300))
print(cv2.wechat_qrcode_WeChatQRCode().detectAndDecode(np.array(c)[:,:,::-1].copy())[0])
