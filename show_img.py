import cv2
import glob
import os
import configparser

# [ToDo]
# 現状、指定した感覚で画像を表示することはできているが、画像ファイルの容量が大きくなると読み込みに時間がかかり、
# 指定した感覚以上の表示となっている。
# 毎回、画像を読み込んでいるが、読み込みは一度に行い、描画だけ行う…といった、容量に依存しない表示方法を検討する

def main():
    # --------------------------------------------------
    # configparserの宣言とiniファイルの読み込み
    # --------------------------------------------------
    config_ini = configparser.ConfigParser()
    config_ini.read('./config/show_img_config.ini', encoding='utf-8')

    # 画像ファイルのフォルダを指定
    image_directory = f"{config_ini['SETTING']['IMAGE_DIRECTORY']}"

    # 指定のディレクトリ内で指定した拡張子の画像リストを取得
    images = glob.glob(f"{image_directory}/*.{config_ini['SETTING']['FILE_EXTENSION']}")

    # 秒間5枚（= 1枚あたりconfigで指定したミリsecで表示）
    show_img(images,float(config_ini['SETTING']['DELAY']))

def show_img(images,delay):
    # images:ファイルのリスト
    # delay:画像一枚あたりの待機時間（ミリ秒）

    # ファイル名でソート
    images = sorted(images)
    print(delay)

    for image in images:
        # 画像ファイルの読み込み
        img = cv2.imread(image)

        if img is not None:
            # 画像を表示（第一引数は画面に表示する名前）
            cv2.imshow("Image", img)
            # 指定したミリ秒待機
            cv2.waitKey(int(delay * 1000)) 

            # テスト用：キー入力ごとに表示
            # cv2.waitKey()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()