text = """
<div class="sh" style="font-size: 110%; display: none;">
<span></span>
<br>
<div class="lmainText">
    <button class="sh-close hidden-lg">×</button>
    <div class="nkv">
        Квартира №153
        <br>
        <font style="font-weight:bold;"> (1стр.)</font>
    </div>
    <br>
        Количество комнат: 2
    <br>
    <br>
        Общая площадь:
    <br>
        63,50кв.м.
    <br>
    <br>
        Площадь квартиры:
    <br>
        63,50/59,30/25,70
    </div>
<div class="nkv">
    Цена:
    <font style="color:#191919;">7 731 125,00 руб</font>
</div>
<br>
<a class="g2button_next" href="#" onclick="$.getobj(18,1);return false;">Подробнее</a></div>
"""

import re

#pattern = r'<br>\s*\n*([^<\n]+)'
pattern_common = r'<br>\s*([^<\s\n][^<\n]*?)\s*(?=<br>|$)'
results_common = re.findall(pattern_common, text)

pattern_price  = r'<font[^>]*>(.*?)</font>'
results_pirce = re.findall(pattern_price, text)

pattern_no = r'№\s*(\d+)'
results_no = re.findall(pattern_no, text)

rooms = re.sub(r'\D', '', results_common[0])
no = results_no[0]
price = results_pirce[1]
area = results_common[2]

data = [no, rooms, area, price]

print(data)
