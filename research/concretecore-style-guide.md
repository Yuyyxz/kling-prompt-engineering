# 砼核 / Concretecore 视觉风格指南

> **KPE 文生图方法论 · 风格专项扩展**
> 适用场景：AI 图像 / 视频生成 Prompt 构建。输出风格：荒芜压抑的巨构混凝土阈限空间美学。

---

## 目录

1. [定义与起源](#1-定义与起源)
2. [核心视觉元素清单](#2-核心视觉元素清单)
3. [典型场景清单](#3-典型场景清单)
4. [情绪氛围关键词](#4-情绪氛围关键词)
5. [色彩体系](#5-色彩体系)
6. [光线体系](#6-光线体系)
7. [材质体系](#7-材质体系)
8. [构图原则](#8-构图原则)
9. [与相邻美学的区分边界](#9-与相邻美学的区分边界)
10. [正面关键词列表 Prompt Positive](#10-正面关键词列表-prompt-positive)
11. [负面关键词列表 Prompt Negative](#11-负面关键词列表-prompt-negative)
12. [Prompt 构建模板](#12-prompt-构建模板)
13. [参考作品与创作者](#13-参考作品与创作者)

---

## 1. 定义与起源

### 1.1 什么是砼核？

**砼核（Concretecore / Cementcore / 水泥核）** 是一种以巨大混凝土建筑为核心视觉元素的网络 -core 美学风格。它属于中文互联网「核类美学」家族（梦核 Dreamcore / 怪核 Weirdcore / 池核 Poolcore / 雨核 Raincore / 植核 Plantcore 等），以粗野主义（Brutalism）建筑和阈限空间（Liminal Space）为视觉根基，但本质是**氛围/情绪导向**的美学，而非建筑流派。

「砼」= 混凝土（人造石），「核」= core，遵循 -core 美学的命名惯例。

### 1.2 核心精神

> **「巨人的沉默」** — 当建筑不再为人而存在，它在表达什么？

砼核美学的精神内核是：**巨型人造构筑物在失去人类使用功能后，呈现出的寂静、永恒、荒芜与压迫感。** 它不是废墟（废墟有坍塌和毁灭），而是**完好的、持续存在的、无人问津的巨构**。混凝土本身在"呼吸"，在沉默中承载时间。

### 1.3 关键文化锚点

| 锚点 | 说明 |
|------|------|
| **粗野主义 Brutalism** | 技术来源（裸露混凝土、几何体量），但砼核是情绪化挪用而非建筑学派 |
| **阈限空间 Liminal Space** | 空间逻辑来源（过渡空间：走廊、楼梯间、地下通道） |
| **巨构建筑 Megastructure** | 尺度来源（容纳万人的单一结构体、新陈代谢派遗梦） |
| **后室 The Backrooms** | 网络文化氛围来源（无限重复的无人空间） |
| **少女终末旅行** | 日本动画中「文明退场后的巨构」视觉参考 |
| **探激工作室 C-EXCITE** | 中文互联网砼核美学核心创作者 |
| **药厂人家** | Bilibili 砼核/粗野主义深度解析作者 |

---

## 2. 核心视觉元素清单

### 2.1 构图 (Composition)

| 构图策略 | 描述 | Prompt 关键词参考 |
|----------|------|-------------------|
| **巨物俯视** | 极高视点俯瞰巨构，人物渺小如蚂蚁 | aerial view, tiny figure, monumental scale |
| **仰视压迫** | 极低视点仰拍，建筑向天空延伸形成压迫感 | worm's-eye view, towering above, vanishing into fog |
| **纵深走廊** | 对称单点透视，走廊/楼梯向远处无限延伸 | one-point perspective, symmetrical corridor, infinite depth |
| **框架层叠** | 多层混凝土框架叠加，形成"框中框"的嵌套感 | layered frames, nested concrete structures, depth planes |
| **空场全景** | 巨大空间内空旷无人，强调空间本身的存在感 | vast empty hall, cathedral-like space, monumental void |
| **尺度对比** | 巨型结构中放置极小的人类/物件来反衬尺度 | scale contrast, miniature human figure, overwhelming structure |

### 2.2 材质 (Material)

| 材质 | 特征 | Prompt 关键词参考 |
|------|------|-------------------|
| **裸露混凝土 (Béton Brut)** | 木模板纹理、粗粝表面、气孔、色差 | raw concrete, board-formed concrete, béton brut, rough texture |
| **风化混凝土** | 水渍、锈迹、剥落、苔藓、钙华流痕 | weathered concrete, water stains, efflorescence, aged surface |
| **锈蚀钢筋** | 混凝土裂缝中露出锈蚀的钢筋 | exposed rebar, rust stains, concrete spalling |
| **水磨石 / 石材** | 冷峻的公共建筑地面 | terrazzo floor, polished stone, institutional flooring |
| **工业金属** | 扶手、管道、通风口，但避免过多机械感 | metal handrails, exposed pipes, ventilation grilles |
| **植被入侵** | 苔藓、蕨类、藤蔓从混凝土缝隙中生长 | moss on concrete, vines creeping, nature reclaiming |

> **关键区分**：砼核的混凝土是**"活的"**——有风化痕迹、有植被入侵、有水渍锈迹——而非刚浇筑的完美光滑混凝土。后者是极简主义/现代主义建筑摄影，不是砼核。

### 2.3 光线 (Lighting)

| 光线类型 | 效果 | Prompt 关键词参考 |
|----------|------|-------------------|
| **阴天漫射光** | 均匀灰色天空，无强烈阴影，模糊时间感 | overcast sky, diffused light, flat grey ambient, no shadows |
| **雾中散射光** | 雾气穿透混凝土结构，柔化边缘，增加神秘 | fog through concrete, misty atmosphere, atmospheric haze |
| **缝隙光 / 天窗光** | 从顶部或缝隙射入的单一光束，形成戏剧性明暗 | shaft of light, skylight beam, god rays through cracks |
| **荧光灯冷光** | 地下/室内阈限空间的冷白色人工光源 | fluorescent lighting, cold white light, institutional lighting |
| **黄昏/清晨低角度光** | 暖色低光拉长阴影，增强建筑体量感 | golden hour low angle, long shadows, warm side light |
| **逆光剪影** | 建筑成为巨大黑色剪影，天空做背景 | backlit silhouette, contre-jour, structure against sky |

> **避免**：霓虹灯光、赛博朋克彩色光源、LED 灯带、暖色温馨室内照明。

### 2.4 色彩 (详见 §5 色彩体系)

砼核色彩以**低饱和、冷灰调**为主，偶有少量自然/衰败色作为点缀。

### 2.5 尺度 (Scale)

砼核的**核心视觉冲击力来自尺度**：

| 尺度策略 | 描述 |
|----------|------|
| **超大尺度** | 建筑体量远超人类日常生活尺度（高百米以上、宽数百米） |
| **重复尺度** | 相同的结构单元无限重复（窗户、柱子、拱门），制造节奏感与迷失感 |
| **无尺度参照** | 画面中没有人类/车辆/树木等参照物，无法判断实际大小 |
| **渺小参照** | 极小的一个人站在巨大的混凝土结构前/中 |

---

## 3. 典型场景清单

### 3.1 一级场景（核心场景）

| 场景类型 | 描述 | 示例 |
|----------|------|------|
| **巨大地下空间** | 地下排水道、地下大厅、地下隧道网络 | 首都圏外郭放水路（日本埼玉"地下神殿"） |
| **无尽走廊** | 两侧对称、纵深无限的混凝土走廊 | 后室 Level 0 黄走廊的"粗野主义版本" |
| **巨型楼梯间** | 层层交错的混凝土楼梯，向上向下延伸 | 粗野主义公寓楼的消防楼梯 |
| **空荡的巨构大厅** | 如大教堂般挑高的混凝土内部空间 | 涡轮大厅 Turbine Hall、粗野主义市政厅 |
| **巨构外部全景** | 整座巨型建筑在阴天/雾中的全景 | 前苏联/东欧粗野主义纪念碑建筑 |
| **高架步道与连廊** | 连接两座巨构的空中混凝土连廊 | 巴比肯中心、布伦瑞克中心 |

### 3.2 二级场景（扩展场景）

| 场景类型 | 描述 |
|----------|------|
| **山间巨构** | 巨大混凝土建筑嵌入山体或悬崖 |
| **水边巨构** | 水库大坝、防波堤、海岸混凝土结构 |
| **雪中巨构** | 积雪覆盖的混凝土建筑（首钢遗址冬季） |
| **地下车站** | 粗野主义风格的地铁站台 |
| **废弃工厂车间** | 工业遗产的巨型厂房内部 |
| **冷却塔内部** | 发电厂冷却塔底部的仰视视角 |
| **巨型柱廊** | 重复的混凝土巨柱形成的柱廊空间 |
| **防御工事/碉堡** | 海岸/山区的巨型混凝土军事设施 |

### 3.3 避免的场景

| 场景 | 原因 |
|------|------|
| 赛博朋克城市夜景 | 滑向霓虹科幻 |
| 完整废墟/坍塌建筑 | 滑向废墟核/Ruin Porn |
| 有人类活动的场所 | 砼核必须是"无人的" |
| 自然景观为主 | 滑向风景摄影 |
| 豪华/精致室内 | 滑向建筑摄影/室内设计 |
| 生机勃勃的生态建筑 | 滑向植核/雨核/太阳朋克 |

---

## 4. 情绪氛围关键词

### 4.1 核心情绪（中文）

| 层级 | 关键词 |
|------|--------|
| **第一层：直接感受** | 压抑、空旷、寂静、荒芜、冷峻、沉重 |
| **第二层：深层共鸣** | 巨人的沉默、无力感、敬畏、疏离、被允许的渺小 |
| **第三层：哲学意味** | 后人类、时间凝固、文明退场后的回响、人造物的永恒性 |
| **第四层：矛盾情感** | 压抑中的安全感、混乱中的秩序感、冰冷中的熟悉感 |

### 4.2 核心情绪（英文）

| 层级 | 关键词 |
|------|--------|
| **Direct** | oppressive, desolate, silent, barren, cold, heavy |
| **Resonance** | sublime dread, awe, insignificance, alienation, the silence of giants |
| **Philosophical** | post-human, frozen time, echoes of a departed civilization, permanence of the artificial |
| **Paradoxical** | safety within oppression, order within chaos, familiarity within the alien |

### 4.3 情绪配方（关键矛盾）

砼核的情绪核心是一个**矛盾综合体**：

> **压迫 × 安全** = 混凝土巨构既是压迫的来源，又是包裹/保护的象征
> **荒芜 × 秩序** = 无人但有结构，混乱世界中的几何秩序感
> **冷峻 × 熟悉** = 混凝土的冷感 + 对旧时代建筑的怀旧温暖
> **恐惧 × 敬畏** = 对尺度的恐惧 + 对巨构之美的迷恋

---

## 5. 色彩体系

### 5.1 主色板 (Primary Palette)

| 色名 | Hex | 使用场景 |
|------|-----|----------|
| 混凝土灰 | `#B0A99F` | 大面积混凝土表面（基本色调） |
| 深灰 | `#8A8580` | 阴影面混凝土 |
| 铁锈棕 | `#8B5E3C` | 锈迹、钢筋裸露处 |
| 冷灰 | `#9E9E9B` | 阴天天空、室内墙面 |

### 5.2 辅助色板 (Secondary Palette)

| 色名 | Hex | 使用场景 |
|------|-----|----------|
| 水泥白 | `#D4CFC7` | 较新/较浅的混凝土面 |
| 水渍灰 | `#7E8A8C` | 渗水痕迹、湿润混凝土 |
| 苔藓绿 | `#5A6E4A` | 植被入侵 |
| 雾白 | `#D8DCD6` | 雾气、散射光 |

### 5.3 点缀色 (Accent, 极少使用)

| 色名 | Hex | 使用场景 |
|------|-----|----------|
| 荧光冷白 | `#E8F0F8` | 室内荧光灯 |
| 暖低光 | `#D4A76A` | 黄昏/清晨金色阳光 |
| 天空蓝灰 | `#A3B5C4` | 阴天天空微弱的蓝色 |
| 锈红 | `#A0522D` | 严重锈蚀的金属部件 |

### 5.4 色彩原则

- **饱和度**：全局低饱和度（desaturated / muted）。不能有鲜艳色彩。
- **色调**：冷灰色调为主，暖色调仅作为光线点缀出现。
- **对比度**：低到中等。避免高对比度的 HDR 风格。
- **氛围色罩**：全局微冷色罩（偏蓝灰或绿灰）。

---

## 6. 光线体系

### 6.1 推荐光线模式

| 模式 | 特点 | 氛围 |
|------|------|------|
| **阴天漫射 (Overcast Diffuse)** | 无阴影、均匀灰光、时间感模糊 | 最核心光线模式 |
| **雾光 (Fog Light)** | 雾气柔化边缘、深度随距离递减 | 神秘、孤寂、距离感 |
| **顶光缝隙 (Skylight Shaft)** | 从天窗/裂缝射入的单一光束 | 宗教感、戏剧性、神圣 |
| **荧光冷光 (Fluorescent)** | 室内阈限空间的冷白光源 | 不安、机构感、非人化 |
| **低角度暖光 (Low Warm)** | 黄昏/清晨光线，长阴影 | 怀旧、时间流逝感 |

### 6.2 避免的光线

- 霓虹灯光 / 彩色 LED — 滑向赛博朋克
- 黄金时刻高饱和暖光 — 滑向风光摄影
- HDR 强对比光 — 滑向商业建筑摄影
- 完全黑暗 / 恐怖电影光 — 滑向怪核/恐怖
- 梦幻柔焦光 — 滑向梦核

---

## 7. 材质体系

### 7.1 材质等级

| 等级 | 材质状态 | 特征 |
|------|----------|------|
| **A 级（最推荐）** | 风化混凝土 | 水渍、锈迹、木模纹理、轻微苔藓、气孔、钙华 |
| **B 级** | 裸露混凝土 | 木模纹理清晰，无风化但保持粗粝 |
| **C 级** | 较新混凝土 | 仅有少量污渍，表面相对平整 |
| **D 级（避免）** | 光滑完美混凝土 | 极简主义/安藤忠雄式，非砼核 |

### 7.2 表面细节清单

- 木模板留下的木纹纹理（board-form marks）
- 混凝土浇筑的气孔和瑕疵（air bubbles, pour lines）
- 水渍垂直流痕（water streak marks）
- 锈迹从内部渗出/从钢筋扩散（rust bleeding）
- 苔藓/地衣在阴湿面生长（moss/lichen patches）
- 混凝土表面的钙华/白华（efflorescence）
- 表面剥落露出骨料（exposed aggregate）
- 裂缝中的植物根系（roots in cracks）

---

## 8. 构图原则

### 8.1 核心几何

| 几何原则 | 说明 |
|----------|------|
| **单点透视** | 走廊/隧道/大厅使用严格对称的单点透视，增强无限感 |
| **三点透视仰角** | 巨构外部使用夸张的三点透视（仰视），制造压迫感 |
| **重复韵律** | 相同建筑单元（窗户/柱/拱）的规律重复，制造节奏 |
| **框中框** | 多层混凝土框架嵌套，深度层次丰富 |
| **巨型负空间** | 巨构之间的空旷"留白"与建筑实体同等重要 |

### 8.2 人物放置原则

- **极少数**：画面中最多 1-2 人，且永远是远景中的渺小剪影
- **功能单一**：仅为尺度参照而存在，不表现人物的情感/动作/面孔
- **位置**：在画面下方边缘或远处，被建筑压倒
- **状态**：站立不动、行走中（去向不明）、或坐卧

> 有人物的画面遵循"反向纪实"原则：人物是构图的工具，建筑才是主体。

---

## 9. 与相邻美学的区分边界

### 9.1 砼核 vs 粗野主义 (Brutalism)

| 维度 | 砼核 Concretecore | 粗野主义 Brutalism |
|------|-------------------|---------------------|
| 本质 | 网络美学/情绪风格 | 建筑流派/设计哲学 |
| 关注点 | 建筑带来的**情绪反应** | 建筑本身的**设计语言** |
| 场景 | 无人、荒芜、废弃/闲置 | 可有人使用、有功能 |
| 时期 | 2022~至今（互联网现象） | 1950s-1970s（建筑史） |
| 色彩处理 | 去饱和、统一冷灰调 | 原色纪实 |
| 代表 | Bilibili/Steam 砼核视频 | 柯布西耶、史密森夫妇 |
| 态度 | 后人类视角的冷眼凝视 | 建筑师的创作热情 |

> **简单区分**：粗野主义是"这建筑怎么设计的"，砼核是"这建筑让我感到什么"。

### 9.2 砼核 vs 梦核 (Dreamcore)

| 维度 | 砼核 | 梦核 |
|------|------|------|
| 核心情感 | 压迫、渺小、敬畏 | 怀旧、温暖、不安 |
| 色彩 | 冷灰低饱和 | 粉彩、柔光、过曝 |
| 空间 | 巨构混凝土 | 童年记忆空间（操场、教室、郊区住宅） |
| 材质 | 混凝土、金属、石材 | 草地、塑料玩具、旧家具 |
| 光线 | 阴天/雾/荧光灯 | 柔焦、梦幻过曝、VHS滤镜 |
| 气氛 | 冷峻 | 温暖而诡异 |

### 9.3 砼核 vs 怪核 (Weirdcore)

| 维度 | 砼核 | 怪核 |
|------|------|------|
| 核心情感 | 敬畏中的平静 | 迷失与恐惧 |
| 视觉元素 | 建筑景观为主 | 拼贴、不协调元素、文字叠加 |
| 超现实程度 | 低（空间可以是真实的） | 高（刻意违和） |
| 美学策略 | 巨构+空场 | 低质量图片+诡异拼接 |
| 色彩 | 克制统一 | 可鲜艳可脏乱 |

### 9.4 砼核 vs 雨核 (Raincore)

| 维度 | 砼核 | 雨核 |
|------|------|------|
| 核心元素 | 混凝土建筑 | 雨水/湿润环境 |
| 空间 | 建筑空间为主 | 任何户外/半户外空间 |
| 可交叉 | ✅ 雨中的巨构 = 砼核+雨核交叉 | - |
| 区别 | 砼核的根本是建筑尺度 | 雨核的根本是水的氛围 |

### 9.5 砼核 vs 后末日 (Post-Apocalyptic)

| 维度 | 砼核 | 后末日 |
|------|------|-------|
| 建筑状态 | 完好，只是无人 | 残破、坍塌、毁灭 |
| 自然入侵 | 轻度（苔藓、水渍） | 重度（丛林覆盖、建筑崩塌） |
| 时间感 | 停滞、永恒的现在 | 灾变后的未来 |
| 情感 | 静默、沉思 | 求生、紧张、荒凉 |
| 叙事 | 无叙事（纯氛围） | 有叙事（发生了灾难） |

### 9.6 砼核 vs 池核 (Poolcore)

| 维度 | 砼核 | 池核 |
|------|------|------|
| 核心空间 | 混凝土建筑巨构 | 游泳池/水上设施 |
| 材质 | 粗粝混凝土 | 瓷砖、水体 |
| 可交叉 | ✅ 巨构中的空泳池 = 交叉 | - |

### 9.7 交叉地带

以下为砼核可与其他美学安全交叉的场景：

| 交叉美学 | 场景 | 示例 Prompt 方向 |
|----------|------|-----------------|
| **砼核 × 雨核** | 雨中的巨构建筑 | wet concrete surfaces, rain streaks, puddles reflecting structure |
| **砼核 × 池核** | 巨构内部的空游泳池 | empty pool inside brutalist hall, still water, tile + concrete |
| **砼核 × 植核** | 被蕨类/苔藓轻度入侵的混凝土 | moss-covered concrete, ferns in cracks, nature gently reclaiming |
| **砼核 × 雪核** | 积雪覆盖的混凝土巨构 | snow-covered brutalist structure, white dusting on grey |

> **不可交叉**：砼核 × 赛博朋克（霓虹灯光毁掉荒芜感）、砼核 × 蒸气波（粉色滤镜毁掉冷峻感）

---

## 10. 正面关键词列表 (Prompt Positive)

### 10.1 英文关键词（按类别）

#### 空间与建筑
```
brutalist architecture, concrete megastructure, monumental scale,
vast empty hall, endless corridor, liminal space, underground chamber,
symmetrical composition, one-point perspective, towering concrete walls,
board-formed concrete, béton brut, exposed concrete surfaces,
monolithic structure, repeating arches, grand staircase, subterranean passage,
institutional architecture, colossal columns, cathedral-like void
```

#### 材质与肌理
```
weathered concrete, raw concrete texture, water stains on concrete,
rust stains, moss patches, efflorescence, concrete spalling,
exposed aggregate, wooden formwork marks, rough unfinished surface,
industrial materials, terrazzo floor, metal railings
```

#### 光线与氛围
```
overcast sky, diffused ambient light, foggy atmosphere, mist through concrete,
atmospheric haze, cold fluorescent lighting, shaft of light from above,
god rays through skylight, dim institutional light, twilight gloom,
soft shadows, muted lighting, low contrast, gloomy atmosphere
```

#### 色彩
```
desaturated colors, muted grey tones, cold grey palette,
grey concrete tones, earthy brown accents, rust orange hints,
monochromatic, subdued color grading, bleak color scheme
```

#### 情绪与气氛
```
desolate, abandoned, empty, uninhabited, silent, silent giant,
oppressive atmosphere, eerie stillness, peaceful desolation,
post-human, timeless, melancholic, contemplative, solitary,
overwhelming scale, awe-inspiring, sublime dread
```

#### 构图技巧
```
tiny figure for scale, miniature human against massive structure,
aerial perspective, looking up, worm's eye view,
vanishing point, infinite depth, layered depth,
negative space, architectural void, framing within frames
```

#### 环境细节
```
overgrown concrete, vines on walls, small plants in cracks,
puddles on floor, damp surfaces, cold humid air,
industrial decay without collapse, standing water,
fallen leaves on concrete, dust motes in light beam
```

### 10.2 中文关键词（按类别）

#### 空间与建筑
```
粗野主义建筑，混凝土巨构，巨大尺度，空旷大厅，
无尽走廊，阈限空间，地下空间，对称构图，
单点透视，高耸混凝土墙，木模混凝土，裸露混凝土，
巨型结构，重复拱门，巨大楼梯间，地下通道，
公共机构建筑，如大教堂般的空洞，巨柱
```

#### 材质与肌理
```
风化混凝土，粗糙混凝土纹理，水渍，锈迹，苔藓，
混凝土剥落，木模板纹理，未完成的粗糙表面，
工业材料，水磨石地面，金属扶手
```

#### 光线与氛围
```
阴天，漫射光，雾气，雾中建筑，大气散射，
冷白荧光灯，天窗光束，上帝光，昏暗灯光，
暮色，柔影，低对比度，阴郁氛围，微光
```

#### 色彩
```
去饱和，灰调，冷灰色系，混凝土灰，土棕色点缀，
锈橙色，单色调，克制的色彩，荒芜色调
```

#### 情绪
```
荒芜，废弃，空旷，无人，寂静，巨人的沉默，
压抑，诡异的寂静，平静的荒芜，后人类，
永恒，忧郁，沉思，孤独，压倒性尺度，敬畏
```

#### 构图
```
渺小人物，尺度对比，俯视，仰视，消失点，
无限延伸，层次纵深，负空间，建筑的空洞，框中框
```

#### 环境细节
```
混凝土上的植被，藤蔓爬墙，裂缝中的植物，地面水洼，
潮湿表面，冷湿空气，工业衰败（不坍塌），
积水，落叶散落混凝土上，光束中的尘埃
```

---

## 11. 负面关键词列表 (Prompt Negative)

### 11.1 禁止风格（最高优先级）

这些词一旦出现，会**完全破坏砼核美学的核心氛围**：

```
NEON LIGHTS, CYBERPUNK, NEON NOIR, LED STRIPS, COLORFUL LIGHTING,
SCI-FI, FUTURISTIC TECH, HOLOGRAMS, FLYING CARS, ROBOTS,
STEAMPUNK, DIESELPUNK, SOLARPUNK, VAPORWAVE, SYNTHWAVE,
FANTASY, MAGICAL, SURREAL (过度的), DREAMLIKE (过度柔美的),
HIGH CONTRAST, HDR, GLOSSY, POLISHED, LUXURY,
WARM COZY, HOME, COMFORT, LIVED-IN,
CROWDED, PEOPLE, BUSY, ACTIVE, LIVELY
```

### 11.2 避免滑向的相邻美学

| 滑向目标 | 触发词（应避免） | 表现 |
|----------|-----------------|------|
| **赛博朋克** | neon, hologram, cyberpunk, rain at night, city lights | 霓虹街景，未来科技 |
| **梦核（过度）** | dreamy, soft glow, pastel, nostalgic playground | 粉彩色调，童年场景 |
| **纯废墟** | collapsed, destroyed, ruined, post-war, rubble | 建筑坍塌、破坏 |
| **建筑摄影** | architectural photography, clean lines, perfect geometry, minimalist | 干净整洁的建筑纪实照 |
| **恐怖怪核** | creepy, monster, ghost, blood, dark shadows, horror | 恐怖元素 |
| **自然风光** | beautiful landscape, sunset, mountain, forest, lake | 以自然为主体的照片 |
| **太阳能朋克** | solar panels, green walls, eco-friendly, bright future | 绿色生态未来 |

### 11.3 材质相关禁止

```
smooth polished concrete, perfect finish, clean modern,
glass curtain wall, steel frame, aluminum panels,
wood interior, warm wood, carpet, wallpaper,
mirrors, reflective surfaces, chrome
```

### 11.4 光线相关禁止

```
sunny day, bright sunlight, golden hour (过度温暖的),
rainbow, colorful lights, party lights,
complete darkness, pitch black, horror lighting,
studio lighting, product photography lighting
```

### 11.5 情绪相关禁止

```
happy, cheerful, energetic, playful, fun, joyful,
romantic, cute, beautiful (过于甜美的), pretty,
terrifying, disgusting, gory, violent
```

---

## 12. Prompt 构建模板

### 12.1 基础模板（KPE 适用）

```
[主要建筑场景], [光线条件], [材质细节], [情绪氛围],
[尺度参照], [色彩处理], [构图方式]
```

### 12.2 示例 Prompt

#### 示例 1：地下神殿

```
vast underground concrete chamber, colossal columns in symmetrical rows,
water on the floor reflecting dim light, shaft of light from distant ceiling opening,
board-formed concrete texture with water stains, rusty metal railings,
desolate and silent atmosphere, tiny solitary figure standing at the far end for scale,
overcast ambient light filtering down, desaturated cold grey tones,
one-point perspective, atmospheric haze, eerie stillness,
weathered concrete surfaces, puddles reflecting the columns
```

#### 示例 2：山间巨构

```
monumental brutalist megastructure embedded in mountainside,
overcast sky with fog rolling through the concrete arches,
weathered raw concrete with moss patches and rust stains,
worm's eye view looking up, towering walls disappearing into mist,
tiny figure walking on a distant bridge for scale,
muted grey-green tones, diffused flat light, no shadows,
repeating archways creating rhythmic depth,
atmosphere of sublime dread and peaceful desolation,
vines creeping along the lower walls, damp surfaces
```

#### 示例 3：无尽走廊

```
endless symmetrical concrete corridor, fluorescent lights buzzing overhead,
one-point perspective vanishing into infinite depth,
raw concrete walls with board-form texture, terrazzo floor with puddles,
water stains running down the walls, rust on metal door frames,
cold institutional atmosphere, oppressive silence,
no people, no furniture, no signs of recent human presence,
desaturated grey-blue color grading, harsh cold white light,
liminal space aesthetic, the feeling of being somewhere you shouldn't be
```

#### 示例 4：巨构雾中仰视

```
looking up at colossal brutalist tower from ground level,
three-point perspective emphasizing impossible height,
fog shrouding the upper floors, building disappearing into grey sky,
weathered concrete facade with vertical water streaks,
rust bleeding from exposed rebar near the base,
tiny birds circling at mid-height revealing the true scale,
overcast muted light, cold desaturated palette,
overwhelming sense of insignificance, the silence of giants,
industrial decay without collapse, standing water at the base
```

### 12.3 风格权重组配（推荐配比）

在为 KPE 构建 prompt 时，建议按以下权重分配关键词：

| 类别 | 权重 | 说明 |
|------|------|------|
| 空间/建筑类型 | 30% | 决定"这是什么地方" |
| 光线/氛围 | 25% | 决定"这是什么时间/天气/感觉" |
| 材质/肌理 | 20% | 决定"表面是什么质感" |
| 色彩/调色 | 10% | 决定"画面的色调" |
| 构图/视角 | 10% | 决定"从什么角度看" |
| 情绪/叙事 | 5% | 轻量提示画面情绪方向 |

---

## 13. 参考作品与创作者

### 13.1 主要创作者（中文互联网）

| 创作者 | 平台 | 特点 |
|--------|------|------|
| **C-EXCITE 探激** | Bilibili / Pinterest | 砼核美学核心创作者，《巨人的沉默》系列 |
| **药厂人家** | Bilibili | 砼核/粗野主义深度解析，「我们喜欢的是巨构，还是被允许的无力感？」 |
| **史蒂芬怪** | Bilibili | Concretecore 解析，「当建筑不再为人而存在」 |
| **巨构 AI** | Bilibili | 「巨构：文明退场后」「巨构：当万物静止」系列 AI 作品 |
| **核艺术 bot** | Bilibili | 核类美学综合创作 |

### 13.2 现实建筑参考

| 建筑 | 地点 | 参考价值 |
|------|------|----------|
| **首都圏外郭放水路** | 日本埼玉 | "地下神殿"，砼核地下空间的原型 |
| **巴比肯中心 (Barbican Centre)** | 英国伦敦 | 粗野主义城市综合体，连廊与平台 |
| **布伦瑞克中心 (Brunswick Centre)** | 英国伦敦 | 粗野主义住宅/商业巨构 |
| **南斯拉夫纪念碑 (Spomeniks)** | 前南斯拉夫各国 | 超尺度抽象混凝土纪念碑 |
| **法国共产党总部** | 法国巴黎 | 奥斯卡·尼迈耶，混凝土曲线巨构大厅 |
| **波士顿市政厅** | 美国波士顿 | 典型粗野主义政府建筑 |
| **蒙特利尔 Habitat 67** | 加拿大蒙特利尔 | 模块化混凝土住宅巨构 |
| **俄罗斯/东欧粗野主义建筑群** | 前苏联各国 | 各种超尺度居住/公共建筑 |
| **首钢遗址（冬季）** | 中国北京 | 工业巨构的"雪中废墟" |

### 13.3 虚构作品参考

| 作品 | 类型 | 参考价值 |
|------|------|----------|
| **少女终末旅行** | 动画 | 文明退场后的多层巨构城市 |
| **BLAME!** | 漫画 | 无尽混凝土巨构城市，后人类氛围 |
| **The Backrooms** | 网络 Creepypasta | 阈限空间/无限重复空间的原型 |
| **Control（控制）** | 游戏 | 粗野主义建筑的"不可能空间" |
| **NaissanceE** | 游戏 | 纯混凝土阈限空间探索 |
| **安藤忠雄建筑（适度参考）** | 建筑 | 混凝土质感参考，但避免"太干净" |
| **《潜行者》(1979)** / **《牺牲》(1986)** | 电影 | 塔可夫斯基的荒芜/沉静氛围 |

### 13.4 关键搜索词（用于扩展研究）

- Bilibili 搜索：「砼核」「Concretecore」「巨构 阈限空间」「巨人的沉默」
- Pinterest 搜索：「Brutalist Megastructure」「Liminal Brutalism」「Concrete Aesthetic」
- Reddit：r/LiminalSpace, r/brutalism
- Steam 创意工坊：Wallpaper Engine 搜索「砼核」

---

## 附录：快速参考卡片

### A. 一句话定义

> **砼核 = 荒芜无人的巨构混凝土建筑 + 阈限空间氛围 + 阴天/雾中/荧光灯光线 + 风化粗粝的材质 + 渺小人物尺度参照 + 冷灰去饱和色调 + "巨人的沉默"情绪**

### B. 5秒判断法

问这 5 个问题判断一张图是否"砼核"：

1. 有人吗？→ **没人（或仅作尺度参照的渺小剪影）**
2. 建筑是什么？→ **巨大的混凝土建筑**
3. 光线如何？→ **阴天/雾/荧光灯/天窗光束**
4. 色彩如何？→ **低饱和冷灰，无鲜艳色**
5. 建筑状态如何？→ **完好但有风化痕迹，不坍塌**

> 5 个全中 → 砼核 ✅

### C. 最简 Prompt 种子

```
desolate brutalist megastructure, overcast foggy atmosphere, weathered concrete,
liminal space, symmetrical infinite corridor, tiny figure for scale,
muted grey tones, no people, oppressive silence, board-formed texture
```

---

*本指南基于 2025-2026 年中文互联网 -core 美学研究整理。*
*核心参考：Bilibili 砼核社区、Aesthetics Wiki、r/LiminalSpace、典藏 ARTouch 阈限空间研究。*
