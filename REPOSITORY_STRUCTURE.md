# 📁 Pet Classification Repository Structure

Bu dosya, oluşturulan repository yapısını ve her dosyanın amacını açıklar.

## 🗂️ Repository Yapısı

```
pet-classification-project/
├── 📄 README.md                           # Ana proje dokümantasyonu
├── 📄 requirements.txt                   # Python bağımlılıkları
├── 📄 DEPLOYMENT.md                      # Deployment rehberi
├── 📄 REPOSITORY_STRUCTURE.md            # Bu dosya
├── 📁 supervised/                        # Supervised learning notebookları
│   └── 📓 pet_classification_cnn.ipynb   # Ana CNN modeli notebook'u
├── 📁 UI/                                # Web arayüzü
│   └── 🐍 app.py                        # Streamlit web uygulaması
└── 📁 models/                            # Eğitilmiş modeller
    └── 🤖 best_pet_cnn_v1.keras          # En iyi model (gelecekte eklenecek)
```

## 📋 Dosya Açıklamaları

### 📄 README.md
- **Amaç**: Projenin ana dokümantasyonu
- **İçerik**: 
  - Proje tanıtımı
  - Veri seti bilgileri
  - Model mimarisi
  - Sonuçlar ve metrikler
  - Gelecek çalışmalar
- **Hedef Kitle**: Projeyi inceleyen herkes

### 📄 requirements.txt
- **Amaç**: Python bağımlılıklarını yönetme
- **İçerik**: 
  - TensorFlow/Keras
  - Streamlit
  - Görselleştirme kütüphaneleri
  - Veri işleme araçları
- **Kullanım**: `pip install -r requirements.txt`

### 📄 DEPLOYMENT.md
- **Amaç**: Deployment rehberi
- **İçerik**:
  - Lokal deployment
  - Cloud deployment (Heroku, Streamlit Cloud)
  - Docker deployment
  - Mobile deployment
  - Troubleshooting
- **Hedef Kitle**: Geliştiriciler

### 📁 supervised/
- **Amaç**: Supervised learning notebookları
- **İçerik**: Ana CNN modeli geliştirme süreci
- **Notebook İçeriği**:
  - Veri yükleme ve keşif
  - Veri ön işleme
  - CNN modeli geliştirme
  - Model eğitimi
  - Değerlendirme
  - Optimizer karşılaştırması

### 📁 UI/
- **Amaç**: Web arayüzü
- **İçerik**: Streamlit uygulaması
- **Özellikler**:
  - Görüntü yükleme
  - Tahmin yapma
  - Model analizi
  - Proje bilgileri
- **Kullanım**: `streamlit run UI/app.py`

### 📁 models/
- **Amaç**: Eğitilmiş modelleri saklama
- **İçerik**: En iyi model dosyaları
- **Format**: .keras (TensorFlow/Keras)

## 🚀 Hızlı Başlangıç

### 1. Repository'yi Klonlayın
```bash
git clone https://github.com/your-username/pet-classification-project.git
cd pet-classification-project
```

### 2. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 3. Notebook'u Çalıştırın
```bash
jupyter notebook supervised/pet_classification_cnn.ipynb
```

### 4. Web Uygulamasını Başlatın
```bash
streamlit run UI/app.py
```

## 📊 Proje Özellikleri

### ✅ Tamamlanan Özellikler
- [x] Kapsamlı README.md
- [x] Requirements.txt
- [x] Notebook organizasyonu
- [x] Streamlit web arayüzü
- [x] Deployment rehberi
- [x] Proje yapısı dokümantasyonu

### 🔄 Gelecek Geliştirmeler
- [ ] Model dosyası eklenecek
- [ ] Transfer learning notebook'u
- [ ] Unsupervised learning bölümü
- [ ] API geliştirme
- [ ] Mobile app

## 🎯 GitHub'a Yükleme

### 1. Git Repository Oluşturun
```bash
git init
git add .
git commit -m "Initial commit: Pet Classification Project"
```

### 2. GitHub'da Repository Oluşturun
- Repository adı: `pet-classification-project`
- Açıklama: "CNN-based pet classification system using Oxford-IIIT Pet Dataset"
- Public repository olarak ayarlayın

### 3. Remote Repository'yi Bağlayın
```bash
git remote add origin https://github.com/your-username/pet-classification-project.git
git push -u origin main
```

## 📝 Notlar

- Bu repository Global AI Hub bootcamp template'ine uygun olarak oluşturulmuştur
- Tüm dosyalar Türkçe dokümantasyon içerir
- Proje eğitim amaçlı geliştirilmiştir
- Oxford-IIIT Pet Dataset kendi lisansına tabidir

## 🔗 Faydalı Linkler

- [Global AI Hub](https://globalaihub.com/)
- [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
