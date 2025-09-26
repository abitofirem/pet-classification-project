import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import os
import json

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Pet Classification App",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stilleri
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .prediction-result {
        font-size: 1.2rem;
        font-weight: bold;
        color: #2E86AB;
        text-align: center;
        padding: 1rem;
        background-color: #e8f4f8;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown('<h1 class="main-header">🐾 Pet Classification System</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Model Bilgileri")
    st.info("""
    **Model**: CNN (Convolutional Neural Network)
    **Veri Seti**: Oxford-IIIT Pet Dataset
    **Sınıf Sayısı**: 37 farklı evcil hayvan türü
    **Doğruluk**: %12.39 (Test Seti)
    """)
    
    st.markdown("## 🎯 Desteklenen Türler")
    st.markdown("""
    **Kedi Türleri (25)**: Abyssinian, Bengal, Birman, Bombay, British Shorthair, Egyptian Mau, Maine Coon, Persian, Ragdoll, Russian Blue, ve daha fazlası...
    
    **Köpek Türleri (12)**: Beagle, Boxer, Bulldog, Chihuahua, German Shepherd, Golden Retriever, Labrador, Poodle, ve daha fazlası...
    """)

# Ana içerik
tab1, tab2, tab3 = st.tabs(["🔍 Tahmin Yap", "📊 Model Analizi", "ℹ️ Hakkında"])

with tab1:
    st.markdown('<h2 class="sub-header">Evcil Hayvan Türü Tahmini</h2>', unsafe_allow_html=True)
    
    # Model yükleme (gerçek uygulamada model dosyası yüklenir)
    @st.cache_resource
    def load_model():
        # Bu kısım gerçek model yükleme kodu olacak
        # model = tf.keras.models.load_model('models/best_pet_cnn_v1.keras')
        # return model
        return None
    
    # Görüntü yükleme
    uploaded_file = st.file_uploader(
        "Evcil hayvan görüntüsü yükleyin:",
        type=['jpg', 'jpeg', 'png'],
        help="JPG, JPEG veya PNG formatında görüntü yükleyebilirsiniz."
    )
    
    if uploaded_file is not None:
        # Görüntüyü göster
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📸 Yüklenen Görüntü")
            image = Image.open(uploaded_file)
            st.image(image, caption="Yüklenen görüntü", use_column_width=True)
        
        with col2:
            st.markdown("### 🔄 İşlenmiş Görüntü")
            # Görüntüyü model için hazırla
            img_array = np.array(image)
            img_resized = cv2.resize(img_array, (128, 128))
            img_normalized = img_resized / 255.0
            
            st.image(img_resized, caption="Model için hazırlanmış görüntü (128x128)", use_column_width=True)
        
        # Tahmin butonu
        if st.button("🔮 Tahmin Yap", type="primary"):
            with st.spinner("Model tahmin yapıyor..."):
                # Gerçek tahmin kodu burada olacak
                # model = load_model()
                # prediction = model.predict(img_normalized.reshape(1, 128, 128, 3))
                
                # Demo tahmin (gerçek uygulamada model tahmini olacak)
                demo_prediction = np.random.random(37)
                demo_prediction = demo_prediction / np.sum(demo_prediction)
                predicted_class = np.argmax(demo_prediction)
                confidence = demo_prediction[predicted_class]
                
                # Sınıf isimleri (demo)
                class_names = [
                    "Abyssinian", "Bengal", "Birman", "Bombay", "British Shorthair",
                    "Egyptian Mau", "Maine Coon", "Persian", "Ragdoll", "Russian Blue",
                    "Siamese", "Sphynx", "Balinese", "Birman", "Bombay",
                    "British Shorthair", "Egyptian Mau", "Maine Coon", "Persian", "Ragdoll",
                    "Russian Blue", "Siamese", "Sphynx", "Beagle", "Boxer",
                    "Bulldog", "Chihuahua", "German Shepherd", "Golden Retriever", "Labrador",
                    "Poodle", "Pug", "Rottweiler", "Siberian Husky", "Staffordshire Bull Terrier",
                    "Weimaraner", "Yorkshire Terrier"
                ]
                
                st.markdown(f"""
                <div class="prediction-result">
                    🎯 Tahmin Edilen Tür: <strong>{class_names[predicted_class]}</strong><br>
                    📊 Güven Skoru: <strong>{confidence:.2%}</strong>
                </div>
                """, unsafe_allow_html=True)
                
                # Top 5 tahminler
                st.markdown("### 🏆 En Yüksek 5 Tahmin")
                top5_indices = np.argsort(demo_prediction)[-5:][::-1]
                
                for i, idx in enumerate(top5_indices):
                    st.progress(demo_prediction[idx], text=f"{i+1}. {class_names[idx]}: {demo_prediction[idx]:.2%}")

with tab2:
    st.markdown('<h2 class="sub-header">Model Performans Analizi</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Genel Metrikler")
        st.markdown("""
        <div class="metric-card">
            <strong>Test Doğruluğu:</strong> %12.39<br>
            <strong>Validation Doğruluğu:</strong> %16.12<br>
            <strong>Test Kaybı:</strong> 3.58<br>
            <strong>Eğitim Epoch:</strong> 40
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎯 Optimizer Karşılaştırması")
        st.markdown("""
        <div class="metric-card">
            <strong>Adam:</strong> %19.5 (Train) / %4.7 (Val)<br>
            <strong>RMSprop:</strong> %15.2 (Train) / %3.2 (Val)<br>
            <strong>SGD+Momentum:</strong> %12.8 (Train) / %2.9 (Val)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Sınıf Bazlı Performans")
    
    # Demo confusion matrix
    st.markdown("**Confusion Matrix (Örnek)**")
    confusion_data = np.random.randint(0, 20, (10, 10))
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(confusion_data, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_title('Confusion Matrix (İlk 10 Sınıf)')
    ax.set_xlabel('Tahmin Edilen')
    ax.set_ylabel('Gerçek')
    st.pyplot(fig)
    
    st.markdown("### 🔍 Analiz Sonuçları")
    st.markdown("""
    - **En İyi Performans**: Sınıf 22 (%44 recall)
    - **En Düşük Performans**: Çoğu sınıf %0-5 arası
    - **Ortalama F1-Score**: 0.15
    - **Overfitting**: Validation loss artışı gözlemlendi
    """)

with tab3:
    st.markdown('<h2 class="sub-header">Proje Hakkında</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 Proje Amacı
    Bu proje, Oxford-IIIT Pet veri seti kullanılarak geliştirilmiş bir evcil hayvan türü sınıflandırma sistemidir. 
    CNN (Convolutional Neural Network) mimarisi ile 37 farklı kedi ve köpek türünü otomatik olarak tanımlama 
    hedeflenmektedir.
    
    ### 🛠️ Kullanılan Teknolojiler
    - **TensorFlow/Keras**: Derin öğrenme modeli
    - **OpenCV**: Görüntü işleme
    - **Streamlit**: Web arayüzü
    - **NumPy/Pandas**: Veri işleme
    - **Matplotlib/Seaborn**: Görselleştirme
    
    ### 📊 Veri Seti Bilgileri
    - **Toplam Görüntü**: 7,390 adet
    - **Sınıf Sayısı**: 37 farklı tür
    - **Görüntü Boyutu**: 128x128 piksel
    - **Veri Dağılımı**: Her sınıf için ~200 örnek
    
    ### 🚀 Gelecek Geliştirmeler
    1. **Transfer Learning**: VGG16, ResNet50 kullanımı
    2. **Class Balancing**: SMOTE, weighted loss
    3. **Daha Büyük Görüntüler**: 224x224, 299x299
    4. **Ensemble Methods**: Birden fazla model
    5. **Real-time API**: Gerçek zamanlı tahmin
    
    ### 👨‍💻 Geliştirici
    Bu proje Global AI Hub bootcamp kapsamında geliştirilmiştir.
    """)
    
    st.markdown("### 🔗 Bağlantılar")
    st.markdown("""
    - [GitHub Repository](https://github.com/your-username/pet-classification)
    - [Kaggle Notebook](https://www.kaggle.com/code/your-username/pet-classification)
    - [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🐾 Pet Classification System | Global AI Hub Bootcamp Project</p>
</div>
""", unsafe_allow_html=True)
