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

<img src="https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun/blob/main/IMG_5570.JPG" width="320px">

## 注意点
- センサーの設置位置はなるべく低くしてください。誤検出が少なくいい結果が得られます。

