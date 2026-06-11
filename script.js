const cards = [
  { name: '愚者', upright: '自由、始まり、可能性、冒険', reversed: '無計画、軽率、不安定、迷い' },
  { name: '魔術師', upright: '行動力、才能、創造、チャンス', reversed: '準備不足、自信のなさ、空回り' },
  { name: '女教皇', upright: '直感、冷静、知性、秘密', reversed: '考えすぎ、不安、閉鎖的' },
  { name: '女帝', upright: '愛情、豊かさ、魅力、実り', reversed: '甘え、依存、わがまま' },
  { name: '皇帝', upright: '安定、責任、リーダーシップ、現実性', reversed: '頑固、支配的、プレッシャー' },
  { name: '恋人', upright: '恋愛、選択、調和、ときめき', reversed: '迷い、優柔不断、すれ違い' },
  { name: '戦車', upright: '前進、勝利、勢い、決断', reversed: '暴走、焦り、空回り' },
  { name: '力', upright: '優しさ、忍耐、信頼、内面の強さ', reversed: '自信喪失、我慢しすぎ、不安' },
  { name: '隠者', upright: '内省、慎重、探求、答えを探す', reversed: '孤独、閉じこもり、考えすぎ' },
  { name: '運命の輪', upright: '転機、チャンス、流れの変化', reversed: '停滞、タイミングのズレ、予想外' },
  { name: '正義', upright: '公平、判断、バランス、誠実', reversed: '不公平、迷い、偏った判断' },
  { name: '吊るされた男', upright: '忍耐、視点の変化、試練、気づき', reversed: '報われない我慢、停滞、無理' },
  { name: '死神', upright: '終わりと再生、変化、区切り', reversed: '変化への抵抗、未練、停滞' },
  { name: '節制', upright: '調和、回復、自然体、バランス', reversed: '不安定、無理、乱れ' },
  { name: '悪魔', upright: '執着、誘惑、依存、本音', reversed: '解放、断ち切る、目が覚める' },
  { name: '塔', upright: '衝撃、崩壊、急な変化、目覚め', reversed: '小さな崩れ、変化を避ける、不安' },
  { name: '星', upright: '希望、癒し、未来、願い', reversed: '失望、自信不足、期待しすぎ' },
  { name: '月', upright: '不安、迷い、直感、曖昧さ', reversed: '真実が見える、不安が晴れる' },
  { name: '太陽', upright: '成功、喜び、明るさ、祝福', reversed: '一時的な不調、子どもっぽさ、油断' },
  { name: '審判', upright: '復活、決断、再スタート、気づき', reversed: '迷い、後悔、決めきれない' },
  { name: '世界', upright: '完成、達成、満足、一区切り', reversed: '未完成、中途半端、あと一歩' },
];

const menus = {
  love: {
    title: '恋愛運',
    lead: '恋にまつわる気持ちを、やさしく読み解きます。',
    questions: [
      '運命の相手はどんな人ですか？',
      '今の恋人は運命の相手ですか？',
      '新しい出会いはありますか？',
    ],
  },
  marriage: {
    title: '結婚運',
    lead: '結婚へ進む流れと、安心できるパートナー像を見ます。',
    questions: [
      'いつ結婚するのでしょうか？',
      '今の恋人を結婚相手として選んでよいですか？',
      '結婚に向けて今必要なことは何ですか？',
    ],
  },
  reunion: {
    title: '復縁',
    lead: '過去のご縁がもう一度動き出す可能性を見ていきます。',
    questions: [
      'あの人と復縁することはできますか？',
      '次の恋に進むべきですか？',
      'あの人は私との復縁を望んでいますか？',
    ],
  },
  secret: {
    title: '禁断の恋',
    lead: '心を守りながら、複雑な気持ちの流れを見ます。',
    questions: [
      'この恋を続けてもよいでしょうか？',
      'この関係に未来はありますか？',
      'この恋から離れるべきですか？',
    ],
  },
  money: {
    title: '金運',
    lead: 'お金の流れと、やさしく増やしていくヒントを探します。',
    questions: [
      '今後の収入はどうなりますか？',
      'お金を増やすために今すべきことは何ですか？',
      '臨時収入やチャンスはありますか？',
    ],
  },
};

const homePanel = document.getElementById('homePanel');
const categoryPanel = document.getElementById('categoryPanel');
const readingPanel = document.getElementById('readingPanel');
const categoryGrid = document.getElementById('categoryGrid');
const questionList = document.getElementById('questionList');
const categoryTitle = document.getElementById('categoryTitle');
const categoryLead = document.getElementById('categoryLead');
const readingTitle = document.getElementById('readingTitle');
const readingQuestion = document.getElementById('readingQuestion');
const shuffleStage = document.getElementById('shuffleStage');
const resultStage = document.getElementById('resultStage');
const resultCards = document.getElementById('resultCards');
const fortuneMessage = document.getElementById('fortuneMessage');
const beforeStage = document.getElementById('beforeStage');
const stopBtn = document.getElementById('stopBtn');

let currentCategoryKey = null;
let currentCategory = null;
let currentQuestionIndex = null;
let currentQuestion = null;
let currentCards = [];
let shuffleTimer = null;
let shuffleTick = 0;

function createCategoryButtons() {
  categoryGrid.innerHTML = '';
  Object.entries(menus).forEach(([key, item]) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'category-btn';
    btn.innerHTML = `<strong>${item.title}</strong><span>${item.lead}</span>`;
    btn.addEventListener('click', () => showCategory(key));
    categoryGrid.appendChild(btn);
  });
}

function getQuestionText(question) {
  if (typeof question === 'string') {
    return question;
  }
  if (question && typeof question === 'object' && typeof question.text === 'string') {
    return question.text;
  }
  return '';
}

function isValidQuestion(question) {
  return getQuestionText(question).trim() !== '';
}

function showCategory(key) {
  currentCategoryKey = key;
  currentCategory = menus[key];

  homePanel.classList.add('hidden');
  categoryPanel.classList.remove('hidden');
  readingPanel.classList.add('hidden');

  categoryTitle.textContent = currentCategory.title;
  categoryLead.textContent = currentCategory.lead;

  questionList.innerHTML = '';
  currentCategory.questions.forEach((question, index) => {
    if (!isValidQuestion(question)) {
      return;
    }

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'question-button';
    btn.textContent = getQuestionText(question);
    btn.addEventListener('click', () => startReading(index));
    questionList.appendChild(btn);
  });
}

function startReading(index) {
  currentQuestionIndex = index;
  currentQuestion = currentCategory.questions[index];

  categoryPanel.classList.add('hidden');
  readingPanel.classList.remove('hidden');
  beforeStage.classList.remove('hidden');
  resultStage.classList.add('hidden');

  readingTitle.textContent = currentCategory.title;
  readingQuestion.textContent = currentQuestion;

  clearInterval(shuffleTimer);
  shuffleTick = 0;
  currentCards = [];
  resultCards.innerHTML = '';
  fortuneMessage.innerHTML = '';
  shuffleStage.innerHTML = '';

  shuffleLoop();
  shuffleTimer = setInterval(shuffleLoop, 90);
}

function pickRandomCards(count) {
  const pool = [...cards];
  const result = [];
  for (let i = 0; i < count; i++) {
    const idx = Math.floor(Math.random() * pool.length);
    const card = pool.splice(idx, 1)[0];
    const direction = Math.random() < 0.5 ? '正位置' : '逆位置';
    result.push({
      name: card.name,
      direction,
      meaning: direction === '正位置' ? card.upright : card.reversed,
    });
  }
  return result;
}

function renderShuffleVisual() {
  shuffleStage.innerHTML = '';
  const visualCount = 7;
  const phase = shuffleTick % 10;
  for (let i = 0; i < visualCount; i++) {
    const token = document.createElement('div');
    token.className = 'card-token';
    const spread = phase < 5 ? 1 : -1;
    const baseX = (i - 3) * 10 * spread;
    const randomX = (Math.random() - 0.5) * 52;
    const randomY = (Math.random() - 0.5) * 32;
    const liftY = i % 2 === 0 ? -10 : 10;
    const rotate = (Math.random() - 0.5) * 28 + (i - 3) * 3.2;
    const scale = 1 - i * 0.025;
    const moveSide = phase === 2 || phase === 7 ? (i % 2 === 0 ? -28 : 28) : 0;

    token.style.zIndex = String(20 + i);
    token.style.opacity = String(0.98 - i * 0.075);
    token.style.transform = `translate(${baseX + randomX + moveSide}px, ${randomY + liftY}px) rotate(${rotate}deg) scale(${scale})`;
    shuffleStage.appendChild(token);
  }
}

function shuffleLoop() {
  currentCards = pickRandomCards(3);
  renderShuffleVisual();
  shuffleTick += 1;
}

function stopShuffle() {
  clearInterval(shuffleTimer);
  beforeStage.classList.add('hidden');
  resultStage.classList.remove('hidden');

  resultCards.innerHTML = '';
  currentCards.forEach((card, index) => {
    const label = ['第一のメッセージ', '第二のメッセージ', '第三のメッセージ'][index] || 'カード';
    const item = document.createElement('article');
    item.className = 'result-card';
    item.innerHTML = `<h3>${label}：${card.name}（${card.direction}）</h3><p><strong>意味：</strong>${card.meaning}</p>`;
    resultCards.appendChild(item);
  });

  fortuneMessage.innerHTML = makeFortuneMessage();
}

function makeFortuneMessage() {
  const first = currentCards[0];
  const second = currentCards[1];
  const third = currentCards[2];
  const summary = `「${first.name}（${first.direction}）」は ${first.meaning}、「${second.name}（${second.direction}）」は ${second.meaning}、そして「${third.name}（${third.direction}）」は ${third.meaning}。今日のあなたに必要なのは、焦らずに心の声を信じること。小さな一歩を積み重ねると、流れはやさしく開いていきます。`;
  return `<p>${summary}</p>`;
}

function backToHome() {
  clearInterval(shuffleTimer);
  homePanel.classList.remove('hidden');
  categoryPanel.classList.add('hidden');
  readingPanel.classList.add('hidden');
}

function backToCategory() {
  clearInterval(shuffleTimer);
  categoryPanel.classList.remove('hidden');
  readingPanel.classList.add('hidden');
}

function restartSameReading() {
  if (currentQuestionIndex !== null) {
    startReading(currentQuestionIndex);
  }
}

stopBtn.addEventListener('click', stopShuffle);
document.getElementById('backHomeBtn').addEventListener('click', backToHome);
document.getElementById('backCategoryBtn').addEventListener('click', backToCategory);
document.getElementById('againBtn').addEventListener('click', restartSameReading);

createCategoryButtons();
