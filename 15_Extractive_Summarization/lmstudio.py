# openai 설치
# pip install openai 

from openai import OpenAI

# 파일에서 문서 텍스트를 읽어오는 함수
def read_document_text(filename):
    with open(filename, 'r') as file:
        document_text = file.read()
    return document_text

# 로컬 서버를 가리키는 클라이언트 설정
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 파일에서 문서 텍스트를 읽어옴
document_text = read_document_text('abstract.txt')

# 완성본 생성 요청
completion = client.chat.completions.create(
  model="model-identifier",
  messages=[
    {"role": "system", "content": "You are an extractive summarizer that follows the output pattern."},
    {"role": "user", "content": f"Please extract sentences as the summary. Document: {document_text}"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)