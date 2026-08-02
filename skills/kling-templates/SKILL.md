---
name: kling-templates
description: "可灵 AI 即用提示词模板库。当用户说'给我一个模板'、'模板'、'给我一个提示词'时触发。覆盖 30+ 场景类型，每个模板可直接编辑使用。"
version: "1.0.0"
---

# kling-templates — 即用模板库

用户不想从零写提示词时，给一个可以编辑的骨架。

## Workflow

1. 识别用户需要的场景类型
2. 加载对应模板骨架
3. 用用户的具体信息填充槽位
4. 运行质量自检（光源、运镜、声音、约束）
5. 输出可直接使用的提示词

## 模板索引

### 产品类

**产品揭示（5s）：**
```
[产品名] 从 [材质/表面] 上缓缓升起，[具体运动描述]。
Camera: [景别], [角度], [运镜]。
Lighting: [具体光源] + [光质]。
Sound: [音效]。
Constraints: No text, no hands, no extra objects.
```

**产品 360°（10s）：**
```
[产品] 悬浮于 [背景描述] 中央，缓慢自转一周。
Camera: 中景，眼平，环绕轨道。
Lighting: [主光] + [轮廓光]。
Sound: [环境音/音乐]。
Constraints: No text, no logos, background stays still.
```

**电商广告（15s）：**
```
0-3秒：[产品特写，展示材质细节]
3-7秒：[使用场景，手持/佩戴/摆放]
7-12秒：[效果展示/对比]
12-15秒：[产品正面 + 品牌落版]
【声音】[节奏感音乐] + [产品音效]
【约束】No text overlay, no watermark
```

### 叙事类

**短剧开场（10s）：**
```
[场景环境], [时间/天气]。[角色描述] [一个具体动作]。
Camera: [景别], [角度], [运镜]。
Lighting: [光源] + [光比/色温]。
Sound: [环境音] + [一个有动机的音效]。
Constraints: No text, no extra people.
```

**情感转折（15s）：**
```
0-5秒：[建立正常状态，温暖/安全]
5-8秒：[触发事件，一个可见变化]
8-12秒：[反应，面部/身体变化]
12-15秒：[新状态确立，价值翻转完成]
【声音】从 [A] 变为 [B]
【约束】No dialogue, no text
```

### 风景/氛围类

**自然风光（10s）：**
```
[地点], [时间], [天气]。[一个自然运动：水流/云动/风吹草]。
Camera: [景别], [运镜]。
Lighting: [自然光源 + 色温]。
Sound: [环境音层次]。
Constraints: No people, no buildings, no text.
```

**城市夜景（10s）：**
```
[城市/街道描述], 夜晚。[一个动态元素：车流/霓虹/行人]。
Camera: [景别], [角度], [运镜]。
Lighting: [人造光源类型 + 色温混合]。
Sound: [城市环境音]。
Constraints: No readable text on signs.
```

### 美食类

**美食特写（5s）：**
```
[食物名称] 的 [具体部位/切面]，[一个物理变化：蒸汽升起/酱汁流淌/切开瞬间]。
Camera: 极近景, 微俯, static 或极缓推进。
Lighting: [侧光/逆光] + [具体光源]。
Sound: [食物音效：切割/沸腾/酥脆]。
Constraints: No hands, no plate text, no utensils.
```

### 科幻/VFX 类

**太空场景（10s）：**
```
[飞船/空间站描述] 以 [速度感] 接近 [天体]。
Camera: [景别], [运镜]。
Lighting: [恒星方向光] + [天体反射光]。
Sound: [低频引擎] + [静默对比]。
Constraints: No text on hull, no lens flare.
```

## 使用规则

- 每个模板是骨架，不是成品——必须用具体描述替换所有 [槽位]
- 填充后必须通过 anti-slop 检查
- 一个模板 = 一个镜头 = 一个节拍
- 多镜头需求：组合多个模板，每个独立生成
