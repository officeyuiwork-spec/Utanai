"""Gemini画像生成でうさぎイラストを作り、src/ai_<name>.png に保存する。
使い方: GEMINI_API_KEY を環境変数に設定して `python3 gen_ai.py` → `python3 make.py`
"""
import base64, json, os, sys, urllib.request

KEY = os.environ.get('GEMINI_API_KEY') or sys.exit('GEMINI_API_KEY が設定されていません')
MODEL = os.environ.get('GEMINI_IMAGE_MODEL', 'gemini-2.5-flash-image')
REF = os.path.join(os.path.dirname(__file__), 'src', 'reference.png')
BASE = ('Use the attached character sheet as the exact character reference: cute pastel hand-drawn rabbit, '
        'cream-white body, pink cheeks, thin brown outline, sleepy half-closed eyes, soft watercolor texture. '
        'Plain flat cream background (#FAF8F0), single centered illustration, no text, no letters. Scene: ')
SCENES = {
    'mama': 'Mama rabbit in a pink apron standing, sleepy, small crescent moon nearby',
    'okita': 'Mama rabbit in a pink apron rubbing her eye, just woken up at night, tiny sweat drop',
    'laptop': 'Mama rabbit typing on a grey laptop at a desk late at night, tired face',
    'muri': 'Mama rabbit collapsed face-down on a table, exhausted, small motion lines',
    'nemui': 'Mama rabbit in a pink apron holding a grey mug of coffee with a rabbit logo, very sleepy',
    'papadakko': 'Papa rabbit with round glasses holding the little sister rabbit (pink bow) who fell asleep instantly, music note and heart',
    'sleep': 'The whole rabbit family (papa with round glasses, mama, brother, sister with pink bow) sleeping together under a blanket, crescent moon',
}
ref = base64.b64encode(open(REF, 'rb').read()).decode()
for name, scene in SCENES.items():
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue
    body = {'contents': [{'parts': [{'inline_data': {'mime_type': 'image/png', 'data': ref}}, {'text': BASE + scene}]}],
            'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '1:1'}}}
    req = urllib.request.Request(
        f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent',
        data=json.dumps(body).encode(), headers={'Content-Type': 'application/json', 'x-goog-api-key': KEY})
    res = json.load(urllib.request.urlopen(req, timeout=180))
    parts = res['candidates'][0]['content']['parts']
    img = next(p.get('inlineData') or p.get('inline_data') for p in parts if 'inlineData' in p or 'inline_data' in p)
    open(f'src/ai_{name}.png', 'wb').write(base64.b64decode(img['data']))
    print('saved', name)
