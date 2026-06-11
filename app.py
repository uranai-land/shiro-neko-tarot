import base64
import random
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="白猫タロット", page_icon="🐈", layout="wide")

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
CARDS_DIR = BASE_DIR / "cards"

TAROT_CARDS = [
    "愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "力", "隠者",
    "運命の輪", "正義", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月", "太陽",
    "審判", "世界",
]

CARD_IMAGE_FILES = {
    "愚者": "00_fool.png",
    "魔術師": "01_magician.png",
    "女教皇": "02_high_priestess.png",
    "女帝": "03_empress.png",
    "皇帝": "04_emperor.png",
    "教皇": "05_hierophant.png",
    "恋人": "06_lovers.png",
    "戦車": "07_chariot.png",
    "力": "08_strength.png",
    "隠者": "09_hermit.png",
    "運命の輪": "10_wheel_of_fortune.png",
    "正義": "11_justice.png",
    "吊るされた男": "12_hanged_man.png",
    "死神": "13_death.png",
    "節制": "14_temperance.png",
    "悪魔": "15_devil.png",
    "塔": "16_tower.png",
    "星": "17_star.png",
    "月": "18_moon.png",
    "太陽": "19_sun.png",
    "審判": "20_judgement.png",
    "世界": "21_world.png",
}

CARD_LIBRARY = {
    "愚者": {
        "upright": "自由、始まり、可能性、冒険",
        "reversed": "無計画、軽率、不安定、迷い",
        "interpretation": "今の悩みに対して、焦らずに一歩ずつ進むのがよい流れです。",
        "advice": "まずは小さな一歩を決めて、気持ちを軽くする行動から始めましょう。",
    },
    "魔術師": {
        "upright": "行動力、才能、創造、チャンス",
        "reversed": "準備不足、自信のなさ、空回り",
        "interpretation": "自分の力を信じて行動を起こすタイミングです。",
        "advice": "何ができるかを一つずつ整理し、今日できることを選んでみてください。",
    },
    "女教皇": {
        "upright": "直感、冷静、知性、秘密",
        "reversed": "考えすぎ、不安、閉鎖的",
        "interpretation": "心の声を信じる余裕がある時期です。",
        "advice": "不安な気持ちを一度置いて、静かな時間を持つと判断が明確になります。",
    },
    "女帝": {
        "upright": "愛情、豊かさ、魅力、実り",
        "reversed": "甘え、依存、わがまま",
        "interpretation": "自分を大切にすることと、相手を信じるバランスが大切です。",
        "advice": "相手に期待しすぎず、まずは自分のペースを守ってください。",
    },
    "皇帝": {
        "upright": "安定、責任、リーダーシップ、現実性",
        "reversed": "頑固、支配的、プレッシャー",
        "interpretation": "現実的な整理と決断が必要なタイミングです。",
        "advice": "手順を少しずつ確かめながら、無理のない形で進めてください。",
    },
    "教皇": {
        "upright": "伝統、教え、安心、信頼",
        "reversed": "固定観念、閉塞感、迷い",
        "interpretation": "今は自分の内なるルールや価値観を見直すと、安心につながります。",
        "advice": "誰かの言い方に流されすぎず、信じたいものを大切にしてください。",
    },
    "恋人": {
        "upright": "恋愛、選択、調和、ときめき",
        "reversed": "迷い、優柔不断、すれ違い",
        "interpretation": "心と心の距離を整えれば、関係は前へ進みやすくなります。",
        "advice": "気持ちを言葉にして、誤解を減らす会話を大切にしてください。",
    },
    "戦車": {
        "upright": "前進、勝利、勢い、決断",
        "reversed": "暴走、焦り、空回り",
        "interpretation": "勢いをつけるのは大事ですが、焦りすぎないことが鍵です。",
        "advice": "一日の中でできる小さな行動を優先して、無理なく進めてください。",
    },
    "力": {
        "upright": "優しさ、忍耐、信頼、内面の強さ",
        "reversed": "自信喪失、我慢しすぎ、不安",
        "interpretation": "自分の中のやわらかさと強さを両立させると、状況は変わります。",
        "advice": "相手に合わせすぎず、まずは自分の心が安らぐ選択を優先してください。",
    },
    "隠者": {
        "upright": "内省、慎重、探求、答えを探す",
        "reversed": "孤独、閉じこもり、考えすぎ",
        "interpretation": "今は一度立ち止まり、心の声を聞く時間が必要です。",
        "advice": "誰かに相談するのもよいですが、まずは自分の気持ちを整理してみてください。",
    },
    "運命の輪": {
        "upright": "転機、チャンス、流れの変化",
        "reversed": "停滞、タイミングのズレ、予想外",
        "interpretation": "流れは変わりつつあり、今の選択が未来をつくります。",
        "advice": "焦らずに、次に進める小さな可能性を見つけてください。",
    },
    "正義": {
        "upright": "公平、判断、バランス、誠実",
        "reversed": "不公平、迷い、偏った判断",
        "interpretation": "自分の気持ちと相手の気持ちの両方を見ながら判断する時です。",
        "advice": "感情に流されず、事実と自分の希望を分けて考えてください。",
    },
    "吊るされた男": {
        "upright": "忍耐、視点の変化、試練、気づき",
        "reversed": "報われない我慢、停滞、無理",
        "interpretation": "今は少し距離を置いて見直すと、答えが見えやすくなります。",
        "advice": "無理を続けるより、息をつく時間を作ると心が整います。",
    },
    "死神": {
        "upright": "終わりと再生、変化、区切り",
        "reversed": "変化への抵抗、未練、停滞",
        "interpretation": "古い関係や考え方を手放すことで、前へ進める段階です。",
        "advice": "変化が怖くても、少しずつ手放すことを優先してみてください。",
    },
    "節制": {
        "upright": "調和、回復、自然体、バランス",
        "reversed": "不安定、無理、乱れ",
        "interpretation": "自分に優しく、ゆっくり進めばよい時期です。",
        "advice": "無理を減らして、生活のリズムを整えると気持ちも安定します。",
    },
    "悪魔": {
        "upright": "執着、誘惑、依存、本音",
        "reversed": "解放、断ち切る、目が覚める",
        "interpretation": "本音に向き合うことで、関係や決断が整理されます。",
        "advice": "気持ちに正直になる一方で、相手への期待を減らしてみてください。",
    },
    "塔": {
        "upright": "衝撃、崩壊、急な変化、目覚め",
        "reversed": "小さな崩れ、変化を避ける、不安",
        "interpretation": "大きな変化は怖いですが、今の状況を見直すきっかけになります。",
        "advice": "変化を恐れず、必要なら小さな整理から始めてください。",
    },
    "星": {
        "upright": "希望、癒し、未来、願い",
        "reversed": "失望、自信不足、期待しすぎ",
        "interpretation": "希望を捨てずに、今できることを少しずつ続けると前向きになります。",
        "advice": "自分を責めすぎず、まずは安心できる一歩を選んでください。",
    },
    "月": {
        "upright": "不安、迷い、直感、曖昧さ",
        "reversed": "真実が見える、不安が晴れる",
        "interpretation": "今は見えない部分があるので、少し距離を取ると整理しやすいです。",
        "advice": "不安を一人で抱え込まず、信頼できる人に話してみてください。",
    },
    "太陽": {
        "upright": "成功、喜び、明るさ、祝福",
        "reversed": "一時的な不調、子どもっぽさ、油断",
        "interpretation": "前向きな気持ちが、現実の流れをやさしく整えます。",
        "advice": "小さな達成感を積み重ねて、自分を励ましながら進めてください。",
    },
    "審判": {
        "upright": "復活、決断、再スタート、気づき",
        "reversed": "迷い、後悔、決めきれない",
        "interpretation": "もう一度自分の気持ちを確かめて、次の選択に進むタイミングです。",
        "advice": "後悔よりも、今の自分に必要な一歩を選んでください。",
    },
    "世界": {
        "upright": "完成、達成、満足、一区切り",
        "reversed": "未完成、中途半端、あと一歩",
        "interpretation": "少しずつでも着実に進めば、満足につながる流れです。",
        "advice": "完璧を目指さず、今日できることだけを積み重ねてください。",
    },
}

CATEGORY_META = {
    "love": {"title": "恋愛運", "lead": "恋にまつわる気持ちを、やさしく読み解きます。", "icon": "lily"},
    "marriage": {"title": "結婚運", "lead": "結婚へ進む流れと、安心できるパートナー像を見ます。", "icon": "lily"},
    "reunion": {"title": "復縁", "lead": "過去のご縁がもう一度動き出す可能性を見ていきます。", "icon": "lily"},
    "secret": {"title": "禁断の恋", "lead": "心を守りながら、複雑な気持ちの流れを見ます。", "icon": "lily"},
    "money": {"title": "金運", "lead": "お金の流れと、やさしく増やしていくヒントを探します。", "icon": "rin"},
}

QUESTION_BANK = {
    "love": ["運命の相手はどんな人ですか？", "今の恋人は運命の相手ですか？", "新しい出会いはありますか？"],
    "marriage": ["いつ結婚するのでしょうか？", "今の恋人を結婚相手として選んでよいですか？", "結婚に向けて今必要なことは何ですか？"],
    "reunion": ["あの人と復縁することはできますか？", "次の恋に進むべきですか？", "あの人は私との復縁を望んでいますか？"],
    "secret": ["この恋を続けてもよいでしょうか？", "この関係に未来はありますか？", "この恋から離れるべきですか？"],
    "money": ["今後の収入はどうなりますか？", "お金を増やすために今すべきことは何ですか？", "臨時収入やチャンスはありますか？"],
}


def to_data_url(path: Path) -> str:
    try:
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        return f"data:image/png;base64,{encoded}"
    except Exception:
        return ""


def get_card_image_url(card_name: str) -> str:
    file_name = CARD_IMAGE_FILES.get(card_name)
    if not file_name:
        return ""
    return to_data_url(CARDS_DIR / file_name)


def render_image_html(path: Path, alt: str, width: str = "100%", height: str = "auto") -> None:
    st.components.v1.html(
        f"""
        <div style="display:flex;justify-content:center;margin:0 0 14px 0;">
          <img src="{to_data_url(path)}" alt="{alt}" style="width:{width};max-width:900px;height:{height};border-radius:24px;" />
        </div>
        """,
        height=220,
    )


def render_icon_chip(icon_name: str) -> str:
    image_path = ASSETS_DIR / ("lily_normal.png" if icon_name == "lily" else "rin_normal.png")
    return f'<img src="{to_data_url(image_path)}" alt="{icon_name}" style="width:38px;height:38px;border-radius:999px;object-fit:cover;box-shadow:0 6px 14px rgba(120,107,126,0.18);" />'


def pick_random_cards(count: int = 3):
    pool = list(CARD_LIBRARY.items())
    random.shuffle(pool)
    chosen = pool[:count]
    result = []
    for idx, (name, meta) in enumerate(chosen):
        direction = random.choice(["正位置", "逆位置"])
        meaning = meta["upright"] if direction == "正位置" else meta["reversed"]
        result.append({
            "position": ["過去", "現在", "未来"][idx],
            "name": name,
            "direction": direction,
            "meaning": meaning,
            "interpretation": meta["interpretation"],
            "advice": meta["advice"],
            "image_url": get_card_image_url(name),
        })
    return result


def make_total_message(cards):
    return (
        "この3枚は、今の悩みを整理し、次に取るべき行動を見つけるための小さな道しるべです。"
        "不安をあおるのではなく、今日できる一歩を選ぶことで、心の流れは少しずつ整っていきます。"
    )


st.markdown("""
<style>
  :root { color-scheme: light; }
  .stApp { background: linear-gradient(180deg, #fffafc 0%, #fff7fb 45%, #edf7ff 100%); }
  .block-container { padding-top: 1rem; padding-bottom: 3rem; }
  h1, h2, h3 { font-family: 'Yu Mincho', 'Hiragino Mincho ProN', 'Noto Serif JP', serif; }
  .soft-card { border: 1px solid #eadbe4; border-radius: 24px; background: rgba(255,255,255,0.92); padding: 18px; box-shadow: 0 18px 42px rgba(129,104,119,0.12); }
  .tiny-note { color: #6e6575; font-size: 0.92rem; line-height: 1.7; }
  .card-visual { width: min(100%, 220px); height: auto; border-radius: 18px; display: block; margin: 0 auto 10px; box-shadow: 0 12px 28px rgba(131,110,122,0.14); }
  @media (max-width: 640px) { .card-visual { width: 78%; max-width: 220px; } }
</style>
""", unsafe_allow_html=True)


if "phase" not in st.session_state:
    st.session_state.phase = "home"
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None
if "cards" not in st.session_state:
    st.session_state.cards = []


st.title("白猫タロット")
render_image_html(ASSETS_DIR / "banner.png", "白猫タロットのバナー", width="100%", height="auto")

st.markdown("""
<div class="soft-card">
  <p class="tiny-note">白猫タロットへようこそ。<br>
  リリーとリンが、3枚のカードで今の悩みを「過去・現在・未来」からやさしく読み解きます。<br>
  カードは未来を決めつけるものではなく、今の状況を整理し、次にどう行動すればよいかを見つけるための小さな道しるべです。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p class='tiny-note'>カテゴリの近くにある小さな顔アイコンは、リリーとリンの雰囲気を少しだけ添えています。</p>
""", unsafe_allow_html=True)

if st.session_state.phase == "home":
    st.subheader("テーマを選ぶ")
    cols = st.columns(5)
    for idx, (key, meta) in enumerate(CATEGORY_META.items()):
        with cols[idx if idx < 5 else 4]:
            icon_path = ASSETS_DIR / ("lily_normal.png" if meta["icon"] == "lily" else "rin_normal.png")
            st.image(icon_path, width=36)
            if st.button(meta["title"], key=f"cat_{key}", use_container_width=True):
                st.session_state.selected_category = key
                st.session_state.selected_question = None
                st.session_state.phase = "questions"
                st.rerun()

    st.caption("恋愛・結婚・復縁・禁断の恋はリリー系、金運はリン系です。")

elif st.session_state.phase == "questions":
    key = st.session_state.selected_category
    meta = CATEGORY_META[key]
    st.subheader(meta["title"])
    st.write(meta["lead"])
    if st.button("← トップへ戻る", key="back_home"):
        st.session_state.phase = "home"
        st.session_state.selected_category = None
        st.session_state.selected_question = None
        st.session_state.cards = []
        st.rerun()

    st.markdown("<div class='soft-card'>", unsafe_allow_html=True)
    for q in QUESTION_BANK[key]:
        if st.button(q, key=f"q_{q}", use_container_width=True):
            st.session_state.selected_question = q
            st.session_state.cards = []
            st.session_state.phase = "shuffle"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.phase == "shuffle":
    st.subheader("カードを整えています")
    st.write("リリーとリンがカードを整えています…")
    st.write("心が静かになったら Stop を押してください。")
    render_image_html(ASSETS_DIR / "shuffle.png", "カードを混ぜるイメージ", width="100%", height="auto")
    if st.button("Stop", key="stop_btn"):
        st.session_state.cards = pick_random_cards(3)
        st.session_state.phase = "result"
        st.rerun()

elif st.session_state.phase == "result":
    st.subheader("鑑定結果")
    render_image_html(ASSETS_DIR / "result.png", "鑑定結果のイメージ", width="100%", height="auto")
    st.write("リリーとリンが、過去・現在・未来の流れを読み解きました。")

    cols = st.columns(3)
    for idx, card in enumerate(st.session_state.cards):
        with cols[idx]:
            st.markdown("<div class='soft-card'>", unsafe_allow_html=True)
            if card.get("image_url"):
                rotation = "rotate(180deg)" if card["direction"] == "逆位置" else "rotate(0deg)"
                st.markdown(
                    f"<img class='card-visual' src='{card['image_url']}' alt='{card['name']}' style='transform:{rotation};transform-origin:center;' />",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown("<p class='tiny-note'>画像を読み込めませんでした。</p>", unsafe_allow_html=True)
            st.markdown(f"### {card['position']}・{card['name']}")
            st.markdown(f"**{card['direction']}**")
            st.write(f"意味: {card['meaning']}")
            st.write(f"今の悩みに対する解釈: {card['interpretation']}")
            st.write(f"具体的なアドバイス: {card['advice']}")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='soft-card'>", unsafe_allow_html=True)
    st.subheader("3枚全体を通した総合メッセージ")
    st.write(make_total_message(st.session_state.cards))
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("もう一度占う", key="again_btn"):
        st.session_state.phase = "home"
        st.session_state.selected_category = None
        st.session_state.selected_question = None
        st.session_state.cards = []
        st.rerun()

st.markdown("---")
st.markdown("""
<div class="soft-card">
  <p class="tiny-note">
  ※この占いは娯楽・自己理解を目的としたものです。<br>
  ※結果は未来を断定するものではありません。<br>
  ※医療・法律・投資・人生の重要な判断については、専門家や信頼できる方にご相談ください。<br>
  ※今後、鑑定結果に合わせたお守りや天然石アイテムをご紹介する場合がありますが、効果を保証するものではありません。
  </p>
</div>
""", unsafe_allow_html=True)
