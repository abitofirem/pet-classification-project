# Pet Classification Project

Bu proje, Oxford-IIIT Pet veri seti üzerinde evcil hayvan türlerini sınıflandırmak için geliştirilmiş bir derin öğrenme uygulamasıdır. CNN (Convolutional Neural Network) mimarisi kullanılarak 37 farklı kedi ve köpek türünü otomatik olarak tanımlama sistemi oluşturulmuştur.

## 📊 Veri Seti

**Oxford-IIIT Pet Dataset** kullanılmıştır:
- **Toplam görüntü sayısı**: 7,390 adet
- **Sınıf sayısı**: 37 farklı evcil hayvan türü
- **Kedi türleri**: 25 farklı kedi ırkı
- **Köpek türleri**: 12 farklı köpek ırkı
- **Görüntü boyutu**: 128x128 piksel (normalize edilmiş)
- **Veri dağılımı**: Her sınıf için yaklaşık 200 örnek

## 🛠️ Kullanılan Teknolojiler

- **Python 3.x**
- **TensorFlow/Keras**: Derin öğrenme modeli geliştirme
- **NumPy & Pandas**: Veri işleme
- **Matplotlib & Seaborn**: Görselleştirme
- **Scikit-learn**: Model değerlendirme
- **PIL (Pillow)**: Görüntü işleme

## 🏗️ Model Mimarisi

### CNN Modeli
- **Giriş katmanı**: 128x128x3 RGB görüntüler
- **Konvolüsyon blokları**: 3 ana blok (32, 64, 128 filtre)
- **Batch Normalization**: Her konvolüsyon katmanından sonra
- **MaxPooling**: Boyut azaltma için
- **Dropout**: Overfitting önleme (0.25, 0.30, 0.40)
- **Dense katmanlar**: 256 nöron + 37 sınıf çıkışı
- **Aktivasyon**: ReLU (gizli katmanlar), Softmax (çıkış)

### Veri Artırma (Data Augmentation)
- **Döndürme**: ±15 derece
- **Kaydırma**: Genişlik/yükseklik %10
- **Yatay çevirme**: Rastgele
- **Yakınlaştırma**: %10 oranında

## 📈 Sonuçlar ve Metrikler

### Model Performansı
- **Test Doğruluğu**: %12.39
- **Validation Doğruluğu**: ~%16
- **Test Kaybı**: 3.58
- **Eğitim süresi**: ~40 epoch (Early Stopping ile)

### Optimizer Karşılaştırması
| Optimizer | Train Accuracy | Val Accuracy | Öğrenme Hızı |
|-----------|----------------|--------------|--------------|
| **Adam** | %19.5 | %4.7 | Hızlı |
| **RMSprop** | %15.2 | %3.2 | Orta |
| **SGD+Momentum** | %12.8 | %2.9 | Yavaş |

### Sınıf Bazlı Performans
- **En iyi performans**: Sınıf 22 (%44 recall)
- **En düşük performans**: Çoğu sınıf %0-5 arası
- **Ortalama F1-Score**: 0.15

## 🔍 Analiz ve Yorumlar

### Güçlü Yönler
- ✅ Başarılı CNN mimarisi uygulaması
- ✅ Kapsamlı veri ön işleme
- ✅ Data augmentation ile overfitting azaltma
- ✅ Farklı optimizer denemeleri
- ✅ Detaylı model değerlendirme

### Geliştirme Alanları
- ❌ Düşük genel doğruluk oranı
- ❌ Sınıf dengesizliği sorunları
- ❌ Transfer learning kullanılmadı
- ❌ Daha büyük görüntü boyutları denenmedi

### Önerilen İyileştirmeler
1. **Transfer Learning**: VGG16, ResNet50, EfficientNet kullanımı
2. **Class Balancing**: SMOTE, weighted loss functions
3. **Daha büyük görüntü boyutları**: 224x224, 299x299
4. **Ensemble Methods**: Birden fazla model kombinasyonu
5. **Hyperparameter Tuning**: Grid search, random search

## 🚀 Kullanım

### Kurulum
```bash
pip install -r requirements.txt
streamlit run UI/app.py
```

## 📁 Proje Yapısı

```
pet-classification-project/
├── README.md
├── requirements.txt
├── supervised/
│   └── pet_classification_cnn.ipynb
├── UI/
│   └── app.py
└── models/
    └── (model files)
```

## 🔗 Kaggle Linkleri

- [Pet Classification CNN Model](https://www.kaggle.com/code/remyaln/pet-classification-project)
- [Oxford-IIIT Pet Dataset](https://www.kaggle.com/datasets/devdgohil/the-oxfordiiit-pet-dataset)

## 🎯 Gelecek Çalışmalar

### Kısa Vadeli Hedefler
- Transfer learning ile model performansını %60+ seviyesine çıkarma
- Real-time prediction API geliştirme
- Mobile app entegrasyonu

### Uzun Vadeli Hedefler
- Gerçek zamanlı video analizi
- Multi-species detection
- Pet health monitoring sistemi
- IoT sensör entegrasyonu

### Teknik Geliştirmeler
- **MLOps Pipeline**: CI/CD, model versioning
- **Cloud Deployment**: AWS, GCP, Azure
- **Edge Computing**: Raspberry Pi, Jetson Nano
- **Advanced Architectures**: Vision Transformers, YOLO

## 👨‍💻 Geliştirici

Bu proje, Global AI Hub bootcamp kapsamında geliştirilmiştir.

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir. Oxford-IIIT Pet Dataset kendi lisansına tabidir.