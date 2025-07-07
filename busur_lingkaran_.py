import streamlit as st
import math
import time
import random
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Fungsi Inti Perhitungan ---
def hitung_busur_juring(radius, sudut_derajat):
    """
    Menghitung panjang busur dan luas juring lingkaran.
    Mengembalikan tuple (panjang_busur, luas_juring) atau (None, None) jika input tidak valid.
    """
    if radius <= 0:
        return None, None # Jari-jari harus positif

    sudut_radian = math.radians(sudut_derajat)
    panjang_busur = radius * sudut_radian
    luas_juring = 0.5 * (radius**2) * sudut_radian
    return panjang_busur, luas_juring

# --- Fungsi untuk Membuat Visualisasi Lingkaran ---
def plot_lingkaran_juring(radius, sudut_derajat):
    fig = go.Figure()

    # Gambar Lingkaran Penuh
    theta_full = np.linspace(0, 2 * np.pi, 100)
    x_full = radius * np.cos(theta_full)
    y_full = radius * np.sin(theta_full)
    fig.add_trace(go.Scatter(x=x_full, y=y_full, mode='lines', name='Lingkaran',
                             line=dict(color='lightgray', width=2)))

    # Gambar Juring
    if sudut_derajat != 0 and radius > 0:
        sudut_radian = math.radians(sudut_derajat)
        
        # Batasi sudut agar tidak terlalu berputar dalam visualisasi jika melebihi 360
        # Untuk visualisasi, kita hanya peduli bentuknya, bukan berapa kali putaran
        visual_sudut_radian = sudut_radian % (2 * math.pi)
        if visual_sudut_radian < 0: # Mengatasi sudut negatif jika diizinkan (saat ini min_value slider = 0)
            visual_sudut_radian += 2 * math.pi

        # Titik-titik untuk juring
        # Mulai dari (0,0), lalu ke (r,0), ikuti busur, lalu kembali ke (0,0)
        theta_juring = np.linspace(0, visual_sudut_radian, 50)
        x_juring_busur = radius * np.cos(theta_juring)
        y_juring_busur = radius * np.sin(theta_juring)

        x_juring = np.concatenate([[0], x_juring_busur, [0]])
        y_juring = np.concatenate([[0], y_juring_busur, [0]])

        fig.add_trace(go.Scatter(x=x_juring, y=y_juring, mode='lines', fill='toself', name='Juring',
                                 fillcolor='rgba(100, 149, 237, 0.5)', # Warna biru muda transparan
                                 line=dict(color='cornflowerblue', width=2)))
        
        # Garis radius
        fig.add_trace(go.Scatter(x=[0, radius * math.cos(0)], y=[0, radius * math.sin(0)],
                                 mode='lines', name='Radius 1', line=dict(color='darkblue', width=2)))
        if visual_sudut_radian > 0:
             fig.add_trace(go.Scatter(x=[0, radius * math.cos(visual_sudut_radian)], y=[0, radius * math.sin(visual_sudut_radian)],
                                 mode='lines', name='Radius 2', line=dict(color='darkblue', width=2)))

    # Pengaturan layout
    max_val = radius * 1.2 # Beri sedikit ruang di sekitar lingkaran
    fig.update_xaxes(range=[-max_val, max_val], showgrid=False, zeroline=False, showticklabels=False)
    fig.update_yaxes(range=[-max_val, max_val], showgrid=False, zeroline=False, showticklabels=False, scaleanchor="x", scaleratio=1)
    fig.update_layout(title='Visualisasi Lingkaran dan Juring', showlegend=False,
                      plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)') # Transparan

    return fig


# --- Halaman Menu 1: Kalkulator Busur & Juring ---
def kalkulator_menu():
    st.title("📏 Kalkulator Panjang Busur & Luas Juring Lingkaran 📐")
    st.markdown("""
    Selamat datang di kalkulator interaktif! Masukkan nilai **jari-jari** lingkaran dan **sudut** juring
    (dalam derajat) untuk menemukan panjang busur dan luas juringnya.
    **Visualisasi akan berubah secara *real-time*!**
    """)

    st.write("---")

    st.header("⚙️ Masukkan Data Lingkaran")

    col1, col2 = st.columns(2)

    with col1:
        radius = st.number_input(
            "Masukkan Jari-jari Lingkaran (r)",
            min_value=0.01,
            value=10.0,
            format="%.2f",
            help="Jari-jari lingkaran harus bernilai positif."
        )
    with col2:
        sudut_derajat = st.slider
