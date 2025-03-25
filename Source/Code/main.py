from PIL import Image

# 바탕화면 경로에 있는 이미지 불러오기
image_path = "/Users/na/Desktop/IMG_6840.JPG"  # 바탕화면 경로에 맞게 수정하세요
image = Image.open(image_path)
image.show()  # 이미지를 열어서 확인
