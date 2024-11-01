import streamlit as st
import json

# Sayfa yapılandırması (yorum satırı) / Page configuration (commented out)
# st.set_page_config(page_title="Streamlit 101", page_icon=":flag-yt:")

# Metin gösterme örnekleri (yorum satırı) / Text display examples (commented out)
# st.write("En yaygın metin gösterme")
# st.markdown("_biçimlendirikmiş metin_")
# st.header("Header örneği")
# st.subheader("subheader örneği")
# st.code("for i in range(10): foo(i)")
# st.latex(r'''e^{i\pi} + 1 = 0''')

# Multimedya gösterimi örnekleri (yorum satırı) / Multimedia display examples (commented out)
# st.image(image="IMG_7688.JPG")
# st.video(data="IMG_7673.MOV")
# st.audio(data="fifa99-1.mp3")

# Kullanıcı girişi örnekleri (yorum satırı) / User input examples (commented out)
# st.write("Lütfen bilgileriniz girin:")
# st.text_input(label="Eposta gir")
# st.text_input(label="şifre girin", type="password")
# st.checkbox(label="şifremi unuttum")
# st.divider()
# st.number_input("Yaşınızı gir", min_value=18, max_value=44, value=20)
# st.slider("Yaşınızı gir", min_value=18, max_value=44, value=20)
# st.divider()
# st.radio(label="statünüz", options=["öğrenci", "çalışan"])
# st.button(label="giriş")
# st.divider()
# st.file_uploader(label="dosya yükleme")

# İki sütunlu düzen örneği (yorum satırı) / Two-column layout example (commented out)
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("<h3><b> kullanıcı bilgileri </b></h3>", unsafe_allow_html=True)
#     st.text_input(label="Eposta gir")
#     st.text_input(label="şifre girin", type="password")
#     st.checkbox(label="şifremi unuttum")
#     st.divider()
#     st.button(label="giriş")
# with col2:
#     st.markdown("<h3><b> kullanım tercihleri </b></h3>", unsafe_allow_html=True)
#     st.divider()
#     st.radio(label="Hesap türü", options=["öğrenci", "çalışan"])
#     st.slider(label="zaman aşım süresi (sn)", min_value=3, max_value=30, value=5)
#     st.file_uploader(label="CV yükle")

# Aktif kod başlangıcı / Start of active code
# Sidebar oluşturma / Create sidebar
st.sidebar.markdown("<h4> hoşgeldiniz </h4>", unsafe_allow_html=True)
st.sidebar.image(image="IMG_7688.JPG")

# Sekmeleri oluşturma / Create tabs
tab1, tab2 = st.tabs(["kullanıcı bilgileri", "kullanım tercihleri"])

# Kullanıcı bilgileri sekmesi / User information tab
with tab1:
    # Kullanıcı giriş alanları / User input fields
    eposta = st.text_input(label="Eposta gir")  # Email input
    sifre = st.text_input(label="şifre girin", type="password")  # Password input
    st.checkbox(label="şifremi unuttum")  # Forgot password checkbox
    st.divider()
    kaydet_btn = st.button(label="kaydet")  # Save button

# Kullanım tercihleri sekmesi / Usage preferences tab
with tab2:
    # Kullanıcı tercihleri / User preferences
    hesap_turu = st.radio(label="Hesap türü", options=["öğrenci", "çalışan"])  # Account type
    st.slider(label="zaman aşım süresi (sn)", min_value=3, max_value=30, value=5)  # Timeout duration
    st.file_uploader(label="CV yükle")  # CV upload

# Kaydetme işlemi / Save process
if kaydet_btn:
    data = []
    data.append({"eposta": eposta})
    data.append({"sifre": sifre})

    # Hesap türüne göre geçerlilik süresi belirleme / Set validity period based on account type
    if hesap_turu == "öğrenci":
        gecerlilik = 365
    elif hesap_turu == "çalışan":
        gecerlilik = 120

    data.append({"Geçerlilik Süresi:": gecerlilik})

    # Kullanıcı bilgilerini dosyaya kaydetme / Save user information to file
    with open("kullanıcı.txt", "w") as file:
        file.write(json.dumps(data))

    # Başarılı kayıt bildirimi / Successful save notification
    st.balloons()
    st.success("dosyanız kaydedildi")
    st.write(f"Geçerlilik süreniz: {gecerlilik}")