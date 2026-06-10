import json
import streamlit as st
import streamlit.components.v1 as components
from tarot_data import TAROT_CARDS

st.set_page_config(
    page_title="白猫タロット",
    page_icon="🐾",
    layout="wide"
)

cards_json = json.dumps(TAROT_CARDS, ensure_ascii=False)

menus = {
    "love": {
        "title": "恋愛運",
        "button": "恋愛",
        "lead": "恋の流れを、白猫タロットがそっと読み解きます。",
        "questions": [
            {"code": "love_destiny_person", "text": "運命の相手はどんな人ですか？", "draw_count": 3, "labels": ["相手の人物像", "出会いのきっかけ", "あなたへの助言"]},
            {"code": "love_current_destiny", "text": "今の恋人は運命の相手ですか？", "draw_count": 3, "labels": ["現在のご縁", "相手の本心", "結ばれる可能性"]},
            {"code": "love_future", "text": "あの人との未来はどうなりますか？", "draw_count": 3, "labels": ["今の関係", "あの人の気持ち", "未来の流れ"]},
            {"code": "love_new_meeting", "text": "新しい出会いはありますか？", "draw_count": 3, "labels": ["今の恋愛運", "出会いの兆し", "出会いを引き寄せる行動"]},
            {"code": "love_feelings_now", "text": "あの人は今、私をどう思っていますか？", "draw_count": 3, "labels": ["表に出ている気持ち", "心の奥の本音", "これからの接し方"]},
            {"code": "love_next_time", "text": "次の恋が訪れるのはいつですか？", "draw_count": 3, "labels": ["今の状態", "恋が動く時期", "準備すべきこと"]},
            {"code": "love_popular_time", "text": "モテ期はいつ訪れますか？", "draw_count": 3, "labels": ["今の魅力", "モテ期の兆し", "魅力を高める鍵"]},
            {"code": "love_interest", "text": "あの人は私に気がありますか？", "draw_count": 3, "labels": ["あの人の意識", "隠れた感情", "距離を縮める鍵"]},
            {"code": "love_other_person", "text": "あの人には、ほかに好きな人がいますか？", "draw_count": 3, "labels": ["あの人の心の向き", "周囲の影響", "あなたへの助言"]},
            {"code": "love_how_think", "text": "あの人は私のことをどう思っていますか？", "draw_count": 3, "labels": ["あなたへの印象", "今の気持ち", "今後の可能性"]},
        ],
    },
    "marriage": {
        "title": "結婚運",
        "button": "結婚",
        "lead": "結婚へ向かう流れと、幸せの形を丁寧に見ていきます。",
        "questions": [
            {"code": "marriage_when", "text": "私はいつ結婚するのでしょうか？", "draw_count": 3, "labels": ["今の結婚運", "結婚が近づく時期", "今から整えること"]},
            {"code": "marriage_with_person", "text": "あの人との結婚は幸せでしょうか？", "draw_count": 3, "labels": ["ふたりの相性", "結婚後の課題", "幸せに進む鍵"]},
            {"code": "marriage_current_partner", "text": "今の恋人を結婚相手として選んでよいですか？", "draw_count": 3, "labels": ["現在の関係", "結婚相手としての可能性", "見極めるポイント"]},
            {"code": "marriage_needed", "text": "結婚に向けて、今必要なことは何ですか？", "draw_count": 3, "labels": ["今の課題", "必要な準備", "未来への助言"]},
        ],
    },
    "reunion": {
        "title": "復縁",
        "button": "復縁",
        "lead": "過去のご縁が、もう一度結び直される可能性を見ていきます。",
        "questions": [
            {"code": "reunion_possible", "text": "あの人と復縁することはできますか？", "draw_count": 3, "labels": ["別れの原因", "あの人の現在", "復縁の可能性"]},
            {"code": "reunion_move_on", "text": "次の恋に進むべきですか？", "draw_count": 3, "labels": ["今の未練", "新しい恋の可能性", "あなたへの助言"]},
            {"code": "reunion_new_partner", "text": "あの人には新しいパートナーがいますか？", "draw_count": 3, "labels": ["あの人の現在", "恋愛状況の気配", "あなたが取るべき距離"]},
            {"code": "reunion_wants", "text": "あの人は私との復縁を望んでいますか？", "draw_count": 3, "labels": ["あの人の本音", "復縁への迷い", "関係を動かす鍵"]},
            {"code": "reunion_regret", "text": "あの人は私に未練がありますか？", "draw_count": 3, "labels": ["残っている感情", "素直になれない理由", "今後の可能性"]},
            {"code": "reunion_meet_again", "text": "あの人とはもう会えないのでしょうか？", "draw_count": 3, "labels": ["再会の可能性", "障害になっているもの", "未来への助言"]},
        ],
    },
    "secret": {
        "title": "禁断の恋",
        "button": "禁断の恋",
        "lead": "簡単には進めない恋だからこそ、心を守るための答えを探します。",
        "questions": [
            {"code": "secret_continue", "text": "この恋を続けてもよいのでしょうか？", "draw_count": 3, "labels": ["今の気持ち", "この恋の危うさ", "あなたを守る助言"]},
            {"code": "secret_serious", "text": "既婚者のあの人は、私を本気で想っていますか？", "draw_count": 3, "labels": ["あの人の本音", "行動と現実", "あなたが見るべき真実"]},
            {"code": "secret_future", "text": "この関係に未来はありますか？", "draw_count": 3, "labels": ["現在の関係", "隠れている問題", "未来の行方"]},
            {"code": "secret_choose", "text": "あの人は家庭と私、どちらを選びますか？", "draw_count": 3, "labels": ["あの人の迷い", "現実の重さ", "あなたへの助言"]},
            {"code": "secret_leave", "text": "この恋から離れるべきですか？", "draw_count": 3, "labels": ["心の執着", "離れることで得るもの", "次に進む力"]},
        ],
    },
    "money": {
        "title": "金運",
        "button": "金運",
        "lead": "お金の流れ、収入、チャンスを白猫タロットで見ていきます。",
        "questions": [
            {"code": "money_income", "text": "今後の収入はどうなりますか？", "draw_count": 3, "labels": ["現在の金運", "収入の流れ", "増やすための行動"]},
            {"code": "money_increase", "text": "お金を増やすために、今すべきことは何ですか？", "draw_count": 3, "labels": ["今の課題", "伸ばすべき力", "金運アップの鍵"]},
            {"code": "money_invest", "text": "今は投資や大きな買い物をしてもよい時期ですか？", "draw_count": 3, "labels": ["現在の判断力", "注意すべきこと", "安全な進め方"]},
            {"code": "money_sidejob", "text": "仕事や副業で収入は増えますか？", "draw_count": 3, "labels": ["仕事運", "副業の可能性", "収入につなげる行動"]},
            {"code": "money_anxiety", "text": "今のお金の不安は解消されますか？", "draw_count": 3, "labels": ["不安の原因", "流れが変わる兆し", "安心に近づく方法"]},
            {"code": "money_chance", "text": "臨時収入やチャンスはありますか？", "draw_count": 3, "labels": ["金運の動き", "チャンスの場所", "受け取るための準備"]},
        ],
    },
}

menus_json = json.dumps(menus, ensure_ascii=False)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            padding: 0;
            background:
                radial-gradient(circle at 20% 10%, rgba(255, 240, 246, 0.95), transparent 32%),
                radial-gradient(circle at 80% 20%, rgba(236, 248, 255, 0.95), transparent 30%),
                linear-gradient(180deg, #ffffff 0%, #f8f4f0 100%);
            color: #4a403a;
            font-family: "Yu Gothic", "Hiragino Sans", sans-serif;
            text-align: center;
        }

        .app {
            min-height: 980px;
            padding: 24px 20px 60px;
        }

        .cat-mark {
            font-size: 30px;
            margin-bottom: 6px;
        }

        .site-title {
            font-size: 46px;
            letter-spacing: 8px;
            font-weight: 300;
            color: #4a403a;
            margin-bottom: 10px;
            font-family: "Yu Mincho", "Hiragino Mincho ProN", serif;
        }

        .site-subtitle {
            font-size: 14px;
            color: #9b8c82;
            letter-spacing: 3px;
            margin-bottom: 58px;
        }

        .menu-icon {
            position: fixed;
            left: 35px;
            top: 150px;
            font-size: 36px;
            color: #a99485;
            z-index: 10;
        }

        .home-grid {
            max-width: 900px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(3, 210px);
            justify-content: center;
            gap: 78px 88px;
        }

        .home-bottom {
            max-width: 520px;
            margin: 78px auto 0;
            display: grid;
            grid-template-columns: repeat(2, 210px);
            justify-content: center;
            gap: 90px;
        }

        .main-button {
            width: 210px;
            height: 210px;
            border-radius: 50%;
            border: 1px solid rgba(214, 198, 184, 0.65);
            background:
                radial-gradient(circle at 35% 28%, #ffffff 0%, #fff9f5 42%, #eadfd5 100%);
            color: #6a5a50;
            font-size: 22px;
            font-weight: bold;
            cursor: pointer;
            line-height: 1.6;
            transition: 0.2s ease;
            box-shadow:
                0 14px 28px rgba(120, 96, 80, 0.12),
                inset 0 0 0 8px rgba(255, 255, 255, 0.55);
            overflow: hidden;
            outline: none;
            appearance: none;
            -webkit-appearance: none;
        }

        .main-button::before,
        .main-button::after {
            content: none !important;
            display: none !important;
        }

        .main-button:hover {
            transform: translateY(-4px) scale(1.03);
            background:
                radial-gradient(circle at 35% 28%, #ffffff 0%, #fff5f7 45%, #e8d7dc 100%);
            color: #57443f;
        }

        .main-button:focus { outline: none; }

        .footer-icons {
            margin-top: 95px;
            color: #9b8c82;
            font-size: 18px;
            letter-spacing: 8px;
        }

        .copyright {
            color: #9b8c82;
            font-size: 11px;
            letter-spacing: 1px;
            margin-top: 10px;
        }

        .category-title {
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #4a403a;
        }

        .category-lead {
            color: #8a7c73;
            font-size: 15px;
            margin-bottom: 28px;
        }

        .small-back-button {
            padding: 10px 22px;
            border-radius: 999px;
            border: 1px solid #d8c8bc;
            background: #ffffff;
            color: #7f6d63;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            margin-bottom: 30px;
            box-shadow: 0 6px 14px rgba(120, 96, 80, 0.08);
        }

        .small-back-button:hover { background: #fff7f3; }

        .question-grid {
            max-width: 950px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(2, minmax(260px, 1fr));
            gap: 16px;
        }

        .question-button {
            min-height: 74px;
            border-radius: 22px;
            border: 1px solid #e1d3c8;
            background: rgba(255, 255, 255, 0.85);
            color: #5b4c44;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            padding: 16px 18px;
            line-height: 1.6;
            box-shadow: 0 8px 18px rgba(120, 96, 80, 0.08);
            transition: 0.18s;
        }

        .question-button:hover {
            background: #fff2f4;
            transform: translateY(-2px);
        }

        .reading-title {
            font-size: 28px;
            font-weight: bold;
            margin-top: 6px;
            margin-bottom: 8px;
        }

        .reading-question {
            color: #6f5f56;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .reading-sub {
            color: #8a7c73;
            font-size: 15px;
            margin-bottom: 18px;
        }

        .shuffle-stage {
            position: relative;
            width: 420px;
            height: 330px;
            margin: 0 auto;
        }

        .deck-shadow {
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 135px;
            height: 198px;
            border-radius: 18px;
            background: rgba(190, 160, 140, 0.16);
            filter: blur(13px);
        }

        .shuffle-card {
            position: absolute;
            left: 50%;
            top: 50%;
            width: 118px;
            height: 186px;
            margin-left: -59px;
            margin-top: -93px;
            border-radius: 16px;
            background: linear-gradient(145deg, #ffffff, #fff7f3);
            border: 1px solid #dfd1c7;
            box-shadow: 0 10px 24px rgba(120, 96, 80, 0.14);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            transition: transform 0.08s linear, opacity 0.08s linear;
        }

        .shuffle-card::before {
            content: "";
            position: absolute;
            inset: 9px;
            border: 1px solid #eadfd8;
            border-radius: 13px;
        }

        .shuffle-card::after {
            content: "✦";
            position: absolute;
            top: 14px;
            right: 14px;
            color: #d5b99c;
            font-size: 14px;
        }

        .shuffle-symbol {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background:
                radial-gradient(circle at 35% 30%, #ffffff 0%, #fff2f2 35%, #d8bca5 100%);
            color: #ffffff;
            font-size: 34px;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 2;
            text-shadow: 0 1px 2px rgba(90, 70, 60, 0.25);
        }

        .shuffle-name {
            position: absolute;
            bottom: 16px;
            left: 0;
            right: 0;
            color: #b59f90;
            font-size: 10px;
            letter-spacing: 2px;
            font-weight: bold;
            z-index: 2;
        }

        .guide {
            color: #8a7c73;
            font-size: 14px;
            margin-top: 4px;
            margin-bottom: 20px;
        }

        .stop-button {
            width: 122px;
            height: 122px;
            border-radius: 50%;
            border: 1px solid #d8c8bc;
            background:
                radial-gradient(circle at 35% 30%, #ffffff 0%, #fff5f5 40%, #d8bca5 100%);
            color: #715f55;
            font-size: 25px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 10px 20px rgba(120, 96, 80, 0.15);
            transition: 0.15s;
        }

        .stop-button:hover {
            transform: scale(1.04);
            background:
                radial-gradient(circle at 35% 30%, #ffffff 0%, #ffeef2 45%, #d2ad98 100%);
        }

        .result-area {
            display: none;
            margin-top: 16px;
        }

        .result-card {
            max-width: 720px;
            margin: 18px auto;
            padding: 22px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid #e1d3c8;
            box-shadow: 0 8px 20px rgba(120, 96, 80, 0.11);
            text-align: left;
        }

        .result-card h3 {
            margin: 0 0 10px;
            color: #4a403a;
            font-size: 22px;
        }

        .result-card p {
            line-height: 1.8;
            font-size: 15px;
            color: #5b4c44;
        }

        .fortune-message {
            max-width: 760px;
            margin: 22px auto;
            padding: 28px;
            border-radius: 20px;
            background: rgba(255, 248, 247, 0.94);
            border: 1px solid #e1d3c8;
            text-align: left;
            line-height: 1.95;
            font-size: 15px;
            color: #534741;
            box-shadow: 0 8px 20px rgba(120, 96, 80, 0.09);
        }

        .fortune-message strong {
            color: #4a403a;
            font-size: 16px;
        }

        .again-button {
            margin-top: 18px;
            padding: 12px 28px;
            border-radius: 999px;
            border: 1px solid #d8c8bc;
            background: #ffffff;
            color: #7f6d63;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        .again-button:hover { background: #fff2f4; }

        .notice {
            max-width: 720px;
            margin: 26px auto 0;
            color: #9b8c82;
            font-size: 12px;
            line-height: 1.8;
        }

        @media screen and (max-width: 850px) {
            .site-title {
                font-size: 36px;
                letter-spacing: 5px;
            }

            .home-grid {
                grid-template-columns: repeat(2, 170px);
                gap: 45px;
            }

            .home-bottom {
                grid-template-columns: repeat(2, 170px);
                gap: 45px;
            }

            .main-button {
                width: 170px;
                height: 170px;
                font-size: 19px;
            }

            .question-grid {
                grid-template-columns: 1fr;
            }

            .shuffle-stage {
                width: 330px;
            }
        }
    </style>
</head>

<body>
    <div class="app">
        <div class="menu-icon">☰</div>

        <div class="cat-mark">🐾</div>
        <div class="site-title">白猫タロット</div>
        <div class="site-subtitle">WHITE CAT TAROT READING</div>

        <div id="homeArea">
            <div class="home-grid">
                <button class="main-button" onclick="showCategory('love')">恋愛</button>
                <button class="main-button" onclick="showCategory('marriage')">結婚</button>
                <button class="main-button" onclick="showCategory('reunion')">復縁</button>
            </div>

            <div class="home-bottom">
                <button class="main-button" onclick="showCategory('secret')">禁断の恋</button>
                <button class="main-button" onclick="showCategory('money')">金運</button>
            </div>

            <div class="footer-icons">🐾 ✦ ♡ ☽ ✦ 🐾</div>
            <div class="copyright">© 2026 WHITE CAT TAROT</div>
        </div>

        <div id="categoryArea" style="display: none;">
            <div class="category-title" id="categoryTitle"></div>
            <div class="category-lead" id="categoryLead"></div>
            <button class="small-back-button" onclick="goHome()">最初の画面に戻る</button>
            <div class="question-grid" id="questionGrid"></div>
        </div>

        <div id="readingArea" style="display: none;">
            <div class="reading-title" id="readingTitle"></div>
            <div class="reading-question" id="readingQuestion"></div>
            <div class="reading-sub">心が静かになったら、Stopを押してください。</div>
            <button class="small-back-button" onclick="backToCategory()">質問一覧に戻る</button>

            <div id="beforeArea">
                <div class="shuffle-stage" id="shuffleStage">
                    <div class="deck-shadow"></div>
                </div>
                <div class="guide">白猫がカードを混ぜています…</div>
                <button class="stop-button" onclick="stopShuffle()">Stop</button>
            </div>

            <div class="result-area" id="resultArea">
                <h2>鑑定結果</h2>
                <div id="resultCards"></div>
                <div class="fortune-message" id="fortuneMessage"></div>
                <button class="again-button" onclick="restartSameReading()">もう一度占う</button>
            </div>

            <div class="notice">
                ※この占いは娯楽・自己理解を目的としたものです。大切な判断は、現実の状況やご自身の安全を最優先にしてください。
            </div>
        </div>
    </div>

    <script>
        const cards = __CARDS_JSON__;
        const menus = __MENUS_JSON__;

        let selectedCategoryKey = null;
        let selectedCategory = null;
        let selectedQuestionIndex = null;
        let selectedQuestion = null;
        let currentCards = [];
        let timer = null;
        let shuffleTick = 0;

        const homeArea = document.getElementById("homeArea");
        const categoryArea = document.getElementById("categoryArea");
        const readingArea = document.getElementById("readingArea");
        const categoryTitle = document.getElementById("categoryTitle");
        const categoryLead = document.getElementById("categoryLead");
        const questionGrid = document.getElementById("questionGrid");
        const readingTitle = document.getElementById("readingTitle");
        const readingQuestion = document.getElementById("readingQuestion");
        const shuffleStage = document.getElementById("shuffleStage");
        const beforeArea = document.getElementById("beforeArea");
        const resultArea = document.getElementById("resultArea");
        const resultCards = document.getElementById("resultCards");
        const fortuneMessage = document.getElementById("fortuneMessage");

        function showCategory(categoryKey) {
            selectedCategoryKey = categoryKey;
            selectedCategory = menus[categoryKey];

            homeArea.style.display = "none";
            readingArea.style.display = "none";
            categoryArea.style.display = "block";

            categoryTitle.innerText = selectedCategory.title;
            categoryLead.innerText = selectedCategory.lead;

            questionGrid.innerHTML = "";

            selectedCategory.questions.forEach(function(question, index) {
                const button = document.createElement("button");
                button.className = "question-button";
                button.innerText = question.text;
                button.onclick = function() {
                    startReading(index);
                };
                questionGrid.appendChild(button);
            });
        }

        function goHome() {
            clearInterval(timer);
            selectedCategoryKey = null;
            selectedCategory = null;
            selectedQuestionIndex = null;
            selectedQuestion = null;

            homeArea.style.display = "block";
            categoryArea.style.display = "none";
            readingArea.style.display = "none";
        }

        function backToCategory() {
            clearInterval(timer);
            readingArea.style.display = "none";
            categoryArea.style.display = "block";
        }

        function startReading(questionIndex) {
            selectedQuestionIndex = questionIndex;
            selectedQuestion = selectedCategory.questions[questionIndex];

            categoryArea.style.display = "none";
            readingArea.style.display = "block";
            beforeArea.style.display = "block";
            resultArea.style.display = "none";

            readingTitle.innerText = selectedCategory.title;
            readingQuestion.innerText = selectedQuestion.text;

            shuffleTick = 0;
            currentCards = [];
            resultCards.innerHTML = "";
            fortuneMessage.innerHTML = "";

            clearInterval(timer);
            shuffleLoop();
            timer = setInterval(shuffleLoop, 90);
        }

        function restartSameReading() {
            if (selectedQuestionIndex !== null) {
                startReading(selectedQuestionIndex);
            }
        }

        function pickRandomCards(count) {
            const copied = [...cards];
            const result = [];

            for (let i = 0; i < count; i++) {
                const index = Math.floor(Math.random() * copied.length);
                const card = copied.splice(index, 1)[0];
                const direction = Math.random() < 0.5 ? "正位置" : "逆位置";
                const meaning = direction === "正位置" ? card.upright : card.reversed;

                result.push({
                    name: card.name,
                    direction: direction,
                    meaning: meaning
                });
            }

            return result;
        }

        function renderShuffleVisual() {
            const oldCards = document.querySelectorAll(".shuffle-card");
            oldCards.forEach(function(el) {
                el.remove();
            });

            const visualCount = 7;
            const phase = shuffleTick % 10;

            for (let i = 0; i < visualCount; i++) {
                const div = document.createElement("div");
                div.className = "shuffle-card";

                const spread = phase < 5 ? 1 : -1;
                const baseX = (i - 3) * 10 * spread;
                const randomX = (Math.random() - 0.5) * 52;
                const randomY = (Math.random() - 0.5) * 34;
                const liftY = i % 2 === 0 ? -14 : 14;
                const rotate = (Math.random() - 0.5) * 28 + (i - 3) * 3.2;
                const scale = 1 - i * 0.025;
                const moveSide = phase === 2 || phase === 7 ? (i % 2 === 0 ? -34 : 34) : 0;

                div.style.zIndex = String(20 + i);
                div.style.opacity = String(0.98 - i * 0.075);

                div.style.transform =
                    "translate(" +
                    (baseX + randomX + moveSide) +
                    "px, " +
                    (randomY + liftY) +
                    "px) rotate(" +
                    rotate +
                    "deg) scale(" +
                    scale +
                    ")";

                div.innerHTML =
                    '<div class="shuffle-symbol">🐾</div>' +
                    '<div class="shuffle-name">WHITE CAT</div>';

                shuffleStage.appendChild(div);
            }
        }

        function shuffleLoop() {
            currentCards = pickRandomCards(selectedQuestion.draw_count);
            renderShuffleVisual();
            shuffleTick += 1;
        }

        function stopShuffle() {
            clearInterval(timer);

            beforeArea.style.display = "none";
            resultArea.style.display = "block";
            resultCards.innerHTML = "";

            currentCards.forEach(function(card, index) {
                const label = selectedQuestion.labels[index] || "カード";
                const div = document.createElement("div");
                div.className = "result-card";

                div.innerHTML =
                    "<h3>" + label + "：" + card.name + "（" + card.direction + "）</h3>" +
                    "<p><strong>カードの意味：</strong>" + card.meaning + "</p>";

                resultCards.appendChild(div);
            });

            makeFortuneMessage();
        }

        function cardSummary(card) {
            return "「" + card.name + "（" + card.direction + "）」は、" + card.meaning + "を示します。";
        }

        function timingWord(card) {
            const name = card.name;
            if (["戦車", "太陽", "魔術師", "運命の輪"].includes(name)) {
                return "比較的早い時期に動きが出やすいでしょう。目安としては、数週間から3か月以内に小さな変化がありそうです。";
            }
            if (["節制", "星", "女帝", "力"].includes(name)) {
                return "ゆっくり育つ流れです。3か月から半年ほどかけて、自然に形になっていくでしょう。";
            }
            if (["隠者", "吊るされた男", "月", "正義"].includes(name)) {
                return "今すぐではなく、心の整理や状況の調整が先になります。半年ほどかけて見極める流れです。";
            }
            if (["塔", "死神", "悪魔"].includes(name)) {
                return "一度大きな変化や区切りを通ってから、次の流れが生まれます。焦らず、まず不要なものを手放す時期です。";
            }
            return "時期は固定されていませんが、あなたの行動次第で流れは早まります。";
        }

        function yesNoTone(card) {
            if (["太陽", "世界", "恋人", "星", "女帝", "魔術師", "運命の輪"].includes(card.name) && card.direction === "正位置") {
                return "かなり前向きな可能性があります。";
            }
            if (["塔", "悪魔", "月", "吊るされた男", "死神"].includes(card.name) && card.direction === "正位置") {
                return "今のまま進めるには注意が必要です。";
            }
            if (card.direction === "逆位置") {
                return "可能性はありますが、まだ迷いや不安定さが残っています。";
            }
            return "可能性はありますが、慎重に見極める必要があります。";
        }

        function makeSpecificReading() {
            const q = selectedQuestion.code;
            const c1 = currentCards[0];
            const c2 = currentCards[1];
            const c3 = currentCards[2];

            let html = "";
            html += "<strong>" + selectedQuestion.text + "</strong><br><br>";

            if (q === "love_destiny_person") {
                html += "運命の相手について見ます。今回のカードでは、あなたの運命の相手は、ただ刺激をくれる人というより、あなたの人生を前へ進めるきっかけを持つ人として出ています。<br><br>";
                html += "<strong>相手の人物像</strong><br>" + cardSummary(c1) + " この人は、あなたに新しい景色を見せてくれるタイプです。行動力がある、決断が早い、または自分の世界をしっかり持っている人の可能性があります。<br><br>";
                html += "<strong>出会いのきっかけ</strong><br>" + cardSummary(c2) + " 出会いは、日常の延長よりも、移動、仕事、紹介、趣味、学びの場など、あなたが少し外へ出ることで近づきます。待つより動くことでご縁が開きます。<br><br>";
                html += "<strong>あなたへの助言</strong><br>" + cardSummary(c3) + " 運命の相手は、最初から完璧な形で現れるとは限りません。白猫タロットは、条件だけで選ばず、一緒にいる時の安心感と未来へ進む力を見てくださいと伝えています。";
                return html;
            }

            if (q === "love_current_destiny") {
                html += "今の恋人が運命の相手かを見ます。結論から言うと、" + yesNoTone(c3) + " ただし、運命の相手かどうかは、好きという気持ちだけでなく、ふたりが現実を一緒に越えられるかで決まります。<br><br>";
                html += "<strong>現在のご縁</strong><br>" + cardSummary(c1) + " ふたりの間には、学び合う縁が出ています。楽しいだけではなく、価値観の違いや向き合うべき課題もあります。<br><br>";
                html += "<strong>相手の本心</strong><br>" + cardSummary(c2) + " 相手はあなたを軽く見ているわけではありません。ただ、言葉にするのが苦手だったり、将来についてまだ慎重に考えている可能性があります。<br><br>";
                html += "<strong>結ばれる可能性</strong><br>" + cardSummary(c3) + " この関係は、ふたりが本音で話せるほど強くなります。白猫タロットは、結婚や未来の話を急がず、安心して話し合える関係を育ててくださいと告げています。";
                return html;
            }

            if (q === "love_future") {
                html += "あの人との未来を見ます。今の流れでは、関係はまだ固定されていません。あなたの接し方と、あの人の心の準備によって未来が変わっていきます。<br><br>";
                html += "<strong>今の関係</strong><br>" + cardSummary(c1) + " 現在は、距離が近いようでいて、まだ見えない部分が残っています。相手の反応を急いで決めつけない方がよいでしょう。<br><br>";
                html += "<strong>あの人の気持ち</strong><br>" + cardSummary(c2) + " あの人の中には、あなたへの関心や意識があります。ただし、それがすぐ行動に出るかは別です。相手のペースを読む必要があります。<br><br>";
                html += "<strong>未来の流れ</strong><br>" + cardSummary(c3) + " 未来は、焦らなければ進展の余地があります。白猫タロットは、押すよりも、相手が安心して近づける余白を作ることが鍵だと伝えています。";
                return html;
            }

            if (q === "love_new_meeting") {
                html += "新しい出会いについて見ます。カードは、出会いの可能性はあると告げています。ただし、家の中で待っているだけでは弱く、あなたの行動範囲を広げることで運が動きます。<br><br>";
                html += "<strong>今の恋愛運</strong><br>" + cardSummary(c1) + " 今のあなたは、恋を受け取る準備を整えている段階です。過去の疲れや不安があるなら、まず心を軽くすることが大切です。<br><br>";
                html += "<strong>出会いの兆し</strong><br>" + cardSummary(c2) + " 出会いは、知人の紹介、仕事関係、趣味の場、普段と少し違う場所に出ています。偶然に見えて、実は流れがつながっているご縁です。<br><br>";
                html += "<strong>出会いを引き寄せる行動</strong><br>" + cardSummary(c3) + " 白猫タロットは、理想を下げるのではなく、まず自分を閉じないことが大切だと伝えています。小さな外出、連絡、発信が恋の入口になります。";
                return html;
            }

            if (q === "love_feelings_now" || q === "love_how_think") {
                html += "あの人の気持ちを見ます。あの人はあなたに対して無関心ではありません。ただ、気持ちの出し方には慎重さや迷いがありそうです。<br><br>";
                html += "<strong>" + selectedQuestion.labels[0] + "</strong><br>" + cardSummary(c1) + " あの人はあなたに対して、印象や存在感をしっかり感じています。表面的には平静でも、心の中ではあなたを意識している気配があります。<br><br>";
                html += "<strong>" + selectedQuestion.labels[1] + "</strong><br>" + cardSummary(c2) + " 本音の部分では、近づきたい気持ちと慎重になりたい気持ちが混ざっています。過去の経験や立場が、素直な行動を止めている可能性があります。<br><br>";
                html += "<strong>" + selectedQuestion.labels[2] + "</strong><br>" + cardSummary(c3) + " 今は相手の気持ちを試すより、安心できるやり取りを重ねる方がよいでしょう。白猫タロットは、急な駆け引きより自然な会話が心を開く鍵だと告げています。";
                return html;
            }

            if (q === "love_next_time") {
                html += "次の恋が訪れる時期を見ます。カードは、恋の流れが止まっているのではなく、準備段階にあると示しています。<br><br>";
                html += "<strong>今の状態</strong><br>" + cardSummary(c1) + " 今のあなたは、恋を求める気持ちと、少し慎重になっている心が同居しています。過去の疲れを整えるほど、新しい恋は入りやすくなります。<br><br>";
                html += "<strong>恋が動く時期</strong><br>" + cardSummary(c2) + " " + timingWord(c2) + "<br><br>";
                html += "<strong>準備すべきこと</strong><br>" + cardSummary(c3) + " 次の恋は、あなたが自分の魅力を思い出した時に近づきます。白猫タロットは、まず日常を整え、人と会う機会を少し増やすことをすすめています。";
                return html;
            }

            if (q === "love_popular_time") {
                html += "モテ期について見ます。カードは、あなたの魅力がこれから外へ伝わりやすくなる流れを示しています。<br><br>";
                html += "<strong>今の魅力</strong><br>" + cardSummary(c1) + " 今のあなたには、自然な魅力があります。ただ、自分ではまだそれを十分に信じきれていないかもしれません。<br><br>";
                html += "<strong>モテ期の兆し</strong><br>" + cardSummary(c2) + " " + timingWord(c2) + " 人から声をかけられる、連絡が増える、褒められるなど、小さなサインから始まりそうです。<br><br>";
                html += "<strong>魅力を高める鍵</strong><br>" + cardSummary(c3) + " 白猫タロットは、無理に誰かに合わせるより、あなたらしさを整えることが一番の開運になると伝えています。";
                return html;
            }

            if (q === "love_interest") {
                html += "あの人があなたに気があるかを見ます。結論として、" + yesNoTone(c2) + " ただし、相手の気持ちはまだ分かりやすく表に出ていないようです。<br><br>";
                html += "<strong>あの人の意識</strong><br>" + cardSummary(c1) + " あの人はあなたの存在を意識しています。完全に恋愛感情と断定するには早いですが、気になる相手として見ている可能性があります。<br><br>";
                html += "<strong>隠れた感情</strong><br>" + cardSummary(c2) + " 心の奥には、近づきたい気持ち、様子を見たい気持ち、迷いのいずれかが出ています。相手はまだ決めきれていません。<br><br>";
                html += "<strong>距離を縮める鍵</strong><br>" + cardSummary(c3) + " 今は重い確認より、軽い会話や自然な接点を増やすことが大切です。白猫タロットは、相手が安心できる空気を作るほど進展しやすいと告げています。";
                return html;
            }

            if (q === "love_other_person") {
                html += "あの人にほかに好きな人がいるかを見ます。カードは、あの人の心が完全にひとつに定まっているわけではない可能性を示しています。ただし、すぐに第三者がいると決めつける必要はありません。<br><br>";
                html += "<strong>あの人の心の向き</strong><br>" + cardSummary(c1) + " あの人の心には、恋愛以外の悩みや迷いも入り込んでいるようです。あなたへの気持ちだけでなく、生活や過去の影響もありそうです。<br><br>";
                html += "<strong>周囲の影響</strong><br>" + cardSummary(c2) + " 周囲の人間関係や過去の相手が、あの人の判断に影響している可能性があります。ただ、それが本命の存在とは限りません。<br><br>";
                html += "<strong>あなたへの助言</strong><br>" + cardSummary(c3) + " 白猫タロットは、不安から相手を追い詰めるより、相手の行動を静かに見ることが必要だと伝えています。言葉より行動に答えが出ます。";
                return html;
            }

            if (q === "marriage_when") {
                html += "結婚の時期を見ます。カードは、結婚運がないのではなく、今は結婚に向けて現実を整える段階だと示しています。<br><br>";
                html += "<strong>今の結婚運</strong><br>" + cardSummary(c1) + " 今のあなたは、結婚に対する意識が高まっています。ただし、理想だけではなく、現実の生活をどう整えるかが大切です。<br><br>";
                html += "<strong>結婚が近づく時期</strong><br>" + cardSummary(c2) + " " + timingWord(c2) + " 出会い、話し合い、関係の節目が結婚運を動かします。<br><br>";
                html += "<strong>今から整えること</strong><br>" + cardSummary(c3) + " 白猫タロットは、結婚相手を探す前に、安心して暮らせる土台を整えることが近道だと伝えています。";
                return html;
            }

            if (q === "marriage_with_person") {
                html += "あの人との結婚が幸せかを見ます。結論として、" + yesNoTone(c3) + " 幸せになるには、好きという気持ちだけでなく、話し合いと現実的な歩み寄りが必要です。<br><br>";
                html += "<strong>ふたりの相性</strong><br>" + cardSummary(c1) + " ふたりには惹かれ合う要素があります。ただし、違いを面白がれるか、負担に感じるかで未来が変わります。<br><br>";
                html += "<strong>結婚後の課題</strong><br>" + cardSummary(c2) + " 結婚後は、お金、生活ペース、家族との関わり、感情表現に課題が出やすいでしょう。先に話しておくことが大切です。<br><br>";
                html += "<strong>幸せに進む鍵</strong><br>" + cardSummary(c3) + " 白猫タロットは、曖昧に進めず、将来の話を穏やかに共有することが幸せへの鍵だと告げています。";
                return html;
            }

            if (q === "marriage_current_partner") {
                html += "今の恋人を結婚相手として選んでよいかを見ます。カードは、感情だけで決めず、生活を共にした時の安心感を見てくださいと伝えています。<br><br>";
                html += "<strong>現在の関係</strong><br>" + cardSummary(c1) + " 今の関係には、愛情と同時に見極めるべき点があります。楽しい時だけでなく、問題が起きた時の態度を見てください。<br><br>";
                html += "<strong>結婚相手としての可能性</strong><br>" + cardSummary(c2) + " " + yesNoTone(c2) + " ただし、相手に任せきりにせず、ふたりで現実を作る意識が必要です。<br><br>";
                html += "<strong>見極めるポイント</strong><br>" + cardSummary(c3) + " 白猫タロットは、相手があなたを大切にする言葉だけでなく、行動で安心をくれるかを見てくださいと告げています。";
                return html;
            }

            if (q === "marriage_needed") {
                html += "結婚に向けて今必要なことを見ます。カードは、結婚運を高めるには、心の準備と現実的な準備の両方が必要だと示しています。<br><br>";
                html += "<strong>今の課題</strong><br>" + cardSummary(c1) + " 今は、理想と現実のすり合わせが必要です。どんな結婚をしたいのか、譲れない条件を整理しましょう。<br><br>";
                html += "<strong>必要な準備</strong><br>" + cardSummary(c2) + " お金、住まい、仕事、家族観など、現実的な話を避けないことが結婚運を上げます。<br><br>";
                html += "<strong>未来への助言</strong><br>" + cardSummary(c3) + " 白猫タロットは、焦って相手を選ぶより、安心して長く続く関係を選ぶことが幸せへの近道だと伝えています。";
                return html;
            }

            if (q === "reunion_possible") {
                html += "復縁できるかを見ます。結論として、" + yesNoTone(c3) + " ただし、ただ戻るだけではなく、別れの原因を越えることが条件になります。<br><br>";
                html += "<strong>別れの原因</strong><br>" + cardSummary(c1) + " 過去には、すれ違い、我慢、誤解、タイミングの悪さがあったようです。ここを見ないまま戻ると同じことを繰り返しやすいです。<br><br>";
                html += "<strong>あの人の現在</strong><br>" + cardSummary(c2) + " あの人は完全に忘れているわけではありません。ただし、今すぐ素直に戻る準備があるとは限りません。<br><br>";
                html += "<strong>復縁の可能性</strong><br>" + cardSummary(c3) + " 白猫タロットは、連絡を急ぐより、自分の心を整えてから動く方が復縁の可能性を上げると伝えています。";
                return html;
            }

            if (q === "reunion_move_on") {
                html += "次の恋に進むべきかを見ます。カードは、あなたが過去を大切にしながらも、新しい幸せを受け取る準備に入っていると示しています。<br><br>";
                html += "<strong>今の未練</strong><br>" + cardSummary(c1) + " まだ心に残っているものがあります。それは愛情だけでなく、後悔や納得できなかった気持ちかもしれません。<br><br>";
                html += "<strong>新しい恋の可能性</strong><br>" + cardSummary(c2) + " 新しい恋の可能性はあります。過去の人と比べすぎなければ、あなたを穏やかに大切にしてくれる相手が入ってきます。<br><br>";
                html += "<strong>あなたへの助言</strong><br>" + cardSummary(c3) + " 白猫タロットは、忘れようと無理をするより、自分が幸せになる方へ少しずつ向きを変えてくださいと告げています。";
                return html;
            }

            if (q === "reunion_new_partner") {
                html += "あの人に新しいパートナーがいるかを見ます。カードは、あの人の周囲に恋愛の気配や人間関係の動きがある可能性を示しています。ただし、確定ではありません。<br><br>";
                html += "<strong>あの人の現在</strong><br>" + cardSummary(c1) + " あの人は今、自分の生活や気持ちを立て直している段階に見えます。恋愛だけに集中しているとは限りません。<br><br>";
                html += "<strong>恋愛状況の気配</strong><br>" + cardSummary(c2) + " 誰かの存在が気になるカードではありますが、それが深い関係か、一時的な関わりかはまだ不安定です。<br><br>";
                html += "<strong>あなたが取るべき距離</strong><br>" + cardSummary(c3) + " 白猫タロットは、相手の状況を探りすぎると心が削られると伝えています。まずは自分の心を守りながら、静かに様子を見ることです。";
                return html;
            }

            if (q === "reunion_wants") {
                html += "あの人が復縁を望んでいるかを見ます。カードは、あの人の中に過去を思い出す気持ちはあるものの、すぐに行動へ移すほど整理できていない可能性を示しています。<br><br>";
                html += "<strong>あの人の本音</strong><br>" + cardSummary(c1) + " あの人はあなたとの時間を完全に否定していません。心のどこかで思い出している気配があります。<br><br>";
                html += "<strong>復縁への迷い</strong><br>" + cardSummary(c2) + " 迷いの原因は、過去の問題、プライド、今の状況、または再び傷つく不安です。<br><br>";
                html += "<strong>関係を動かす鍵</strong><br>" + cardSummary(c3) + " 白猫タロットは、責める言葉より、落ち着いた連絡や自然なきっかけが復縁の扉を開くと伝えています。";
                return html;
            }

            if (q === "reunion_regret") {
                html += "あの人に未練があるかを見ます。カードは、あの人の中にまだ完全には消えていない感情があると示しています。ただし、それを素直に認めているとは限りません。<br><br>";
                html += "<strong>残っている感情</strong><br>" + cardSummary(c1) + " あの人には、あなたを思い出す瞬間があります。寂しさ、後悔、懐かしさが混ざっているようです。<br><br>";
                html += "<strong>素直になれない理由</strong><br>" + cardSummary(c2) + " プライドや過去の傷が、あの人の行動を止めています。気持ちがあっても、すぐに連絡できない状態です。<br><br>";
                html += "<strong>今後の可能性</strong><br>" + cardSummary(c3) + " 白猫タロットは、未練を復縁に変えるには時間と安心感が必要だと伝えています。急がず、相手が向き合える空気を作ることです。";
                return html;
            }

            if (q === "reunion_meet_again") {
                html += "あの人と再会できるかを見ます。カードは、完全に縁が切れたというより、今は距離や状況に隔てられていると示しています。<br><br>";
                html += "<strong>再会の可能性</strong><br>" + cardSummary(c1) + " 再会の可能性は残っています。ただし偶然任せでは弱く、何らかのきっかけやタイミングが必要です。<br><br>";
                html += "<strong>障害になっているもの</strong><br>" + cardSummary(c2) + " 障害は、気まずさ、誤解、相手の環境、あなた自身の不安に出ています。無理に突破しようとすると逆効果です。<br><br>";
                html += "<strong>未来への助言</strong><br>" + cardSummary(c3) + " 白猫タロットは、再会を願うなら、重い感情をぶつけるより、穏やかな接点を作ることが大切だと告げています。";
                return html;
            }

            if (q === "secret_continue") {
                html += "この恋を続けてよいかを見ます。カードは、この恋に強い感情がある一方で、あなたの心が消耗しやすい流れも示しています。<br><br>";
                html += "<strong>今の気持ち</strong><br>" + cardSummary(c1) + " あなたの気持ちは本物です。ただし、好きだからこそ苦しさを我慢してしまっている可能性があります。<br><br>";
                html += "<strong>この恋の危うさ</strong><br>" + cardSummary(c2) + " この関係には、秘密、待つ時間、約束の曖昧さが影を落としています。相手の都合に合わせすぎると心が削られます。<br><br>";
                html += "<strong>あなたを守る助言</strong><br>" + cardSummary(c3) + " 白猫タロットは、続けるなら期限と境界線を持つこと、苦しさが愛情を上回るなら一度立ち止まることを伝えています。";
                return html;
            }

            if (q === "secret_serious") {
                html += "既婚者のあの人が本気かを見ます。カードは、気持ちはあるかもしれませんが、それを現実の行動に変えられるかは別問題だと示しています。<br><br>";
                html += "<strong>あの人の本音</strong><br>" + cardSummary(c1) + " あの人の中には、あなたへの惹かれる気持ちがあります。ただし、気持ちの強さと責任を取る覚悟は同じではありません。<br><br>";
                html += "<strong>行動と現実</strong><br>" + cardSummary(c2) + " 現実のカードは重めです。言葉では甘くても、行動が伴っているかを冷静に見る必要があります。<br><br>";
                html += "<strong>あなたが見るべき真実</strong><br>" + cardSummary(c3) + " 白猫タロットは、あの人の言葉より、あなたを不安にさせない行動があるかを見てくださいと告げています。";
                return html;
            }

            if (q === "secret_future") {
                html += "この関係の未来を見ます。カードは、未来がまったくないとは言いませんが、今のままでは曖昧さが続きやすいと示しています。<br><br>";
                html += "<strong>現在の関係</strong><br>" + cardSummary(c1) + " 今は感情でつながっている一方、現実面の不安定さがあります。幸せと不安が交互に来やすい関係です。<br><br>";
                html += "<strong>隠れている問題</strong><br>" + cardSummary(c2) + " 隠れている問題は、相手の決断力、周囲への責任、あなたの待つ時間です。ここを曖昧にすると苦しさが長引きます。<br><br>";
                html += "<strong>未来の行方</strong><br>" + cardSummary(c3) + " 白猫タロットは、未来を望むなら、相手の言葉ではなく具体的な行動と期限を見ることが必要だと伝えています。";
                return html;
            }

            if (q === "secret_choose") {
                html += "あの人が家庭とあなたのどちらを選ぶかを見ます。カードは、あの人が迷いを抱えている一方で、現実を大きく変えることには慎重であると示しています。<br><br>";
                html += "<strong>あの人の迷い</strong><br>" + cardSummary(c1) + " あの人の心には揺れがあります。あなたに惹かれる気持ちはあっても、簡単に決断できる状態ではありません。<br><br>";
                html += "<strong>現実の重さ</strong><br>" + cardSummary(c2) + " 家庭、責任、世間体、生活の安定が大きく影響しています。気持ちだけで動けない現実があります。<br><br>";
                html += "<strong>あなたへの助言</strong><br>" + cardSummary(c3) + " 白猫タロットは、選ばれることを待ち続けるより、あなた自身が幸せを選ぶ立場に戻ることが大切だと告げています。";
                return html;
            }

            if (q === "secret_leave") {
                html += "この恋から離れるべきかを見ます。カードは、あなたの心がかなり疲れている可能性を示しています。離れることは負けではなく、自分を守る選択になる場合があります。<br><br>";
                html += "<strong>心の執着</strong><br>" + cardSummary(c1) + " この恋には強い引力があります。ただ、その引力が安心より苦しさを増やしていないか見つめてください。<br><br>";
                html += "<strong>離れることで得るもの</strong><br>" + cardSummary(c2) + " 離れることで、心の静けさ、自分の時間、自尊心を取り戻せる可能性があります。<br><br>";
                html += "<strong>次に進む力</strong><br>" + cardSummary(c3) + " 白猫タロットは、急に忘れなくてよいと伝えています。ただ、自分を傷つける場所から少しずつ離れる勇気は必要です。";
                return html;
            }

            if (q === "money_income") {
                html += "今後の収入について見ます。カードは、収入が急に大きく変わるというより、行動の積み重ねで流れが安定していくと示しています。<br><br>";
                html += "<strong>現在の金運</strong><br>" + cardSummary(c1) + " 今は収支の見直しが必要な時期です。入ってくるお金だけでなく、出ていくお金の流れも整えましょう。<br><br>";
                html += "<strong>収入の流れ</strong><br>" + cardSummary(c2) + " 収入は、仕事の工夫、副業、継続している努力から伸びる可能性があります。一発逆転より積み上げ型です。<br><br>";
                html += "<strong>増やすための行動</strong><br>" + cardSummary(c3) + " 白猫タロットは、得意なことをお金につなげる準備をしてくださいと伝えています。小さく始めて数字を見ることが開運です。";
                return html;
            }

            if (q === "money_increase") {
                html += "お金を増やすために今すべきことを見ます。カードは、感覚だけで動くより、仕組みを作ることが大切だと示しています。<br><br>";
                html += "<strong>今の課題</strong><br>" + cardSummary(c1) + " 今の課題は、お金の流れを見える形にすることです。何に使い、何が残るのかを把握しましょう。<br><br>";
                html += "<strong>伸ばすべき力</strong><br>" + cardSummary(c2) + " 伸ばすべき力は、継続力、発信力、交渉力、または専門性です。今あるものを磨くことで収入に変わります。<br><br>";
                html += "<strong>金運アップの鍵</strong><br>" + cardSummary(c3) + " 白猫タロットは、浪費を責めるより、お金が残る仕組みを作ることが大切だと告げています。";
                return html;
            }

            if (q === "money_invest") {
                html += "投資や大きな買い物をしてよい時期かを見ます。カードは、勢いだけで決めるのは避け、情報確認と余裕資金を重視するべきだと示しています。<br><br>";
                html += "<strong>現在の判断力</strong><br>" + cardSummary(c1) + " 今は気持ちが前のめりになりやすい可能性があります。欲しい理由と必要な理由を分けて考えてください。<br><br>";
                html += "<strong>注意すべきこと</strong><br>" + cardSummary(c2) + " 見落とし、焦り、周囲の雰囲気に流されることに注意が必要です。損を取り返そうとする判断は避けましょう。<br><br>";
                html += "<strong>安全な進め方</strong><br>" + cardSummary(c3) + " 白猫タロットは、小さく試す、期限を置く、比較する、この3つを守ることで金運を守れると伝えています。";
                return html;
            }

            if (q === "money_sidejob") {
                html += "仕事や副業で収入が増えるかを見ます。カードは、可能性ありと出ています。ただし、すぐ大きく稼ぐより、続けられる形を作ることが大切です。<br><br>";
                html += "<strong>仕事運</strong><br>" + cardSummary(c1) + " 今の仕事運は、工夫次第で伸ばせる状態です。今までの経験や得意分野が収入につながります。<br><br>";
                html += "<strong>副業の可能性</strong><br>" + cardSummary(c2) + " 副業は、あなたの知識、販売、発信、制作、サービス提供と相性が出ています。小さく始めて改善する形が合っています。<br><br>";
                html += "<strong>収入につなげる行動</strong><br>" + cardSummary(c3) + " 白猫タロットは、完璧に準備してからではなく、まず小さく出して反応を見ることが金運を動かすと伝えています。";
                return html;
            }

            if (q === "money_anxiety") {
                html += "お金の不安が解消されるかを見ます。カードは、不安は少しずつ軽くなると示しています。ただし、気持ちだけでなく、具体的な管理が必要です。<br><br>";
                html += "<strong>不安の原因</strong><br>" + cardSummary(c1) + " 不安の原因は、先が見えないこと、支出の読みにくさ、または収入の波にあります。まず見える化が必要です。<br><br>";
                html += "<strong>流れが変わる兆し</strong><br>" + cardSummary(c2) + " 流れは変わり始めます。小さな入金、仕事の変化、節約の成果など、安心材料が出てくるでしょう。<br><br>";
                html += "<strong>安心に近づく方法</strong><br>" + cardSummary(c3) + " 白猫タロットは、ひとりで抱え込まず、数字で確認することが不安を小さくすると伝えています。";
                return html;
            }

            if (q === "money_chance") {
                html += "臨時収入やチャンスについて見ます。カードは、予想外の形で小さなチャンスが入る可能性を示しています。<br><br>";
                html += "<strong>金運の動き</strong><br>" + cardSummary(c1) + " 金運は停滞ではなく、動きがあります。拾えるチャンスを見逃さないことが大切です。<br><br>";
                html += "<strong>チャンスの場所</strong><br>" + cardSummary(c2) + " チャンスは、人からの話、仕事の依頼、不要品の整理、過去のつながりから来やすいでしょう。<br><br>";
                html += "<strong>受け取るための準備</strong><br>" + cardSummary(c3) + " 白猫タロットは、すぐ動ける状態にしておくことが金運をつかむ鍵だと伝えています。情報、時間、気持ちの余白を作ってください。";
                return html;
            }

            return "白猫タロットが、今のあなたに必要な流れを読み解きました。カードが示す意味を、焦らず受け取ってください。";
        }

        function makeFortuneMessage() {
            fortuneMessage.innerHTML = makeSpecificReading();
        }
    </script>
</body>
</html>
"""

html_code = html_code.replace("__CARDS_JSON__", cards_json)
html_code = html_code.replace("__MENUS_JSON__", menus_json)

components.html(html_code, height=1040, scrolling=True)

st.caption("※この占いは娯楽・自己理解を目的としたものです。大切な判断は、現実の状況やご自身の安全を最優先にしてください。")