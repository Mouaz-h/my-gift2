import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="A story about the girl i adore ❤️", page_icon="💖", layout="centered")

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

# --- GET CURRENT DIRECTORY ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- CSS: THEME & BACKGROUND EFFECTS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Fade-in animation for new steps */
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    h1 {
        color: #c9184a !important;
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem !important;
        text-align: center;
    }
    .message-box {
        text-align: center;
        color: #800f2f;
        font-size: 1.5rem;
        background: rgba(255, 255, 255, 0.3);
        padding: 20px;
        border-radius: 20px;
        margin: 20px 0;
    }
    
    /* Floating background hearts */
    .bg-heart {
        color: rgba(201, 24, 74, 0.3); 
        font-size: 20px;
        position: fixed;
        top: -10%;
        z-index: 0; 
        animation: heartFloat 8s linear infinite;
    }
    @keyframes heartFloat {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    
    <div class="bg-heart" style="left:10%; animation-delay:0s;">❤️</div>
    <div class="bg-heart" style="left:40%; animation-delay:2s;">💖</div>
    <div class="bg-heart" style="left:80%; animation-delay:1s;">💕</div>
    """, unsafe_allow_html=True)

# --- THE JOURNEY LOGIC ---

# STEP 0: THE START
if st.session_state.step == 0:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.markdown("<h1>Hey my shadozaa... ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>I made special story just for you. Are you ready to see it?</div>", unsafe_allow_html=True)
    st.button("Yes, I'm Ready! 🥰", on_click=lambda: setattr(st.session_state, 'step', 2))
    st.button("No, I'm Not Ready! ", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 1: warning
elif st.session_state.step == 1:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>Stop being idiotic and go back 😡 </div>", unsafe_allow_html=True)
    st.button("Next Surprise ✨", on_click=lambda: setattr(st.session_state, 'step', 0) or st.rerun())
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 2: FIRST PHOTO
elif st.session_state.step == 2:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC1.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>this beautiful girl sudnly appeared in my life and changed everything</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 3: SECOND PHOTO
elif st.session_state.step == 3:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC2.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>know she means every thing to me</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 4: THIRD PHOTO
elif st.session_state.step == 4:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC3.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>you know why ?</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>beacause she appeared in my life at the perfect time</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>the time when every thing is meaningless and dark</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 5: FOURTH PHOTO
elif st.session_state.step == 5:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC4.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>i was so lost, sad and stressed</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>but when she appeared every thing changed</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>she was like an angel she always made me smile</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 6: FIFTH PHOTO
elif st.session_state.step == 6:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.image(os.path.join(BASE_DIR, "PIC5.jpg"), use_container_width=True)
    st.markdown("<div class='message-box'>she gave me hope and life and the spirit to keep going in whatever i do just by her smile and cutness</div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>soo i just want to say thank you for being here with me </div>", unsafe_allow_html=True)
    st.markdown("<div class='message-box'>i love you so much, you are (جميلة )like how i always say to you</div>", unsafe_allow_html=True)
    st.button("Continue... ❤️", on_click=next_step)
    st.markdown("</div>", unsafe_allow_html=True)

# STEP 7: THE FINAL MESSAGE
elif st.session_state.step == 7:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.markdown("<h1>I Love You to the Moon and Back ❤️</h1>", unsafe_allow_html=True)
    st.write(""" last thing i want to say that 
        I am sorry for being away sometimes (let you alone and sleep i mean), but I promise to make it up to you. 
        I want to make all your wishes come true because you deserve the world.
    """)
    if st.button("Click for the Ultimate Surprise! 🌹"):
        st.balloons()
        # The heart burst JS from before
        st.markdown("""
            <script>
            for(let i=0; i<100; i++) {
                const heart = document.createElement('div');
                heart.innerText = '❤️', '💖', '💕', '💗', '💓', '❤️‍🔥', '💝';
                heart.style.position = 'fixed';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.top = '100vh';
                heart.style.fontSize = '30px';
                heart.style.animation = `up ${Math.random()*2+2}s forwards`;
                document.body.appendChild(heart);
                const s = document.createElement('style');
                s.innerHTML = `@keyframes up { to { transform: translateY(-120vh); opacity:0; } }`;
                document.head.appendChild(s);
            }
            </script>
        """, unsafe_allow_html=True)
    
    if st.button("Restart Journey 🔄"):
        st.session_state.step = 0
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)