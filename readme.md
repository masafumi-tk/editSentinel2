## 追加が必要なパッケージ
    - pip install opencv-python # opencv
    - pip install boto3　# S3の操作用

## 開発環境
    - pythonバージョン：3.10.2
    - mac book air(m1)

## edit_img.py
### 概要
画像の切り抜きなどの加工をする。
main関数で出力時の設定（ファイル名など）と入力ファイルの設定後、下記で実行。
```
$ python edit_img.py
```
 
#### return_frame_size
入力した画像の解像度を取得する
#### cut_out_img
入力した画像を指定した原点から任意のピクセル分切り抜く処理を行う。
※衛星データの拡張子はjp2だが、jp2は小さいサイズの画像に対応していない可能性あるため、1ピクセルだけ切り抜くといったことはできない。


## generate_movie.py
### 概要
指定したフォルダ内の画像ファイルを読み込み、指定したFPSの動画を作成する。
config/generate_movie_config.iniで各設定後、下記を実行。
```
$ python generate_movie.py
```
### 備考
現状、異なる拡張子が保存されていた場合のエラー対応など、各種エラー対応は組み込めていない