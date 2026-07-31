# 20 — 风格标签系统（Style Tags）

> 用户说"宫崎骏风"、"赛博朋克"、"韦斯·安德森"，自动映射到具体的镜头/色调/运动/光线参数。

---

## 使用方式

用户输入一个或多个风格标签，系统自动组合对应的镜头语言参数。

**示例：**
- "帮我拍一个产品视频，赛博朋克风" → 冷色调 + 霓虹光 + 低角度 + 手持
- "风景片，宫崎骏治愈风" → 暖色调 + 平视 + 缓慢横移 + 自然光
- "短剧，诺兰悬疑风" → 冷色调 + 高对比 + 快速剪辑 + 不对称构图

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

#### 蒸汽朋克（Steampunk）
| 参数 | 值 |
|------|-----|
| 色调 | 暖铜色/棕色 |
| 光线 | 暖色侧光，烟雾 |
| 环境 | 齿轮、管道、蒸汽 |
| 运动 | 缓慢推进，环绕 |
| 提示词 | steampunk, copper/bronze tones, gears, pipes, steam, warm side lighting |

#### 复古胶片（Retro Film）
| 参数 | 值 |
|------|-----|
| 色调 | 暖色调，低饱和 |
| 光线 | 自然光，柔和 |
| 环境 | 70-80年代风格 |
| 运动 | 手持，慢快门 |
| 提示词 | film grain, warm tones, desaturated, 70s aesthetic, vintage look |

#### 黑色电影（Film Noir）
| 参数 | 值 |
|------|-----|
| 色调 | 黑白/低饱和 |
| 光线 | 高对比，侧光，百叶窗光影 |
| 环境 | 城市夜景，雨天 |
| 运动 | 固定机位，低角度 |
| 提示词 | film noir, high contrast, venetian blind shadows, black and white, low angle |

#### 极简主义（Minimalist）
| 参数 | 值 |
|------|-----|
| 色调 | 中性色/黑白 |
| 光线 | 均匀柔和 |
| 环境 | 干净背景，少元素 |
| 运动 | 锁定或极慢推进 |
| 提示词 | minimalist, clean background, neutral colors, simple composition, slow movement |

#### 超现实（Surreal）
| 参数 | 值 |
|------|-----|
| 色调 | 高饱和，对比色 |
| 光线 | 非自然光线 |
| 环境 | 梦境般场景 |
| 运动 | 缓慢，失重感 |
| 提示词 | surreal, dreamlike, high saturation, unnatural lighting, floating/dreamy motion |

#### 日系清新（Japanese Fresh）
| 参数 | 值 |
|------|-----|
| 色调 | 暖白/淡蓝，高亮度 |
| 光线 | 自然光，柔和 |
| 环境 | 日式街道/室内 |
| 运动 | 平视，缓慢 |
| 提示词 | Japanese aesthetic, soft warm tones, natural light, clean, fresh, airy |

#### 暗黑哥特（Dark Gothic）
| 参数 | 值 |
|------|-----|
| 色调 | 暗紫/暗红，低饱和 |
| 光线 | 低调光，烛光 |
| 环境 | 哥特建筑，教堂 |
| 运动 | 缓慢推进，环绕 |
| 提示词 | gothic, dark purple/red, low-key lighting, candlelight, gothic architecture |

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

#### 紧张悬疑（Suspense）
| 参数 | 值 |
|------|-----|
| 色调 | 冷色调，高对比 |
| 光线 | 低调光，阴影 |
| 运动 | 快速剪辑，手持 |
| 节奏 | 快，紧张 |
| 提示词 | suspense, cold tones, high contrast, low-key lighting, quick cuts, tension |

#### 热血燃（Hype）
| 参数 | 值 |
|------|-----|
| 色调 | 高饱和，暖色 |
| 光线 | 强光，逆光 |
| 运动 | 快速跟拍，手持 |
| 节奏 | 快，爆发感 |
| 提示词 | hype, high saturation, fast cuts, backlight, energetic, explosive |

#### 文艺忧郁（Melancholy）
| 参数 | 值 |
|------|-----|
| 色调 | 低饱和，冷灰 |
| 光线 | 阴天，柔和 |
| 运动 | 缓慢，静态 |
| 节奏 | 慢，沉思 |
| 提示词 | melancholy, desaturated, grey tones, overcast, slow movement, contemplative |

#### 浪漫（Romantic）
| 参数 | 值 |
|------|-----|
| 色调 | 暖粉/暖橙 |
| 光线 | 黄金时刻，逆光 |
| 运动 | 缓慢推进，环绕 |
| 节奏 | 慢，温柔 |
| 提示词 | romantic, warm pink/orange, golden hour, backlit, gentle movement |

#### 史诗感（Epic）
| 参数 | 值 |
|------|-----|
| 色调 | 冷色调，高对比 |
| 光线 | 强光，体积光 |
| 运动 | 无人机，摇臂上升 |
| 节奏 | 慢→快，宏大 |
| 提示词 | epic, cold tones, volumetric lighting, drone shot, crane up, grand scale |

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

当用户输入风格标签时，输出：

```
【风格组合】
导演：[导演风格]
视觉：[视觉风格]
情绪：[情绪风格]

【镜头参数】
构图：[构图方式]
色调：[色调描述]
光线：[光线设置]
运动：[镜头运动]
节奏：[节奏描述]

【提示词】
[完整提示词，包含风格关键词]
```
