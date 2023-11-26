import cv2

# [メモ]jp2は小さいサイズの画像に対応していない可能性あるため、1ピクセルだけ切り抜くといったことはできない。

def main():
    # 加工元データpath及びファイル名
    ORIGINAL_IMG_PATH = "./"
    ORIGINAL_IMG_NAME = "B02-10m.jp2"

    # 出力ファイルの指定
    OUT_PUT_IMG_PATH = "./"
    OUT_PUT_IMG_NAME = "outputimg"
    OUT_PUT_IMG_EXTENSION = ".jp2"

    # 画像の読み込み
    original_image = cv2.imread(f"{ORIGINAL_IMG_PATH}{ORIGINAL_IMG_NAME}")
    
    # 画像の切り抜き
    # cutOutImg("出力する画像ファイルのpathと名前、拡張子",対象の画像,切り抜きの原点y,切り抜きの原点x,高さ,幅)
    cut_out_img(f"{OUT_PUT_IMG_PATH}{OUT_PUT_IMG_NAME}{OUT_PUT_IMG_EXTENSION}",original_image,6000,7000,500,500)

# 画像の解像度を取得する関数
def return_frame_size(img):
    frame = img
    height, width, layers = frame.shape
    size = (width, height)
    
    return size

def cut_out_img(out_put_file,img,top,bottom,height,width):
    # outputfilename:出力するファイル名（path,拡張子も含めて受け取る）
    # img:切り抜く画像
    # top: 切り抜く原点y座標
    # bottom: 切り抜く原点x座標
    # height: 原点から切り抜きたい高さ
    # width: 原点から切り抜きたい幅

    """
    [参考]切り取りの順番
    img[切り抜く原点のy座標:原点から切り抜きたい点のy座標, 切り抜く原点のx座標:原点から切り抜きたい点のy座標]
    """
    output_image = img[top:top+height,bottom:bottom+width]
    cv2.imwrite(out_put_file,output_image)

if __name__ == '__main__':
    main()
