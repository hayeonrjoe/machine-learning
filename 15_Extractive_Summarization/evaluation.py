# rouge 설치
# pip install rouge

from rouge import Rouge

# 텍스트 파일 내용을 읽어오는 함수 정의
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.readlines()
    return [line.strip() for line in contents]

# 참조 요약 텍스트 파일 경로 정의
ref_summary_file_1 = "abstract.txt"
ref_summary_file_2 = "chatgpt_summary.txt"

# 생성된 요약 텍스트 파일 경로 정의
gen_summary_file_1 = "mistral_summary.txt"
gen_summary_file_2 = "gemma_summary.txt"

# 참조 요약 텍스트 파일 내용 읽기
ref_summaries_1 = read_text_file(ref_summary_file_1)
ref_summaries_2 = read_text_file(ref_summary_file_2)

# 생성된 요약 텍스트 파일 내용 읽기
gen_summaries_1 = read_text_file(gen_summary_file_1)
gen_summaries_2 = read_text_file(gen_summary_file_2)

# ROUGE 점수 계산을 위한 초기화
rouge = Rouge()

# 각 생성된 요약에 대한 각 참조 요약에 대한 ROUGE 점수 계산
scores_gen1_ref1 = rouge.get_scores(gen_summaries_1, ref_summaries_1)
scores_gen1_ref2 = rouge.get_scores(gen_summaries_1, ref_summaries_2)

scores_gen2_ref1 = rouge.get_scores(gen_summaries_2, ref_summaries_1)
scores_gen2_ref2 = rouge.get_scores(gen_summaries_2, ref_summaries_2)

# 각 생성된 요약에 대한 각 참조 요약에 대한 ROUGE 점수 출력
print("ROUGE scores for Mistral 7B Instruct v0.2:")
print("Against Abstract:", scores_gen1_ref1)
print("Against ChatGPT Summary:", scores_gen1_ref2)

print("\nROUGE scores for Gemma 7B Instruct:")
print("Against Abstract:", scores_gen2_ref1)
print("Against ChatGPT Summary:", scores_gen2_ref2)

# 각 생성된 요약에 대한 각 참조 요약에 대한 ROUGE 점수 출력
def calculate_avg_scores(scores):
    avg_scores = {}
    for metric in scores[0][0]:
        avg_scores[metric] = sum(score[0][metric]['f'] for score in scores) / len(scores)
    return avg_scores

# 각 생성된 요약에 대한 평균 ROUGE 점수 계산
avg_scores_gen1 = calculate_avg_scores([scores_gen1_ref1, scores_gen1_ref2])
avg_scores_gen2 = calculate_avg_scores([scores_gen2_ref1, scores_gen2_ref2])

# 각 생성된 요약에 대한 평균 ROUGE 점수 출력
print("\nAverage ROUGE scores for Mistral 7B Instruct v0.2:", avg_scores_gen1)
print("Average ROUGE scores for Gemma 7B Instruct:", avg_scores_gen2)