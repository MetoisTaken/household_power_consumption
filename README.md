# Enerji Tüketimi Sınıflandırma Uygulaması

Bu proje, ev içi elektriksel özelliklere dayalı olarak enerji tüketim düzeyini (yüksek / düşük) sınıflandırmak amacıyla geliştirilmiş bir makine öğrenmesi uygulamasıdır. Streamlit arayüzü üzerinden kullanıcıdan alınan giriş verileri, seçilen model ve özellik seçiciye göre işlenerek sınıflandırma yapılır.

## Proje Yapısı

- `app.py` : Streamlit tabanlı kullanıcı arayüzü.
- `requirements.txt` : Gerekli Python kütüphaneleri.
- `030122029_Metehan_BEYAZ_Proje.ipynb` : Model eğitimi, özellik seçimi ve değerlendirmelerin yapıldığı Jupyter notebook.
- `pkl_models/` : Eğitilmiş modeller ve özellik seçicilerin kayıtlı olduğu dizin.
    - Örnek model dosyaları: `KNN_PCA.pkl`, `MLP_LDA.pkl`, `SelectKBest_selector.pkl` vb.

## Özellikler

- Kullanıcıdan alınan 7 giriş parametresi ile çalışır:
  - Global_active_power
  - Global_reactive_power
  - Voltage
  - Global_intensity
  - Sub_metering_1
  - Sub_metering_2
  - Sub_metering_3
- Desteklenen makine öğrenmesi modelleri:
  - K-Nearest Neighbors (KNN)
  - Naive Bayes
  - Multi-layer Perceptron (MLP)
  - XGBoost
- Desteklenen özellik seçiciler:
  - Principal Component Analysis (PCA)
  - SelectKBest
  - Linear Discriminant Analysis (LDA)

## Kullanılan Kütüphaneler

Aşağıdaki temel Python kütüphaneleri kullanılmaktadır:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- xgboost
- streamlit
- joblib

## Model Eğitimi ve Değerlendirme

Model eğitimi ve analiz işlemleri `030122029_Metehan_BEYAZ_Proje.ipynb` dosyasında yürütülmüştür. Bu dosyada;

- Verilerin temizlenmesi ve normalize edilmesi,
- Özellik seçimi yöntemlerinin uygulanması (PCA, SelectKBest, LDA),
- Farklı modellerle sınıflandırma performanslarının karşılaştırılması,
- En iyi sonuç veren modellerin `.pkl` formatında dışa aktarılması işlemleri gerçekleştirilmiştir.

## Uyarılar

- `pkl_models/` klasörünün içeriği eksikse uygulama tahmin aşamasında hata verebilir.
- Uygulama demo amaçlı geliştirilmiştir. Gerçek zamanlı üretim ortamlarında güvenlik ve veri bütünlüğü testleri gereklidir.
- `StandardScaler` nesnesi sadece giriş ölçekleme amacıyla örneklem üzerinden yeniden hesaplanmaktadır. Gerçek senaryolarda eğitilmiş `scaler` nesnesinin de ayrı olarak kaydedilmesi önerilir.

## Uygulamayı Deneyin

Canlı demo için aşağıdaki bağlantıyı kullanabilirsiniz:

[Uygulamayı Açın](https://householdpowerconsumption.streamlit.app/)
