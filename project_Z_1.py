import streamlit as st

st.set_page_config(page_title="For you :)", page_icon="🐻", layout="centered")

# ====== CSS CUSTOM ======
page_bg = """
<style>
/* Background gradien biru langit */
.stApp {
    background: linear-gradient(135deg, #a2d2ff, #cdb4db);
    color: #1e1e1e;
    font-family: "Segoe UI", sans-serif;
}

/* Card style */
.question-box {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

/* Judul pertanyaan */
.question-box h3 {
    color: #2d6eb5;
    margin-bottom: 10px;
}

/* Tombol custom */
div.stButton > button:first-child {
    background-color: #4a90e2;
    color: white;
    border-radius: 12px;
    padding: 10px 24px;
    font-weight: bold;
    border: none;
    box-shadow: 1px 3px 6px rgba(0,0,0,0.2);
    transition: all 0.3s ease-in-out;
}

div.stButton > button:first-child:hover {
    background-color: #2d6eb5;
    transform: scale(1.05);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ====== Judul ======
st.title("✨ Spesial Untuk Zalfa si Paling Suka Tebak-Tebakan ✨")
st.write("Allooo Zalfa, aku punya game tebak-tebakan manis buat kamu. Coba jawab ya, aku kasih clue satu per satu 😉")

# ====== Daftar Tebakan ======
tebakan_list = [
    ("Aku punya topi koboi, temanku Buzz Lightyear, tapi sekarang aku jadi boneka kesayanganmu. Siapa aku?",
     "woody", "Hebat, emang kmu paling sayang sama Woody yaa wkwk 🤠"),

    ("Aku robot putih gembul, suka bilang 'Ba-la-la-la~'. Siapa aku?",
     "baymax", "Yee bener, Baymax yang gendut gemes kayak kamu kalau lagi peluk boneka 🤭"),

    ("Aku bulu-buluan, suka ngeong, suka manjain kamu, dan namaku warna langit. Siapa aku?",
     "blue", "Iyaa, Blue kucing kesayangan kamu 😺"),

    ("Aku bikin perih, bikin sakit, tapi juga bukti kamu kuat bisa bangkit lagi. Aku apa?",
     "luka", ", siapa yg kemaren abiss jatohh, orang ko hobinya jatoh -_- but anyway GWS YAAA..💪"),

    ("Aku datang diam-diam, bikin hati berat, kadang bikin air mata jatuh. Aku siapa?",
     "sedih", "Iya, tapi inget Zalfa, aku selalu ada buat bikin kamu bahagia lagii wkwk candaa 😊"),

    ("Kalau bunga itu mawar, kalau bintang itu rembulan, kalau gadis cantik dan baik hati itu siapa?",
     "zalfa", "Hehe jelas jawabannya kamu, Zalfa yang cantik dan baik hati✨, ini paling berat sii nulisnyaa hahahah"),

    ("Aku kadang datang dari orang yang salah, bikin hati remuk, tapi juga ngajarin kamu buat lebih kuat. Aku apa?",
     "sakit hati", "Yaa, tapi sekarang semoga nggak ada yang berani nyakitin kamu lagi yaa, semangatt💖"),

    ("Aku nggak kelihatan, tapi bisa bikin kamu bangun tiap pagi, bikin kamu tetap bertahan. Aku apa?",
     "semangat", "Betul! Walaupun kmu banyak masalahnyaa tapii kmuu bisa tetap semangatt dan ceriaa is impresive tho🔥"),
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

    # tampilkan progress bar
    progress = int((index / total) * 100)
    st.progress(progress, text=f"Progress: {index}/{total} pertanyaan selesai")

    # tampilkan pertanyaan dalam card putih
    st.markdown(
        f"""
        <div class="question-box">
            <h3>Pertanyaan {index+1} dari {total}</h3>
            <p>{pertanyaan}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    jawaban_input = st.text_input("Jawabanmu apa? (ketik di sini)", key=f"jawaban_{index}")

    if st.button("Cek Jawaban"):
        if jawaban_input.strip().lower() == jawaban:
            st.success(respon)
            st.session_state.score += 1
        else:
            st.error(f"Belum tepat 😅. Jawaban yang benar 👉 **{jawaban.capitalize()}**")
        st.session_state.answered = True

    if st.session_state.answered:
        if st.button("Lanjut ➡️"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.rerun()

else:
    st.balloons()
    st.success("Horeee! Kamu sudah jawab semua tebak-tebakan 🎉✨")
    st.write(f"Skor akhir kamu: **{st.session_state.score} / {total}** 💯")

    # pesan semangat di akhir
    st.markdown(
        """
        ---
        ### 🌸 A Little Motivation for You, Zalfa 🌸
        Life may sometimes knock you down and leave scars,  
        but don’t forget, you are strong 💪 and truly precious ✨.  
        Keep smiling, keep your spirit alive, and most importantly: Keep Alive ❤️  
        Because the world is a brighter place with you in it. 🌍💖
        """,
        unsafe_allow_html=True
    )
