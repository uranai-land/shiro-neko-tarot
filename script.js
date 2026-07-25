const tarotCards = [
  {
    name: "愚者",
    image: "cards/00_fool.png",
    upright: {
      meaning: "自由、新しい始まり、可能性、軽やかな一歩。",
      baseMessage: "愚者のカードは、気持ちを軽くして新しい流れに入ることを示しています。完璧な答えを待つより、小さく動くことで道が開けていきそうです。",
      advice: "考えすぎず、今日できる小さな一歩を選んでみましょう。"
    },
    reversed: {
      meaning: "迷い、準備不足、落ち着きのなさ、空回り。",
      baseMessage: "愚者の逆位置は、少し気持ちが先に走っていることを示しています。急いで決めるより、足元を整えることで安心して進めるようになります。",
      advice: "今日は大きく動かず、予定や気持ちを整理する時間を作りましょう。"
    }
  },
  {
    name: "魔術師",
    image: "cards/01_magician.png",
    upright: {
      meaning: "始まり、工夫、才能、言葉の力。",
      baseMessage: "魔術師のカードは、あなたの中にすでに使える力があることを示しています。言葉にする、形にする、試してみることで運が動き始めます。",
      advice: "思いついたことを一つ、紙に書いたり誰かに伝えたりしてみましょう。"
    },
    reversed: {
      meaning: "自信不足、空回り、準備不足、伝え方のずれ。",
      baseMessage: "魔術師の逆位置は、力はあるのにうまく出せていない状態を示しています。焦って見せようとするより、整えてから伝えるとよさそうです。",
      advice: "今日は無理に完璧に見せず、正直でわかりやすい言葉を選びましょう。"
    }
  },
  {
    name: "女教皇",
    image: "cards/02_high_priestess.png",
    upright: {
      meaning: "直感、静けさ、知性、内面の声。",
      baseMessage: "女教皇のカードは、静かな時間の中に答えがあることを示しています。外の声に振り回されず、自分の感覚を丁寧に見つめるとよさそうです。",
      advice: "今日はひとりで落ち着ける時間を少し作りましょう。"
    },
    reversed: {
      meaning: "考えすぎ、不安、心の閉じこもり、迷い。",
      baseMessage: "女教皇の逆位置は、考えが多くなりすぎて本音が見えにくくなっている状態を示しています。答えを急がなくても大丈夫です。",
      advice: "今日は情報を集めすぎず、自分の本音を一つだけ書き出してみましょう。"
    }
  },
  {
    name: "女帝",
    image: "cards/03_empress.png",
    upright: {
      meaning: "愛情、豊かさ、育てる力、安心感。",
      baseMessage: "女帝のカードは、やさしさや豊かさが広がっていくことを示しています。無理に急がず、心地よいものを大切にすると運が整います。",
      advice: "今日は自分を少し甘やかす時間を作ってください。"
    },
    reversed: {
      meaning: "疲れ、与えすぎ、依存、満たされなさ。",
      baseMessage: "女帝の逆位置は、誰かのために頑張りすぎて自分が後回しになっていることを示しています。まず自分を満たすことが大切です。",
      advice: "今日は人に与える前に、自分の休息を優先しましょう。"
    }
  },
  {
    name: "皇帝",
    image: "cards/04_emperor.png",
    upright: {
      meaning: "安定、責任、計画、現実的な力。",
      baseMessage: "皇帝のカードは、土台を整えることで安心が生まれることを示しています。感覚だけでなく、計画や仕組みを作ると流れが安定します。",
      advice: "今日は予定、家計、段取りを一つ見直してみましょう。"
    },
    reversed: {
      meaning: "頑固、抱え込み、支配、不安定さ。",
      baseMessage: "皇帝の逆位置は、力が入りすぎている状態を示しています。すべてを自分だけで背負わなくても大丈夫です。",
      advice: "今日は一つだけ人に頼ることを考えてみましょう。"
    }
  },
  {
    name: "教皇",
    image: "cards/05_hierophant.png",
    upright: {
      meaning: "信頼、学び、伝統、助言。",
      baseMessage: "教皇のカードは、信頼できる人や基本に戻ることが助けになることを示しています。ひとりで抱えず、知恵を借りると安心できそうです。",
      advice: "今日は経験者の話や、長く続いている方法を参考にしてみましょう。"
    },
    reversed: {
      meaning: "思い込み、形式へのこだわり、窮屈さ。",
      baseMessage: "教皇の逆位置は、常識や周囲の期待に合わせすぎていることを示しています。あなたらしい答えを見直す時です。",
      advice: "今日は『本当にそうしなければいけない？』と一度問い直してみましょう。"
    }
  },
  {
    name: "恋人",
    image: "cards/06_lovers.png",
    upright: {
      meaning: "選択、調和、心地よさ、ときめき。",
      baseMessage: "恋人のカードは、心が自然に向かうものを選ぶ大切さを示しています。義務感より、納得感や心地よさを大切にするとよさそうです。",
      advice: "今日は好き、安心する、心地よいという感覚を信じて選びましょう。"
    },
    reversed: {
      meaning: "迷い、不一致、優柔不断、すれ違い。",
      baseMessage: "恋人の逆位置は、心の中で迷いが生まれていることを示しています。すぐに答えを出さず、自分の本音を確認する時です。",
      advice: "今日は周りの期待より、自分がどう感じているかを先に見つめましょう。"
    }
  },
  {
    name: "戦車",
    image: "cards/07_chariot.png",
    upright: {
      meaning: "前進、行動、勢い、突破力。",
      baseMessage: "戦車のカードは、流れが動きやすくなっていることを示しています。迷いを抱えたままでも、まず動くことで状況が見えてきます。",
      advice: "今日は連絡する、片付ける、申し込むなど、具体的な行動を一つ選びましょう。"
    },
    reversed: {
      meaning: "焦り、暴走、方向のずれ、疲れ。",
      baseMessage: "戦車の逆位置は、進みたい気持ちがある一方で、方向が少し散らかっていることを示しています。急ぐ前に整えることが必要です。",
      advice: "今日は優先順位を一つに絞りましょう。"
    }
  },
  {
    name: "力",
    image: "cards/08_strength.png",
    upright: {
      meaning: "やさしい強さ、忍耐、信頼、内なる勇気。",
      baseMessage: "力のカードは、静かに続ける強さを示しています。強く押すより、やさしく向き合うことで状況が変わっていきます。",
      advice: "今日は無理に勝とうとせず、落ち着いて続けることを選びましょう。"
    },
    reversed: {
      meaning: "自信低下、我慢の限界、不安、消耗。",
      baseMessage: "力の逆位置は、自分を責める気持ちや疲れが出やすいことを示しています。弱さではなく、休息が必要なサインです。",
      advice: "今日は自分に厳しい言葉を使わず、少し楽になる選択をしてください。"
    }
  },
  {
    name: "隠者",
    image: "cards/09_hermit.png",
    upright: {
      meaning: "内省、探求、慎重さ、本質を見る力。",
      baseMessage: "隠者のカードは、静かな時間の中で本当の答えが見えてくることを示しています。急ぐほど見えにくくなるので、ゆっくりで大丈夫です。",
      advice: "今日は必要なことと不要なことを分けてみましょう。"
    },
    reversed: {
      meaning: "孤立、考え込みすぎ、視野の狭さ。",
      baseMessage: "隠者の逆位置は、一人で抱え込みすぎている状態を示しています。言葉にすると心が軽くなることもあります。",
      advice: "今日は信頼できる人に一言だけ話してみましょう。"
    }
  },
  {
    name: "運命の輪",
    image: "cards/10_wheel_of_fortune.png",
    upright: {
      meaning: "転機、流れ、タイミング、チャンス。",
      baseMessage: "運命の輪のカードは、流れが少しずつ動き始めることを示しています。思いがけない変化も、必要なきっかけになりそうです。",
      advice: "今日は来た話や誘いを、一度前向きに受け止めてみましょう。"
    },
    reversed: {
      meaning: "停滞、タイミングのずれ、流れに乗れない感覚。",
      baseMessage: "運命の輪の逆位置は、今は無理に動かそうとしても噛み合いにくいことを示しています。止まっている時間にも意味があります。",
      advice: "今日は急いで結論を出さず、準備と調整に使いましょう。"
    }
  },
  {
    name: "正義",
    image: "cards/11_justice.png",
    upright: {
      meaning: "公平、判断、バランス、誠実さ。",
      baseMessage: "正義のカードは、冷静に事実を見ることが助けになることを示しています。感情だけでなく、バランスを見直すと答えがはっきりします。",
      advice: "今日はメリットとデメリットを書き出してみましょう。"
    },
    reversed: {
      meaning: "偏り、不公平、判断ミス、違和感。",
      baseMessage: "正義の逆位置は、どこかで無理に納得しようとしていることを示しています。違和感を無視しないことが大切です。",
      advice: "今日はすぐ決めず、事実確認を優先しましょう。"
    }
  },
  {
    name: "吊るされた男",
    image: "cards/12_hanged_man.png",
    upright: {
      meaning: "待つこと、視点の転換、手放し、学び。",
      baseMessage: "吊るされた男のカードは、無理に動かすより見方を変えることで道が見えることを示しています。待つことも前進の一部です。",
      advice: "今日は別の角度から考えてみましょう。"
    },
    reversed: {
      meaning: "報われない我慢、停滞、執着、疲れ。",
      baseMessage: "吊るされた男の逆位置は、必要以上に我慢していることを示しています。続けることだけが正解ではありません。",
      advice: "今日は手放していい負担を一つ探しましょう。"
    }
  },
  {
    name: "死神",
    image: "cards/13_death.png",
    upright: {
      meaning: "終わりと始まり、区切り、再生、整理。",
      baseMessage: "死神のカードは、古いものを手放すことで新しい流れが入ることを示しています。怖いカードではなく、区切りと再生の合図です。",
      advice: "今日は不要なものや続けなくていい習慣を一つ手放してみましょう。"
    },
    reversed: {
      meaning: "変化への抵抗、未練、先延ばし。",
      baseMessage: "死神の逆位置は、本当は変えたいことをまだ抱えている状態を示しています。急に全部変えなくても大丈夫です。",
      advice: "今日は小さな整理から始めましょう。"
    }
  },
  {
    name: "節制",
    image: "cards/14_temperance.png",
    upright: {
      meaning: "調和、回復、自然な流れ、ほどよさ。",
      baseMessage: "節制のカードは、無理なく整えていくことを示しています。急激な変化より、少しずつバランスを取ることが合っています。",
      advice: "今日は予定、食事、休息のバランスを整えましょう。"
    },
    reversed: {
      meaning: "乱れ、無理、不調和、偏り。",
      baseMessage: "節制の逆位置は、生活や気持ちのバランスが少し崩れていることを示しています。頑張る前に整えることが必要です。",
      advice: "今日は予定を詰め込みすぎないようにしましょう。"
    }
  },
  {
    name: "悪魔",
    image: "cards/15_devil.png",
    upright: {
      meaning: "執着、誘惑、依存、見ないふり。",
      baseMessage: "悪魔のカードは、気になって離れにくいものや繰り返している癖に気づくことを示しています。まず気づくことが第一歩です。",
      advice: "今日は自分を責めず、繰り返しているパターンを一つ観察してみましょう。"
    },
    reversed: {
      meaning: "解放、悪習慣からの離脱、目覚め。",
      baseMessage: "悪魔の逆位置は、縛られていたものから少しずつ離れ始めていることを示しています。完全でなくても変化は始まっています。",
      advice: "今日は距離を置きたいものから、ほんの少し離れてみましょう。"
    }
  },
  {
    name: "塔",
    image: "cards/16_tower.png",
    upright: {
      meaning: "急な変化、気づき、古い土台の見直し。",
      baseMessage: "塔のカードは、思い通りでない出来事が本音に気づくきっかけになることを示しています。壊れるものは作り直せます。",
      advice: "今日は慌てすぎず、まず安全で落ち着ける場所に戻りましょう。"
    },
    reversed: {
      meaning: "変化の回避、小さな揺れ、先延ばし。",
      baseMessage: "塔の逆位置は、大きな変化を避けるための小さなサインが出ていることを示しています。今なら穏やかに整えられます。",
      advice: "今日は気になっていた問題を一つだけ直しましょう。"
    }
  },
  {
    name: "星",
    image: "cards/17_star.png",
    upright: {
      meaning: "希望、癒し、未来への光、素直さ。",
      baseMessage: "星のカードは、少し先に明るい可能性があることを示しています。今は完璧でなくても、希望を消さないことが大切です。",
      advice: "今日は未来の楽しみを一つ決めてみましょう。"
    },
    reversed: {
      meaning: "希望を見失う、不安、理想疲れ。",
      baseMessage: "星の逆位置は、理想と現実の差に疲れていることを示しています。でも、光が消えたわけではありません。",
      advice: "今日は大きな夢より、今日できる安心を一つ選びましょう。"
    }
  },
  {
    name: "月",
    image: "cards/18_moon.png",
    upright: {
      meaning: "不安、想像、曖昧さ、夢。",
      baseMessage: "月のカードは、まだ全体がはっきり見えていないことを示しています。不安な時ほど、事実と想像を分けることが大切です。",
      advice: "今日は夜に考えすぎず、気になることは紙に書いて明るい時間に見直しましょう。"
    },
    reversed: {
      meaning: "不安が晴れる、真実が見え始める、誤解の解消。",
      baseMessage: "月の逆位置は、ぼんやりしていたことが少しずつ見え始めていることを示しています。焦らず確認すれば大丈夫です。",
      advice: "今日は曖昧なことを一つ確認しましょう。"
    }
  },
  {
    name: "太陽",
    image: "cards/19_sun.png",
    upright: {
      meaning: "喜び、成功、明るさ、素直な表現。",
      baseMessage: "太陽のカードは、明るい流れが入っていることを示しています。あなたらしさを隠さず出すことで、良い反応が返ってきやすい日です。",
      advice: "今日は笑顔で伝えることを意識しましょう。"
    },
    reversed: {
      meaning: "元気不足、素直になれない、小さな停滞。",
      baseMessage: "太陽の逆位置は、本来の明るさが少し雲に隠れている状態を示しています。無理に元気に見せなくても大丈夫です。",
      advice: "今日は体を温めたり、外の光を浴びたりして心を起こしましょう。"
    }
  },
  {
    name: "審判",
    image: "cards/20_judgement.png",
    upright: {
      meaning: "復活、再挑戦、目覚め、知らせ。",
      baseMessage: "審判のカードは、過去に止まっていたことがもう一度動き出す可能性を示しています。諦めたことにも新しい形がありそうです。",
      advice: "今日は昔のメモや計画を見直してみましょう。"
    },
    reversed: {
      meaning: "ためらい、過去へのこだわり、決断の遅れ。",
      baseMessage: "審判の逆位置は、もう進めるのに自分でブレーキをかけていることを示しています。過去を責めなくて大丈夫です。",
      advice: "今日は『次にどうするか』だけを考えてみましょう。"
    }
  },
  {
    name: "世界",
    image: "cards/21_world.png",
    upright: {
      meaning: "完成、達成、統合、次のステージ。",
      baseMessage: "世界のカードは、一つの流れがまとまりつつあることを示しています。ここまでの経験は、次の場所へ進む土台になります。",
      advice: "今日はできたことを認めて、一区切りをつけましょう。"
    },
    reversed: {
      meaning: "未完成、あと一歩、区切りがつかない状態。",
      baseMessage: "世界の逆位置は、ゴールが近いのに最後の整理が残っていることを示しています。焦らず仕上げれば大丈夫です。",
      advice: "今日は途中のままになっていることを一つ終わらせましょう。"
    }
  }
];

const readingTypes = {
  daily: {
    label: "今日のわたしへの一枚",
    resultTitle: "今日のわたしへの一枚",
    messageHeading: "今日のあなたへのメッセージ"
  },
  relationship: {
    label: "人間関係を心地よくするには？",
    resultTitle: "人間関係を心地よくするヒント",
    messageHeading: "人付き合いをやわらかくするために"
  },
  money: {
    label: "金運が上がる時期はいつ？",
    resultTitle: "金運が上がる流れ",
    messageHeading: "お金の流れが良くなるタイミング"
  },
  flow: {
    label: "これからの流れ",
    resultTitle: "これからの流れ",
    messageHeading: "これから意識したいこと"
  },
  relief: {
    label: "近々、人付き合いは楽になる？",
    resultTitle: "人付き合いが楽になる流れ",
    messageHeading: "心が軽くなるためのヒント"
  }
};

const extraResults = {
  daily: {
    upright: [
      "今日は、目の前のことを丁寧に扱うほど運が整います。",
      "気持ちがふっと軽くなる小さな出来事が、今日のあなたを助けてくれそうです。",
      "急ぐよりも、味わう時間が必要です。穏やかな選択がよい流れを呼びます。",
      "今日は自分のペースを大切にすると、思った以上に物事が進みやすくなります。"
    ],
    reversed: [
      "今日は少し疲れが出やすいかもしれません。無理に元気を出そうとしなくて大丈夫です。",
      "予定を詰め込みすぎると、心が窮屈になりそうです。余白を作ることが運を守ります。",
      "気持ちがまとまらない時は、考えることを一度休ませましょう。",
      "今日は人のペースに引っ張られすぎないことが大切です。"
    ]
  },
  relationship: {
    upright: [
      "相手に合わせすぎず、あなたが自然でいられる関わり方を選ぶと、人間関係がやわらぎます。",
      "今日は短い言葉でも、やさしい気持ちが伝わりやすい日です。",
      "無理に距離を縮めるより、穏やかな空気を保つことが関係を心地よくします。",
      "人とのつながりの中に、小さな助けや気づきがありそうです。"
    ],
    reversed: [
      "気を使いすぎて、少し疲れが出ているかもしれません。距離を取ることも大切です。",
      "今日は無理に仲良くしようとしなくて大丈夫です。静かに過ごす選択も良い選択です。",
      "相手の言葉を深く受け止めすぎると、心が重くなりそうです。",
      "人の機嫌を背負いすぎないでください。あなたの責任ではないこともあります。"
    ]
  },
  money: {
    upright: [
      "金運は、身近な見直しから上がりやすい流れです。無理な勝負より、整えることが近道です。",
      "今ある収入や支出を丁寧に見ることで、次のチャンスに気づきやすくなります。",
      "お金の流れは少しずつ上向きです。行動したことが後から実りやすいでしょう。",
      "小さな節約や価格の見直しが、思った以上に良い流れを作ります。"
    ],
    reversed: [
      "今は勢いでお金を動かすより、守る意識が大切です。",
      "支出の小さな積み重ねが気になりやすい時です。見直すだけでも流れは変わります。",
      "焦って増やそうとすると、かえって迷いが生まれそうです。",
      "今日は大きな買い物や契約は慎重に考えましょう。"
    ]
  },
  flow: {
    upright: [
      "これからの流れは、少しずつ明るい方向へ向かっています。焦らず準備を続けましょう。",
      "今すぐ大きく変わらなくても、静かに次の場面へ移っていく気配があります。",
      "人や予定の流れが、自然にあなたを次の場所へ運んでくれそうです。",
      "小さなきっかけが、後から大きな変化につながる可能性があります。"
    ],
    reversed: [
      "これからの流れに入る前に、少し整理が必要です。",
      "焦って変えようとすると、かえって疲れてしまいそうです。",
      "今は準備の時期です。見えないところを整えるほど、あとで楽になります。",
      "流れが止まって見えても、内側では次の準備が進んでいます。"
    ]
  },
  relief: {
    upright: [
      "人付き合いの重たさは、少しずつやわらいでいきそうです。",
      "あなたが無理をしない距離を選ぶことで、心が軽くなっていきます。",
      "近いうちに、話しやすい空気や安心できる関係が戻ってくる可能性があります。",
      "頑張りすぎていた関係に、少しずつ風通しが生まれそうです。"
    ],
    reversed: [
      "今はまだ、人付き合いに疲れを感じやすいかもしれません。",
      "すぐに楽になろうと無理をすると、余計に心が重くなることがあります。",
      "相手の言葉を全部受け止めなくて大丈夫です。",
      "関係を急いで直そうとせず、あなたの心が落ち着く時間を優先しましょう。"
    ]
  }
};

const extraAdvice = {
  daily: [
    "温かい飲み物をゆっくり飲む時間を作ってみましょう。",
    "今日は予定を一つ軽くして、自分のための余白を作りましょう。",
    "好きな香り、好きな音、好きな景色を一つ選んで心を整えましょう。",
    "自分を責める言葉を、今日は一つ減らしてみましょう。"
  ],
  relationship: [
    "短くても、やわらかい言葉を一つ選んでみましょう。",
    "苦手な人とは、近すぎず遠すぎずの距離を意識しましょう。",
    "返事を急がず、心が落ち着いてから向き合って大丈夫です。",
    "無理な約束はせず、できる範囲で関わりましょう。"
  ],
  money: [
    "今日使う予定のお金を一度書き出してみましょう。",
    "買う前に一晩考えるルールを作ると金運が整います。",
    "不要なものを一つ手放すと、お金の流れにも余白が生まれます。",
    "収入を増やす小さな工夫を一つ考えてみましょう。"
  ],
  flow: [
    "先の心配を一度置いて、今日できる準備を一つ進めましょう。",
    "予定を見直して、詰まりすぎているところに余白を作りましょう。",
    "気になっていた小さな用事を一つ片付けましょう。",
    "急がず、順番を決めることから始めましょう。"
  ],
  relief: [
    "今日は気を使いすぎる場面を一つ減らしてみましょう。",
    "人と会った後は、ひとりで休む時間を作りましょう。",
    "返事をすぐ返さなくても大丈夫です。落ち着いてからで十分です。",
    "自然体でいられる人との時間を大切にしましょう。"
  ]
};

document.addEventListener("DOMContentLoaded", function () {
  const homeScreen = document.getElementById("homeScreen");
  const shuffleScreen = document.getElementById("shuffleScreen");
  const resultScreen = document.getElementById("resultScreen");

  const readingButtons = document.querySelectorAll(".reading-button");
  const stopBtn = document.getElementById("stopBtn");
  const againBtn = document.getElementById("againBtn");

  const resultCategoryLabel = document.getElementById("resultCategoryLabel");
  const resultTitle = document.getElementById("resultTitle");
  const messageHeading = document.getElementById("messageHeading");

  const resultCardImage = document.getElementById("resultCardImage");
  const cardName = document.getElementById("cardName");
  const cardDirection = document.getElementById("cardDirection");
  const cardMeaning = document.getElementById("cardMeaning");
  const cardMessage = document.getElementById("cardMessage");
  const cardAdvice = document.getElementById("cardAdvice");

  let selectedCard = null;
  let selectedDirection = "upright";
  let selectedReadingKey = "daily";

  function randomItem(list) {
    return list[Math.floor(Math.random() * list.length)];
  }

  function showScreen(screen) {
    homeScreen.classList.remove("active");
    shuffleScreen.classList.remove("active");
    resultScreen.classList.remove("active");
    screen.classList.add("active");

    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  }

  function pickCard() {
    const cardIndex = Math.floor(Math.random() * tarotCards.length);
    const isReversed = Math.random() < 0.5;

    selectedCard = tarotCards[cardIndex];
    selectedDirection = isReversed ? "reversed" : "upright";
  }

  function startReading(readingKey) {
    selectedReadingKey = readingKey || "daily";
    pickCard();
    showScreen(shuffleScreen);
  }

  function stopShuffle() {
    if (!selectedCard) {
      pickCard();
    }

    const reading = readingTypes[selectedReadingKey] || readingTypes.daily;
    const resultPool = extraResults[selectedReadingKey] || extraResults.daily;
    const advicePool = extraAdvice[selectedReadingKey] || extraAdvice.daily;

    const data = selectedCard[selectedDirection];
    const directionText = selectedDirection === "upright" ? "正位置" : "逆位置";
    const extraMessage = randomItem(resultPool[selectedDirection]);
    const adviceMessage = randomItem(advicePool);

    resultCategoryLabel.textContent = reading.label;
    resultTitle.textContent = reading.resultTitle;
    messageHeading.textContent = reading.messageHeading;

    resultCardImage.src = selectedCard.image;
    resultCardImage.alt = selectedCard.name + "のカード";
    resultCardImage.classList.toggle("reversed", selectedDirection === "reversed");

    cardName.textContent = selectedCard.name;
    cardDirection.textContent = directionText;
    cardMeaning.textContent = data.meaning;
    cardMessage.textContent = data.baseMessage + " " + extraMessage;
    cardAdvice.textContent = data.advice + " " + adviceMessage;

    showScreen(resultScreen);
  }

  function backToHome() {
    selectedCard = null;
    selectedDirection = "upright";
    selectedReadingKey = "daily";

    resultCardImage.src = "";
    resultCardImage.classList.remove("reversed");

    showScreen(homeScreen);
  }

  readingButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      startReading(button.dataset.reading);
    });
  });

  if (stopBtn) {
    stopBtn.addEventListener("click", stopShuffle);
  }

  if (againBtn) {
    againBtn.addEventListener("click", backToHome);
  }

  window.stopShuffle = stopShuffle;
});