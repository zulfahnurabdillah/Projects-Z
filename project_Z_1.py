import streamlit as st
import random

st.set_page_config(page_title="For you :)", page_icon="🐻", layout="centered")

# ====== CSS CUSTOM ======
page_bg = """
<style>
/* Background gradien biru langit */
.stApp {{
    background: linear-gradient(135deg, #a2d2ff, #cdb4db);
    color: #1e1e1e;
    font-family: "Segoe UI", sans-serif;
}}

/* Animasi fade-in */
@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.fade-in {{
    animation: fadeIn 0.8s ease-in-out;
}}

/* Card style */
.question-box {{
    background-color: rgba(255, 255, 255, 0.92);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}}

/* Judul pertanyaan */
.question-box h3 {{
    color: #2d6eb5;
    margin-bottom: 10px;
}}

/* Tombol custom */
div.stButton > button:first-child {{
    background-color: #4a90e2;
    color: white;
    border-radius: 12px;
    padding: 10px 24px;
    font-weight: bold;
    border: none;
    box-shadow: 1px 3px 6px rgba(0,0,0,0.2);
    transition: all 0.3s ease-in-out;
}}

div.stButton > button:first-child:hover {{
    background-color: #2d6eb5;
    transform: scale(1.05);
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ====== Judul ======
st.title("✨ Spesial Untuk Zalfa si Paling Suka Tebak-Tebakan ✨")
st.write("Allooo Zalfa, aku punya game tebak-tebakan nihh buat kamu. Coba jawab ya, aku kasih clue satu per satu 😉")

# ====== Daftar Tebakan ======
tebakan_list = [
    ("Aku punya topi koboi, temanku Buzz Lightyear, tapi sekarang aku jadi boneka kesayanganmu. Siapa aku?",
     "woody", "Good job!!, emang kmu paling sayang sama Woody yaa, tiatii klo malem diliatin wkwkk 🤠"),
    ("Aku robot putih gembul, suka bilang 'Ba-la-la-la~'. Siapa aku?",
     "baymax", "Yee bener, Baymax yang gendut gemes kayak kamu kalau lagi peluk boneka 🤭"),
    ("Aku bulu-buluan, suka ngeong, suka manjain kamu, dan namaku warna langit. Siapa aku?",
     "blue", "Iyaa, Blue kucing kesayangan kamu😺, btw namanya grey ngga si harusnyaa -_-"),
    ("Aku bikin perih, bikin sakit, tapi juga bukti kamu kuat bisa bangkit lagi. Aku apa?",
     "luka", "yapp bener, hayoo Siapa yg kemaren abiss jatohh? Orang ko hobinya jatoh, but anyway GWS YAAA..💪"),
    ("Aku datang diam-diam, bikin hati berat, kadang bikin air mata jatuh. Aku siapa?",
     "sedih", "True, tapi inget Zalfa, aku selalu ada buat bikin kamu bahagia lagii 😊, ahahahh candaa"),
    ("Kalau bunga itu mawar, kalau bintang itu rembulan, kalau gadis cantik dan baik hati itu siapa?",
     "zalfa", "Hehe jelas jawabannya kamu, Zalfa yang cantik dan baik hati✨, sejujurnya berat sii ngetik bagian ini wkwkk"),
    ("Aku kadang datang dari orang yang salah, bikin hati remuk, tapi juga ngajarin kamu buat lebih kuat. Aku apa?",
     "sakit hati", "Yaa, tapi sekarang semoga nggak ada yang berani nyakitin kamu lagi yaa, semangatt💖"),
    ("Aku nggak kelihatan, tapi bisa bikin kamu bangun tiap pagi, bikin kamu tetap bertahan. Aku apa?",
     "semangat", "Betul! Walaupun kmu banyak masalahnyaa tapii kmuu bisa tetap semangatt dan ceriaa it's impressive tho🔥"),
]

# ====== State ======
if "index" not in st.session_state:
    st.session_state.index = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "score" not in st.session_state:
    st.session_state.score = 0

index = st.session_state.index
total = len(tebakan_list)

# ====== Konten utama ======
if index < total:
    pertanyaan, jawaban, respon = tebakan_list[index]

    # Progress bar + caption
    progress = index / total
    st.progress(progress)
    st.caption(f"Progress: {index}/{total} pertanyaan selesai")

    # Pertanyaan dalam card + fade-in animasi
    st.markdown(
        f"""
        <div class="question-box fade-in">
            <h3>Pertanyaan {index+1} dari {total}</h3>
            <p>{pertanyaan}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    jawaban_input = st.text_input("Jawabanmu apa? (ketik di sini)", key=f"jawaban_{index}")

    # Tombol cek jawaban
    if st.button("Cek Jawaban"):
        if jawaban_input.strip().lower() == jawaban:
            st.success(respon)
            st.session_state.score += 1
            st.session_state.answered = True
        else:
            st.error("TETOTTT!!! Salahh 😅 coba lagi ya!")
            st.session_state.answered = False

    # Tombol next hanya aktif kalau jawaban sudah benar
    if st.session_state.answered:
        if st.button("➡️ Next"):
            st.session_state.index += 1
            st.session_state.answered = False

else:
    # Generate bintang statis
    NUM_STARS = 120
    shadows = []
    for _ in range(NUM_STARS):
        x = round(random.uniform(1, 99), 2)
        y = round(random.uniform(1, 99), 2)
        spread = random.choice([0, 1])
        opacity = round(random.uniform(0.6, 1.0), 2)
        shadows.append(f"{x}vw {y}vh 0 {spread}px rgba(255,255,255,{opacity})")

    box_shadow_css = ",\n            ".join(shadows)

    night_bg_template = """
    <style>
    .stApp {{
        position: relative;
        background: linear-gradient(to bottom, #0d1b2a, #1b263b, #0d1b2a);
        color: #ffffff;
        font-family: "Segoe UI", sans-serif;
        overflow: hidden;
    }}

    /* Aurora */
    .aurora {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 40%;
        background: radial-gradient(circle at 50% 0%,
            rgba(0, 255, 150, 0.35),
            rgba(180, 0, 255, 0.25),
            rgba(0, 200, 255, 0.2),
            transparent 70%
        );
        background-size: 400% 400%;
        animation: aurora 18s ease-in-out infinite;
        z-index: -2;
    }}

    @keyframes aurora {{
        0%   {{ background-position: 0% 50%; }}
        50%  {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Pastikan konten tetap di atas */
    .stApp > div {{
        position: relative;
        z-index: 1;
    }}

    /* Bintang */
    .stars {{
        position: fixed;
        top: 0;
        left: 0;
        width: 1px;
        height: 1px;
        background: transparent;
        border-radius: 50%;
        box-shadow: {box_shadow_css};
        filter: blur(0.2px);
        opacity: 0.95;
        z-index: -2;
    }}

    /* Bulan */
    .moon {{
        width: 120px;
        height: 120px;
        background: radial-gradient(circle at 30% 30%, #fdfd96, #f1c40f);
        border-radius: 50%;
        position: fixed;
        top: 10%;
        right: 15%;
        box-shadow: 0 0 40px 12px rgba(255, 255, 200, 0.5);
        z-index: -2;
    }}

    /* Card motivasi */
    .motivation-card {{
        background: rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 25px;
        margin-top: 20px;
        backdrop-filter: blur(6px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        text-align: center;
        font-size: 18px;
        line-height: 1.6;
    }}

    /* Judul glow */
    .glow-text {{
        font-size: 22px;
        font-weight: bold;
        color: #fff;
        text-align: center;
        text-shadow: 0 0 10px #fff,
                     0 0 20px #4facfe,
                     0 0 30px #00f2fe;
    }}
    </style>

    <div class="stars"></div>
    <div class="moon"></div>
    <div class="aurora"></div>
    """

    night_bg = night_bg_template.format(box_shadow_css=box_shadow_css)
    st.markdown(night_bg, unsafe_allow_html=True)

    # Balon bawaan Streamlit
    st.balloons()

    # Pesan akhir
    st.success("Horeee! Kamu sudah jawab semua tebak-tebakan 🎉✨")
    st.write(f"Skor akhir kamu: **{st.session_state.score} / {total}** 💯")

    st.markdown(
        """
        <div class="motivation-card">
            <div class="glow-text">🌸 A Little Motivation for You, Zalfa 🌸</div>
            <p>
                Life may sometimes knock you down and leave scars,<br>
                but don’t forget, you are strong 💪 and truly precious ✨.<br>
                Keep smiling, keep your spirit alive, and most importantly: <b>Keep Living</b> ❤️<br>
                Because the world is a brighter place with you in it. 🌍💖
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
