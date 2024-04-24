<h1>🤖 머신러닝 학습</h1>
개인 학습을 위한 머신러닝 알고리즘 및 실험 저장소<br/><br/>

<h2>🖥️ 머신러닝 알고리즘 연습</h2>
<ol>
  <li>선형회귀 (Linear Regression)</li>
  <details>
  <summary>캐시 크기와 히트 비율 간의 관계를 탐색하는 선형 회귀 분석</summary>
    <p>
      합성된 데이터셋을 사용하여 캐시 크기와 히트 비율 간의 관계를 선형 회귀 분석으로 탐색합니다. 
      다양한 캐시 크기에 대한 히트 비율을 기록하고, 이를 바탕으로 선형 회귀 모델을 구축하였습니다. 
      분석 결과, 계수, 평균 제곱 오차, R-제곱 값들이 제시되었으며, 실제 데이터와 함께 선형 회귀선, 잔차, 예측 지점이 시각적으로 표현되었습니다. 
      합성 데이터셋을 사용한 이 실험은 캐시 크기와 히트 비율 간의 관계를 이해하는 데 도움을 주며, 모델의 성능과 예측 정확도를 평가하는 데 기여합니다.
    </p>
  </details>
  <li>의사결정 트리 (Decision Tree)</li>
  <details>
  <summary>의사결정 트리를 활용한 웹사이트 분류</summary>
    <p>
      Hetul Mehta의 Kaggle 데이터셋 "Website Classification"을 기반으로 한 웹사이트 분류를 수행합니다. 
      데이터를 훈련 및 테스트 세트로 나누고 TF-IDF 벡터화한 후 의사결정 트리 모델을 학습합니다. 
      모델의 정확도를 평가하고, 분류 보고서 및 혼동 행렬을 출력하여 결과를 상세하게 제시합니다. 
      생성된 의사결정 트리 그래픽은 모델의 결정 과정을 시각적으로 나타냅니다.
    </p>
  </details>
  <li>클러스터링 (Clustering)</li>
  <details>
  <summary>텍스트 데이터를 활용한 클러스터링 분석</summary>
    <p>
      Kaggle에서 다운로드한 'IAB 텍스트/웹사이트 분류' 데이터셋을 기반으로 한 클러스터링 분석입니다.
      데이터를 전처리하고 TF-IDF 벡터화한 후, KMeans 클러스터링을 적용하여 웹사이트를 그룹화합니다. 
      Elbow Method 및 Silhouette Score를 사용하여 최적의 클러스터 수를 찾고, 최적 클러스터 수로 모델을 학습합니다. 
      t-SNE를 활용하여 클러스터 결과를 2D로 시각화하고, 각 클러스터의 특징을 요약하여 CSV 파일로 출력합니다. 
      또한, 무작위 샘플링 및 클러스터링된 데이터를 CSV 파일로 내보내어 결과를 확인합니다.
    </p>
  </details>
  <li>서포트 벡터 머신 (SVM, Support Vector Machine)</li>
  <details>
  <summary>웹사이트 분류를 위한 서포트 벡터 머신 (SVM)</summary>
    <p>
      Hetul Mehta의 Kaggle에서 가져온 "웹사이트 분류" 데이터셋을 활용하여 웹사이트 분류를 위해 서포트 벡터 머신 (SVM)을 사용합니다. 
      데이터를 읽고 전처리하며, TF-IDF 벡터화를 수행하고, 선형 커널을 사용한 SVM 분류기를 훈련합니다. 
      모델의 정확도를 평가하고, 분류 보고서 및 혼동 행렬이 제시됩니다. 
      또한, 스크립트는 t-SNE를 사용하여 SVM의 결정 경계를 시각화하여 분류기의 행동을 파악합니다.
    </p>
  </details>
  <li>베이지안 네트워크 (Bayesian Network)</li>
  <details>
  <summary>베이지안 네트워크를 사용한 웹사이트 카테고리 분류</summary>
    <p>
      Hetul Mehta의 Kaggle에서 수집한 "웹사이트 분류" 데이터셋을 기반으로 한 베이지안 네트워크 모델을 구축하여 웹사이트의 특징과 카테고리 간의 관계를 모델링합니다. 
      데이터를 불러오고 전처리한 후, 언어 감지를 통해 영어 단어를 추출하여 베이지안 네트워크의 학습 데이터로 활용합니다. 
      모델 학습 이후, 조건부 확률을 계산하고 시각적으로 나타내기 위해 네트워크 그래프를 생성합니다. 
      생성된 그래프는 'Streaming Services' 및 'Other Categories'에 대한 조건부 확률을 시각적으로 표현하여 웹사이트의 특정 키워드가 특정 카테고리에 속할 확률을 제시합니다.
    </p>
  </details>
  <li>로지스틱 회귀 (Logistic Regression)</li>
  <details>
  <summary>웹사이트 카테고리 분류를 위한 로지스틱 회귀 모델링</summary>
    <p>
      Hetul Mehta의 Kaggle에서 수집한 "웹사이트 분류" 데이터셋을 활용하여 로지스틱 회귀 모델을 훈련하고 웹사이트의 특징을 기반으로 'Streaming Services'와 'Other Categories'를 분류합니다. 
      데이터를 불러오고 전처리한 후, TF-IDF 벡터화를 통해 텍스트 데이터를 수치형으로 변환합니다. 
      훈련된 로지스틱 회귀 모델을 평가하고, 정확도, 분류 보고서, 혼동 행렬을 출력합니다. 
      또한, 의사결정 트리와 서포트 벡터 머신 테스트 결과와 비교하여 이 실험의 결과를 종합적으로 고려했습니다.
    </p>
  </details>
  <li>LSTM 기반 신경망 (LSTM Neural Network, Long Short-Term Memory Recurrent Neural Network)</li>
  <details>
  <summary>웹사이트 카테고리 분류를 위한 LSTM 기반 신경망 모델</summary>
    <p>
      Hetul Mehta의 Kaggle에서 수집한 "웹사이트 분류" 데이터셋을 기반으로 한 웹사이트 카테고리 분류를 위한 LSTM 기반 신경망 모델을 구축하였습니다. 
      데이터는 GloVe 워드 임베딩을 활용하여 토큰화되었고, 훈련 및 테스트를 위해 적절히 전처리되었습니다. 
      모델은 LSTM (Long Short-Term Memory) 레이어를 통과한 후 시그모이드 활성화 함수를 사용하는 Dense 레이어로 구성되었습니다. 
      훈련 결과를 시각적으로 나타낸 그래프와 테스트 데이터에 대한 정확도와 손실값이 제시되었습니다. 
      또한 이진 분류의 평가 지표로는 혼동 행렬과 ROC 커브를 활용하여 성능을 평가하였습니다.
    </p>
  </details>
  <li>CNN (Convolutional Neural Network)</li>
  <details>
  <summary>I3D (Inflated 3D CNN) 모델을 활용한 동작 인식</summary>
    <p>
      Kaggle 노트북 'Action Recognition with i3d-kinetics (400)'을 기반으로 한 I3D 모델을 활용한 동작 인식 실험입니다. 
      I3D 모델은 2D 이미지 분류 DNN을 기반으로 하는 공간-시간 아키텍처이며, RGB 프레임과 연속 RGB 프레임 사이의 광학 흐름 예측을 처리하는 두 개의 3D CNN을 결합합니다.
      이 모델은 사전 훈련된 Kinetics 데이터셋을 기반으로 하며, 실험에서는 해당 데이터셋의 동작 레이블을 활용하여 선택된 동영상에 대한 상위 5가지 동작을 예측하는 테스트를 수행했습니다. 
      실험에는 UCF101 데이터셋에서 선택한 비디오와 YouTube에서 가져온 '피아노 연주'와 '타이핑' 동영상이 포함되었습니다. 
      또한 결과를 평가하기 위해 Kinetics-400 데이터셋의 동작 레이블을 활용하여 모델의 예측 정확도를 확인하였습니다. 
      이를 통해 I3D 모델이 다양한 데이터에서 상위 동작을 어떻게 예측하는지를 시각적으로 확인할 수 있었습니다.
    </p>
  </details>
  <li>트랜스포머 (Transformer)</li>
  <details>
  <summary>DistilBERT을 활용한 종양 분류</summary>
    <p>
      Kaggle의 'Medical Text Dataset - Cancer Doc Classification'을 기반으로 한 DistilBERT 모델을 사용한 종양 분류 실험입니다. 
      DistilBERT은 BERT base 모델의 간추려진 버전으로, 작고 빠르며 가벼운 트랜스포머 모델입니다.
      실험에서는 DistilBERT를 사용하여 각 텍스트 데이터의 토큰화 및 분류를 수행하였습니다. 
      주어진 데이터셋은 'Thyroid_Cancer', 'Colon_Cancer', 'Lung_Cancer'과 같은 3가지 범주로 분류될 수 있는 암 관련 생물 의학 텍스트 문서를 포함하고 있습니다. 
      실험에서는 2개의 에포크로 축소하여 진행되었습니다. Google Colab의 제한으로 인해 3개의 에포크로 훈련하는 데 시간이 오래 걸렸습니다. 
      훈련 및 검증 데이터셋으로 나눈 후, DistilBERT 모델을 학습시키고 평가하여 정확도를 확인하였습니다. 
      실험 결과는 혼동 행렬과 분류 보고서를 통해 모델의 성능을 평가하고 있습니다.
    </p>
  </details>
    <li>앙상블 기법 (Ensemble Method)</li>
  <details>
  <summary>XGBoost 앙상블 모델을 활용한 미생물 서식지 예측</summary>
    <p>
      Kaggle의 'Human Microbiome Project' 데이터셋을 사용하여 인체 부위에서 분리된 미생물의 서식지를 분류하는 다중 클래스 분류 실험입니다. 
      데이터셋은 탐색 및 전처리 과정을 통해 결측값 제거, 원핫 인코딩 및 범주형 열과 수치형 열 분리를 수행하였습니다. 
      분류기로는 XGBoost를 사용하였으며, 개별 모델 및 앙상블 모델을 훈련하였습니다.
      각 모델에 대한 정확도, 분류 보고서, 혼동 행렬 및 ROC Curve를 통해 성능을 평가하였습니다. 
      실험 결과, 개별 모델과 앙상블 모델 모두 정확도 55.40%의 동일한 성능을 보였으며, 앙상블 모델이 개별 모델보다 더 나은 정확도와 ROC AUC를 보이지 않았습니다. 
      따라서, 앙상블 모델이 개별 모델보다 유의미한 성능 향상을 제공하지 않았다고 할 수 있으며, 다양한 인체 부위에서 분리된 미생물의 서식지를 정확하게 예측하는 것이 어려울 수 있다는 것을 알 수 있습니다.
    </p>
  </details>
      <li>강화 학습 (Reinforcement Learning)</li>
  <details>
  <summary>Q-러닝을 이용한 환자 특징 기반 치료 옵션 결정</summary>
    <p>
      Q-러닝 알고리즘을 적용하여 합성 의료 데이터셋에서 나이, 혈압, 콜레스테롤, BMI, 흡연 여부, 당뇨 등과 같은 일반적인 환자 특징을 기반으로 한 치료 옵션에 대한 결정을 내리는 것을 탐구합니다. 
      합성 데이터셋은 무작위로 생성되었으며, 나이, 혈압, 콜레스테롤, BMI, 흡연 상태, 그리고 당뇨와 같은 특징을 가진 가상의 환자 정보를 포함합니다. 
      실험 결과, 모델은 초기에는 보상의 큰 변동성을 보였지만, 에피소드 100 이후에는 안정적으로 수렴하며 평균 보상은 약간 감소하였습니다. 
      이러한 결과는 Q-러닝이 의료 데이터셋에서 학습 가능하며 시간이 지남에 따라 안정적인 성과를 보일 수 있음을 시사하나, 모델의 성능은 특정 환자 집단과 데이터셋의 크기 및 품질과 같은 추가 요인의 영향을 받을 수 있습니다.
    </p>
  </details>
        <li>자연어 처리 (Natural Language Processing, NLP)</li>
  <details>
  <summary>Word2Vec을 활용한 방사선학과 병리학에서의 의미 유사성 추출 및 어휘 유추</summary>
    <p>
      방사선학과 병리학의 텍스트 데이터에서 Word2Vec 임베딩을 활용하여 두 도메인 간의 용어와 개념 간의 유사성을 파악했습니다.
      텍스트 PDF에서 문장을 추출하고 전처리하여 Word2Vec 모델을 훈련하고 각 도메인에서 가장 일반적으로 사용되는 용어를 식별했습니다.
      두 도메인 간 용어의 코사인 유사성을 계산하고, 용어 유추 작업을 수행하여 모델이 다른 용어 간의 관련성을 추론할 수 있는지 평가했습니다.
      방사선학과 병리학에서 동일한 용어의 Word2Vec 임베딩 사이의 코사인 유사도가 낮은 것은 이러한 용어가 각 도메인에서 의미와 용법이 다름을 의미합니다.
      용어 유추 작업 결과, 방사선학, 인공지능 및 병리학 용어 간의 관계에서는 방사선학 및 병리학 도메인 내에서 특정한 의미적 유사성 정도가 있습니다.
    </p>
  </details>
          <li>감정 분석 (Sentiment Analysis)</li>
  <details>
  <summary>BERT를 활용한 의료기관 환자 만족도 데이터셋 감정 분석</summary>
    <p>
      Kaggle의 'Healthcare Patient Satisfaction - Data Collection' 데이터셋을 활용하여 BERT 사전 훈련 언어 모델을 사용한 감정 분석을 수행했습니다. 
      환자가 병원에 대한 경험을 설명하는 텍스트 데이터를 토큰화하고 긍정적, 부정적, 그리고 정의되지 않음의 세 가지 클래스로 분류했습니다. 
      500개의 텍스트를 무작위로 추출하였고, 각 텍스트의 최대 길이는 512로 제한했습니다. 
      감정은 긍정적인 경우 1, 부정적인 경우 0, 정의되지 않은 경우 -1로 레이블링되었습니다. 
      모델은 67.11%의 정확도로 데이터셋을 분류했지만, 정밀도가 낮고 FP가 존재하여 모델을 개선하는 여지가 있을 것으로 나타났습니다. 
      이러한 결과는 의료 분야에서 BERT 모델을 감정 분석에 더욱 효과적으로 적용하기 위해 정밀도를 높이고 혼동 행렬의 균형을 맞추는 방향으로 조정하는 것이 필요함을 시사하고 있습니다.
    </p>
  </details>
          <li>텍스트 요약 (Summarization)</li>
  <details>
  <summary>BART, T5 및 Pegasus 트랜스포머 모델 간 텍스트 요약 성능 비교</summary>
    <p>
      BillSum 데이터셋을 활용하여 BART Fine-Tuned, T5 Fine-Tuned, 그리고 Pegasus와 같은 트랜스포머 모델들의 텍스트 요약 성능을 측정하였습니다.
      데이터셋은 미국 의회 및 캘리포니아 주 법안의 요약을 담고 있으며, 캘리포니아 주 법안의 1237개 데이터만 사용하였습니다.
      각 모델의 생성된 요약과 실제 요약 사이의 유사성을 평가하기 위해 ROUGE(Recall-Oriented Understudy for Gisting Evaluation) 점수를 계산하였습니다.
      각 데이터의 ROUGE-1, ROUGE-2, ROUGE-L F1 점수를 측정하고 이를 평균하여 각 모델의 ROUGE-1, ROUGE-2, ROUGE-L F1 점수를 계산합니다.
      T5 Fine-Tuned가 세 모델 중에서 가장 우수한 성능을 보였으며, ROUGE-1 평균 F1 점수는 0.1395, ROUGE-2 평균 F1 점수는 0.0590, ROUGE-L 평균 F1 점수는 0.1042입니다.
      이는 T5가 세 모델 중에서 가장 작은 파라미터를 가지고 있음에도 불구하고, 다양한 문서 뿐만 아니라 해당 문서의 인간이 생성한 요약에 대해 미세 조정되었기 때문으로 생각됩니다.
    </p>
  </details>
            <li>추출 요약 (Extractive Summarization)</li>
  <details>
  <summary>LM Studio를 활용한 Mistral 7B Instruct 및 Gemma 7B Instruct LLM 추출 요약</summary>
    <p>
      LM Studio를 활용하여 Mistral 7B Instruct v0.2 및 Gemma 7B Instruct LLM에게 <em>Biomarkers for immunotherapy of hepatocellular carcinoma</em> 논문 초록의 요약을 생성하도록 설정했습니다. 
      의료 분야에서는 생성 요약보다는 추출 요약이 더 적합하다는 판단하에, <em>Extractive Summarization via ChatGPT for Faithful Summary Generation</em> 논문의 프롬프트를 활용했습니다.
      비록 정답 요약이 없었지만, 논문 초록과 품질이 양호한 ChatGPT 생성 요약을 정답으로 삼아 추출된 단어의 관련성을 평가했습니다.
      각 요약에 대해 ROUGE-1, ROUGE-2, ROUGE-L를 평균화하여 성능을 평가한 결과, Mistral 7B Instruct가 더 우수한 성능을 보였습니다.
    </p>
  </details>
</ol>
