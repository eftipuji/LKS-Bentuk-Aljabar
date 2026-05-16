Tentu, sebagai ahli pengembangan media pembelajaran matematika, saya akan membantu Anda menyusun kode Python menggunakan **Streamlit** untuk materi **Bentuk Aljabar** kelas 7. 

Kode ini dirancang agar selaras dengan struktur "Jelajah" yang telah Anda buat sebelumnya, dengan mengintegrasikan materi dari buku teks seperti **unsur-unsur aljabar (variabel, koefisien, konstanta)**, **substitusi nilai**, dan **operasi aljabar**.

Berikut adalah kode lengkap yang dapat Anda unggah ke GitHub:

```python
import streamlit as st
import sympy as sp # Library untuk manipulasi aljabar simbolik

### ─────────────────────────────────────────
### KONFIGURASI HALAMAN
### ─────────────────────────────────────────
st.set_page_config(
    page_title="Jelajah Bentuk Aljabar",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

### ─────────────────────────────────────────
### CSS KUSTOM (Selaras dengan seri Jelajah)
### ─────────────────────────────────────────
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stHeader { background-color: #4A90E2; color: white; padding: 20px; border-radius: 10px; }
    .sidebar-title { font-size: 1.5rem; font-weight: bold; color: #1E3A8A; margin-bottom: 1rem; }
    .card { background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

### ─────────────────────────────────────────
### SIDEBAR NAVIGASI
### ─────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Menu Jelajah</div>', unsafe_allow_html=True)
    tab_choice = st.radio(
        "Pilih Tahap Eksplorasi:",
        options=[
            "🏠 Beranda",
            "🔍 KP 1 — Unsur-Unsur Aljabar",
            "🧮 KP 2 — Nilai Bentuk Aljabar",
            "➗ KP 3 — Operasi & Sederhanakan",
            "📝 Latihan Mandiri"
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.info("**Petunjuk:** Gunakan kalkulator ini untuk memverifikasi temuanmu di LKS.")

### ══════════════════════════════════════════
### HALAMAN BERANDA
### ══════════════════════════════════════════
if tab_choice == "🏠 Beranda":
    st.markdown("<div class='stHeader'><h1>🧬 Selamat Datang di Jelajah Bentuk Aljabar!</h1></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div class='card'>
    <h3>Mengapa kita menggunakan huruf dalam matematika?</h3>
    Bentuk aljabar membantu kita menyatakan kuantitas yang berubah-ubah atau tidak diketahui dengan simbol atau <b>variabel</b>. 
    Mari kita jelajahi bagaimana aljabar memudahkan kita memodelkan masalah sehari-hari!
    </div>
    """, unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Al-Khwarizmi_portrait.jpg/220px-Al-Khwarizmi_portrait.jpg", caption="Al-Khawarizmi: Bapak Aljabar")

### ══════════════════════════════════════════
### KP 1 — UNSUR-UNSUR ALJABAR
### ══════════════════════════════════════════
elif tab_choice == "🔍 KP 1 — Unsur-Unsur Aljabar":
    st.header("🔍 Eksplorasi Unsur-Unsur Aljabar")
    st.write("Identifikasi variabel, koefisien, dan konstanta dalam ekspresi aljabar.")
    
    with st.expander("📝 Masukkan Ekspresi Aljabar (Contoh: 3x + 5)"):
        user_expr = st.text_input("Ekspresi:", "3*x + 5")
    
    if user_expr:
        try:
            expr = sp.sympify(user_expr)
            free_symbols = expr.free_symbols
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Variabel", str(list(free_symbols)) if free_symbols else "Tidak ada")
            with col2:
                # Logika sederhana mencari koefisien untuk satu variabel
                if free_symbols:
                    var = list(free_symbols)
                    coeff = expr.coeff(var)
                    st.metric("Koefisien", str(coeff))
            with col3:
                constant = expr.as_coeff_add()
                st.metric("Konstanta", str(constant))
                
            st.success(f"Bentuk Aljabar: ${sp.latex(expr)}$")
        except:
            st.error("Gunakan format penulisan Python (Contoh: 3*x untuk 3x)")

### ══════════════════════════════════════════
### KP 2 — NILAI BENTUK ALJABAR (SUBSTITUSI)
### ══════════════════════════════════════════
elif tab_choice == "🧮 KP 2 — Nilai Bentuk Aljabar":
    st.header("🧮 Kalkulator Substitusi")
    st.write("Hitung nilai aljabar dengan mengganti variabel menjadi angka.")
    
    expr_input = st.text_input("Masukkan Ekspresi (misal: 2*x - 3):", "2*x - 3")
    val_input = st.number_input("Masukkan Nilai x:", value=5)
    
    if st.button("Hitung Nilai"):
        try:
            x = sp.symbols('x')
            expr = sp.sympify(expr_input)
            result = expr.subs(x, val_input)
            st.markdown(f"### Hasil: **{result}**")
            st.write(f"Proses: {expr_input.replace('x', f'({val_input})')} = {result}")
        except:
            st.error("Input tidak valid.")

### ══════════════════════════════════════════
### KP 3 — OPERASI & SEDERHANAKAN
### ══════════════════════════════════════════
elif tab_choice == "➗ KP 3 — Operasi & Sederhanakan":
    st.header("➗ Sederhanakan Operasi Aljabar")
    st.write("Gunakan sifat distributif, komutatif, dan asosiatif untuk menyederhanakan suku sejenis.")
    
    op_type = st.selectbox("Pilih Operasi:", ["Sederhanakan Suku Sejenis", "Jabarkan (Distributif)"])
    
    if op_type == "Sederhanakan Suku Sejenis":
        raw_input = st.text_input("Contoh: 2*x + 3*x + 5 - 2", "2*x + 3*x + 5 - 2")
        if st.button("Sederhanakan"):
            res = sp.simplify(raw_input)
            st.latex(f"{sp.latex(sp.sympify(raw_input))} = {sp.latex(res)}")
            
    else:
        raw_input = st.text_input("Contoh: 3*(x + 2)", "3*(x + 2)")
        if st.button("Jabarkan"):
            res = sp.expand(raw_input)
            st.latex(f"{sp.latex(sp.sympify(raw_input))} = {sp.latex(res)}")

### ══════════════════════════════════════════
### LATIHAN MANDIRI
### ══════════════════════════════════════════
elif tab_choice == "📝 Latihan Mandiri":
    st.header("📝 Uji Pemahamanmu")
    st.write("Kerjakan soal berikut dan periksa jawabanmu secara mandiri.")
    
    soal = "Jika $a = -4$ dan $b = 7$, berapakah nilai dari $2a - b + ab$?"
    st.markdown(f"<div class='card'>{soal}</div>", unsafe_allow_html=True)
    
    jawaban_user = st.number_input("Jawabanmu:", value=0)
    if st.button("Cek Jawaban"):
        # Hitung: 2(-4) - 7 + (-4)(7) = -8 - 7 - 28 = -43
        if jawaban_user == -43:
            st.balloons()
            st.success("Luar biasa! Jawabanmu benar.")
        else:
            st.error("Coba lagi, ya! Perhatikan tanda negatifnya.")

### ─────────────────────────────────────────
### FOOTER
### ─────────────────────────────────────────
st.markdown("---")
st.markdown("<center><small>Jelajah Matematika VII | Dikembangkan dengan Streamlit & Sympy</small></center>", unsafe_allow_html=True)
```

### Penjelasan Singkat Fitur:
1.  **Library `sympy`**: Saya menambahkan `sympy` karena sangat kuat untuk menangani aljabar secara simbolik (menyederhanakan, menjabarkan, dan substitusi) sehingga hasilnya akurat sesuai kaidah matematika.
2.  **Unsur Aljabar (KP 1)**: Memungkinkan siswa memasukkan bentuk apa pun dan aplikasi akan memisahkan koefisien dan konstanta secara otomatis sesuai definisi di sumber.
3.  **Substitusi (KP 2)**: Membantu siswa memahami proses mengganti variabel dengan angka.
4.  **Operasi (KP 3)**: Mendukung penyederhanaan suku sejenis dan penjabaran distributif seperti contoh $3(x+2) = 3x+6$ dalam buku.
5.  **Latihan (Evaluasi)**: Saya menyertakan salah satu soal uraian dari LKS Anda mengenai nilai substitusi $a$ dan $b$ sebagai fitur interaktif.

Anda bisa menyimpan kode ini sebagai file `app.py` dan menghubungkannya ke repositori GitHub untuk dijalankan di **Streamlit Community Cloud**.
