import cv2
import os
import glob
import configparser

# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
# --------------------------------------------------
config_ini = configparser.ConfigParser()
config_ini.read('./config/generate_movie_config.ini', encoding='utf-8')

# 画像が保存されているフォルダを指定
image_folder = config_ini['SETTING']['IMAGE_DIRECTORY']

# 出力動画の設定
fps = config_ini['SETTING']['FPS']  # フレームレート
video_name = config_ini['SETTING']['OUT_PUT_VIDEO_NAME'] # 出力する動画名
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # コーデックを指定

# 特定のパターンに一致する画像リストを取得
images = [img for img in glob.glob(f"{image_folder}/{config_ini['SETTING']['FILE_EXTENSION']}")]
images.sort()  # ファイル名でソート

# 最初の画像から動画の解像度を取得
frame = cv2.imread(images[0])
height, width, layers = frame.shape
size = (width, height)

# VideoWriterオブジェクトの作成
out = cv2.VideoWriter(video_name, fourcc, fps, size)

# 画像を動画に追加
for image in images:
    frame = cv2.imread(image)
    out.write(frame)

# 出力動画を閉じる
out.release()

