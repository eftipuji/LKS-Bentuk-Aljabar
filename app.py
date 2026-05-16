import streamlit as st
import sympy as sp

### ─────────────────────────────────────────
### 1. KONFIGURASI HALAMAN
### ─────────────────────────────────────────
st.set_page_config(
    page_title="Jelajah Bentuk Aljabar",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

### ─────────────────────────────────────────
### 2. CSS KUSTOM (Selaras dengan seri Jelajah)
### ─────────────────────────────────────────
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stHeader { background-color: #1E3A8A; color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    .card { background: white; padding: 1.5rem; border-radius: 15px; border-left: 5px solid #1E3A8A; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 1rem; }
    .sidebar-title { font-size: 1.3rem; font-weight: bold; color: #1E3A8A; }
    </style>
""", unsafe_allow_html=True)

### ─────────────────────────────────────────
### 3. SIDEBAR NAVIGASI
### ─────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Menu Eksplorasi</div>', unsafe_allow_html=True)
    tab_choice = st.radio(
        "Pilih Kegiatan Pembelajaran (KP):",
        options=[
            "🏠 Beranda",
            "🔍 KP 1 — Unsur Bentuk Aljabar",
            "🧮 KP 2 — Nilai Bentuk Aljabar",
            "➗ KP 3 — Operasi & Sifat Aljabar",
            "📝 Latihan Mandiri"
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.info("**Petunjuk:** Gunakan kalkulator ini untuk memverifikasi jawaban pada LKS Anda.")
    st.markdown("<small>Penulis: Efti Puji Lestari</small>", unsafe_allow_html=True)

### ─────────────────────────────────────────
### 4. HALAMAN BERANDA
### ─────────────────────────────────────────
if tab_choice == "🏠 Beranda":
    st.markdown("<div class='stHeader'><h1>🧬 Selamat Datang di Jelajah Bentuk Aljabar!</h1></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns()
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>Mengapa Belajar Aljabar?</h3>
        Bentuk aljabar memungkinkan kita menyatakan kuantitas yang berubah-ubah atau tidak diketahui dengan simbol atau <b>variabel</b>. 
        Aljabar membantu kita menyampaikan informasi matematika secara lebih ringkas dan universal.
        <br><br>
        <b>Tokoh Penting:</b><br>
        Al-Khwarizmi dijuluki sebagai "Bapak Aljabar". Penemuannya digunakan untuk menyelesaikan masalah matematika dengan pendekatan geometris.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Al-Khwarizmi_portrait.jpg/220px-Al-Khwarizmi_portrait.jpg", caption="Al-Khawarizmi")

### ─────────────────────────────────────────
### 5. KP 1 — UNSUR-UNSUR ALJABAR
### ─────────────────────────────────────────
elif tab_choice == "🔍 KP 1 — Unsur Bentuk Aljabar":
    st.header("🔍 Identifikasi Unsur Aljabar")
    st.write("Variabel adalah huruf/simbol untuk kuantitas yang tidak diketahui. Koefisien adalah pengali variabel, dan konstanta adalah bilangan tetap.")
    
    with st.expander("📝 Input Ekspresi (Contoh: 3*x + 5)"):
        input_teks = st.text_input("Ketik bentuk aljabar (gunakan '*' untuk perkalian):", "3*x + 5")
    
    if input_teks:
        try:
            expr = sp.sympify(input_teks)
            st.success(f"Bentuk Matematika: ${sp.latex(expr)}$")
            
            # Analisis Unsur
            vars_found = expr.free_symbols
            st.write("---")
            c1, c2, c3 = st.columns(3)
            
            with c1:
                st.metric("Variabel", str(list(vars_found)) if vars_found else "Tidak ada")
            with c2:
                if vars_found:
                    v = list(vars_found)
                    st.metric(f"Koefisien {v}", str(expr.coeff(v)))
            with c3:
                # Mengambil bagian konstanta
                konstanta = expr.as_coeff_add()
                st.metric("Konstanta", str(konstanta))
        except:
            st.error("Format salah. Gunakan 'x' atau 'y' dan tanda '*' (Contoh: 2*x untuk 2x).")

### ─────────────────────────────────────────
### 6. KP 2 — NILAI BENTUK ALJABAR (SUBSTITUSI)
### ─────────────────────────────────────────
elif tab_choice == "🧮 KP 2 — Nilai Bentuk Aljabar":
    st.header("🧮 Kalkulator Substitusi")
    st.write("Hitung nilai aljabar dengan mengganti variabel dengan angka tertentu.")
    
    col1, col2 = st.columns(2)
    with col1:
        expr_sub = st.text_input("Masukkan Ekspresi (Contoh: 2*x - 3):", "2*x - 3")
    with col2:
        val_x = st.number_input("Nilai x =", value=5)
    
    if st.button("Hitung Nilai"):
        try:
            x = sp.symbols('x')
            hasil = sp.sympify(expr_sub).subs(x, val_x)
            st.markdown(f"<div class='card'><h4>Hasil: {hasil}</h4><p>Proses: {expr_sub.replace('x', f'({val_x})')} = {hasil}</p></div>", unsafe_allow_html=True)
        except:
            st.error("Terjadi kesalahan input.")

### ─────────────────────────────────────────
### 7. KP 3 — OPERASI & SIFAT ALJABAR
### ─────────────────────────────────────────
elif tab_choice == "➗ KP 3 — Operasi & Sifat Aljabar":
    st.header("➗ Sederhanakan Operasi Aljabar")
    st.write("Gunakan sifat distributif $a(b+c) = ab + ac$ dan gabungkan suku sejenis.")
    
    op_mode = st.selectbox("Pilih Jenis Operasi:", ["Sederhanakan Suku Sejenis", "Jabarkan (Sifat Distributif)"])
    
    if op_mode == "Sederhanakan Suku Sejenis":
        user_in = st.text_input("Input (Contoh: 2*x + 5 + 3*x - 2):", "2*x + 5 + 3*x - 2")
        if st.button("Sederhanakan"):
            res = sp.simplify(user_in)
            st.latex(f"{sp.latex(sp.sympify(user_in))} = {sp.latex(res)}")
    else:
        user_in = st.text_input("Input (Contoh: 3*(x + 2)):", "3*(x + 2)")
        if st.button("Jabarkan"):
            res = sp.expand(user_in)
            st.latex(f"{sp.latex(sp.sympify(user_in))} = {sp.latex(res)}")

### ─────────────────────────────────────────
### 8. LATIHAN MANDIRI
### ─────────────────────────────────────────
elif tab_choice == "📝 Latihan Mandiri":
    st.header("📝 Uji Pemahaman")
    st.write("Coba kerjakan soal dari evaluasi LKS Anda.")
    
    st.markdown("""
    <div class='card'>
    <b>Soal:</b> Jika $a = -4$ dan $b = 7$, berapakah nilai dari $2a - b + ab$?
    </div>
    """, unsafe_allow_html=True)
    
    jawaban = st.number_input("Masukkan jawabanmu:", value=0)
    if st.button("Cek Jawaban"):
        # Hitung manual: 2(-4) - 7 + (-4)(7) = -8 - 7 - 28 = -43
        if jawaban == -43:
            st.balloons()
            st.success("Benar! Luar biasa.")
        else:
            st.error("Masih kurang tepat. Coba perhatikan tanda negatifnya kembali.")

### ─────────────────────────────────────────
### 9. FOOTER
### ─────────────────────────────────────────
st.markdown("---")
st.markdown("<center><small>Jelajah Matematika VII | Streamlit & SymPy Implementation</small></center>", unsafe_allow_html=True)
```

