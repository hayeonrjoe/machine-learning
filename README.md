<h1>🤖 머신러닝 학습</h1>
개인 학습을 위한 머신러닝 알고리즘 및 실험 저장소<br/><br/>

<h2>🖥️ 머신러닝 알고리즘 연습</h2>
<ol>
  <li>선형회귀 (Linear Regression)</li>
  <details>
  <summary>모의 데이터를 활용한 선형 회귀 분석</summary>
    <p>
      캐시 크기 (Cache Size)와 히트 비율 (Hit Rate) 간의 관계를 탐색하기 위한 선형 회귀 분석을 수행합니다.
      분석 결과인 계수, 평균 제곱 오차 및 R-제곱 값들이 제시되었습니다. 
      또한 실제 데이터, 선형 회귀선, 잔차 및 예측 지점을 시각적으로 나타내기 위해 자세한 플롯이 작성되었습니다.
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
      Kaggle에서 다운로드한 웹사이트 카테고리 분류 데이터를 기반으로 한 클러스터링 분석을 수행합니다. 
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
</ol>
