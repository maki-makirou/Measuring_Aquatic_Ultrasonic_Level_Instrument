# Measuring Aquatic Ultrasonic Level Instrument (MAULI)
　Raspberry Pi Pico を用いた電子工作による**安価で高性能なロガー付き超音波式水位計**です。（1台約6,000円で作成できます。）　プログラムや部品を自由に変更して改造を楽しむことができます。

This is a low-cost, high-performance ultrasonic water level meter with logger that is electronically built using Raspberry Pi Pico. (One can be made for about 6,000 yen.) You can freely change the program and parts to have fun modifying it.

<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/IMG_6465.JPG" width="320px">　　<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/IMG_6523.JPG" width="320px">

## 特徴
- 主要コードは MicroPython で書かれており、測定間隔等の変更が容易なプログラマブル水位計です。
- 超音波センサーの性能に基づき、概ね mm 単位の計測が可能です。（測定距離min: 0.02m、測定距離max: 4.5m、動作温度min: -10℃、動作温度max: 70℃）
- 小型プラボックスに格納しているため屋外での計測が可能です。雨天時の計測もできます。
- 故障した場合でも部品単位で修理することが容易です。

## ライセンス
- 作者が作成した python コードは MIT ライセンスに従って自由に改変することが出来ます。
- 作者以外の方が作成したコードについては、以下の通り各作者の主張するライセンスに従う必要があります。
  - 内蔵温度計から温度を取得する[コード](https://github.com/raspberrypi/pico-micropython-examples/blob/master/adc/temperature.py)の著作権は Raspberry Pi Ltd. にあります。ライセンスは [LICENSE.txt](https://github.com/raspberrypi/pico-micropython-examples/blob/master/LICENSE.txt)に従う必要があります。
  - LCD関係のコードの著作権は Tyler Peppy(T-622) 氏にあります。https://github.com/T-622/RPI-PICO-I2C-LCD

## 作り方

以下のリンクの通りです。

- [2025年1月版](https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/MAULI_202501/MAULI_202501.md)

## 改造について
改造についても自己責任となります。大容量の電池に交換すればより実用的になります。水位計を wifi 対応したい場合は、私の以下のサイトなどをご参考ください。
https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun

## 注意点
屋外設置の際は、土地所有者や水路管理者の許可が必要です。**許可なく水位計を設置しないようご注意ください。**

## 謝辞
Raspberry Pi財団の皆様と電子部品やプラボックス等を供給してくださるメーカーの皆様に感謝します。最後に私の妻に感謝します。

