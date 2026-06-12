const tarotCards = [
{
name: "愚者",
image: "cards/00_fool.png",
upright: {
meaning: "自由、新しい始まり、可能性、軽やかな一歩。",
message: "今のあなたには、まだ形になっていない可能性が広がっています。完璧な準備を待つより、小さく始めることで流れが動き出しそうです。",
advice: "今日は考えすぎず、まず一歩だけ動いてみましょう。小さな挑戦が、次の扉を開く鍵になります。"
},
reversed: {
meaning: "迷い、準備不足、無計画、落ち着きのなさ。",
message: "気持ちが先に走りすぎて、足元が少し見えにくくなっているかもしれません。焦らなくても大丈夫です。",
advice: "今日は大きな決断より、情報整理を優先しましょう。持ち物、予定、気持ちを整えると進みやすくなります。"
}
},
{
name: "魔術師",
image: "cards/01_magician.png",
upright: {
meaning: "始動、才能、工夫、言葉の力。",
message: "あなたの中には、すでに使える力や材料があります。今はそれを組み合わせて、形にしていくタイミングです。",
advice: "思いついたことをメモし、今日できる小さな作業に変えてください。言葉にすると現実が動きやすくなります。"
},
reversed: {
meaning: "自信不足、空回り、言葉の行き違い。",
message: "できることはあるのに、自分で可能性を小さく見積もっているかもしれません。焦って見せようとしなくて大丈夫です。",
advice: "今日は無理に完璧に見せず、正直に伝えることを意識しましょう。言葉を整えるだけで流れが変わります。"
}
},
{
name: "女教皇",
image: "cards/02_high_priestess.png",
upright: {
meaning: "直感、静けさ、知性、内面の声。",
message: "答えは外側より、あなたの内側に静かにあります。すぐに動くより、感じていることを丁寧に見つめる時です。",
advice: "今日はひとりで落ち着ける時間を作りましょう。違和感や安心感を大切にしてください。"
},
reversed: {
meaning: "考えすぎ、秘密、不安、心の閉じこもり。",
message: "本当はわかっている気持ちに、ふたをしている可能性があります。不安が大きい時ほど、答えを急がなくて大丈夫です。",
advice: "今日は誰かの意見を集めすぎないこと。静かな場所で、自分の本音を一つだけ書き出してみましょう。"
}
},
{
name: "女帝",
image: "cards/03_empress.png",
upright: {
meaning: "愛情、豊かさ、育てる力、安心感。",
message: "あなたのやさしさや魅力が、周囲に穏やかな影響を与えています。今は無理に急がず、育てることに運があります。",
advice: "今日は自分にも人にも、少し甘いくらいで大丈夫。心地よいものを選ぶと運気が整います。"
},
reversed: {
meaning: "甘やかしすぎ、依存、疲れ、満たされなさ。",
message: "誰かのために頑張りすぎて、自分の心が置いてきぼりになっているかもしれません。",
advice: "今日は人に与える前に、自分を満たしましょう。休むことも立派な選択です。"
}
},
{
name: "皇帝",
image: "cards/04_emperor.png",
upright: {
meaning: "安定、責任、計画、現実的な力。",
message: "今は感覚だけでなく、計画を立てることで安心が増える時です。土台を整えるほど、願いが現実に近づきます。",
advice: "今日は予定、予算、手順を見直しましょう。紙に書くと頭の中がすっきりします。"
},
reversed: {
meaning: "頑固、支配、不安定、責任の重さ。",
message: "全部を自分で背負おうとして、少し力が入りすぎているかもしれません。",
advice: "今日は一つだけ人に頼ることを考えてみましょう。柔らかさが状況を動かします。"
}
},
{
name: "教皇",
image: "cards/05_hierophant.png",
upright: {
meaning: "信頼、学び、伝統、助言。",
message: "信頼できる人や、長く続いている方法にヒントがあります。ひとりで抱えず、知恵を借りるとよさそうです。",
advice: "今日は経験者の話を聞いたり、基本に戻ったりしてみましょう。王道の中に答えがあります。"
},
reversed: {
meaning: "思い込み、形式へのこだわり、窮屈さ。",
message: "常識や周りの期待に合わせすぎて、あなたらしい答えが見えにくくなっているかもしれません。",
advice: "今日は『本当にそうしなければいけない？』と一度問い直してみましょう。"
}
},
{
name: "恋人",
image: "cards/06_lovers.png",
upright: {
meaning: "選択、愛、調和、ときめき。",
message: "心が自然に向かうものの中に、今のあなたに必要な答えがあります。義務感より、納得感を大切にするとよさそうです。",
advice: "今日は好き・心地よい・安心する、という感覚を信じて選んでみましょう。"
},
reversed: {
meaning: "迷い、不一致、優柔不断、気持ちのすれ違い。",
message: "心ではわかっているのに、迷いが選択を難しくしているかもしれません。すぐに白黒つけなくても大丈夫です。",
advice: "今日は相手や周囲ではなく、自分が何を望むかを先に確認しましょう。"
}
},
{
name: "戦車",
image: "cards/07_chariot.png",
upright: {
meaning: "前進、行動、勝負、勢い。",
message: "今は流れが動きやすい時です。迷いを抱えたままでも、進みながら整えていけます。",
advice: "今日はひとつ行動を起こしてください。連絡する、申し込む、片付けるなど、具体的な一歩が吉です。"
},
reversed: {
meaning: "暴走、焦り、方向のずれ、疲れ。",
message: "頑張りたい気持ちはあるのに、進む方向が少し散らかっているかもしれません。",
advice: "今日はスピードを落として、優先順位を一つに絞りましょう。"
}
},
{
name: "力",
image: "cards/08_strength.png",
upright: {
meaning: "やさしい強さ、忍耐、信頼、内なる勇気。",
message: "今のあなたには、静かに乗り越える力があります。強く押すより、やさしく続けることが状況を変えます。",
advice: "今日は無理に勝とうとせず、落ち着いて続けることを選びましょう。"
},
reversed: {
meaning: "自信低下、我慢の限界、不安、消耗。",
message: "自分を責める気持ちが強くなっているかもしれません。弱さがあるからダメなのではなく、休息が必要なだけです。",
advice: "今日は自分に厳しい言葉を使わないこと。心が少し楽になる選択をしてください。"
}
},
{
name: "隠者",
image: "cards/09_hermit.png",
upright: {
meaning: "内省、探求、慎重さ、本質を見る力。",
message: "今はにぎやかな場所より、静かな時間の中に答えがあります。急ぐほど見えにくくなるので、ゆっくりで大丈夫です。",
advice: "今日は一人で考える時間を作り、必要なことと不要なことを分けてみましょう。"
},
reversed: {
meaning: "孤立、考え込みすぎ、視野の狭さ。",
message: "一人で抱え込みすぎて、答えが重たくなっている可能性があります。",
advice: "今日は信頼できる人に一言だけ話してみましょう。言葉にすると軽くなります。"
}
},
{
name: "運命の輪",
image: "cards/10_wheel_of_fortune.png",
upright: {
meaning: "転機、流れ、タイミング、チャンス。",
message: "状況が少しずつ動き始めています。思いがけない変化も、後から見ると必要な流れだったと感じられそうです。",
advice: "今日は変化を怖がりすぎず、来た話や誘いを一度受け止めてみましょう。"
},
reversed: {
meaning: "停滞、タイミングのずれ、流れに乗れない感覚。",
message: "今は無理に動かそうとしても、少し噛み合いにくいかもしれません。止まっている時間にも意味があります。",
advice: "今日は急いで結論を出さず、準備と調整に使いましょう。"
}
},
{
name: "正義",
image: "cards/11_justice.png",
upright: {
meaning: "公平、判断、バランス、誠実さ。",
message: "感情だけでなく、事実を見つめることで答えがはっきりしてきます。誠実な選択があなたを守ります。",
advice: "今日はメリットとデメリットを書き出しましょう。冷静に見るほど迷いが減ります。"
},
reversed: {
meaning: "偏り、不公平、判断ミス、納得できない気持ち。",
message: "どこかで無理に納得しようとしている可能性があります。心の中の違和感を無視しないでください。",
advice: "今日はすぐ決めず、事実確認をしましょう。曖昧なまま進めないことが大切です。"
}
},
{
name: "吊るされた男",
image: "cards/12_hanged_man.png",
upright: {
meaning: "待つこと、視点の転換、手放し、学び。",
message: "今は無理に動かすより、見方を変えることで道が見えてきます。止まっているようで、内側では大切な変化が起きています。",
advice: "今日は結論を急がず、別の角度から考えてみましょう。待つことも前進です。"
},
reversed: {
meaning: "報われない我慢、停滞、執着、疲れ。",
message: "必要以上に我慢していることがあるかもしれません。続けることだけが正解ではありません。",
advice: "今日は手放していい負担を一つ探してみましょう。"
}
},
{
name: "死神",
image: "cards/13_death.png",
upright: {
meaning: "終わりと始まり、区切り、再生、整理。",
message: "何かを終わらせることで、新しい流れが入ってきます。怖いカードではなく、古い殻を脱ぐ合図です。",
advice: "今日は不要なもの、続けなくていい習慣を一つ手放してみましょう。"
},
reversed: {
meaning: "変化への抵抗、未練、先延ばし。",
message: "本当は変えたいことを、まだ抱えたままにしているかもしれません。急に全部変えなくても大丈夫です。",
advice: "今日は小さな整理から始めましょう。まずは一つだけ終わらせること。"
}
},
{
name: "節制",
image: "cards/14_temperance.png",
upright: {
meaning: "調和、回復、自然な流れ、ほどよさ。",
message: "今は無理なく整えていくことが大切です。急激な変化より、少しずつ混ぜ合わせるような進み方が合っています。",
advice: "今日は睡眠、食事、予定のバランスを整えましょう。ほどほどが幸運を呼びます。"
},
reversed: {
meaning: "乱れ、無理、不調和、偏り。",
message: "生活や気持ちのバランスが少し崩れているかもしれません。頑張る前に整えることが必要です。",
advice: "今日は予定を詰め込みすぎないこと。余白を作ると心も戻ってきます。"
}
},
{
name: "悪魔",
image: "cards/15_devil.png",
upright: {
meaning: "執着、誘惑、依存、見ないふり。",
message: "やめたいのに気になること、離れたいのに離れにくいものがあるかもしれません。まず気づくことが第一歩です。",
advice: "今日は自分を責めず、繰り返しているパターンを一つ観察してみましょう。"
},
reversed: {
meaning: "解放、悪習慣からの離脱、目覚め。",
message: "あなたは少しずつ、縛られていたものから離れ始めています。完全でなくても、変化はもう始まっています。",
advice: "今日は距離を置きたいものから、ほんの少し離れてみましょう。"
}
},
{
name: "塔",
image: "cards/16_tower.png",
upright: {
meaning: "急な変化、気づき、崩れる古い土台。",
message: "思い通りでない出来事が、実は本音に気づくきっかけになるかもしれません。壊れるものは、作り直せます。",
advice: "今日は予定外のことに慌てすぎず、まず安全な場所に立ち戻りましょう。"
},
reversed: {
meaning: "変化の回避、小さな揺れ、先延ばし。",
message: "大きな変化を避けるために、小さなサインが出ている可能性があります。今なら穏やかに整えられます。",
advice: "今日は気になっていた問題を一つだけ直しましょう。小さな修正が大きな安心につながります。"
}
},
{
name: "星",
image: "cards/17_star.png",
upright: {
meaning: "希望、癒し、未来への光、素直さ。",
message: "少し先に、明るい可能性が見えています。今は完璧でなくても、あなたの中の希望を消さないことが大切です。",
advice: "今日は未来の楽しみを一つ決めましょう。小さな希望が心を回復させます。"
},
reversed: {
meaning: "希望を見失う、不安、理想疲れ。",
message: "理想と現実の差に疲れているかもしれません。でも、光が消えたわけではありません。",
advice: "今日は大きな夢より、今日できる安心を一つ選びましょう。"
}
},
{
name: "月",
image: "cards/18_moon.png",
upright: {
meaning: "不安、想像、曖昧さ、夢。",
message: "まだ全体がはっきり見えていない時です。不安が強いほど、事実と想像を分けることが大切になります。",
advice: "今日は夜に考えすぎないこと。気になることは紙に書いて、明るい時間に見直しましょう。"
},
reversed: {
meaning: "不安が晴れる、真実が見え始める、誤解の解消。",
message: "ぼんやりしていたことが、少しずつ見え始めています。焦らず確認すれば大丈夫です。",
advice: "今日は曖昧なことを一つ確認しましょう。聞く、調べる、見直すが助けになります。"
}
},
{
name: "太陽",
image: "cards/19_sun.png",
upright: {
meaning: "喜び、成功、明るさ、素直な表現。",
message: "明るい流れが入っています。あなたらしさを隠さず出すことで、良い反応が返ってきやすい日です。",
advice: "今日は笑顔で伝えることを意識しましょう。シンプルで明るい行動が運を呼びます。"
},
reversed: {
meaning: "元気不足、素直になれない、小さな停滞。",
message: "本来の明るさが少し雲に隠れているだけです。無理に元気に見せなくても大丈夫です。",
advice: "今日は体を温めたり、外の光を浴びたりして、心を少しずつ起こしましょう。"
}
},
{
name: "審判",
image: "cards/20_judgement.png",
upright: {
meaning: "復活、再挑戦、目覚め、知らせ。",
message: "過去に止まっていたことが、もう一度動き出す可能性があります。諦めたことにも新しい形がありそうです。",
advice: "今日は昔のメモ、連絡先、計画を見直してみましょう。再開のヒントがあります。"
},
reversed: {
meaning: "ためらい、過去へのこだわり、決断の遅れ。",
message: "もう進めるのに、自分でブレーキをかけている可能性があります。過去を責めなくて大丈夫です。",
advice: "今日は『次にどうするか』だけを考えましょう。過去の答え合わせは少し休んでください。"
}
},
{
name: "世界",
image: "cards/21_world.png",
upright: {
meaning: "完成、達成、統合、次のステージ。",
message: "ひとつの流れがまとまりつつあります。ここまでの経験は無駄ではなく、次の場所へ進む土台になっています。",
advice: "今日はできたことを認めましょう。一区切りをつけると、新しい扉が開きます。"
},
reversed: {
meaning: "未完成、あと一歩、区切りがつかない状態。",
message: "ゴールは近いのに、最後の整理が残っているかもしれません。焦らず仕上げれば大丈夫です。",
advice: "今日は途中のままになっていることを一つ終わらせましょう。小さな完了が運を整えます。"
}
}
];

const homeScreen = document.getElementById("homeScreen");
const shuffleScreen = document.getElementById("shuffleScreen");
const resultScreen = document.getElementById("resultScreen");

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const againBtn = document.getElementById("againBtn");

const resultCardImage = document.getElementById("resultCardImage");
const cardName = document.getElementById("cardName");
const cardDirection = document.getElementById("cardDirection");
const cardMeaning = document.getElementById("cardMeaning");
const cardMessage = document.getElementById("cardMessage");
const cardAdvice = document.getElementById("cardAdvice");

let selectedCard = null;
let selectedDirection = "upright";

function showScreen(screen) {
homeScreen.classList.remove("active");
shuffleScreen.classList.remove("active");
resultScreen.classList.remove("active");
screen.classList.add("active");
window.scrollTo({ top: 0, behavior: "smooth" });
}

function pickCard() {
const cardIndex = Math.floor(Math.random() * tarotCards.length);
const isReversed = Math.random() < 0.5;

selectedCard = tarotCards[cardIndex];
selectedDirection = isReversed ? "reversed" : "upright";
}

function startReading() {
pickCard();
showScreen(shuffleScreen);
}

function stopShuffle() {
if (!selectedCard) {
pickCard();
}

const data = selectedCard[selectedDirection];
const directionText = selectedDirection === "upright" ? "正位置" : "逆位置";

resultCardImage.src = selectedCard.image;
resultCardImage.alt = selectedCard.name + "のカード";
resultCardImage.classList.toggle("reversed", selectedDirection === "reversed");

cardName.textContent = selectedCard.name;
cardDirection.textContent = directionText;
cardMeaning.textContent = data.meaning;
cardMessage.textContent = data.message;
cardAdvice.textContent = data.advice;

showScreen(resultScreen);
}

function backToHome() {
selectedCard = null;
selectedDirection = "upright";
resultCardImage.src = "";
resultCardImage.classList.remove("reversed");
showScreen(homeScreen);
}

startBtn.addEventListener("click", startReading);
stopBtn.addEventListener("click", stopShuffle);
againBtn.addEventListener("click", backToHome);
