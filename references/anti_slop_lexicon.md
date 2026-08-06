# Anti-Slop 替换表 (Anti-Slop Lexicon)

独立参考文件。Skill 管"怎么做"，这个文件管"查什么"。

核心原则只有一条：**空话删掉，换成模型能画出来的东西。**

不是换个中文同义词。"cinematic"换成"电影级质感"——模型依然不知道你要什么。换成"ARRI Alexa + Cooke 50mm, 侧光，浅景深"——模型知道了。

---

## 硬删除：画质词

这些词由 API 参数控制，写在 prompt 里是废话。直接删，不替换。

| 删掉 | 为什么 |
|------|--------|
| 4K / 8K / ultra HD / high resolution | 分辨率由 `resolution` 参数控制 |
| high quality / masterpiece / best quality / top quality | 画质词，没有任何信息量 |

---

## 硬删除：空形容词

以下词汇必须从 prompt 中移除。不是"建议不用"，是"必须删"。

| 删掉 | 为什么 |
|------|--------|
| beautiful / stunning / amazing / awesome | 你在说"好看"，但没说长什么样 |
| epic | 你在说"宏大"，但没给宏大的物理证据 |
| breathtaking | 同上 |
| realistic / photorealistic | 真实摄影机型号比这个词有效得多（经验观察） |

---

## 特殊处理：cinematic

`cinematic` 单独出现 → 删。
`cinematic` 后面跟了具体景别 + 光源 → 保留（但建议换成真实设备名）。

---

## 替换表：空话 → 具体物理描述

每个条目格式：空话 → 它到底该说什么 → 改前改后对比。

### 视觉风格

**cinematic / 电影感**
- 空在哪：你说"像电影"，但哪种电影？王家卫还是诺兰？
- 该写什么：真实摄影机 + 镜头型号 + 景别 + 光源
- Before: `cinematic shot of a woman in a hallway`
- After: `Medium shot, ARRI Alexa Mini + Cooke S4 50mm f/2.8. Single window light from camera left, deep shadows on the right. A woman stands in a narrow hallway.`

**beautiful / 美**
- 空在哪：美是个判断，不是描述。你得告诉模型"美"长什么样。
- 该写什么：具体的光线、色彩、材质、空间关系
- Before: `beautiful sunset scene`
- After: `Wide shot. Golden hour, sun sitting on the horizon. Orange light raking across wet sand, long shadows from scattered rocks. Color temperature around 3200K.`

**stunning / 震撼**
- 空在哪：你在表达你自己的感受，不是在描述画面。
- 该写什么：让画面本身产生冲击——尺度对比、角度、光影反差
- Before: `stunning mountain view`
- After: `Extreme wide shot, low angle from valley floor. Granite cliffs rise 800m on both sides, a thread of river at the bottom. Overcast sky, single break in clouds letting a shaft of light hit the far peak.`

**dramatic / 戏剧性**
- 空在哪：戏剧性是效果，不是手法。
- 该写什么：光比、角度、构图的具体选择
- Before: `dramatic lighting on his face`
- After: `Close-up. Hard key light from directly above, deep eye socket shadows. No fill. Half the face in shadow, half in light.`

### 情感

**emotional / 感人**
- 空在哪：你在给画面贴标签，不是在构建画面。
- 该写什么：角色的具体身体语言、面部微表情、环境细节
- Before: `emotional reunion scene`
- After: `Medium close-up. Two people face each other. One reaches out slowly, fingers trembling, touches the other's cheek. The other's eyes close. Shallow depth of field, background blurred.`

**powerful / 强烈**
- 空在哪：同上，贴标签。
- 该写什么：力量的物理表现——肌肉、姿态、空间占有
- Before: `a powerful moment of determination`
- After: `Close-up on hands gripping the edge of a table. Knuckles white. Camera slowly pushes in. Jaw muscles tighten in the background, out of focus.`

**intense / 紧张**
- 空在哪：紧张是观众的感受，你得描述产生这种感受的画面元素。
- 该写什么：镜头运动、节奏、空间压迫
- Before: `intense chase scene`
- After: `Handheld camera, shaky, breathing rhythm. Tight framing — walls closing in on both sides. Fast tracking shot from behind. Footsteps echoing, getting louder.`

### 运动

**smooth / 流畅**
- 空在哪：流畅是个感受词。你得说清楚用什么设备、怎么动。
- 该写什么：稳定器类型、运动速度、方向
- Before: `smooth camera movement through the room`
- After: `Steadicam shot, eye level, slow forward glide at walking pace. Camera passes between furniture, maintaining consistent speed. No shake, no tilt.`

**dynamic / 动感**
- 空在哪：动感不是指令，是结果。
- 该写什么：速度变化、方向变化、镜头类型
- Before: `dynamic action sequence`
- After: `Quick cuts between low-angle tracking and overhead wide. Camera switches direction every 2 seconds. Speed ramps: slow-mo at peak action, real-time on landing.`

**elegant / 优雅**
- 空在哪：优雅是审美判断。
- 该写什么：运动的速度、轨迹、节奏
- Before: `elegant dance movement`
- After: `Slow lateral tracking shot. Dancer's arm extends in a continuous arc from lower left to upper right. Movement takes 3 seconds. Soft backlight creating rim light on the arm.`

### 光影

**moody / 氛围感**
- 空在哪：氛围是个空筐，什么都能往里装。
- 该写什么：光源位置、光比、色温
- Before: `moody bar interior`
- After: `Interior, dimly lit bar. Single pendant lamp over the counter, warm tungsten 2700K. Deep shadows in corners. Light falls off sharply — bright at the bar, nearly black three meters away.`

**atmospheric / 有氛围**
- 空在哪：同上。
- 该写什么：空气中的粒子、能见度、光线散射
- Before: `atmospheric forest morning`
- After: `Wide shot in a dense forest. Ground-level mist, 2 meters thick. Early morning sun at 15° angle, beams visible through the mist. Trees as dark silhouettes.`

**warm lighting / 暖光**
- 空在哪："暖"是感受。得说色温和光源类型。
- 该写什么：色温值、光源类型
- Before: `warm lighting in a living room`
- After: `Living room lit by table lamps, 2700K tungsten. Soft shadows, no hard edges. Light bounces off cream-colored walls, filling the room evenly.`

**cold lighting / 冷光**
- 空在哪：同上。
- 该写什么：色温值、光源类型
- Before: `cold sterile hospital corridor`
- After: `Hospital corridor, overhead fluorescent panels, 5600K daylight. Flat, shadowless light. Green-tinted white walls, polished floor reflecting the panels.`

---

## 执行方式

1. 正则匹配，自动检测
2. 命中硬删除列表 → 直接删，不替换
3. 命中替换表 → 删掉空话，用具体描述重写那个句子
4. 重写后句子不通顺 → 重写整句，不是硬拼

---

## 完整处理示例

**输入：**
```
帮我做一个 cinematic、beautiful、epic 的 4K masterpiece 视频，
画面 stunning，motion smooth，非常 realistic
```

**处理过程：**
1. 删 4K、masterpiece（画质词，API 控制）
2. 删 realistic（空话，用设备名替代）
3. cinematic → 换成具体设备+景别
4. beautiful → 换成具体光线+色彩
5. epic → 换成尺度对比+构图
6. stunning → 换成具体画面元素
7. smooth → 换成稳定器+速度

**输出：**
```
Wide shot, ARRI Alexa Mini + Panavision C-series 35mm f/4. 
Golden hour, low sun behind the subject, long shadows stretching 
toward camera. Slow Steadicam push-in at walking pace. 
Subject stands at the edge of a cliff, wind pulling at their coat.
```

一个词都没留。每个描述都是模型能画出来的东西。

---

## 约束

- 硬删除是强制的，不是建议
- 替换目标是物理描述，不是中文同义词
- "电影级质感""震撼""氛围感"都是空话——它们和原文一样空
- 如果你发现自己写的词无法被画出来，那就还不够具体
