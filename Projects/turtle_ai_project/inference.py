import cv2
import numpy as np
import onnxruntime as ort
import os

# 1. 환경 설정
MODEL_PATH = "mobilenet_v2.onnx"
LABEL_PATH = "imagenet_classes.txt"
IMAGE_PATH = "dog.jpg"

# 2. 파일 존재 확인
if not os.path.exists(IMAGE_PATH):
    print(f"❌ 에러: {IMAGE_PATH} 파일이 없습니다. 다운로드를 확인해 주세요!")
    exit()

# 3. 모델 및 라벨 로드
session = ort.InferenceSession(MODEL_PATH)
input_name = session.get_inputs()[0].name
with open(LABEL_PATH, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

# 4. 이미지 읽기 및 검증
image = cv2.imread(IMAGE_PATH)
if image is None:
    print(f"❌ 에러: {IMAGE_PATH}를 읽을 수 없습니다. 파일이 깨졌을 수 있습니다.")
    exit()

# 5. 전처리
img = cv2.resize(image, (224, 224))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.astype(np.float32) / 255.0
img = np.transpose(img, (2, 0, 1))
img = np.expand_dims(img, axis=0)

# 6. 추론 실행
outputs = session.run(None, {input_name: img})
predicted_idx = np.argmax(outputs[0])

# 7. 결과 출력
print("-" * 30)
print(f"📸 이미지 분석 결과: {labels[predicted_idx]}")
print("-" * 30)
