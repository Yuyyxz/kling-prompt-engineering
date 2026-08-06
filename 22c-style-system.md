# 22C — 风格体系（Style System）

> 文生图 Prompt 工程的 12 种核心风格 + 20+ 扩展风格标签速查。
> 这是拆分的子文件——主入口见 [22-text-to-image.md](22-text-to-image.md)。
> 更完整的风格与氛围配方见 [24-prompt-library.md](24-prompt-library.md)（156 条）。

---

## 风格体系：12 种核心风格

反塑料感不是"不要风格"。是"风格要可控"。

下面 12 种风格覆盖了 90% 的文生图场景。每种给三样东西：关键词组合、相机/后期参数、适用场景。直接抄，改具体数值就能用。

### 1. 写实摄影（Realistic Photography）

```
关键词：natural lighting, natural skin texture, pores visible, unfiltered,
       no over-smoothing, candid, documentary style
相机：Fujifilm X100V, 23mm f/2, 自然色彩模式
后期：Lightroom 自然预设，低对比度，轻微颗粒
```

适合：日常人像、纪实、街拍、生活方式。最安全的风格——选错其他参数也不会翻车太远。

### 2. 电影剧照（Cinematic Still）

```
关键词：cinematic color grading, anamorphic lens flare, shallow depth of field,
       film grain, widescreen aspect ratio 2.39:1
相机：ARRI Alexa Mini + Panavision Anamorphic 35mm，或 Sony Venice + Canon K-35
后期：Teal and orange LUT，暗部偏青，高光偏橙
```

适合：叙事场景、故事分镜、情绪强烈的画面。关键是宽高比——写上 2.39:1 或 2.35:1，画面立刻有"电影"的味道。

### 3. 胶片复古（Film Grain / Vintage）

```
关键词：film grain, vintage, Kodak Portra 400 / Fuji Superia 400 / Kodachrome,
       faded colors, light leak, slight overexposure
相机：Canon AE-1 + 50mm f/1.8 或 Contax T2
后期：暖色调偏移，暗部褪色（lifted blacks），颗粒感
```

Portra 400 出暖肤色，Superia 出冷绿调，Kodachrome 出高饱和红黄。选对胶片型号比写"复古"有用 10 倍。

适合：怀旧人像、复古街拍、90 年代氛围。

### 4. 日系清新（Japanese Soft / Airy）

```
关键词：soft, pastel tones, slightly overexposed, airy, high key,
       gentle bokeh, Fujifilm Astia / Pro Neg Hi
相机：Fujifilm X100V 或 Olympus PEN，28mm 等效
后期：低对比度，高光微过曝，色彩偏粉偏淡
```

适合：少女写真、咖啡甜品、旅行日常、小物件静物。核心是"过曝一档 + 降饱和"。

### 5. 港风（Hong Kong 90s）

```
关键词：90s Hong Kong aesthetic, bleach-bypass, desaturated, high contrast,
       neon reflections on wet streets, Wong Kar-wai mood
相机：Kodak 35mm vintage film，bleach-bypass 处理
后期：去饱和，推高对比度，暗部偏青绿，高光偏琥珀
```

适合：都市夜景、武侠氛围、雨夜街头、暧昧情绪。王家卫的精髓不是霓虹灯——是"潮湿 + 暧昧 + 时间感"。

### 6. 赛博朋克（Cyberpunk）

```
关键词：neon lights, rain-soaked streets, holographic signs, cyberpunk aesthetic,
       blade runner mood, pink and cyan color palette
相机：Sony Venice + Anamorphic lens，宽银幕变形镜头光晕
后期：高饱和霓虹，暗部极暗，青+品红双色主导
```

适合：科幻场景、未来城市、夜店、科技产品。注意：别只堆霓虹灯。加"湿地面反射"和"雾气中的光束"才有层次。

### 7. 中国水墨（Chinese Ink Wash）

```
关键词：Chinese ink painting style, 水墨, ink wash rendering,
       negative space, misty mountains, layered mountains fading into distance,
       brush strokes, rice paper texture
相机：无（非摄影风格）。可加 "traditional scroll painting format"
后期：黑白为主，局部淡彩（花青/赭石），大量留白
```

适合：山水、国风、茶文化、禅意场景。关键不是"画得像水墨"——是留白。留白占画面 30% 以上才对。

### 8. 油画（Oil Painting）

```
关键词：oil painting, impasto technique, visible brushstrokes, rich colors,
       classical composition, Rembrandt lighting, canvas texture
参考：伦勃朗、维米尔、萨金特
后期：厚涂质感，暖色主导，暗部通透不死黑
```

适合：古典肖像、静物、历史场景、庄重氛围。impasto（厚涂）这个词很关键——它让画面有"笔触凸起"的质感，不是平面的。

### 9. 水彩（Watercolor）

```
关键词：watercolor painting, soft edges, flowing colors, paper texture,
       wet-on-wet technique, color bleeding, delicate washes
后期：边缘扩散、颜色渗透、纸纹透出
```

适合：插画、童话、梦幻场景、植物花卉。和油画相反——水彩的精髓是"控制不住"的流动感。

### 10. 概念艺术（Concept Art）

```
关键词：concept art, digital painting, painterly, dramatic lighting,
       matte painting, epic scale, Craig Mullins / Sparth style
相机：无。但可加 "digital matte painting, 4K resolution"
后期：高动态范围，强烈明暗对比，环境光遮蔽
```

适合：游戏场景、奇幻/科幻世界观、环境设计、史诗场面。关键词是"epic scale"——画面里要有尺度参照物（人/树/建筑），不然"史诗"变"壁纸"。

### 11. 动漫（Anime）

```
关键词：anime style, cel-shaded, clean lineart, vibrant colors,
       Makoto Shinkai lighting / Studio Ghibli warmth
参考：新海诚（光影华丽）、吉卜力（温暖自然）、今敏（写实心理）
后期：平涂色块，清晰线稿，天空和光线特别华丽
```

适合：角色设计、插画、故事分镜、二次元风格。新海诚和吉卜力差别很大——新海诚是"光污染级别的华丽"，吉卜力是"安静但温暖"。写清楚。

### 12. 3D 渲染（3D Render）

```
关键词：3D render, Octane render / Arnold, subsurface scattering,
       global illumination, ray tracing, photorealistic CGI
引擎：Octane（偏艺术）、Arnold（偏写实）、Blender Cycles（免费）
后期：SSS 材质让皮肤通透，焦散和反射要真实
```

适合：产品可视化、角色设计、建筑表现、抽象艺术。关键区分：Octane 出图偏"艺术感"（色彩饱和、光线柔美），Arnold 偏"物理正确"。写错引擎名字出来的味道不一样。

### 风格混合规则

可以混。但有规矩：

**能混的：** 写实摄影 + 胶片复古（天然搭配）、电影剧照 + 港风（王家卫就是例子）、概念艺术 + 中国水墨（国风概念艺术）

**别混的：** 动漫 + 写实摄影（风格打架）、油画 + 3D 渲染（质感矛盾）、水彩 + 赛博朋克（除非你想做实验）

混合时，选一个主风格（占 70%），一个辅风格（占 30%）。prompt 里主风格写前面，辅风格写后面。别 50/50——模型会精神分裂。

---


---

## 风格标签速查：20+ 扩展风格库

12 种核心风格覆盖 90% 场景。剩下 10% 在这里。每种风格一行速查，需要时直接复制关键词块。

### 13. 粗野主义建筑（Brutalist Architecture）

```
关键词：brutalist architecture, raw concrete, béton brut, massive geometric forms,
       repetitive modular elements, monumental scale
色彩：混凝土灰、天空灰、苔藓绿
光线：阴天漫射最佳，硬光也可强化体量感
景深：中等景深，建筑整体清晰
适用：建筑摄影、概念设计、砼核美学
相机：24mm 广角仰拍，强化纵向压迫
```

### 14. 蒸汽朋克（Steampunk）

```
关键词：steampunk, brass gears, steam pipes, Victorian machinery,
       clockwork mechanisms, goggles, dirigibles
色彩：黄铜金、深棕、铁锈红、墨绿
光线：钨丝暖光 3000K，体积光穿过蒸汽
景深：中等，机械细节清晰
适用：概念设计、角色设计、奇幻场景
相机：50mm 标准，中等景深
```

### 15. 黑色电影（Film Noir）

```
关键词：film noir, high contrast black and white, deep shadows,
       venetian blind shadows, femme fatale, wet streets, 1940s
色彩：纯黑白，或极低饱和冷色
光线：硬光，百叶窗条纹阴影，单一主光
景深：中等到深景深
适用：犯罪、悬疑、心理题材
相机：35mm，f/4-5.6，深景深
```

### 16. 韦斯安德森（Wes Anderson）

```
关键词：Wes Anderson style, symmetrical composition, pastel palette,
       flat color planes, whimsical props, deadpan expression
色彩：粉彩系：薄荷绿、奶油黄、腮红粉、天蓝
光线：均匀柔光，少阴影
景深：中等景深，画面元素都清晰
适用：喜剧、时尚、产品、生活方式
相机：50mm 正面平拍，严格对称
```

### 17. 超现实主义（Surrealism）

```
关键词：surrealism, dreamlike, impossible geometry, Escher-inspired,
       melting objects, floating elements, juxtaposition of unrelated items
色彩：写实色彩但组合荒诞，或超饱和
光线：正常光线照在荒诞物体上，反差感
景深：深景深，所有荒诞元素都清晰
适用：概念艺术、广告、MV
相机：50mm 标准，深景深
```

### 18. 极简主义（Minimalism）

```
关键词：minimalism, clean lines, negative space, single subject,
       geometric simplicity, reduced palette, no clutter
色彩：1-2 色，大量白/灰
光线：均匀柔光或单一方向硬光
景深：中等到深景深
适用：产品、建筑、平面、高端品牌
相机：50-85mm，f/8，深景深
```

### 19. 哥特式（Gothic）

```
关键词：gothic, pointed arches, ribbed vaults, flying buttresses,
       dark atmosphere, stained glass, gargoyles, verticality
色彩：深灰、黑、暗红、深紫
光线：体积光穿过彩色玻璃，暗调
景深：深景深，建筑细节清晰
适用：建筑、奇幻、恐怖、宗教题材
相机：24mm 仰拍，强化垂直感
```

### 20. 波普艺术（Pop Art）

```
关键词：pop art, Andy Warhol, Roy Lichtenstein, bold colors,
       Ben-Day dots, comic strip, mass culture, repetition
色彩：高饱和原色：红黄蓝+黑线
光线：平光，无阴影，色块分明
景深：无景深概念，平面化
适用：广告、时尚、文化评论
相机：无，平面化处理
```

### 21. 新海诚风格（Makoto Shinkai）

```
关键词：Makoto Shinkai style, hyper-detailed sky, god rays,
       lens flare, vibrant clouds, emotional lighting, rain drops
色彩：高饱和蓝天、橘粉晚霞、翠绿植物
光线：逆光/体积光/镜头光晕，光线华丽
景深：浅到中等，背景天空虚化但云层细节保留
适用：动画场景、青春题材、风景
相机：无，动画渲染
```

### 22. 吉卜力风格（Studio Ghibli）

```
关键词：Studio Ghibli style, warm hand-drawn feel, lush green landscapes,
       fluffy clouds, cozy interiors, gentle characters
色彩：自然饱和，绿色为主，温暖柔和
光线：自然光，柔和温暖
景深：中等，背景细节丰富
适用：治愈系、童话、日常、自然
相机：无，手绘动画渲染
```

### 23. 浮世绘（Ukiyo-e）

```
关键词：ukiyo-e, Japanese woodblock print, flat color areas,
       bold outlines, Hokusai wave, Hiroshige landscape
色彩：靛蓝、朱红、藤黄、墨黑，平涂色块
光线：无光影，平面化
景深：无景深，前后一样清晰
适用：日本题材、装饰画、风格化
相机：无，版画风格
```

### 24. 像素艺术（Pixel Art）

```
关键词：pixel art, 8-bit, 16-bit, retro game aesthetic,
       limited color palette, dithering, sprite
色彩：限制色板（16-256 色）
光线：简化光影，色块过渡
景深：无，平面化
适用：游戏、复古、图标
相机：无，像素化渲染
```

### 25. 等距视角（Isometric）

```
关键词：isometric view, 30-degree angle, no perspective distortion,
       miniature diorama, cutaway view, game asset
色彩：任意，但通常干净明快
光线：均匀光照，少阴影
景深：无，所有面清晰
适用：游戏资产、建筑展示、信息图
相机：无，等距投影
```

### 26. 微距摄影（Macro Photography）

```
关键词：macro photography, extreme close-up, insect eye, water droplet,
       flower detail, texture, 1:1 magnification
色彩：主体真实色，背景虚化成色块
光线：环形闪光灯或柔光，避免硬阴影
景深：极浅，只有主体一小片清晰
适用：产品细节、自然、科学
相机：100mm macro lens, f/2.8, 极浅景深
```

### 27. 航拍（Aerial Photography）

```
关键词：aerial photography, drone shot, bird's eye view,
       top-down, geometric patterns, miniature effect
色彩：真实色彩，或增强饱和度
光线：黄金时刻最佳，长阴影强化地形
景深：深景深，地面全部清晰
适用：风景、城市、地产、环境
相机：无人机，24mm 等效，f/8
```

### 28. 双重曝光（Double Exposure）

```
关键词：double exposure, superimposed images, silhouette filled with landscape,
       overlapping transparencies, dreamlike fusion
色彩：两层图像色彩混合
光线：两层光线独立
景深：两层都清晰或都虚化
适用：概念艺术、海报、音乐封面
相机：两次曝光合成
```

### 29. 移轴摄影（Tilt-Shift）

```
关键词：tilt-shift photography, miniature effect, selective focus band,
       toy-like, compressed perspective
色彩：真实色彩，高饱和
光线：自然光
景深：极浅选择性对焦带，上下虚化
适用：城市微缩、创意风景
相机：tilt-shift lens, f/2.8, 极窄对焦带
```

### 30. 暗角复古（Vignette Vintage）

```
关键词：vintage vignette, darkened corners, faded center,
       old photograph, sepia tone, scratched surface
色彩：棕褐色/褪色暖色
光线：中心亮，四角暗
景深：中等
适用：怀旧、历史题材、老照片效果
相机：老镜头，自然暗角
```

### 31. 高饱和波普（Hyper-Saturated Pop）

```
关键词：hyper-saturated, neon colors, electric blue, hot pink,
       eye-popping contrast, commercial pop
色彩：电光蓝、荧光粉、柠檬黄、亮橙
光线：平光或霓虹光
景深：中等
适用：时尚、音乐、青年文化
相机：50mm, f/4
```

### 32. 单色极简（Monochrome Minimal）

```
关键词：monochrome, single color palette, tonal variation,
       minimal composition, single subject, quiet mood
色彩：一个色相，靠明度拉开层次
光线：柔光，少阴影
景深：中等到深
适用：艺术、品牌、高端产品
相机：85mm, f/5.6
```

### 33. 砼核（Concretecore / 巨构混凝土）

> 网络 -core 美学(2022 至今)。不是粗野主义建筑风格,是**情绪**:荒芜无人的巨构混凝土建筑 + 阈限空间 + "巨人的沉默"。核心不是"这建筑怎么设计",是"这建筑让我感到什么"。

```
触发词：brutalist megastructure + liminal space（两个固定 token 锁定风格）
关键词：brutalist architecture, concrete megastructure, monumental scale,
       vast empty hall, endless corridor, liminal space, underground chamber,
       board-formed concrete, béton brut, weathered concrete, water stains,
       moss on concrete, rust stains, exposed rebar, overcast sky,
       diffused ambient light, foggy atmosphere, shaft of light from above,
       cold fluorescent lighting, tiny figure for scale, desolate, silent,
       one-point perspective, symmetrical composition, desaturated grey tones
负面词（风格防跑偏）：cyberpunk, neon lights, hologram, sci-fi, fantasy,
       dreamy, pastel, vaporwave, collapsed ruins, luxury, cozy warm home,
       glass curtain wall, polished concrete, people, crowded, HDR
色彩：混凝土灰 #B0A99F 主调、铁锈棕 #8B5E3C 点缀、苔藓绿 #5A6E4A 点缀；
      全局低饱和冷灰，暖色只作为光线点缀
光线：阴天漫射（最核心）、雾光、天窗缝隙光、荧光灯冷光；
      避免霓虹/黄金时刻高饱和/HDR
景深：深景深，建筑整体清晰；人物作渺小尺度参照（1-2 人远景剪影）
适用：巨构建筑、阈限空间、后人类氛围、竞赛视频首帧/分镜
不适用（会滑向）：赛博朋克（加霓虹）、梦核（加粉彩柔光）、
       纯废墟（加坍塌）、建筑摄影（加完美几何）
相机：24mm 广角仰拍（压迫感）/ 极远景俯拍（巨物感）/ 对称单点透视（无限感）
```

**和 13 号粗野主义的区别**：13 号是建筑风格（设计语言、功能、几何体量）；33 号是情绪美学（无人、荒芜、风化痕迹、渺小感）。粗野主义可有人的活动，砼核必须无人或仅尺度参照。

**示例 prompt（巨构雾中仰视，完整版带景别+相机锚定）：**
```
极远景，低角度仰拍（worm's-eye view）。一座巨大的粗野主义混凝土巨塔直插灰白天空，
三点透视强化它的高度，塔的上半部分消失在雾里。外立面是风化混凝土，
竖向水渍条纹沿着墙面流下，底部有钢筋锈蚀渗出的锈痕。
建筑中段有几只鸟在盘旋——用它们的渺小反衬巨塔的真实尺度。
光线：阴天均匀漫射光，冷灰低饱和调。地面有积水，倒映着巨塔。
氛围：压倒性的渺小感，巨人的沉默，工业衰败但结构完好、没有坍塌。
镜头：Sony Venice 拍摄，24mm f/8，深景深，全画面清晰。
负面：无霓虹灯，无赛博朋克，无人物特写，无梦幻柔光，无坍塌废墟。
```

英文版（可直接粘贴）：
```
extreme wide shot, worm's-eye view, looking up at colossal brutalist tower from ground level,
three-point perspective emphasizing impossible height,
fog shrouding the upper floors, building disappearing into grey sky,
weathered concrete facade with vertical water streaks,
rust bleeding from exposed rebar near the base,
tiny birds circling at mid-height revealing the true scale,
overcast muted light, cold desaturated palette,
overwhelming sense of insignificance, the silence of giants,
industrial decay without collapse, standing water at the base,
Sony Venice, 24mm, f/8, deep depth of field
```

**完整方法论 → 参考 research/concretecore-style-guide.md（风格全要素/场景清单/相邻美学边界/30+ 关键词分类）**

---

