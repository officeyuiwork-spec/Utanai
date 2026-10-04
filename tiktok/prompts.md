# 夜ママうさぎ TikTok 7コマ

- サイズ: 1080×1920
- 安全エリア: 上20%（0〜384px）、下30%（1344〜1920px）、右20%（864〜1080px）を除いた **x 0〜864 / y 384〜1344**
- 再生成: `cd tiktok && pip install pillow && python3 make.py`（`out/` に出力）

## 構成

| # | ラベル | メインテキスト | サブテキスト | うさぎ |
|---|---|---|---|---|
| 1 | 夜ママあるある | 夜中の育児 がんばってるママへ | 「わかる…」ってなったら最後まで見てね | エプロンのママ |
| 2 | PM 9:30 | やっと寝かしつけ完了…と思ったら | また起きた…（まだ30分しか経ってない） | 目をこするママ |
| 3 | AM 0:00 | 寝かしつけ後の「自分時間」のはずが | 家事・仕事・連絡帳… 今日もやることおわらない | パソコンのママ |
| 4 | AM 2:00 | 夜泣き・授乳・抱っこ エンドレス | もうムリ… でも抱っこはやめられない | 机につっぷすママ |
| 5 | AM 3:30 | 眠いのに目が冴えちゃう謎 | とりあえずコーヒー（たぶん逆効果） | コーヒーのママ |
| 6 | あるある | パパが抱っこするとなぜか即寝る | ママの1時間はなんだったの…？ | 妹を抱っこするパパ |
| 7 | 今夜も | ほんとうにおつかれさま | 誰にも見えない夜のがんばり ちゃんと届いてるよ | 家族みんなで |

## 画像生成AI用プロンプト（キャラ参照画像を添付して使う）

共通:
```
Use the attached character sheet as the exact character reference. Cute pastel hand-drawn rabbit,
cream-white body, pink cheeks, thin brown outline, sleepy half-closed eyes, soft watercolor texture,
plain cream background, simple, centered, no text. Vertical 9:16.
```

1. `Mama rabbit in a pink apron standing, sleepy half-closed eyes, small crescent moon in the background`
2. `Mama rabbit in a pink apron rubbing her eye, just woken up at night, tiny sweat drops`
3. `Mama rabbit working on a grey laptop at a desk late at night, tired face, desk lamp`
4. `Mama rabbit collapsed face-down on a table, exhausted, small motion lines`
5. `Mama rabbit with round glasses-free sleepy eyes holding a grey mug of coffee with a rabbit logo, 3am`
6. `Papa rabbit with round glasses holding the little sister rabbit (pink bow) who is instantly asleep, music note and heart`
7. `The whole rabbit family (papa with glasses, mama, brother, sister with pink bow) sleeping together under a blanket, crescent moon`

※ テキストは生成AIに描かせず、後から重ねるのがおすすめ（日本語が崩れにくい）。
