# Measuring Aquatic Ultrasonic Level Instrument (MAULI)
Raspberry Pi Pico を用いた電子工作による安価で高性能なロガー付き超音波式水位計です。（1台約5,000円で作成できます。）　プログラムや部品を自由に変更して改造を楽しむことができます。

This is a low-cost, high-performance ultrasonic water level meter with logger that is electronically built using Raspberry Pi Pico. (One can be made for about 5,000 yen.) You can freely change the program and parts to have fun modifying it.

## 特徴
- 主要コードは MicroPython で書かれており、測定間隔等の変更が容易なプログラマブル水位計となっています。
- 超音波センサーの性能に基づき、概ね mm 単位の計測が可能です。
- 市販の小型プラボックスに格納することにより、雨天時の計測が可能です。
- 電源は入手が容易な乾電池を使用しています。
- 故障した場合でも部品単位で簡単に修理することが可能です。

## ライセンス
- 作者が作成した python コードは MIT ライセンスに従うことを前提に改変の自由が守られています。
- 作者以外の方が作成した一部のコードについては、各作者の主張するライセンスに従う必要があります。具体的には以下の通りです。
  - 内蔵温度計から温度を取得する[コード](https://github.com/raspberrypi/pico-micropython-examples/blob/master/adc/temperature.py)の著作権は Raspberry Pi Ltd. にあります。ライセンスは [LICENSE.txt](https://github.com/raspberrypi/pico-micropython-examples/blob/master/LICENSE.txt)に従う必要があります。
  - LCD関係のコードの著作権は Tyler Peppy(T-622) 氏にあります。https://github.com/T-622/RPI-PICO-I2C-LCD

## 作り方
- [2025年1月版](https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/MAULI_202501)




**「玄関みまもるくん」（Raspberry Pi Pico W を使用した玄関の出入り監視装置）**

<img src="https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun/blob/main/IMG_5380.JPG" width="320px">　　<img src="https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun/blob/main/IMG_5493.JPG" width="320px">

<img src="https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun/blob/main/IMG_5575.jpg" width="320px">

人感センサーの反応回数（測定間隔1秒）を記録し、1日1回、1時間単位で集計してLINE通知してくれます。
その他に以下の機能があります。

- 1日1回指定時間でのNTPサーバを使った時間合わせ
- 指定時間内、初感知時のリアルタイムLINE通知（人感センサーが連続3秒反応があった時。曜日指定可能。初期設定：月～金のみ）
- 毎時計測値のpico内ログ記録（急に電源が落ちても過去1日の計測値を確認出来る）


## 使用部品
- Raspberry Pi Pico W
- 人感センサー(HC-SR501)
- USB ACアダプタ
- USBケーブル (2.0タイプAオス-マイクロBケーブル) 
- 取付ケース（例としてティッシュペーパーの箱😅　取付方法は写真を参考に自由に作成してください。）

## 人感センサーの設定
ジャンパはH側とし待ち時間なしとする。
ジャンパに近い方が感度調整（3〜7m）なのでドライバで反時計回りに最大にし3mとする。
ジャンパから遠い方が時間遅延調整（5〜200秒）なので反時計回りに最大にして5秒とする。

<img src="https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun/blob/main/IMG_5570.JPG" width="320px">

**接続は、電源+を VBUS に、電源-を GND に、信号を GP16 にしてください。**


## 使い方
main.py と同じ場所に以下の参考サイトにある tiny_line.py を置いてください（参考サイト参照）。
また、main.py の以下を忘れずに書き換えてください。

- 「自宅Wi-FiのSSIDとパスワードを入力」
- 「LINE tokenを入力」

初期設定は以下の通りです。必要に応じて適宜コード修正してください。
　
- NTP時刻合わせ時間 3時29分
- レポート送信時間 8時10分
- 帰宅時間通知開始および終了時間 12時から21時まで

LINE token の取得方法については以下の参考サイトをご覧ください。

**無事に繋がると Raspberry Pi Pico W の LED が3回点滅**します。その他の場合は再度ACアダプタを抜き差しして電源を入れなおしてください。


## 注意点
- センサーの設置位置はなるべく低くしてください。誤検出が少なくいい結果が得られます。
- 現在、通信に失敗した場合はエラーとなって止まります。その場合は電源を入れなおしてください。そのうちコードを直すかもしれません。


## 参考サイト
- sozorablog | Raspberry Piで電子工作をはじめよう
https://sozorablog.com/raspberry-pi-pico-w-review/

本コードは、そぞらさんのサイト（sozorablog）を全面的に参考にさせていただいております。
コード掲載のご許可もいただきました。ありがとうございます。
