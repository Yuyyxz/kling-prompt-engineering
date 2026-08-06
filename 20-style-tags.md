# 20 — 风格标签系统（Style Tags）

> 风格标签是**起点**，不是终点。

先说清楚这个文件和 [09-反空话词典](09-anti-slop.md) 的关系——09 说"别直接写风格标签"，这个文件就是一堆风格标签。矛盾吗？不矛盾。

09 反对的是：把"Wes Anderson"写进 prompt 就完事。
这个文件做的是：帮你从"Wes Anderson"出发，找到**具体的镜头/光线/构图参数**。

**核心规则：每个风格标签都必须被"翻译"成物理描述后才能写进 prompt。**

标签是搜索词，不是 prompt 词。你用标签找到方向，然后用物理描述锁定画面。

---

## 使用规则

1. **标签 → 翻译 → 写进 prompt。** 先用标签确定方向，再展开成具体的镜头型号、光线方向、构图方式、材质描述。
2. **禁止直接丢标签。** 写"Wes Anderson 风格"不行。写"对称构图，粉彩色调，平面光，镜头匀速横移"才行。
3. **组合不超过两个风格。** 叠三个风格 = 模型不知道听谁的。选一个导演风格 + 一个视觉/情绪风格就够了。
4. **冲突风格不要硬组。** 极简 + 赛博朋克、治愈 + 暗黑哥特——情绪相反的参数会互相抵消。

**翻译示例：**

| 你说的 | 你应该写的 |
|--------|-----------|
| 韦斯·安德森风 | 对称构图，居中主体，粉彩色调，镜头匀速横移，平面柔光 |
| 赛博朋克 | 冷蓝色调，霓虹粉紫光混合，雨天街道反射光，手持轻微晃动 |
| 宫崎骏治愈风 | 暖色调，自然光黄金时刻，缓慢横移，风拂过草地，远景层叠山峦 |

---

## 风格标签库

### 🎬 导演风格

#### 韦斯·安德森（Wes Anderson）
| 参数 | 值 |
|------|-----|
| 构图 | 对称构图，居中主体 |
| 色调 | 粉彩/暖色调，低饱和 |
| 镜头 | 横移、俯拍、whip pan（快速摇镜） |
| 运动 | 平稳横移、whip pan、缓慢推进 |
| 光线 | 均匀柔和光线 |
| 节奏 | 匀速、有节奏感 |
| 提示词 | symmetric composition, pastel colors, centered subject, smooth lateral track, whip pan |
| → 翻译成 prompt | 对称构图，主体居中，粉彩色调（低饱和粉/薄荷绿/奶油黄），镜头匀速横移，平面柔光无硬阴影 |

#### 诺兰（Christopher Nolan）
| 参数 | 值 |
|------|-----|
| 构图 | 不对称构图，前景遮挡 |
| 色调 | 冷色调，高对比 |
| 镜头 | IMAX大画幅，广角，稳定器 |
| 运动 | 快速剪辑，时间线交叉，非手持为主 |
| 光线 | 自然光，低调光 |
| 节奏 | 快慢交替，紧张感 |
| 提示词 | IMAX feel, wide angle, cold tones, high contrast, large format photography |
| → 翻译成 prompt | IMAX 画幅比（1.43:1），20mm 广角镜头畸变，冷蓝色调，高对比度，自然光为主，暗部占画面 60% 以上 |

#### 库布里克（Stanley Kubrick）
| 参数 | 值 |
|------|-----|
| 构图 | 单点透视，对称构图，低角度仰视 |
| 色调 | 冷色调，高饱和 |
| 镜头 | 单点透视，低角度仰视（Kubrick stare），轨道跟踪 |
| 运动 | 缓慢推进，轨道跟踪（tracking shot），对称构图 |
| 光线 | 低调光，强对比 |
| 节奏 | 缓慢，压迫感 |
| 提示词 | one-point perspective, slow tracking shot, low angle looking up, cold tones, low-key lighting, symmetrical |
| → 翻译成 prompt | 单点透视走廊，镜头从低角度仰视，对称构图，冷色调高饱和，低调光强对比，缓慢轨道推进 |

#### 王家卫（Wong Kar-wai）
| 参数 | 值 |
|------|-----|
| 构图 | 框中框，前景遮挡 |
| 色调 | 高饱和，霓虹+暖色 |
| 镜头 | 手持，慢快门，抽帧 |
| 运动 | 手持晃动，慢快门拖影 |
| 光线 | 霓虹灯，混合色温 |
| 节奏 | 慢，情绪化 |
| 提示词 | high saturation, neon + warm tones, handheld, slow shutter, frame skipping |
| → 翻译成 prompt | 框中框构图（门框/窗框前景），高饱和霓虹+暖色混合，手持晃动，慢快门拖影，抽帧跳切 |

#### 宫崎骏（Hayao Miyazaki）
| 参数 | 值 |
|------|-----|
| 构图 | 平视，自然构图 |
| 色调 | 暖色调，柔和色板 |
| 镜头 | 平视，多景别混合（近景表情+中景日常+远景自然） |
| 运动 | 缓慢横移，云/风/水的自然运动，日常细节 |
| 光线 | 自然光，黄金时刻 |
| 节奏 | 缓慢，治愈感 |
| 提示词 | warm tones, soft palette, natural light, gentle movement, wind in hair, flowing water, drifting clouds, everyday details |
| → 翻译成 prompt | 暖色调柔和色板，自然光黄金时刻，缓慢横移，风拂过草地，远景层叠山峦，日常细节特写 |

#### 是枝裕和（Hirokazu Kore-eda）
| 参数 | 值 |
|------|-----|
| 构图 | 平视，自然构图 |
| 色调 | 暖色调，低对比 |
| 镜头 | 固定机位，平视 |
| 运动 | 极少运动，静态 |
| 光线 | 自然光，柔和 |
| 节奏 | 缓慢，日常感 |
| 提示词 | natural light, low contrast, fixed camera, everyday feel, warm tones |
| → 翻译成 prompt | 固定机位平视，自然光低对比，暖色调，日常家庭场景，极少镜头运动 |

#### 大卫·芬奇（David Fincher）
| 参数 | 值 |
|------|-----|
| 构图 | 精确构图，冷色调 |
| 色调 | 暗绿/暗蓝，低饱和 |
| 镜头 | 稳定器，精确运动 |
| 运动 | 平稳推进/横移 |
| 光线 | 低调光，控制精确 |
| 节奏 | 精确，控制感 |
| 提示词 | dark green/blue tones, desaturated, precise camera movement, controlled lighting |
| → 翻译成 prompt | 暗绿/暗蓝色调，低饱和，精确控制的低调光，稳定器缓慢推进，画面冷峻克制 |

#### 塔可夫斯基（Andrei Tarkovsky）
| 参数 | 值 |
|------|-----|
| 构图 | 长镜头，诗意构图 |
| 色调 | 暖色调，胶片质感 |
| 镜头 | 广角，长镜头 |
| 运动 | 极慢长镜头，水元素（雨/雾/倒影） |
| 光线 | 自然光，柔和 |
| 节奏 | 极慢，冥想感 |
| 提示词 | long take, wide angle, poetic composition, film grain, warm tones, very slow movement, water/rain/mist |
| → 翻译成 prompt | 极慢长镜头，广角诗意构图，胶片颗粒质感，暖色调，雨/雾/倒影元素，自然光柔和 |

---

### 🎨 视觉风格

#### 赛博朋克（Cyberpunk）
| 参数 | 值 |
|------|-----|
| 色调 | 冷蓝+霓虹粉/紫 |
| 光线 | 霓虹灯，混合色温 |
| 环境 | 雨天街道，高楼，全息广告 |
| 运动 | 手持，快速剪辑 |
| 提示词 | neon lights, cyberpunk city, rain, holographic ads, cold blue + neon pink |
| → 翻译成 prompt | 冷蓝+霓虹粉紫光混合，雨天湿街道反射光，高楼密集，手持轻微晃动 |

#### 蒸汽朋克（Steampunk）
| 参数 | 值 |
|------|-----|
| 色调 | 暖铜色/棕色 |
| 光线 | 暖色侧光，烟雾 |
| 环境 | 齿轮、管道、蒸汽 |
| 运动 | 缓慢推进，环绕 |
| 提示词 | steampunk, copper/bronze tones, gears, pipes, steam, warm side lighting |
| → 翻译成 prompt | 暖铜色调，齿轮管道蒸汽元素，暖色侧光穿烟雾，缓慢环绕 |

#### 复古胶片（Retro Film）
| 参数 | 值 |
|------|-----|
| 色调 | 暖色调，低饱和 |
| 光线 | 自然光，柔和 |
| 环境 | 70-80年代风格 |
| 运动 | 手持，慢快门 |
| 提示词 | film grain, warm tones, desaturated, 70s aesthetic, vintage look |
| → 翻译成 prompt | 胶片颗粒质感，暖色调低饱和，70年代复古美术，自然光柔和 |

#### 黑色电影（Film Noir）
| 参数 | 值 |
|------|-----|
| 色调 | 黑白/低饱和 |
| 光线 | 高对比，侧光，百叶窗光影 |
| 环境 | 城市夜景，雨天 |
| 运动 | 固定机位，低角度 |
| 提示词 | film noir, high contrast, venetian blind shadows, black and white, low angle |
| → 翻译成 prompt | 黑白低饱和，高对比侧光，百叶窗条纹阴影，低角度仰拍，城市夜景雨天 |

#### 极简主义（Minimalist）
| 参数 | 值 |
|------|-----|
| 色调 | 中性色/黑白 |
| 光线 | 均匀柔和 |
| 环境 | 干净背景，少元素 |
| 运动 | 锁定或极慢推进 |
| 提示词 | minimalist, clean background, neutral colors, simple composition, slow movement |
| → 翻译成 prompt | 干净背景中性色调，画面元素极少，主体居中，锁定或极慢推进 |

#### 超现实（Surreal）
| 参数 | 值 |
|------|-----|
| 色调 | 高饱和，对比色 |
| 光线 | 非自然光线 |
| 环境 | 梦境般场景 |
| 运动 | 缓慢，失重感 |
| 提示词 | surreal, dreamlike, high saturation, unnatural lighting, floating/dreamy motion |
| → 翻译成 prompt | 高饱和对比色，非自然光源（自发光物体），失重缓慢运动，梦境般场景 |

#### 日系清新（Japanese Fresh）
| 参数 | 值 |
|------|-----|
| 色调 | 暖白/淡蓝，高亮度 |
| 光线 | 自然光，柔和 |
| 环境 | 日式街道/室内 |
| 运动 | 平视，缓慢 |
| 提示词 | Japanese aesthetic, soft warm tones, natural light, clean, fresh, airy |
| → 翻译成 prompt | 暖白/淡蓝色调高亮度，自然光柔和，日式街道/室内，平视缓慢移动 |

#### 暗黑哥特（Dark Gothic）
| 参数 | 值 |
|------|-----|
| 色调 | 暗紫/暗红，低饱和 |
| 光线 | 低调光，烛光 |
| 环境 | 哥特建筑，教堂 |
| 运动 | 缓慢推进，环绕 |
| 提示词 | gothic, dark purple/red, low-key lighting, candlelight, gothic architecture |
| → 翻译成 prompt | 暗紫/暗红色调低饱和，烛光低调光，哥特式尖拱/石柱建筑，缓慢推进或环绕 |

---

### 🎵 情绪风格

#### 治愈系（Healing）
| 参数 | 值 |
|------|-----|
| 色调 | 暖色调，柔和 |
| 光线 | 自然光，黄金时刻 |
| 运动 | 缓慢横移，云/风/水 |
| 节奏 | 缓慢，放松 |
| 提示词 | healing, warm tones, golden hour, gentle breeze, slow movement, relaxing |
| → 翻译成 prompt | 暖色调柔和，黄金时刻自然光，微风拂过，缓慢横移，放松节奏 |

#### 紧张悬疑（Suspense）
| 参数 | 值 |
|------|-----|
| 色调 | 冷色调，高对比 |
| 光线 | 低调光，阴影 |
| 运动 | 快速剪辑，手持 |
| 节奏 | 快，紧张 |
| 提示词 | suspense, cold tones, high contrast, low-key lighting, quick cuts, tension |
| → 翻译成 prompt | 冷色调高对比，低调光深阴影，快速剪辑手持晃动，紧张节奏 |

#### 热血燃（Hype）
| 参数 | 值 |
|------|-----|
| 色调 | 高饱和，暖色 |
| 光线 | 强光，逆光 |
| 运动 | 快速跟拍，手持 |
| 节奏 | 快，爆发感 |
| 提示词 | hype, high saturation, fast cuts, backlight, energetic, explosive |
| → 翻译成 prompt | 高饱和暖色调，强光逆光剪影，快速跟拍手持，爆发感剪辑节奏 |

#### 文艺忧郁（Melancholy）
| 参数 | 值 |
|------|-----|
| 色调 | 低饱和，冷灰 |
| 光线 | 阴天，柔和 |
| 运动 | 缓慢，静态 |
| 节奏 | 慢，沉思 |
| 提示词 | melancholy, desaturated, grey tones, overcast, slow movement, contemplative |
| → 翻译成 prompt | 低饱和冷灰色调，阴天漫射柔光，极慢或静态镜头，沉思节奏 |

#### 浪漫（Romantic）
| 参数 | 值 |
|------|-----|
| 色调 | 暖粉/暖橙 |
| 光线 | 黄金时刻，逆光 |
| 运动 | 缓慢推进，环绕 |
| 节奏 | 慢，温柔 |
| 提示词 | romantic, warm pink/orange, golden hour, backlit, gentle movement |
| → 翻译成 prompt | 暖粉/暖橙色调，黄金时刻逆光，发丝/轮廓光晕，缓慢推进或轻环绕 |

#### 宏大叙事（Grand Scale）
| 参数 | 值 |
|------|-----|
| 色调 | 冷色调，高对比 |
| 光线 | 强光，体积光 |
| 运动 | 无人机，摇臂上升 |
| 节奏 | 慢→快，宏大 |
| 提示词 | grand scale, cold tones, volumetric lighting, drone shot, crane up, massive structure |
| → 翻译成 prompt | 冷色调高对比，体积光穿透空间，无人机高空缓降或摇臂上升，巨构建筑/大规模场景 |

---

## 风格组合规则

### 组合公式
```
[导演风格] + [视觉风格] + [情绪风格] = 最终风格
```

### 示例组合

| 组合 | 效果 |
|------|------|
| 韦斯·安德森 + 极简 + 治愈 | 对称构图、粉彩、柔和、治愈感 |
| 诺兰 + 赛博朋克 + 紧张 | IMAX感、霓虹、快速剪辑、紧张感 |
| 宫崎骏 + 日系清新 + 治愈 | 自然光、暖色、缓慢、治愈感 |
| 王家卫 + 复古胶片 + 文艺忧郁 | 手持、胶片质感、慢快门、忧郁感 |
| 库布里克 + 暗黑哥特 + 紧张 | 对称构图、低调光、缓慢推进、压迫感 |

### 冲突规则

以下风格组合会产生冲突，需要手动调整：
- **极简 + 赛博朋克**（极简追求少元素，赛博朋克追求多细节）
- **治愈 + 暗黑哥特**（情绪相反）
- **热血燃 + 文艺忧郁**（节奏相反）

---

## 输出格式

当用户输入风格标签时，输出翻译后的物理描述——不是把标签丢进 prompt：

```
【风格来源】
导演：[导演风格]
视觉：[视觉风格]
情绪：[情绪风格]

【翻译结果】
构图：[具体构图方式]
色调：[具体色调描述]
光线：[具体光线设置]
运动：[具体镜头运动]
节奏：[具体节奏描述]

【最终 prompt】
[用物理描述写成的 prompt，不包含任何风格标签]
```

**注意：** 最终 prompt 里不应该出现"Wes Anderson""赛博朋克"这类标签词。标签已经翻译成具体参数了。

---

## 交叉引用

- 需要**现成的完整配方**（触发词/关键词/负面词/光线/示例）→ [24-prompt-library.md](24-prompt-library.md)（105 风格 + 50 氛围 = 155 条，附模型适配层）
- 需要**风格翻译的完整方法论** → [22-text-to-image.md](22-text-to-image.md)（相机锚定/景深/布光/色彩）
- 本文件 = 标签 → 物理描述的翻译器;24 号 = 已经翻译好的完整配方。两个配合用：先查 24 号有没有现成配方，没有再自己用本文件翻译。
