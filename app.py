import streamlit as st
import asyncio
import tempfile
import base64
import os
import random

# ----- Audio Setup -----
try:
    import edge_tts
    import nest_asyncio
    nest_asyncio.apply()
    EDGE_TTS_AVAILABLE = True
except (ModuleNotFoundError, ImportError):
    EDGE_TTS_AVAILABLE = False

st.set_page_config(page_title="Let's Learn Chinese with Gesner", layout="wide")

def set_colorful_style():
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #1a0b2e, #2d1b4e, #1a0b2e); }
        .main-header { background: linear-gradient(135deg, #ff6b6b, #feca57, #48dbfb); padding: 1.5rem; border-radius: 20px; text-align: center; margin-bottom: 1rem; }
        .main-header h1 { color: white; text-shadow: 2px 2px 4px #000000; font-size: 2.5rem; margin: 0; }
        .main-header p { color: #fff5cc; font-size: 1.2rem; margin: 0; }
        html, body, .stApp, .stMarkdown, .stText, .stRadio label, .stSelectbox label, .stTextInput label, .stButton button, .stTitle, .stSubheader, .stHeader, .stCaption, .stAlert, .stException, .stCodeBlock, .stDataFrame, .stTable, .stTabs [role="tab"], .stTabs [role="tablist"] button, .stExpander, .stProgress > div, .stMetric label, .stMetric value, div, p, span, pre, code, .element-container, .stTextArea label, .stText p, .stText div, .stText span, .stText code { color: white !important; }
        .stText { color: white !important; font-size: 1rem; background: transparent !important; }
        .stTabs [role="tab"] { color: white !important; background: rgba(255,255,255,0.1); border-radius: 10px; margin: 0 2px; }
        .stTabs [role="tab"][aria-selected="true"] { background: rgba(255,255,255,0.3); color: white !important; }
        .stRadio [role="radiogroup"] label { background: rgba(255,255,255,0.15); border-radius: 10px; padding: 0.3rem; margin: 0.2rem 0; color: white !important; }
        .stButton button { background-color: #ff6b6b; color: white; border-radius: 30px; font-weight: bold; }
        .stButton button:hover { background-color: #feca57; color: black; }
        section[data-testid="stSidebar"] { background: linear-gradient(135deg, #1a0b2e, #2d1b4e); }
        section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] .stText, section[data-testid="stSidebar"] label { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox label { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] { background-color: #2d1b4e; border: 1px solid #ffcc00; border-radius: 10px; }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox svg { fill: white; }
        section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] span { color: white !important; }
        div[data-baseweb="popover"] ul { background-color: #2d1b4e; border: 1px solid #ffcc00; }
        div[data-baseweb="popover"] li { color: white !important; background-color: #2d1b4e; }
        div[data-baseweb="popover"] li:hover { background-color: #ff6b6b; }
        </style>
    """, unsafe_allow_html=True)

def show_logo():
    st.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <svg width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="url(#gradLogo)" stroke="#ffcc00" stroke-width="3"/>
                <defs><linearGradient id="gradLogo" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ff007f"/>
                    <stop offset="50%" stop-color="#ffcc00"/>
                    <stop offset="100%" stop-color="#00ffcc"/>
                </linearGradient></defs>
                <text x="50" y="65" font-size="40" text-anchor="middle" fill="white" font-weight="bold">中</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    set_colorful_style()
    st.title("🔐 Access Required")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_logo()
        st.markdown("<h2 style='text-align: center;'>Let's Learn Chinese with Gesner</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #FFD700;'>Book 1 – Lessons 1 to 20</p>", unsafe_allow_html=True)
        password_input = st.text_input("Enter password to access", type="password")
        if st.button("Login"):
            if password_input == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Access denied.")
    st.stop()

set_colorful_style()
st.markdown("""
<div class="main-header">
    <h1>📘 Let's Learn Chinese with Gesner</h1>
    <p>Book 1 – 20 interactive lessons | Daily conversations | Vocabulary | Grammar | Pronunciation | Quizzes</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    show_logo()
    st.markdown("## 🎯 Select a lesson")
    lesson_number = st.selectbox("Lesson", list(range(1, 21)), index=0)
    st.markdown("---")
    st.markdown("### 📚 Your progress")
    st.progress(lesson_number / 20)
    st.markdown(f"✅ Lesson {lesson_number} of 20 completed")
    st.markdown("---")
    st.markdown("**Founder & Developer:**")
    st.markdown("Gesner Deslandes")
    st.markdown("📞 WhatsApp: (509) 4738-5663")
    st.markdown("📧 Email: deslandes78@gmail.com")
    st.markdown("🌐 [Main website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Price")
    st.markdown("**$299 USD** (full book – 20 lessons, source code included)")
    st.markdown("---")
    st.markdown("### © 2025 GlobalInternet.py")
    st.markdown("All rights reserved")
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ----- Lesson topics (Chinese) -----
topics = [
    "自我介绍", "日常生活", "在超市", "点餐", "问路",
    "谈论家庭", "看医生", "工作面试", "计划旅行", "天气与季节",
    "买衣服", "在银行", "乘坐公共交通", "租房", "庆祝生日",
    "去电影院", "在健身房", "打电话", "写邮件", "谈论爱好"
]

def generate_conversations(topic):
    conv1 = f"A: 你好！今天怎么样？\nB: 我很好，谢谢！我正在学习关于{topic}。\nA: 太好了。你能多告诉我一些吗？\nB: 当然！我每天都练习。"
    conv2 = f"A: 打扰一下，你能帮我学习{topic}吗？\nB: 当然！你想知道什么？\nA: 我想提高我的中文。\nB: 这是个很好的目标。继续练习！"
    conv3 = f"A: 你好，我是新来的。你能解释一下{topic}吗？\nB: 当然！这对日常生活非常有用。\nA: 非常感谢！\nB: 不客气。我们一起练习吧。"
    return [conv1, conv2, conv3]

def generate_vocabulary(topic):
    base_words = ["你好", "再见", "请", "谢谢", "是", "不是", "也许", "总是", "有时", "从不",
                  "快速地", "慢慢地", "仔细地", "快乐地", "悲伤地", "大声地", "轻声地", "明亮地", "黑暗地", "温柔地"]
    topic_words = [topic + str(i) for i in range(1, 6)]
    all_words = base_words[:15] + topic_words
    return all_words[:20]

def get_grammar_rules():
    return [
        {
            "rule": "1. 使用主谓宾结构（我吃饭）。",
            "examples": ["我爱你。", "他喝水。", "我们学习中文。"]
        },
        {
            "rule": "2. 使用'是'表示判断（我是学生）。",
            "examples": ["她是老师。", "这是书。", "他是我的朋友。"]
        },
        {
            "rule": "3. 使用'有'表示拥有（我有一本书）。",
            "examples": ["他有一辆车。", "我们有两个孩子。", "她有一个弟弟。"]
        },
        {
            "rule": "4. 使用'能'表示能力或允许（我能说中文）。",
            "examples": ["我能游泳。", "你能帮我吗？", "她不能来。"]
        },
        {
            "rule": "5. 使用'会'表示技能或未来计划（我会去北京）。",
            "examples": ["我会说英语。", "明天会下雨。", "他会做饭。"]
        },
        {
            "rule": "6. 频率副词（总是、有时、从不）放在动词前。",
            "examples": ["我总是在八点吃早餐。", "有时我去看电影。", "我从不迟到。"]
        },
        {
            "rule": "7. 使用介词（在、上面、下面）表示位置。",
            "examples": ["书在桌子上。", "猫在椅子下面。", "她住在上海。"]
        },
        {
            "rule": "8. 使用'有'表示存在（有一个餐厅）。",
            "examples": ["附近有一个餐厅。", "这里有很多人。", "冰箱里有牛奶吗？"]
        },
        {
            "rule": "9. 使用'想要'表示愿望（我想要一杯咖啡）。",
            "examples": ["我想要去北京。", "他想要一辆新车。", "她想要学习更多。"]
        },
        {
            "rule": "10. 使用'要'表示计划（我要去旅行）。",
            "examples": ["明天我要去上海。", "他们要吃饭。", "你今晚要学习吗？"]
        }
    ]

def generate_pronunciation_sentences(topic):
    return [
        f"我今天学习{topic}。",
        f"你能给我解释{topic}吗？",
        f"练习{topic}帮助我提高中文。",
        f"我们一起讨论{topic}吧。",
        f"理解{topic}非常有用。"
    ]

def generate_quiz_questions(topic):
    return [
        {"question": "这一课的主要话题是什么？", "options": [topic, "体育", "音乐", "电影"], "answer": topic},
        {"question": "哪个词表示'感谢'？", "options": ["请", "对不起", "谢谢", "打扰一下"], "answer": "谢谢"},
        {"question": "如何礼貌地请求帮助？", "options": ["给我帮助", "帮助现在", "你能帮我吗？", "你必须帮助"], "answer": "你能帮我吗？"},
        {"question": "'总是'是什么意思？", "options": ["从不", "有时", "每次", "很少"], "answer": "每次"},
        {"question": "哪个句子是正确的？", "options": ["他去学校", "他去学校。", "他去学校吗", "他去学校了"], "answer": "他去学校。"}
    ]

@st.cache_data
def get_lesson_data(num_lesson):
    topic = topics[num_lesson - 1]
    return {
        "topic": topic,
        "conversations": generate_conversations(topic),
        "vocabulary": generate_vocabulary(topic),
        "grammar": get_grammar_rules(),
        "pronunciation": generate_pronunciation_sentences(topic),
        "quiz": generate_quiz_questions(topic)
    }

lesson_data = get_lesson_data(lesson_number)
st.markdown(f"## 📖 Lesson {lesson_number}: {lesson_data['topic']}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["💬 Conversations", "📚 Vocabulary", "📖 Grammar", "🎧 Pronunciation", "❓ Quiz"])

# ----- Audio function (Chinese voice) -----
async def save_speech(text, file_path):
    communicate = edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural")
    await communicate.save(file_path)

def play_audio(text, key):
    if not EDGE_TTS_AVAILABLE:
        st.info("🔇 Audio disabled. Please install edge-tts.")
        return
    if st.button(f"🔊", key=key):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            try:
                asyncio.run(save_speech(text, tmp.name))
                with open(tmp.name, "rb") as f:
                    audio_bytes = f.read()
                    b64 = base64.b64encode(audio_bytes).decode()
                    st.markdown(f'<audio controls src="data:audio/mp3;base64,{b64}" autoplay style="width: 100%;"></audio>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Audio error: {e}")
            finally:
                if os.path.exists(tmp.name):
                    os.unlink(tmp.name)

# ----- TAB 1: CONVERSATIONS -----
with tab1:
    for i, conv in enumerate(lesson_data["conversations"], 1):
        st.markdown(f"**Conversation {i}**")
        st.text(conv)
        play_audio(conv, f"conv_{lesson_number}_{i}")
        st.markdown("---")

# ----- TAB 2: VOCABULARY -----
with tab2:
    cols = st.columns(4)
    for idx, word in enumerate(lesson_data["vocabulary"]):
        with cols[idx % 4]:
            st.markdown(f"**{word}**")
            play_audio(word, f"vocab_{lesson_number}_{idx}")

# ----- TAB 3: GRAMMAR -----
with tab3:
    st.subheader("💡 Grammar Rules (with examples and audio)")
    for idx, item in enumerate(lesson_data["grammar"]):
        st.markdown(f"**{item['rule']}**")
        play_audio(item['rule'], f"gram_rule_{lesson_number}_{idx}")
        st.markdown("**Examples:**")
        for ex_idx, ex in enumerate(item['examples']):
            col_ex, col_btn = st.columns([4, 1])
            col_ex.write(f"• {ex}")
            with col_btn:
                play_audio(ex, f"gram_ex_{lesson_number}_{idx}_{ex_idx}")
        st.markdown("---")
    
    st.markdown("---")
    st.subheader("🌟 The Basics")
    with st.expander("🔤 Chinese Pinyin (Initials & Finals)", expanded=True):
        st.markdown("**Initials:** b p m f d t n l g k h j q x zh ch sh r z c s")
        st.markdown("**Finals:** a o e i u ü ai ei ui ao ou iu ie üe er an en in un ün ang eng ing ong")
        st.caption("Click the audio button to hear pronunciation.")
        play_audio("b p m f d t n l g k h j q x zh ch sh r z c s", "pinyin_initials")
        play_audio("a o e i u ü ai ei ui ao ou iu ie üe er an en in un ün ang eng ing ong", "pinyin_finals")

    with st.expander("🔢 Numbers (Cardinal & Ordinal)"):
        st.markdown("**Cardinal Numbers (1 to 10)**")
        cardinals = [
            ("1", "一 yī"), ("2", "二 èr"), ("3", "三 sān"), ("4", "四 sì"),
            ("5", "五 wǔ"), ("6", "六 liù"), ("7", "七 qī"), ("8", "八 bā"),
            ("9", "九 jiǔ"), ("10", "十 shí")
        ]
        cols_card = st.columns(5)
        for idx, (num, word) in enumerate(cardinals):
            with cols_card[idx % 5]:
                st.write(f"**{num}** – {word}")
                play_audio(word, f"card_{num}_{lesson_number}")
        
        st.markdown("---")
        st.markdown("**Ordinal Numbers (1st to 10th)**")
        ordinals = [
            ("1st", "第一 dì yī"), ("2nd", "第二 dì èr"), ("3rd", "第三 dì sān"), ("4th", "第四 dì sì"),
            ("5th", "第五 dì wǔ"), ("6th", "第六 dì liù"), ("7th", "第七 dì qī"), ("8th", "第八 dì bā"),
            ("9th", "第九 dì jiǔ"), ("10th", "第十 dì shí")
        ]
        cols_ord = st.columns(5)
        for idx, (num, word) in enumerate(ordinals):
            with cols_ord[idx % 5]:
                st.write(f"**{num}** – {word}")
                play_audio(word, f"ord_{num}_{lesson_number}")

    with st.expander("🗣️ Common Idioms"):
        idioms = [
            {"phrase": "马马虎虎", "meaning": "So-so, average."},
            {"phrase": "一见钟情", "meaning": "Love at first sight."},
            {"phrase": "对牛弹琴", "meaning": "To play the lute to a cow – waste of time."}
        ]
        for idx, item in enumerate(idioms):
            st.markdown(f"**{item['phrase']}**")
            st.caption(item['meaning'])
            play_audio(f"{item['phrase']}. 意思是: {item['meaning']}", f"idiom_{idx}_{lesson_number}")
            st.markdown("---")

# ----- TAB 4: PRONUNCIATION -----
with tab4:
    st.markdown("Listen to each sentence, then repeat out loud.")
    for idx, sentence in enumerate(lesson_data["pronunciation"]):
        st.markdown(f"**Sentence {idx+1}:** {sentence}")
        play_audio(sentence, f"pron_{lesson_number}_{idx}")
        st.markdown("---")

# ----- TAB 5: QUIZ (with audio for questions, options, and correct answers) -----
with tab5:
    st.markdown("Test your understanding of this lesson.")
    
    quiz_key = f"quiz_answers_{lesson_number}"
    if quiz_key not in st.session_state:
        st.session_state[quiz_key] = {}
    
    questions = lesson_data["quiz"]
    
    for q_idx, q in enumerate(questions):
        st.markdown(f"**{q_idx+1}. {q['question']}**")
        play_audio(q['question'], f"quiz_question_{lesson_number}_{q_idx}")
        
        selected = st.session_state[quiz_key].get(q_idx, None)
        for opt_idx, opt in enumerate(q['options']):
            col_text, col_audio = st.columns([5, 1])
            with col_text:
                if st.button(opt, key=f"select_{lesson_number}_{q_idx}_{opt_idx}"):
                    st.session_state[quiz_key][q_idx] = opt
                    st.rerun()
            with col_audio:
                play_audio(opt, f"quiz_opt_{lesson_number}_{q_idx}_{opt_idx}")
            st.markdown("---")
        if selected:
            st.success(f"Selected: {selected}")
        else:
            st.info("You have not selected an answer yet. Click on an option above.")
        st.markdown("---")
    
    if st.button("Check answers", key=f"check_{lesson_number}"):
        score = 0
        for q_idx, q in enumerate(questions):
            if st.session_state[quiz_key].get(q_idx) == q["answer"]:
                score += 1
        st.success(f"You got {score} out of {len(questions)} correct!")
        if score == len(questions):
            st.balloons()
            st.markdown("🎉 Perfect! You have mastered this lesson.")
        else:
            with st.expander("Show correct answers"):
                for q_idx, q in enumerate(questions):
                    col_text, col_audio = st.columns([5, 1])
                    with col_text:
                        st.write(f"{q_idx+1}. {q['question']} → Correct answer: {q['answer']}")
                    with col_audio:
                        correct_text = f"{q['question']} Correct answer: {q['answer']}"
                        play_audio(correct_text, f"correct_ans_{lesson_number}_{q_idx}")

# ----- END OF BOOK -----
if lesson_number == 20:
    st.markdown("---")
    st.markdown("## 🎓 Congratulations! You have completed Book 1.")
    st.markdown("""
    ### 📞 To continue with Book 2, contact us:
    - **Gesner Deslandes** – Founder
    - 📱 WhatsApp: (509) 4738-5663
    - 📧 Email: deslandes78@gmail.com
    - 🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
    
    Book 2 will contain more advanced conversations, vocabulary, grammar, and real‑life simulations.
    """)
