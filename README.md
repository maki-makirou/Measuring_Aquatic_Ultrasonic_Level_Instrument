# Measuring Aquatic Ultrasonic Level Instrument (MAULI)
　Raspberry Pi Pico を用いた電子工作による**安価で高性能なロガー付き超音波式水位計**です。（1台約6,000円で作成できます。）　プログラムや部品を自由に変更して改造を楽しむことができます。

This is a low-cost, high-performance ultrasonic water level meter with logger that is electronically built using Raspberry Pi Pico. (One can be made for about 6,000 yen.) You can freely change the program and parts to have fun modifying it.

<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/img/IMG_6569.JPG" width="320px">　　<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/img/IMG_6572.JPG" width="320px">

<br>

## 特徴
- 主要コードは MicroPython で書かれており、測定間隔等の変更が容易なプログラマブル水位計です。
- 超音波センサーの性能に基づき、概ね mm 単位の計測が可能です。（測定距離min: 0.02m、測定距離max: 4.5m、動作温度min: -10℃、動作温度max: 70℃）
- 小型プラボックスに格納しているため屋外での計測が可能です。雨天時の計測もできます。
- 異常値が出た時に設定した時間間隔、回数で再計測させることができます。
- アルカリ単3電池3本で約7.5日間の連続計測ができます。単1電池6本にすれば約3ヶ月の連続計測ができます。
- 故障した場合でも部品単位で修理が容易です。

<br>

## 短所
- 耐久性はあまりないと思われます。但し、これまで屋外計測で壊れたことはありません。
- 組み立てが面倒です。
- 部品が改良された場合、正しく動作させるために配線やコードの修正が必要になる可能性があります。

<br>

## ライセンス
- 作者が作成した python コードは MIT ライセンスに従って自由に改変することが出来ます。
- 作者以外の方が作成したコードについては、以下の通り各作者の主張するライセンスに従う必要があります。
  - 内蔵温度計から温度を取得する[コード](https://github.com/raspberrypi/pico-micropython-examples/blob/master/adc/temperature.py)の著作権は Raspberry Pi Ltd. にあります。ライセンスは [LICENSE.txt](https://github.com/raspberrypi/pico-micropython-examples/blob/master/LICENSE.txt)に従う必要があります。
  - LCD関係のコードの著作権は Tyler Peppy(T-622) 氏にあります。https://github.com/T-622/RPI-PICO-I2C-LCD

<br>

## 作り方
以下のリンク先をご覧ください。
- [2025年1月版](https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/MAULI_202501/MAULI_202501.md)

<br>

## 使い方
### 設置時

1 水位観測においては、水位計の設置位置の選定が重要です。**水位計は水深が変化しない地点に設置してください。**
また、**超音波の有効角度が15度であることを踏まえ、超音波が不要なもの（構造物や植物等）に当たって反射しないように（水面だけに当たるように）設置してください。**

2 初期設定では、**電源を入れて1分間は計測値が液晶ディスプレイに表示されるスタートモード**になり、**1分後以降はログ記録モードになり測定値を内部メモリに1分間隔で記録します**。電池をセットし、時計を見ながら 00 秒ちょうどに電源を入れてください。**1分後の時刻を忘れずにメモしてください。**

3 **水位計の設置地点の水深をmm単位で測り、忘れずにメモしておいてください。**

4 屋外で使用する場合は、風等の衝撃で電池が外れることがあります。**電池が外れないように必ずセロハンテープ等で固定してください。**

<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/img/IMG_6586.JPG" width="320px">

5 **南京錠等でフタが開かないようにしてください。**

<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/img/IMG_6585.JPG" width="320px">　　<img src="https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument/blob/main/img/IMG_6583.JPG" width="320px">

<br>

### データ回収時

1 水位計を回収したら　PC に接続して Thonny を起動して、右上の「STOP」ボタンを押した後、ラズパイ pico 内の「log.csv」ファイルを開いてデータをコピーしてください。Thonny の使い方は他のサイトで調べてください。

2 表計算ソフトを立ち上げてコピーしたデータをペーストして一旦保存してください。

3 メモした記録開始時間と水深データを使って、水位の時刻変化のデータに変換してください。ロガーに記録されている 「Distance(m)」 は水面までの距離を記録したものですので水位への変換が必要です。

4 無事にデータを水位に変換できたら、次の測定のために Thonny でラズパイ pico 内の「log.csv」ファイルを右クリックして「Delete」してください。

<br>

## 改造について
大容量の電池を使用できるようになればより実用的になります。[このサイト（単1電池6本版）](https://github.com/maki-makirou/Measuring_Aquatic_Ultrasonic_Level_Instrument_Mod)をご参考ください。また、水位計を wifi 対応したい場合は、[このサイト](https://github.com/maki-makirou/RPI-RP2_genkan_mimamoru_kun)などをご参考ください。なお、改造についても自己責任となります。

<br>

## 注意点
屋外設置の際は、土地所有者や水路管理者の許可が必要です。**許可なく水位計を設置しないようご注意ください。**

<br>

## 謝辞
Raspberry Pi財団の皆様と電子部品やプラボックス等を供給してくださるメーカーの皆様に感謝します。最後に私の妻に感謝します。

<br>

