from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random, os
W,H=1080,1920
SAFE=(0,int(H*.2),int(W*.8),int(H*.7))   # x0,y0,x1,y1 = 0,384,864,1344
F='kiwi.ttf'
CARD=(250,248,240); INK=(74,62,58); PINK=(232,150,160); SUB=(140,120,112)
def font(s): return ImageFont.truetype(F,s)
frames=[
 ('夜ママあるある','夜中の育児\nがんばってるママへ','mama','「わかる…」ってなったら\n最後まで見てね'),
 ('PM 9:30','やっと寝かしつけ\n完了…と思ったら','okita','また起きた…\n（まだ30分しか経ってない）'),
 ('AM 0:00','寝かしつけ後の\n「自分時間」のはずが','laptop','家事・仕事・連絡帳…\n今日もやることおわらない'),
 ('AM 2:00','夜泣き・授乳・抱っこ\nエンドレス','muri','もうムリ…\nでも抱っこはやめられない'),
 ('AM 3:30','眠いのに\n目が冴えちゃう謎','nemui','とりあえずコーヒー\n（たぶん逆効果）'),
 ('あるある','パパが抱っこすると\nなぜか即寝る','papadakko','ママの1時間は\nなんだったの…？'),
 ('今夜も','ほんとうに\nおつかれさま','sleep','誰にも見えない夜のがんばり\nちゃんと届いてるよ'),
]
def bg():
    im=Image.new('RGB',(W,H)); d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)],fill=(int(44+30*t),int(52+28*t),int(92+20*t)))
    random.seed(7)
    for _ in range(90):
        x,y=random.randrange(W),random.randrange(H); r=random.choice([1,1,2,2,3])
        d.ellipse([x-r,y-r,x+r,y+r],fill=(255,244,200))
    return im
def moon(d,cx,cy,r):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(250,222,140))
def ctext(d,cx,y,txt,f,fill,sp=14):
    for line in txt.split('\n'):
        w=d.textlength(line,font=f); d.text((cx-w/2,y),line,font=f,fill=fill); y+=f.size+sp
    return y
os.makedirs('out',exist_ok=True)
for i,(chip,head,art,sub) in enumerate(frames,1):
    im=bg(); d=ImageDraw.Draw(im)
    x0,y0,x1,y1=SAFE; pad=36
    cx0,cy0,cx1,cy1=x0+pad,y0+16,x1-16,y1-16
    # soft shadow + card
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rounded_rectangle([cx0,cy0+10,cx1,cy1+10],48,fill=110)
    im.paste((20,24,50),mask=sh.filter(ImageFilter.GaussianBlur(18)))
    d.rounded_rectangle([cx0,cy0,cx1,cy1],48,fill=CARD)
    # moon on card corner
    d.ellipse([cx1-110,cy0+34,cx1-50,cy0+94],fill=(250,222,140)); d.ellipse([cx1-92,cy0+24,cx1-38,cy0+78],fill=CARD)
    mid=(cx0+cx1)//2
    fc=font(34); t=chip; tw=d.textlength(t,font=fc)
    d.rounded_rectangle([mid-tw/2-28,cy0+44,mid+tw/2+28,cy0+44+60],30,fill=PINK)
    d.text((mid-tw/2,cy0+52),t,font=fc,fill='white')
    y=ctext(d,mid,cy0+138,head,font(58),INK,16)
    # illustration
    src=f'src/ai_{art}.png' if os.path.exists(f'src/ai_{art}.png') else f'src/c_{art}.png'
    a=Image.open(src).convert('RGB')
    boxw,boxh=cx1-cx0-60, 470
    s=min(boxw/a.width,boxh/a.height); a=a.resize((int(a.width*s),int(a.height*s)),Image.LANCZOS)
    m=Image.new('L',a.size,0); e=26
    ImageDraw.Draw(m).rounded_rectangle([e,e,a.width-e,a.height-e],40,fill=255); m=m.filter(ImageFilter.GaussianBlur(14))
    ay=y+20+(boxh-a.height)//2
    im.paste(a,(mid-a.width//2,ay),m)
    ctext(d,mid,y+20+boxh+26,sub,font(40),SUB,12)
    fp=font(26); d.text((cx1-80,cy1-52),f'{i}/7',font=fp,fill=(200,190,180))
    im.save(f'out/frame{i}.png')
# guide overlay for frame1
g=Image.open('out/frame1.png').convert('RGBA'); o=Image.new('RGBA',g.size,(0,0,0,0)); od=ImageDraw.Draw(o)
od.rectangle([0,0,W,SAFE[1]],fill=(255,0,0,70)); od.rectangle([0,SAFE[3],W,H],fill=(255,0,0,70)); od.rectangle([SAFE[2],SAFE[1],W,SAFE[3]],fill=(255,0,0,70))
Image.alpha_composite(g,o).convert('RGB').save('guide.png')
