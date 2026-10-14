S=[("tapeo","Tapeo",None,[
("Patatas Bravas de la casa","",7),("Morro de cerdo frito","",8.5),("Oreja de cerdo frita","",8.5),("Rabo de cerdo frito","",9),
("Albóndigas de la casa en salsa de tomate","",10),("Calamares a la romana","",12),("Boquerones rebozados","",11),
("Sepia a la plancha con Mery","",14),("Alitas de pollo a la barbacoa","",9.5),("Croquetón de jamón o bacalao","",2),
("Croquetón de carabineros","",2.8),("Croquetón de boletus con salsa roquefort (und.)","",2.5),
("Delicias de morcilla rellenas de cebolla caramelizada","",2),("Croquetas de cecina (und.)","",1.5),
("Queso fresco en tempura con mermelada de tomate","",9.5),("Medallones de rulo fritos con mermelada de tomate","",9.5),
("Lechecillas de cordero rebozadas al ajillo","",13),
("Delicias de Teruel","Pan tostado, jamón de Teruel, tomate natural, aceite de oliva",14),
("Huevos rotos con jamón serrano y ajo perejil (Mery)","",11)]),
("platos","Platos","Acompañado de patatas y verduras · Guarnición extra 2,00 €",[
("Rabo de toro a la andaluza con guarnición","",18),("Manitas de cerdo en salsa de almendras","",15),
("Entrecot de ternera (300 g)","",20),("Chuletillas de ternasco a la plancha","",16),
("Pechuga de pollo a la plancha con guarnición","",13),("Bacalao a la vizcaína con guarnición","",15)]),
("ninos","Para niños",None,[("Alitas de pollo con patatas fritas","",7.5),("Nuggets de pollo con patatas fritas","",7.5),
("Tortilla francesa con patatas","",7),("Meteoritos de pollo con kétchup","",9)]),
("ensaladas","Ensaladas de la casa",None,[
("Ensalada mixta grande para compartir (4 personas)","Lechuga, tomate, cebolla, zanahoria, remolacha, olivas, espárragos blancos",13),
("Ensalada de queso de rulo (100%)","Con mermelada de tomate, frutos secos y cebolla frita",13),
("Ensalada mixta de la casa con atún y olivas","",10),("Espárragos blancos con jamón serrano y mayonesa","",11)]),
("postres","Postres de la casa",None,[("Profiteroles rellenos de nata","",4.5),("Coulant de chocolate con helado de vainilla","",5.5),
("Flan de queso curado con nata y caramelo","",4.5),("Tarta de queso casera con sirope de frutos rojos","",5.5)])]
p=lambda x:f"{x:.2f}".replace(".",",")+"&nbsp;€"
CSS='''
:root{--g:#d9822b;--au:#d9822b;--br:#2b1d14;--ink:#2b2b2b;--mut:#7a7a7a;--bg:#fbfaf7;--ln:#e6e1d6}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"Helvetica Neue","Segoe UI",Roboto,Arial,sans-serif;font-weight:300;line-height:1.5}
.wrap{max-width:600px;margin:0 auto;min-height:100vh;padding:0 4px}
header{text-align:center;padding:40px 24px 8px}header img{width:56%;max-width:240px}
header.small{padding:22px 24px 0}header.small img{width:84px}
header h1{font-family:Georgia,"Times New Roman",serif;font-weight:normal;letter-spacing:.06em;color:var(--ink);margin:18px 0 0;font-size:1.7rem}
header p{margin:4px 0;letter-spacing:.35em;font-size:.72rem;color:var(--mut)}
.menu{display:flex;flex-direction:column;gap:12px;padding:36px 32px 20px}
.menu a{display:block;text-align:center;text-decoration:none;color:var(--br);border:1px solid var(--au);border-radius:2px;padding:16px 10px;font-family:Georgia,serif;font-size:1.15rem;letter-spacing:.04em;background:#fff}
.menu a:active{background:#f3efe5}
.back{display:block;margin:20px 24px 0;text-align:center;text-decoration:none;color:var(--br);border:1px solid var(--g);border-radius:2px;padding:11px;font-size:.92rem;letter-spacing:.04em;background:#fff}
.back:active{border-color:var(--g)}
section{padding:30px 24px 6px}
h2{text-align:center;font-family:Georgia,"Times New Roman",serif;color:var(--ink);font-weight:normal;letter-spacing:.06em;font-size:1.7rem;margin:0}
.div{width:48px;height:1px;background:var(--au);margin:12px auto 26px}.div span{display:none}
.note{text-align:center;font-size:.85rem;color:var(--mut);margin:-12px 0 22px}
.item{padding:13px 0;border-bottom:1px solid var(--ln)}.item:last-child{border-bottom:0}
.row{display:flex;align-items:baseline;gap:16px;justify-content:space-between}.dots{display:none}
.name{font-size:1rem}.price{color:#b8661c;white-space:nowrap;font-weight:500;font-size:.95rem}.desc{margin:3px 0 0;font-size:.82rem;color:var(--mut)}
.res{text-align:center;padding:4px 32px 0}.res p{margin:0 0 8px;font-family:Georgia,serif;font-size:1rem;letter-spacing:.2em;text-transform:uppercase;color:var(--br)}.res a{display:inline-block;text-decoration:none;color:#fff;background:var(--g);border-radius:2px;padding:12px 26px;font-size:1.1rem;letter-spacing:.06em}.res a:active{background:var(--br)}.tel{display:block;text-align:center;margin:26px 0 0;font-size:.9rem;color:var(--br);text-decoration:none}.tel b{color:#b8661c;font-weight:500}
.ig{display:inline-block;margin-top:14px;text-decoration:none;color:var(--br);border:1px solid var(--g);border-radius:2px;padding:8px 16px;font-size:.85rem;letter-spacing:.03em}.ig b{color:#b8661c;font-weight:500}
.res a.ig{background:none;color:var(--br);padding:8px 16px;font-size:.85rem}.res a.qrl{background:none;padding:0;display:block}
.igqr{display:block;width:180px;margin:16px auto 0}
body.dark{background:#0e0b09;color:#f3ead2}body.dark header h1{color:#f3ead2}body.dark header p,body.dark footer{color:#b9ad97}
body.dark .menu a{background:transparent;color:#f3ead2;border-color:#d9822b}body.dark .menu a:active{background:#d9822b33}
body.dark .res p{color:#f3ead2}body.dark .res a.ig{color:#f3ead2;border-color:#d9822b}body.dark .res a.ig b{color:#e8964a}
body.dark .igqr{background:#fff;border-radius:14px;padding:10px}
.igb{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;background:radial-gradient(circle at 30% 107%,#fdf497 0%,#fd5949 45%,#d6249f 60%,#285AEB 90%);text-decoration:none}
.res a.igb{display:inline-flex;border-radius:50%;width:56px;height:56px;padding:0;margin-top:0;background:radial-gradient(circle at 30% 107%,#fdf497 0%,#fd5949 45%,#d6249f 60%,#285AEB 90%)}
.igh{display:block;margin:6px 0 0;font-size:.85rem;color:#e8964a;text-decoration:none}.res a.igh{display:block;margin-top:6px;background:none;padding:0;color:#e8964a;font-size:.85rem;letter-spacing:.02em}
.sf{display:flex;align-items:center;justify-content:center;gap:12px;margin:26px 0 0}.sf .tel{margin:0}.sf .igb{width:34px;height:34px}
.res p.sg{margin:26px 0 10px;font-family:Georgia,serif;font-style:italic;font-size:.95rem;letter-spacing:.08em;text-transform:none;color:#f3ead2}
footer{text-align:center;padding:32px 16px 40px;font-size:.72rem;letter-spacing:.1em;color:var(--mut)}
'''
def page(title,inner,cls=''):
  return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="theme-color" content="#1f3d2b"><style>{CSS}</style></head><body class="{cls}"><div class="wrap">{inner}<footer>Bar El Cazador · Villel (Teruel)</footer></div></body></html>'''
btns="".join(f'<a href="{i}.html">{t}</a>' for i,t,_,_ in S)
open("index.html","w").write(page("Carta · Bar El Cazador · Villel",
 f'<header><img src="logo.png" alt="Bar El Cazador · Villel"><h1>Bar El Cazador</h1><p>VILLEL · TERUEL</p></header><nav class="menu">{btns}</nav><div class="res"><p>Reservas</p><a href="tel:+34978092531">&#9742;&nbsp; 978 09 25 31</a><p class="sg">Síguenos en</p><a class="igb" href="https://www.instagram.com/barelcazadorvillel/" target="_blank" rel="noopener" aria-label="Instagram @barelcazadorvillel"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="#fff" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="#fff" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3" fill="#fff"/></svg></a><a class="igh" href="https://www.instagram.com/barelcazadorvillel/" target="_blank" rel="noopener">@barelcazadorvillel</a></div>',"dark"))
for i,t,n,items in S:
  b=f'<header class="small"><a href="index.html"><img src="logo.png" alt="Bar El Cazador"></a></header><a class="back" href="index.html">← Volver a la carta</a><section><h2>{t}</h2><div class="div"><span>✦</span></div>'
  if n: b+=f'<p class="note">{n}</p>'
  for a,d,pr in items:
    b+=f'<div class="item"><div class="row"><span class="name">{a}</span><span class="dots"></span><span class="price">{p(pr)}</span></div>'+(f'<p class="desc">{d}</p>' if d else '')+'</div>'
  b+='</section><a class="back" href="index.html">← Volver a la carta</a><div class="sf"><a class="tel" href="tel:+34978092531">Reservas: <b>978 09 25 31</b></a><a class="igb" href="https://www.instagram.com/barelcazadorvillel/" target="_blank" rel="noopener" aria-label="Instagram @barelcazadorvillel"><svg viewBox="0 0 24 24" width="19" height="19" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="#fff" stroke-width="2"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="#fff" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3" fill="#fff"/></svg></a></div>'
  open(f"{i}.html","w").write(page(f"{t} · Bar El Cazador",b))
