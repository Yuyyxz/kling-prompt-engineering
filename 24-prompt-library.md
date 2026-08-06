# Prompt 库 — 风格与氛围大全

> 文生图/图生视频提示词库。每个条目 = 完整配方:触发词 + 关键词 + 负面词 + 光线色彩 + 构图 + 示例 prompt。
> 原则:宁可少而精,不要多而滥。每个条目都经过 prompt_lint 质检(无空话、有光源、有景别、有锚定)。
> 使用方式:复制"示例 prompt"直接粘贴,或用"关键词"自行组合。
> **模型适配**:库内配方为「模型中性」写法,交给哪个模型前先过一遍下方「模型适配层」按模型规则转换。

---

# 模型适配层（Model Adapter Layer）

> 同一个配方,三个模型三种写法。适配规则来自 [adapters/t2i_adapter.yaml](adapters/t2i_adapter.yaml) + 22 号「多模型适配」章节。

## 三模型速查

| 维度 | Kolors（可图） | Qwen Image 3 Pro（通义万相） | Seedream 5.0（即梦） |
|------|---------------|------------------------------|---------------------|
| 最佳长度 | 80-120 字中文 | 长 prompt 吃得下(4500 token) | 要素完整比长度重要 |
| 语言 | 中文为主 | 中英混合,可写细节 | 中英都可,要素齐全 |
| 相机型号 | **别写**——对镜头语言不敏感 | 写,能理解 | 写,能理解 |
| 文字渲染 | 中文文字最强 | 文字排版独一档 | 一般 |
| 擅长 | 中国文化场景/含中文字 | 复杂分镜/多元素 | 写实人像/皮肤质感 |
| 负面词 | 独立参数提交 | 支持 | 支持 |

## 转换三规则

1. **→ Kolors**:砍到 80-120 字,中文描述,删相机型号,质量词结尾(高清,精细,专业品质)
2. **→ Qwen**:可展开全细节(景别/光线/材质/情绪全写),技术词中英混用,相机+焦段保留
3. **→ Seedream**:七个要素缺一不可(主体/场景/光线/风格/构图/色调/镜头)——少一个它自由发挥一个

## 示范:A1 砼核配方 → 三模型

**中性配方**:brutalist megastructure + liminal space, weathered concrete, overcast diffused light, tiny figure for scale, Sony Venice 24mm f/8

- **→ Kolors**:巨大粗野主义混凝土建筑,无人,风化墙面有水流痕迹,阴天漫射光,冷灰调,一个小人影在楼底做尺度对比,高清,精细,专业品质
- **→ Qwen**:extreme wide shot looking up at a colossal brutalist megastructure, board-formed weathered concrete with water stains and moss, overcast diffused lighting, cold desaturated grey palette, a tiny figure at the base for scale, fog shrouding the upper floors, Sony Venice 24mm f/8, deep depth of field, sense of silence and monumental isolation
- **→ Seedream**:主体:巨大粗野主义混凝土巨构建筑;场景:空旷地面,薄雾;光线:阴天均匀漫射;风格:写实摄影,砼核美学;构图:低角度仰视,人物微小;色调:冷灰低饱和;镜头:24mm 广角深景深

**适配口诀**:Kolors 压缩、Qwen 展开、Seedream 补齐。

---

# 第一部分 · 风格系

## A. 经典艺术风格

### A1. 砼核（Concretecore / 巨构混凝土）
- **触发词**:brutalist megastructure + liminal space
- **关键词**:brutalist architecture, concrete megastructure, monumental scale, vast empty hall, endless corridor, liminal space, board-formed concrete, béton brut, weathered concrete, water stains, moss on concrete, rust stains, overcast sky, diffused ambient light, foggy atmosphere, cold fluorescent lighting, tiny figure for scale, desolate, silent, one-point perspective, desaturated grey tones
- **负面词**:cyberpunk, neon lights, hologram, sci-fi, fantasy, dreamy, pastel, vaporwave, collapsed ruins, luxury, cozy, glass curtain wall, polished concrete, people, crowded, HDR
- **光线**:阴天漫射(核心)/雾光/天窗缝隙光/荧光灯冷光
- **色彩**:混凝土灰 #B0A99F 主调,铁锈棕 #8B5E3C / 苔藓绿 #5A6E4A 点缀,全局低饱和冷灰
- **构图**:极远景仰视压迫 / 极远景俯视巨物 / 对称单点透视无限感
- **示例**:extreme wide shot, worm's-eye view, looking up at colossal brutalist tower from ground level, three-point perspective emphasizing impossible height, fog shrouding the upper floors, weathered concrete facade with vertical water streaks, rust bleeding from exposed rebar near the base, tiny birds circling at mid-height revealing the true scale, overcast muted light, cold desaturated palette, the silence of giants, industrial decay without collapse, Sony Venice, 24mm, f/8
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素
- **详见**:research/concretecore-style-guide.md + 22-text-to-image.md「33. 砼核」

### A2. 水墨国风（Chinese Ink Wash）
- **触发词**:Chinese ink painting style
- **关键词**:ink wash rendering, layered mountains, misty clouds, brush strokes, rice paper texture, negative space, breathing room, mountains fading into white mist, traditional Chinese painting
- **负面词**:oil painting, 3d render, photorealistic, vibrant colors, digital art, neon
- **光线**:留白即光,雾霭层次
- **色彩**:墨色浓淡(焦浓重淡清),宣纸白,极少量朱砂/花青点缀
- **构图**:S 形构图,留白 > 实景,远山淡影
- **示例**:traditional Chinese landscape painting, ink wash rendering, layered mountains in different ink densities, pine trees on cliff edges, a small pavilion half-hidden in clouds, negative space, rice paper texture, soft morning mist light, pale sky glow
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A3. 油画古典（Classical Oil Painting）
- **触发词**:classical oil painting
- **关键词**:Rembrandt lighting, chiaroscuro, impasto brushstrokes, canvas texture, rich warm tones, 17th century portraiture, dramatic shadow, Old Master style
- **负面词**:photorealistic, digital art, flat lighting, modern minimalist, anime
- **光线**:伦勃朗光,明暗对照,暖烛光感
- **色彩**:深褐/赭石/鎏金/暗红,厚重层次
- **构图**:三分法,主体受光面朝光源
- **示例**:classical oil painting of a merchant in 17th century Dutch clothing, Rembrandt lighting, chiaroscuro, impasto brushstrokes, canvas texture, rich warm brown and gold tones, dramatic shadow falling across the face
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A4. 浮世绘（Ukiyo-e）
- **触发词**:ukiyo-e style
- **关键词**:Japanese woodblock print, flat color planes, bold outlines, Hokusai, waves, Edo period, grain of woodblock paper
- **负面词**:3d, photorealistic, oil painting, soft gradient shading
- **光线**:平面化,无真实光影
- **色彩**:普鲁士蓝/朱红/山吹黄,高饱和平面色
- **构图**:大胆对角线,装饰性边框
- **示例**:ukiyo-e woodblock print, great wave style, bold blue outlines, flat color planes, Hokusai influence, Edo period aesthetic, grain texture, even flat light with no shadows, high-contrast outline against pale sky
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A5. 赛博朋克（Cyberpunk）※砼核反义词,谨慎混用
- **触发词**:cyberpunk, neon noir
- **关键词**:rain-soaked streets, neon reflections, holographic advertisements, megacity, augmented reality, cybernetic, high contrast, magenta and cyan
- **负面词**:noir (纯黑白), rural, nature, daytime, desaturated
- **光线**:霓虹主光,雨夜反射,紫青对撞
- **色彩**:品红/青/电光蓝,高饱和
- **构图**:拥挤街道,仰视巨楼,密集招牌
- **示例**:cyberpunk city street at night, rain-soaked asphalt reflecting neon signs, holographic ads, crowded megacity, magenta and cyan palette, high contrast, wet reflections, wide shot
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A6. 蒸汽朋克（Steampunk）
- **触发词**:steampunk
- **关键词**:brass gears, steam pipes, Victorian machinery, clockwork mechanisms, goggles, dirigibles, copper and bronze
- **负面词**:modern tech, clean futuristic, neon, minimalism
- **光线**:钨丝暖光,蒸汽体积光
- **色彩**:黄铜金/深棕/铁锈红/墨绿
- **构图**:机械细节特写,齿轮分层
- **示例**:steampunk workshop interior, brass gears and steam pipes, Victorian machinery, clockwork mechanisms, warm tungsten light through steam, copper and bronze tones, intricate mechanical details
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A7. 黑色电影（Film Noir）
- **触发词**:film noir
- **关键词**:high contrast, low-key lighting, venetian blind shadows, cigarette smoke, rain-soaked streets, 1950s detective, monochrome, chiaroscuro
- **负面词**:colorful, bright, daylight, neon, comedy
- **光线**:低调光,强对比,百叶窗影,烟雾
- **色彩**:黑白,深灰阶
- **构图**:斜线构图,人物半脸阴影
- **示例**:film noir scene, detective in trench coat, venetian blind shadows across face, cigarette smoke, high contrast low-key lighting, monochrome, rain-soaked street through window
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A8. 超现实主义（Surrealism）
- **触发词**:surrealism, dreamlike
- **关键词**:melting objects, impossible geometry, floating elements, Dali, Magritte, dream logic, scale distortion, empty sky
- **负面词**:realistic, mundane, coherent architecture, everyday
- **光线**:均匀梦幻光/矛盾光源
- **色彩**:低饱和,单一主调 + 强调色
- **构图**:错位透视,悬浮物体,极端尺度
- **示例**:surrealist scene, a colossal whale floating above a desert highway, impossible scale, dream logic, Dali influence, muted earth tones with one red accent, soft dreamlike light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A9. 极简主义（Minimalism）
- **触发词**:minimalist, minimal composition
- **关键词**:negative space, single subject, clean lines, monochrome, quiet mood, flat color, simplicity
- **负面词**:busy, cluttered, ornate, detailed background, multiple subjects
- **光线**:均匀柔光,少阴影
- **色彩**:单色系,靠明度拉开
- **构图**:大量留白,主体极小/居中
- **示例**:minimalist composition, a single black stone on white sand, vast negative space, clean lines, quiet mood, soft diffused light, monochrome
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A10. 波普艺术（Pop Art）
- **触发词**:pop art
- **关键词**:bold colors, halftone dots, Andy Warhol, comic style, consumer culture, thick outlines, flat colors
- **负面词**:photorealistic, subtle, muted, realistic lighting
- **光线**:平面光,无真实感
- **色彩**:原色对撞,高饱和
- **构图**:重复网格,单主体放大
- **示例**:pop art portrait, bold primary colors, halftone dots, thick black outlines, Andy Warhol style, flat color planes, consumer culture aesthetic, hard studio flash lighting, graphic contrast
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A11. 哥特式（Gothic）
- **触发词**:gothic architecture
- **关键词**:pointed arches, flying buttresses, stained glass, cathedral, gargoyles, dark stone, candlelight, vaulted ceiling
- **负面词**:modern, bright, cheerful, minimalist, glass curtain wall
- **光线**:烛光,彩色玻璃光斑,昏暗
- **色彩**:暗石灰/深蓝紫/彩窗红蓝
- **构图**:仰视拱顶,对称中轴
- **示例**:gothic cathedral interior, pointed arches and vaulted ceiling, stained glass casting colored light, candlelight, gargoyles in shadow, dark stone, solemn atmosphere
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A12. 浮世梦核（Chinese Dreamcore）※中式梦核
- **触发词**:中式梦核, Chinese dreamcore
- **关键词**:千禧年记忆, 旧小区, 老式家具, 斑驳墙面, 阳光斜照, VHS质感, 半透明窗帘, 记忆模糊感, 怀旧不安
- **负面词**:现代建筑, 科幻, 恐怖, 鲜艳, 清晰锐利
- **光线**:过曝柔光,夕阳斜照,记忆感模糊
- **色彩**:米黄/粉彩/褪色,低饱和
- **构图**:日常场景错位,熟悉又陌生
- **示例**:中式梦核, 千禧年旧小区的楼道, 老式防盗门, 斑驳的米黄墙面, 夕阳从窗户斜照进来, 地面有拖把的水痕, VHS质感, 怀旧而微微不安
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A13. 印象派（Impressionism）
- **触发词**:impressionist painting
- **关键词**:visible brushstrokes, loose texture, light and color study, Monet, Renoir, soft edges, plein air, atmospheric color, dappled light, pastel dabs
- **负面词**:photorealistic, sharp edges, dark chiaroscuro, digital airbrush
- **光线**:户外自然光,光斑,薄雾感
- **色彩**:高亮低对比,补色并置(蓝橙/紫黄)
- **构图**:随意截取,非中心构图
- **示例**:impressionist oil painting, Monet style water lilies, visible brushstrokes, dappled light on water, soft edges, plein air color study, pastel dabs of blue and pink, glow of low morning sun, no hard lines, wide landscape view, even natural light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A14. 新艺术运动（Art Nouveau）
- **触发词**:art nouveau
- **关键词**:flowing organic lines, floral motifs, whiplash curves, stained glass, Mucha, decorative borders, gilded details, elegant female figure
- **负面词**:geometric, brutalist, minimal, industrial
- **光线**:平面装饰光,柔和
- **色彩**:金/祖母绿/赭红,装饰性高饱和
- **构图**:对称装饰框,曲线主导
- **示例**:art nouveau poster, Mucha style, flowing organic lines, floral motifs, whiplash curves, elegant female figure with flowing hair, decorative gold border, emerald and ochre palette, stained glass background, soft diffused backlight glow
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A15. 巴洛克（Baroque）
- **触发词**:baroque style
- **关键词**:dramatic chiaroscuro, opulent detail, Caravaggio, rich drapery, gilded frames, intense emotion, heavenly light, grand composition
- **负面词**:minimal, flat lighting, modern, austere
- **光线**:强明暗对照,天光穿透
- **色彩**:深褐/鎏金/宝蓝/绯红
- **构图**:对角线动势,强舞台感
- **示例**:baroque painting, Caravaggio style, dramatic chiaroscuro, a figure in rich crimson drapery caught in heavenly light from above, gilded details, intense emotional expression, opulent dark background, grand diagonal composition
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A16. 国潮插画（Chinese Trendy Illustration）
- **触发词**:国潮, Chinese trendy illustration
- **关键词**:traditional motifs modernized, red and gold, dragon and phoenix, ink lines with flat color, chinoiserie, festive, graphic design, bold shapes
- **负面词**:western style, minimal, muted, realistic photography
- **光线**:平面光,装饰性
- **色彩**:中国红/鎏金/墨黑/青花蓝,高饱和
- **构图**:对称,纹样满铺,中心主体
- **示例**:国潮插画, 中国传统纹样现代化, 龙与凤, 朱红与鎏金配色, 墨线勾勒配平面色块, 装饰性构图, 对称排列, 喜庆而时尚, 平面设计感, 均匀平光无阴影, 无西方写实感
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A17. 立体主义（Cubism）
- **触发词**:cubism
- **关键词**:geometric faceting, multiple perspectives, Picasso, Braque, fragmented planes, monochrome browns, angular forms, abstracted reality
- **负面词**:realistic, smooth, natural colors, soft lighting, romantic
- **光线**:平面光,无立体真实感
- **色彩**:赭褐/灰/墨黑,低饱和几何色块
- **构图**:多视角叠加,几何切面
- **示例**:cubist painting, Picasso style, fragmented geometric planes, multiple perspectives of a guitar, angular forms, monochrome browns and greys, abstracted reality, flat light, no smooth shading
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A18. 野兽派（Fauvism）
- **触发词**:fauvism
- **关键词**:wild color, bold unnatural palette, Matisse, thick brushstrokes, flat perspective, expressive color, pure hues, simplified forms
- **负面词**:muted, naturalistic, realistic skin tone, subtle
- **光线**:平光,色彩即光线
- **色彩**:朱红/钴蓝/明黄/翠绿,纯色直撞
- **构图**:简化形,装饰性平面
- **示例**:fauvist painting, Matisse style, wild unnatural colors, pure red and cobalt blue, thick expressive brushstrokes, flat perspective, simplified forms, color as emotion, no naturalistic tones, broad landscape view, even flat daylight
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A19. 装饰艺术（Art Deco）
- **触发词**:art deco
- **关键词**:geometric symmetry, gold and black, stepped forms, sunburst motifs, luxury, chrome accents, sharp lines, 1920s glamour
- **负面词**:organic curves, rustic, minimal, gothic
- **光线**:强对比,金属反光,舞台光
- **色彩**:黑金/翠绿/深红/象牙白
- **构图**:对称几何,放射状,阶梯造型
- **示例**:art deco style, geometric sunburst pattern, gold and black palette, stepped skyscraper silhouette, chrome accents, sharp symmetrical lines, 1920s luxury, glamorous lighting with metal reflections
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A20. 文艺复兴（Renaissance）
- **触发词**:renaissance
- **关键词**:classical composition, sfumato, Leonardo, Raphael, biblical scenes, warm oil glow, balanced symmetry, ideal beauty, architectural background
- **负面词**:modern, abstract, impressionistic, casual
- **光线**:柔和侧光,sfumato 烟雾渐变
- **色彩**:暖褐/金/深红/群青
- **构图**:金字塔式,中心对称,背景透视
- **示例**:renaissance painting, classical composition, sfumato soft light, a Madonna with child in warm oil tones, balanced symmetry, architectural background with perspective, ideal beauty, deep red and ultramarine robes, gentle chiaroscuro
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A21. 抽象表现主义（Abstract Expressionism）
- **触发词**:abstract expressionism
- **关键词**:gestural brushstrokes, color field, Pollock, Rothko, drips and splashes, emotional color, canvas texture, large scale, non-representational
- **负面词**:realistic, representational, geometric precision, figurative
- **光线**:无光源逻辑,色彩自发光
- **色彩**:大色块对撞,或单色场域渐变
- **构图**:无构图,直觉泼洒/色域分割
- **示例**:abstract expressionism, gestural brushstrokes, Pollock style drips and splashes, emotional color field, layered paint texture, large canvas scale, raw energy, no recognizable subject, Rothko-like deep color blocks, gallery spotlight from above, full-frame composition
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A22. 水彩（Watercolor）
- **触发词**:watercolor painting
- **关键词**:transparent washes, paper texture, soft bleeding edges, wet-on-wet, delicate pigment, light through color, loose sketch, granulation
- **负面词**:oil, thick impasto, photorealistic, hard edges, digital airbrush
- **光线**:留白高光,色彩透光感
- **色彩**:通透淡彩,多层罩染
- **构图**:留白>实景,晕染边缘
- **示例**:watercolor painting, transparent washes, wet-on-wet bleeding, soft edges, paper texture visible, delicate pigment in blues and greens, light through color, loose sketch of a harbor, granulation effect, white paper as highlight
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A23. 涂鸦艺术（Street Graffiti）
- **触发词**:graffiti, street art
- **关键词**:spray paint, bold letters, stencil, urban wall, Banksy, dripping paint, vibrant colors, tags, layered murals, concrete background
- **负面词**:clean gallery, minimal, corporate design, polished
- **光线**:街头日光/黄昏霓虹,涂鸦在墙上
- **色彩**:荧光橙/青/粉,高饱和撞色
- **构图**:墙面为主体,涂鸦满铺或单点
- **示例**:graffiti street art, spray paint mural on concrete wall, bold stencil figure, dripping paint, vibrant orange and cyan, layered tags, urban texture, Banksy influence, evening street light on the wall
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A24. 低多边形（Low Poly）
- **触发词**:low poly, lowpoly
- **关键词**:geometric triangles, flat facets, stylized 3d, minimal detail, clean shapes, vibrant flat colors, video game aesthetic, polygon mesh
- **负面词**:photorealistic, smooth surface, high detail, realistic texture
- **光线**:硬边光影,无渐变
- **色彩**:平面亮色,每面一色
- **构图**:几何造型,对称或散点
- **示例**:low poly style, geometric triangle facets, a deer made of flat polygons, vibrant flat colors, clean shapes, stylized 3d game aesthetic, hard-edged shadows, minimal detail, polygon mesh visible, even studio light, centered subject
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A25. 洛可可（Rococo）
- **触发词**:rococo
- **关键词**:ornate curves, pastel gold, playful cherubs, floral decoration, Watteau, luxury salon, shell motifs, soft romantic, lighthearted
- **负面词**:dark, minimal, austere, modern
- **光线**:柔和粉彩光,无硬影
- **色彩**:粉彩+鎏金+象牙白
- **构图**:S 形曲线,装饰满铺
- **示例**:rococo style, ornate pastel interior, gold floral curves, playful cherubs on the ceiling, shell motifs, salon with silk drapery and marble, soft romantic light, ivory and blush pink with gold, lighthearted elegance, wide interior view, even soft glow
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A26. 新古典主义（Neoclassicism）
- **触发词**:neoclassicism
- **关键词**:heroic figures, classical columns, austere symmetry, David, ideal forms, marble, dramatic historical scene, restrained palette
- **负面词**:ornate, pastel, playful, baroque excess
- **光线**:强明暗侧光,雕塑感
- **色彩**:大理石灰+深褐+暗红,克制
- **构图**:对称稳定,古典三角
- **示例**:neoclassical painting, heroic figure in classical setting, marble columns, austere symmetry, ideal forms, restrained palette of grey and deep red, dramatic side light, sculptural quality, historical gravitas
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A27. 浪漫主义（Romanticism）
- **触发词**:romanticism painting
- **关键词**:sublime nature, stormy seas, dramatic sky, emotional intensity, Turner, Delacroix, wild landscape, heroic struggle, vivid emotion
- **负面词**:calm, restrained, minimal, documentary
- **光线**:风暴光,破云光,强烈天空层次
- **色彩**:墨蓝/暖金/深红,浓烈
- **构图**:对角线动势,自然压倒人
- **示例**:romanticism painting, Turner style stormy sea, dramatic sky with breaking light, a small ship in wild waves, emotional intensity, sublime nature overwhelming man, vivid warm light against dark clouds, turbulent energy
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A28. 表现主义（Expressionism）
- **触发词**:expressionism
- **关键词**:distorted forms, emotional color, exaggerated perspective, Munch, angular shapes, inner feeling, anxiety, raw brushwork, stark contrast
- **负面词**:realistic, calm, beautiful, harmonious
- **光线**:非自然光,情绪化明暗
- **色彩**:高对比撞色,焦虑色调
- **构图**:扭曲透视,失衡
- **示例**:expressionist painting, Munch style, distorted figure on a bridge, emotional swirling sky, exaggerated perspective, raw brushwork, stark color contrast, inner anxiety made visible, unsettling energy, wide view, harsh unnatural light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A29. 点彩派（Pointillism）
- **触发词**:pointillism
- **关键词**:tiny dots, optical mixing, Seurat, dots of pure color, divisionism, distance reveals image, scientific color, stippled texture
- **负面词**:smooth gradients, blended strokes, photorealistic
- **光线**:均匀日光,无渐变
- **色彩**:纯色点密集,光学混合
- **构图**:点阵铺满,远景清晰
- **示例**:pointillism, Seurat style, a riverside scene made of tiny dots of pure color, optical mixing, stippled texture, even daylight, dots of blue yellow and red, divisionism, image resolves at distance
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A30. 未来主义（Futurism）
- **触发词**:futurism
- **关键词**:speed, motion blur, dynamic lines, Boccioni, machine age, fragmented motion, angular energy, industrial power, movement trails
- **负面词**:static, calm, traditional, pastoral
- **光线**:动态光,速度感
- **色彩**:钢灰+红橙能量色
- **构图**:对角线冲刺,重复动势
- **示例**:futurist painting, Boccioni style, a racing train with fragmented motion lines, dynamic diagonal composition, speed and energy, machine age aesthetic, angular forms, motion trails, industrial power, bold red and steel grey, dynamic directional light, full-frame action view
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A31. 包豪斯（Bauhaus）
- **触发词**:bauhaus
- **关键词**:geometric shapes, primary colors, functional design, grid layout, sans-serif typography feel, Kandinsky, clean lines, form follows function, abstract geometry
- **负面词**:ornate, organic curves, baroque, decorative excess
- **光线**:均匀平面光
- **色彩**:红黄蓝+黑白灰
- **构图**:几何网格,非对称平衡
- **示例**:bauhaus style, geometric composition of circles squares and triangles, primary colors red yellow blue with black and white, clean grid layout, functional design, Kandinsky influence, non-symmetric balance, flat even light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开画面细节;→Seedream 补齐七要素

### A32. 敦煌壁画（Dunhuang Mural）
- **触发词**:敦煌, Dunhuang mural
- **关键词**:flying apsaras, Buddhist art, cave painting, mineral pigments, gold leaf, Tang dynasty, lotus patterns, painted ceiling, aged fresco, celestial musicians
- **负面词**:modern, western, photorealistic, minimal
- **光线**:洞窟幽光,金箔反光
- **色彩**:赭红/石青/石绿/金箔
- **构图**:飞天飘带,对称神像,满铺纹样
- **示例**:敦煌壁画, 飞天神女衣带飘舞, 石青石绿与赭红矿物颜料, 金箔点缀, 莲花纹样, 唐代风格, 洞窟墙面的年代剥落感, 宝相花边饰, 庄重华美, 幽光下的金箔微亮
- **适配**:→Kolors 中文最优;→Qwen 展开纹样细节;→Seedream 要素齐全

### A33. 工笔重彩（Gongbi Meticulous）
- **触发词**:工笔, gongbi
- **关键词**:fine brush lines, meticulous detail, mineral color, silk painting, Tang-Song style, court painting, gold accents, bird-and-flower, delicate washes
- **负面词**:sketchy, loose, impressionist, modern abstract
- **光线**:平光,绢面柔和
- **色彩**:石青/朱砂/藤黄,矿物色沉稳
- **构图**:精细勾线,留白,均衡
- **示例**:工笔重彩, 绢本设色, 精细勾线的花鸟, 石青与朱砂矿物颜料, 金粉点缀, 唐宋院体画风, 纤毫毕现的羽毛, 丝绸质感, 沉稳华贵, 平光柔和
- **适配**:→Kolors 中文最优;→Qwen 展开勾线细节;→Seedream 要素齐全

### A34. 剪纸（Chinese Paper Cutting）
- **触发词**:剪纸, paper cutting
- **关键词**:red paper, intricate cutout patterns, folk art, symmetry, window decoration, zodiac animals, auspicious symbols, hollowed design
- **负面词**:3d, photorealistic, colored complex, modern minimal
- **光线**:透光,红色剪纸贴窗
- **色彩**:中国红为主,纸白
- **构图**:对称,满铺纹样,负形镂空
- **示例**:剪纸, 红色镂空窗花, 精细对称图案, 生肖动物造型, 吉祥纹样, 民间艺术, 透光效果, 纸面质感, 镂空负形, 喜庆传统
- **适配**:→Kolors 中文最优;→Qwen 展开纹样细节;→Seedream 要素齐全

### A35. 木版年画（New Year Woodblock Print）
- **触发词**:年画, woodblock print
- **关键词**:door gods, vibrant folk colors, New Year auspicious, coarse woodblock lines, Chinese folk art, festive symbols, bright red gold
- **负面词**:minimal, muted, modern digital, realistic photo
- **光线**:平面光,民俗喜庆
- **色彩**:大红/金黄/翠绿/桃粉,高饱和
- **构图**:对称门神,满铺装饰
- **示例**:木版年画, 门神像, 粗犷木刻线条, 大红与金黄配色, 吉祥符号, 民俗喜庆, 高饱和平面色, 纸面印刷质感, 传统节庆气氛, 对称中景构图, 均匀平光
- **适配**:→Kolors 中文最优;→Qwen 展开线条细节;→Seedream 要素齐全

### A36. 青花瓷（Blue and White Porcelain）
- **触发词**:青花, blue and white porcelain
- **关键词**:cobalt blue on white, porcelain glaze, Ming dynasty, floral scroll patterns, crackle texture, ceramic shine, underglaze painting
- **负面词**:colorful glaze, modern design, rough clay, photorealistic people
- **光线**:瓷面反光,柔光
- **色彩**:钴蓝+瓷白
- **构图**:器物居中,缠枝纹样,留白
- **示例**:青花瓷, 白瓷钴蓝, 缠枝莲纹, 明代风格, 釉面光泽, 开片纹理, 器形典雅, 柔光下的瓷面反光, 素净高雅
- **适配**:→Kolors 中文最优;→Qwen 展开纹样细节;→Seedream 要素齐全

### A37. 极简 Zine 海报（Minimal Zine Poster）
- **触发词**:minimal zine poster, editorial zine, quiet paper poster
- **关键词**:tall vertical 3:5 paper canvas, huge negative space, old paper texture, tiny visual anchor, sparse typography, one high-chroma color anchor, risograph grain, xerox softness, halftone, scanned-paper look, flat orthographic, matte paper, ink bleed, aged paper mottling, serif/typewriter microtext
- **负面词**:full-bleed scene, commercial headline, product ad, logo, glossy mockup, clean UI white, cinematic lighting, 3D render, neon, cute cartoon, dense scrapbook, too many colors, long clean text blocks, hard shadow, depth of field
- **光线**:均匀漫射,平扫光感,无硬影,无景深
- **色彩**:纸色+灰黑基底,支撑**一个**高饱和色锚(钴蓝/群青/柠檬黄/翠绿,占画面 0.8-2.5%,缩略图可见),主色锚不降饱和
- **构图**:70-90% 留白;一个视觉簇占 8-25%,居中/中上/中下/左下/右上,不贴边
- **示例**:tall vertical 3:5 paper poster, full-frame aged paper, 80 percent empty negative space, a small visual cluster occupying 15 percent placed lower-left, flat front-facing composition; a torn-paper clipping of a rainy old bookstore as the anchor, xerox softness, halftone grain, ink bleed at the torn edge; tiny serif type pressing against the image edge, one fully saturated cobalt-blue ink block behind the text, risograph misregistration, aged paper mottling; flat orthographic scanned-paper view, diffuse light, no shadow, no 3D, no neon, no commercial headline
- **适配**:→Kolors 压缩为中文描述(留白+色锚);→Qwen 展开四段式细节(画布/锚点/字体/纹理);→Seedream 要素齐全(构图比例写清楚)

---

## B. 电影/导演风格

### B1. 韦斯·安德森（Wes Anderson）
- **触发词**:wes anderson style
- **关键词**:symmetric composition, pastel colors, centered subject, flat camera, quirky set design, meticulous staging, vintage aesthetic
- **负面词**:asymmetric, dark, realistic grittiness, handheld shake
- **光线**:均匀柔和,平面感
- **色彩**:粉彩低饱和(粉/薄荷绿/奶油黄)
- **构图**:严格对称,居中,正面平拍
- **示例**:wes anderson style, symmetric composition, pastel color palette, centered subject in vintage hotel lobby, flat camera angle, meticulous staging, quirky details, soft even lighting
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B2. 诺兰（Christopher Nolan）
- **触发词**:nolan style, IMAX feel
- **关键词**:large format, wide angle, cold tones, high contrast, natural light, practical effects, gravity-defying, monumental scale
- **负面词**:neon, colorful, playful, sitcom lighting
- **光线**:自然光,低调光
- **色彩**:冷蓝灰,高对比
- **构图**:广角畸变,人物小环境大
- **示例**:nolan style, IMAX large format, wide angle lens distortion, cold blue tones, high contrast, monumental architecture dwarfing a tiny figure, natural light, practical feel
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B3. 王家卫（Wong Kar-wai）
- **触发词**:wong kar wai style
- **关键词**:high saturation, neon + warm tones, handheld, slow shutter, frame skipping, close-up, rain, cigarette smoke, longing atmosphere
- **负面词**:clean, bright daylight, static tripod, documentary
- **光线**:霓虹混合色温,慢门拖影
- **色彩**:高饱和霓虹+暖色对撞
- **构图**:框中框,前景遮挡,特写
- **示例**:wong kar wai style, high saturation neon and warm tones, handheld camera, slow shutter motion blur, close-up of a woman in rain, cigarette smoke, longing atmosphere, frame skipping
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B4. 塔可夫斯基（Andrei Tarkovsky）
- **触发词**:tarkovsky style
- **关键词**:long takes, natural elemental, water rain earth, slow meditative pace, muted color, religious iconography, vast landscapes, ruined spaces
- **负面词**:fast cutting, bright commercial, colorful, dialogue-driven
- **光线**:自然光,雾,潮湿感
- **色彩**:土黄/灰绿/暗褐,低饱和
- **构图**:缓慢横移,人物渺小于自然
- **示例**:tarkovsky style, vast misty landscape with a lone figure, extreme wide shot, wet earth and rain, muted earth tones, slow meditative composition, ruined wooden structure, natural elemental atmosphere, low overcast light
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B5. 宫崎骏（Hayao Miyazaki）
- **触发词**:ghibli style, miyazaki style
- **关键词**:hand-drawn animation, soft watercolor backgrounds, lush nature, whimsical, warm palette, detailed mechanical, floating clouds, gentle light
- **负面词**:photorealistic, dark, gritty, neon, horror
- **光线**:自然光,黄金时刻,柔光
- **色彩**:暖色柔和色板,清新绿/天空蓝
- **构图**:平视,多景别,自然融入
- **示例**:ghibli style, hand-drawn animation, lush green valley with whimsical small house, soft watercolor background, warm golden light, floating clouds, detailed grass blades, gentle peaceful mood
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B6. 新海诚（Makoto Shinkai）
- **触发词**:shinkai style, makoto shinkai
- **关键词**:hyper-detailed sky, volumetric clouds, lens flare, vivid blue, light rays, cityscape, romantic longing, bokeh
- **负面词**:flat sky, muted, desaturated, gloomy
- **光线**:逆光,丁达尔,光斑
- **色彩**:高饱和蓝天,黄昏橙紫渐变
- **构图**:天空占 2/3,人物小,远景大
- **示例**:shinkai style, hyper-detailed cumulus clouds, vivid blue sky with light rays, lens flare, distant cityscape, small figure on hill, romantic longing mood, bokeh
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B7. 昆汀（Quentin Tarantino）
- **触发词**:tarantino style
- **关键词**:bold saturated colors, trunk shot, retro cars, diner neon, 70s grain, close-up on eyes, pop culture props, stylized violence, dialogue tension
- **负面词**:muted, realistic boring, modern clean, desaturated
- **光线**:霓虹+钨丝混合,硬光
- **色彩**:高饱和红黄,复古暖调
- **构图**:低角度仰视,特写循环,车内/餐桌场景
- **示例**:tarantino style, retro 70s diner interior, bold saturated red and yellow, neon sign glow, trunk shot angle, close-up on eyes, vintage car outside, film grain, stylized tension, pop culture props
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B8. 是枝裕和（Hirokazu Kore-eda）
- **触发词**:kore-eda style, 是枝裕和
- **关键词**:natural everyday, warm family moments, soft window light, handheld gentle, shallow depth, quiet observation, domestic details, muted warm tones
- **负面词**:dramatic, stylized, high contrast, action
- **光线**:窗边自然柔光,黄昏暖光
- **色彩**:低饱和暖调,米白/木褐
- **构图**:固定机位长镜,日常局部特写
- **示例**:kore-eda style, family dinner scene in small apartment, soft window light, gentle handheld, shallow depth of field, quiet observation of everyday gesture, warm muted tones, domestic details, tender stillness
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B9. 希区柯克（Alfred Hitchcock）
- **触发词**:hitchcock style
- **关键词**:suspense composition, vertigo spiral, dutch angle, voyeuristic framing, dramatic backlight, silhouette, doppelganger, staircase, birds on wire
- **负面词**:bright comedy, flat lighting, cheerful, action-packed
- **光线**:低调光,剪影背光,强轮廓光
- **色彩**:冷灰蓝+强暗部,西装黑
- **构图**:荷兰角,楼梯螺旋,窗框窥视
- **示例**:hitchcock style, dutch angle of a man on spiral staircase, voyeuristic window framing, dramatic backlight creating silhouette, cold grey-blue tones, suspense composition, birds flying across window, tension in the air
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B10. 大卫·林奇（David Lynch）
- **触发词**:lynch style, david lynch
- **关键词**:suburban dread, uncanny Americana, red curtain, distorted reality, humming sound, dream logic, wood paneling, harsh neon in daylight, surreal small town
- **负面词**:clean narrative, bright cheerful, straightforward, realistic drama
- **光线**:过曝日光+室内昏光,不自然混合
- **色彩**:褪色美国郊区别墅色,红帘/绿草反常饱和
- **构图**:对称但失衡,缓慢推镜感,异常细节
- **示例**:lynch style, suburban american street in harsh daylight, red curtain in an open doorway, wood paneled living room with odd shadow, uncanny normalcy, dream logic, distorted reality, humming atmosphere, surreal small town dread
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B11. 斯皮尔伯格（Steven Spielberg）
- **触发词**:spielberg style
- **关键词**:wonder and awe, lens flare, backlit silhouettes, magical golden light, childlike wonder, grand adventure, practical effects, glowing horizon, gentle music feel
- **负面词**:dark gritty, cynical, flat lighting, horror
- **光线**:逆光+镜头光晕,黄金时刻,发光地平线
- **色彩**:暖金/天空蓝,高光灿烂
- **构图**:剪影望向光,人物小世界大
- **示例**:spielberg style, backlit silhouette of a boy on a bicycle against a glowing sunset horizon, lens flare, warm golden light, sense of wonder and adventure, practical feel, childlike awe, magical atmosphere
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B12. 维伦纽瓦（Denis Villeneuve）
- **触发词**:villeneuve style
- **关键词**:monolithic scale, minimalist composition, desert vastness, muted earth tones, sound design implied, slow grandeur, stark geometry, dust and silence
- **负面词**:colorful, fast-paced, cluttered, neon
- **光线**:硬朗侧光,沙漠尘光,低调
- **色彩**:沙黄/土灰/墨黑,极低饱和
- **构图**:巨物居中,人物极小,对称或留白
- **示例**:villeneuve style, colossal monolith in vast desert, minimalist composition, tiny human figure for scale, stark geometry, muted sand and grey tones, hard side light, dust in the air, slow grandeur, oppressive silence
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B13. 库布里克（Stanley Kubrick）
- **触发词**:kubrick style
- **关键词**:one-point perspective, symmetrical hallways, wide angle, cold precision, slow tracking, unsettling perfection, clinical lighting, repeating patterns
- **负面词**:handheld chaos, warm cozy, casual, colorful
- **光线**:冷白均匀光,无菌感
- **色彩**:冷白/金属灰/深黑,高对比克制
- **构图**:严格对称,单点透视走廊
- **示例**:kubrick style, symmetrical hallway with one-point perspective, cold white even lighting, repeating doors, wide angle lens, unsettling perfection, clinical atmosphere, a lone figure at the vanishing point, precise composition
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B14. 黑泽明（Akira Kurosawa）
- **触发词**:kurosawa style
- **关键词**:weather as drama, wind in grass, rain battle, dramatic clouds, wide compositions, movement within frame, samurai, lens flare, epic staging
- **负面词**:static, indoor, flat lighting, modern city
- **光线**:自然光+风/雨/云动势
- **色彩**:墨色+大地色+天空强烈层次
- **构图**:宽幅群像,人物错落,天气主导
- **示例**:kurosawa style, samurai on a hilltop, wind bending tall grass, dramatic clouds rolling, rain beginning, wide composition with multiple figures, weather as drama, natural light, grand staging, movement within frame
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B15. 姜文（Jiang Wen）
- **触发词**:jiang wen style, 姜文
- **关键词**:bold satire, warm nostalgic, exaggerated performance, dramatic contrast, period setting, masculine energy, sun-drenched, playful violence, operatic
- **负面词**:subtle, realistic restraint, documentary, cold
- **光线**:强烈日光,硬阴影,暖调
- **色彩**:暖黄/红/高饱和,怀旧戏剧感
- **构图**:中近景压迫,夸张角度
- **示例**:jiang wen style, sun-drenched courtyard in 1930s Beijing, exaggerated operatic composition, warm yellow light with hard shadows, bold colors, period setting, playful tension, bravado, nostalgic drama
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B16. 奉俊昊（Bong Joon-ho）
- **触发词**:bong joon-ho style
- **关键词**:class satire, dramatic shifts, basement to penthouse, social tension, moody interiors, rain, claustrophobic framing, dark humor, precise staging
- **负面词**:bright comedy, flat, simple, optimistic
- **光线**:明暗分区(地下室暗/上层亮),雨天冷光
- **色彩**:暗绿/冷灰+局部暖
- **构图**:阶级对比构图,楼梯纵深
- **示例**:bong joon-ho style, contrast between a dark basement room and a bright upper-class living room, rain outside window, claustrophobic framing, social tension, precise staging, cold grey light in basement and warm light above, dark humor implied, class divide visible in architecture, two-level interior view
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B17. 斯科塞斯（Martin Scorsese）
- **触发词**:scorsese style
- **关键词**:fast cuts, handheld energy, urban grit, voiceover feel, slow motion violence, neon streets, 70s grain, close-up faces, restless camera
- **负面词**:static, clean, pastoral, slow meditative
- **光线**:城市混合光,霓虹+街灯
- **色彩**:暗红/土黄/深蓝,粗粝
- **构图**:手持晃动,特写群像,跟拍
- **示例**:scorsese style, urban street at night, handheld camera energy, close-up faces in neon light, slow motion moment, 70s film grain, gritty atmosphere, restless composition, city heat and tension
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

### B18. 雷德利·斯科特（Ridley Scott）
- **触发词**:ridley scott style
- **关键词**:sci-fi noir, atmospheric haze, monumental spaces, backlit smoke, industrial gloom, xenomorph shadow, commercial sheen, vast interiors
- **负面词**:bright clean, cozy, playful, simple
- **光线**:背光+烟雾体积光,工业冷光
- **色彩**:暗金属/青灰+荧光点缀
- **构图**:巨厅透视,烟雾层次,剪影
- **示例**:ridley scott style, vast industrial interior with haze, backlit figure in smoke, monumental scale, sci-fi noir mood, cold metal and teal tones, shafts of light through grates, oppressive grandeur, gloom, wide hall view, volumetric light through smoke
- **适配**:→Kolors 删镜头型号写中文场景;→Qwen 展开光线/运动细节;→Seedream 要素齐全

---

## C. 建筑/空间风格

### C1. 粗野主义（Brutalism）※砼核的建筑版
- **触发词**:brutalist architecture
- **关键词**:raw concrete, béton brut, massive geometric forms, repetitive modular elements, monumental scale
- **负面词**:ornate, glass curtain wall, cozy, wood interior, polished
- **光线**:阴天漫射,硬光强化体量
- **色彩**:混凝土灰,天空灰,苔藓绿
- **构图**:24mm 广角仰拍,纵向压迫
- **示例**:brutalist architecture, raw concrete massive geometric forms, repetitive modular balconies, monumental scale, overcast sky, hard shadow on one facade, 24mm wide angle from below
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C2. 后末日废土（Post-Apocalyptic）
- **触发词**:post-apocalyptic, wasteland
- **关键词**:overgrown ruins, abandoned city, rusted vehicles, dust, collapsed buildings, nature reclaiming, desolate highway, survivors' camp, muted brown-grey
- **负面词**:clean, futuristic tech, neon, crowded, pristine
- **光线**:扬尘昏黄,破云光柱,烟霾
- **色彩**:土黄/锈棕/灰绿,低饱和
- **构图**:废墟中渺小人物,引导线
- **示例**:post-apocalyptic wasteland, extreme wide shot, overgrown abandoned city ruins, rusted vehicles half-buried in dust, collapsed skyscrapers, nature reclaiming concrete, dusty haze, muted brown-grey tones, lone survivor walking the highway, harsh noon light through dust
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C3. 阈限空间（Liminal Space）※砼核的空间版
- **触发词**:liminal space, liminalcore
- **关键词**:empty transition space, infinite corridor, vacant pool, abandoned mall, fluorescent lighting, no people, uncanny familiarity, the backrooms
- **负面词**:people, furniture, lived-in, cozy, colorful decor
- **光线**:荧光灯冷白,均匀无影
- **色彩**:冷白/米黄,褪色感
- **构图**:单点透视,对称,无限延伸
- **示例**:liminal space, empty mall corridor at closing time, fluorescent lights, polished floor reflecting, no people, no signs of life, uncanny familiarity, one-point perspective, eerie stillness
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C4. 巨构城市（Megacity）
- **触发词**:megacity, megastructure
- **关键词**:colossal cityscape, towering megastructures, aerial perspective, endless urban sprawl, scale contrast, tiny figures, monumental urbanism
- **负面词**:rural, single building, flat skyline, cozy
- **光线**:蓝时/黄昏,城市灯光,雾
- **色彩**:冷蓝灰+暖窗灯点缀
- **构图**:航拍极远景,尺度对比
- **示例**:megacity aerial view, colossal megastructures towering to the sky, endless urban sprawl fading into fog, tiny figures on plaza for scale, blue hour, cold blue-grey with warm window lights, monumental urbanism
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C5. 中式园林（Chinese Garden）
- **触发词**:Chinese classical garden, 中式园林
- **关键词**:rockery, moon gate, pavilion, lattice window, koi pond, mist, bonsai, bamboo, curved eaves, poetic atmosphere
- **负面词**:modern glass, western palace, crowded, neon
- **光线**:晨雾柔光,月光,灯笼暖光
- **色彩**:黛瓦白墙,竹青,木褐,水影
- **构图**:框景(月洞门/花窗),借景,留白
- **示例**:Chinese classical garden, white wall and dark tiles, rockery with moss, moon gate framing bamboo, koi pond with mist, lattice window, morning soft light, poetic quiet atmosphere, ink-wash color palette
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C6. 废墟神庙（Ruined Temple）
- **触发词**:ruined temple, ancient ruins
- **关键词**:crumbling columns, broken statues, overgrown stone, dappled light, sacred decay, moss, fallen blocks, eternal silence
- **负面词**:modern, restored, bright, tourist-filled, pristine
- **光线**:树影斑驳,斜阳穿林
- **色彩**:石灰+苔绿+暖金斜光
- **构图**:柱列透视,仰视断柱
- **示例**:ruined ancient temple, crumbling marble columns, broken statue half-covered in moss, dappled sunlight through trees, overgrown stone blocks, sacred decay, eternal silence, warm gold light on grey stone
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C7. 太空港（Spaceport）
- **触发词**:spaceport, space station
- **关键词**:massive docking bay, spacecraft, industrial corridors, panoramic space view, launch towers, engineering scale, cold metal and glass, orbital station
- **负面词**:cyberpunk neon, fantasy, steam, medieval
- **光线**:舷窗硬光,空间站冷白照明
- **色彩**:金属灰/深空黑+舷窗蓝
- **构图**:巨构对比小人,对称轴线
- **示例**:spaceport interior, massive docking bay with a spacecraft, industrial catwalks, panoramic window showing planet below, launch tower, engineering scale, tiny technicians for scale, cold metal and glass, hard window light, symmetrical axis
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C8. 江南水乡（Jiangnan Water Town）
- **触发词**:江南水乡, Jiangnan water town
- **关键词**:whitewashed walls, black tiles, stone bridge, canal, gondola, willows, misty morning, lanterns, water reflection, rain
- **负面词**:modern skyscraper, desert, neon, western
- **光线**:晨雾柔光,黄昏灯笼暖光,雨幕
- **色彩**:黛瓦白墙/青灰水面/红灯笼点缀
- **构图**:河道透视,拱桥框架,倒影对称
- **示例**:江南水乡, 白墙黛瓦沿河而建, 石拱桥跨过河道, 乌篷船停靠, 晨雾弥漫, 水面倒影, 柳枝垂落, 几点红灯笼, 青灰调, 宁静诗意, 雨后湿润感
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C9. 徽派建筑（Huizhou Architecture）
- **触发词**:徽派, Huizhou architecture
- **关键词**:horse-head walls, white plaster, black tiles, carved gate, courtyard, ink landscape, ancestral hall, wood carvings, mountain village
- **负面词**:modern glass, skyscraper, colorful, western
- **光线**:晨雾天光,黄昏暖檐
- **色彩**:白墙/黛瓦/青灰/木褐
- **构图**:马头墙层叠,天井框景,远山衬景
- **示例**:徽派建筑, 粉墙黛瓦马头墙, 层叠的白色山墙在晨雾中, 青灰瓦檐, 木雕门楼, 天井院落, 远处青山如黛, 墨色氛围, 静谧古村, 晨光透过薄雾
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C10. 地中海小镇（Mediterranean Town）
- **触发词**:mediterranean, greek island
- **关键词**:whitewashed walls, blue domes, narrow alleys, bougainvillea, terracotta, sea view, stone steps, sun-washed, Santorini
- **负面词**:grey, industrial, modern skyscraper, cold
- **光线**:正午阳光,海面反光,蓝白强对比
- **色彩**:纯白/圣托里尼蓝/陶土橙/三角梅紫红
- **构图**:阶梯巷道,圆顶天际线,海景纵深
- **示例**:mediterranean town, whitewashed houses with blue domes, narrow stone alleys with bougainvillea, terracotta pots, sea view in the distance, bright noon sunlight, strong blue-white contrast, Santorini feel, sun-washed colors
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C11. 日式建筑（Japanese Architecture）
- **触发词**:japanese architecture, 和風
- **关键词**:sliding shoji screens, tatami room, torii gate, wooden engawa veranda, zen garden, koi pond, curved roof tiles, lanterns, wabi-sabi
- **负面词**:western, modern glass, colorful, ornate
- **光线**:纸门透光,竹影,黄昏灯笼
- **色彩**:木褐/纸白/青苔绿/墨
- **构图**:框景(门/窗),对称,低视角
- **示例**:japanese architecture, tatami room with sliding shoji screens, light diffusing through rice paper, wooden engawa veranda, zen garden with raked sand, low angle view, wabi-sabi, warm wood and paper white, quiet elegance
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C12. 未来都市（Neo-Futuristic City）
- **触发词**:neo-futurism, futuristic city
- **关键词**:sleek curves, white and glass, vertical gardens, floating transport, clean geometry, sky bridges, biophilic design, utopian skyline, soft ambient glow
- **负面词**:cyberpunk grime, neon overload, dystopian decay, steam
- **光线**:柔和环境光,大面积发光面板
- **色彩**:白/浅灰+玻璃蓝绿+植被绿
- **构图**:仰视曲线楼,空中廊桥透视
- **示例**:neo-futuristic city, sleek curved white buildings with vertical gardens, sky bridges between towers, floating transport pods, soft ambient glow, clean geometry, utopian skyline, glass and greenery, bright airy atmosphere
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C13. 哥特式教堂（Gothic Cathedral）
- **触发词**:gothic cathedral
- **关键词**:ribbed vaults, pointed arches, flying buttresses, rose window, stained glass, towering nave, stone columns, cathedral light
- **负面词**:modern, minimal, glass tower, cozy
- **光线**:彩窗透光,烛光,高窗天光
- **色彩**:石灰+彩窗红蓝+烛金
- **构图**:仰视拱顶,中轴对称,纵深
- **示例**:gothic cathedral interior, ribbed vaults and pointed arches, towering nave, rose window casting colored light, stone columns receding, candlelight, solemn height, stained glass glow, symmetric axis
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C14. 拜占庭（Byzantine）
- **触发词**:byzantine architecture
- **关键词**:mosaic domes, golden interior, pendentives, Hagia Sophia, gilded icons, marble columns, arched windows, holy light, intricate tile
- **负面词**:minimal, wooden, modern, gothic
- **光线**:穹顶光环,金色反射
- **色彩**:金箔/深蓝/砖红+马赛克
- **构图**:仰视穹顶,对称中轴,马赛克满铺
- **示例**:byzantine interior, golden mosaic dome, Hagia Sophia style, pendentives, gilded icons, marble columns, arched windows, warm holy light reflecting off gold, deep blue and red mosaics, grand symmetry
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C15. 福建土楼（Fujian Tulou）
- **触发词**:福建土楼, tulou
- **关键词**:circular earthen building, concentric rings, communal courtyard, clay walls, wooden balconies, tiled roofs, mountain valley, ancient fortress home
- **负面词**:modern, glass, skyscraper, western
- **光线**:天井光,黄昏暖墙
- **色彩**:夯土黄/青瓦灰/木褐
- **构图**:圆形中庭透视,环形楼层,仰视
- **示例**:福建土楼, 圆形夯土建筑, 环形木结构楼层, 天井中庭, 青瓦屋顶, 山间谷地, 黄昏暖光打在土墙上, 古朴厚重, 俯视可见完整圆环, 家庭堡垒的岁月感
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C16. 摩天大楼（Skyscraper）
- **触发词**:skyscraper, high-rise
- **关键词**:glass curtain wall, steel frame, vertical lines, observation deck, looking down, looking up, cloud level, city grid below, reflective facade
- **负面词**:low-rise, rural, horizontal, cozy
- **光线**:玻璃反光,高空日光/城市夜景
- **色彩**:玻璃蓝绿+钢灰+天空
- **构图**:仰视通天,俯视城市网格,对角线
- **示例**:skyscraper looking up from street level, glass curtain wall reflecting clouds, vertical lines converging to sky, steel frame visible, dizzying height, city below, blue-grey glass tones, modern verticality, sense of scale, bright reflected daylight
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C17. 地下防空洞（Underground Bunker）
- **触发词**:underground bunker, fallout shelter
- **关键词**:concrete walls, bare bulbs, metal bunks, air ducts, emergency light, stocked shelves, cold damp, utilitarian, sealed heavy door
- **负面词**:cozy, modern, bright, decorated
- **光线**:裸露灯泡冷光,应急灯绿光
- **色彩**:混凝土灰+铁锈+应急绿
- **构图**:纵深通道,门框透视,压抑低顶
- **示例**:underground bunker interior, raw concrete walls, bare bulbs hanging, metal bunks in rows, air ducts along ceiling, dim emergency light, stocked shelves, cold damp atmosphere, heavy sealed door, utilitarian gloom
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

### C18. 灯塔（Lighthouse）
- **触发词**:lighthouse
- **关键词**:lone tower, cliff edge, rotating beam, storm waves, white and red stripes, keeper's cottage, beacon light, sea mist, isolation
- **负面词**:city, bright sunny inland, crowded
- **光线**:光束旋转,月光/风暴光
- **色彩**:白塔+红条+墨蓝海
- **构图**:塔立悬崖,光束扫海,低角度
- **示例**:lighthouse on a cliff, white tower with red stripes, rotating beam sweeping the dark sea, storm waves below, sea mist, keeper's cottage at the base, isolation and duty, moonlight breaking through clouds, dramatic coastal light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开空间细节;→Seedream 要素齐全

---

## D. 网络美学（-core 系）

### D1. 梦核（Dreamcore）
- **触发词**:dreamcore, dreamlike nostalgia
- **关键词**:nostalgic childhood space, soft glow, pastel colors, VHS texture, memory blur, familiar yet strange, playground, school corridor, old mall, warm but uneasy
- **负面词**:sharp focus, modern, scary, dark horror, neon
- **光线**:过曝柔光,记忆感模糊
- **色彩**:粉彩低饱和,米黄/粉/薄荷绿
- **构图**:日常场景错位,熟悉又陌生
- **示例**:dreamcore aesthetic, empty 90s school corridor, soft overexposed light from window, pastel colors, VHS texture, nostalgic but slightly unsettling, familiar yet strange, no people, memory-like blur
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D2. 怪核（Weirdcore）
- **触发词**:weirdcore
- **关键词**:low quality, glitch, uncanny, distorted, cryptic text, out of place, unsettling, liminal, analog distortion, eerie collage
- **负面词**:clean, polished, beautiful, coherent, high quality
- **光线**:过曝/欠曝,不自然光
- **色彩**:褪色/灰绿/局部鲜艳
- **构图**:失衡,拼贴感,违和元素
- **示例**:weirdcore image, low quality analog photo, glitch distortion, a bedroom with a tree growing through the floor, cryptic handwritten text, uncanny unsettling mood, faded colors, distorted perspective, harsh unnatural flash lighting
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D3. 雨核（Raincore）
- **触发词**:raincore
- **关键词**:heavy rain, wet reflections, window raindrops, blurred city, cozy inside, moody sky, water droplets, grey-blue tones, rain sound
- **负面词**:sunny, dry, bright cheerful, harsh shadows
- **光线**:阴雨漫射,室内暖灯
- **色彩**:冷灰蓝+室内暖光
- **构图**:窗内看外,雨中街道,水洼倒影
- **示例**:raincore, heavy rain on window glass, blurred city outside, a warm lamp glowing inside the room, water droplets running down, cold grey-blue tones with warm indoor light, wet reflections, close-up through window, shallow depth of field
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D4. 池核（Poolcore）
- **触发词**:poolcore
- **关键词**:empty swimming pool, still water, tiles, reflection, indoor pool light, echo, chlorine blue, liminal water, vacant
- **负面词**:crowded, beach, sunny fun, people swimming
- **光线**:天窗光,水面反光
- **色彩**:池水蓝绿+瓷砖白
- **构图**:俯视水面,对称泳道,空无一人
- **示例**:poolcore, empty indoor swimming pool, perfectly still turquoise water, white tile walls, skylight reflection on water surface, no people, echo of silence, liminal atmosphere, blue-green tones
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D5. 植核（Plantcore）
- **触发词**:plantcore, overgrown
- **关键词**:plants reclaiming, moss covered, vines on structures, greenhouse, lush greenery, nature takeover, humid, ferns, botanical ruins
- **负面词**:desert, dead, sterile, minimal
- **光线**:温室散射光,叶影
- **色彩**:深绿/苔绿/雾白
- **构图**:植被前景框架,爬藤引导线
- **示例**:plantcore, abandoned greenhouse overgrown with ferns and vines, moss covering concrete paths, lush green everywhere, humid atmosphere, soft diffused light through glass, nature reclaiming, deep greens
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D6. 中式梦核（Chinese Dreamcore）
- **触发词**:中式梦核, Chinese dreamcore
- **关键词**:千禧年记忆, 旧小区, 老式家具, 斑驳墙面, 阳光斜照, VHS质感, 半透明窗帘, 记忆模糊感, 怀旧不安
- **负面词**:现代建筑, 科幻, 恐怖, 鲜艳, 清晰锐利
- **光线**:过曝柔光,夕阳斜照,记忆感模糊
- **色彩**:米黄/粉彩/褪色,低饱和
- **构图**:日常场景错位,熟悉又陌生
- **示例**:中式梦核, 千禧年旧小区的楼道, 老式防盗门, 斑驳的米黄墙面, 夕阳从窗户斜照进来, 地面有拖把的水痕, VHS质感, 怀旧而微微不安
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D7. 旧核（Oldcore / 复古核）
- **触发词**:oldcore, retro core
- **关键词**:1950s-80s nostalgia, old photographs, CRT TV, wood paneling, vintage tech, family album, retro kitchen, warm decay, forgotten era
- **负面词**:modern clean, futuristic, sharp digital, neon cyberpunk
- **光线**:旧照片泛黄光,CRT 荧幕光
- **色彩**:棕褐/米黄/褪色红,暖旧调
- **构图**:家庭旧物堆叠,电视/收音机时代道具
- **示例**:oldcore aesthetic, 1980s family living room, wood paneling walls, CRT television glowing, retro kitchen appliances, faded family photos on shelf, warm decay, forgotten era, vintage texture, brown and beige tones
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D8. 云核（Cloudcore）
- **触发词**:cloudcore
- **关键词**:floating islands, clouds below, soft dreamy sky, surreal altitude, lone structure on cloud, gentle pastel, weightless, ethereal
- **负面词**:dark, stormy, grounded, gritty, neon
- **光线**:高空柔光,云海反照
- **色彩**:云白/天空蓝/淡金
- **构图**:云海为地平,悬浮主体,留白
- **示例**:cloudcore, a small white chapel floating on a cloud sea, wide shot, soft dreamy sky, pastel blue and gold, ethereal weightless atmosphere, clouds below as horizon, gentle surrealism, lone structure, airy composition, high-altitude soft light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D9. 伤核（Traumacore）
- **触发词**:traumacore
- **关键词**:childhood hurt, broken toys, faded photos, soft violence, melancholy innocence, band-aids, tear-stained, nursery rhymes, gentle decay
- **负面词**:happy, bright cheerful, clean, polished, aggressive gore
- **光线**:过曝软光,记忆碎片感
- **色彩**:粉彩褪色+灰暗局部,婴儿蓝粉
- **构图**:童年物件特写,孤立主体,负空间
- **示例**:traumacore, a worn teddy bear on a nursery floor, faded pastel pink, tear stains on its fur, broken crayons scattered, soft overexposed light, melancholy innocence, gentle decay, nostalgic hurt, quiet sadness
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D10. 天使核（Angelcore）
- **触发词**:angelcore
- **关键词**:soft white wings, halo glow, heavenly light, marble statues, clouds, ethereal purity, white lace, church light, serene beauty
- **负面词**:dark, gothic horror, gritty, neon, sinful
- **光线**:天窗圣光,柔白光晕
- **色彩**:纯白/浅金/天蓝,高调明亮
- **构图**:仰视圣像,羽毛飘落,对称
- **示例**:angelcore, white marble angel statue in soft heavenly light, halo glow, delicate wings, white lace and light fabric, clouds outside the window, ethereal purity, serene beauty, warm golden-white palette, gentle holy atmosphere
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D11. 梦境核（Dreamlike Liminal）
- **触发词**:dreamlike liminal, 梦境阈限
- **关键词**:unreal architecture, floating rooms, impossible stairs, corridor to nowhere, soft fog, muted pastel, gravity defied, quiet wonder
- **负面词**:grounded, realistic physics, dark horror, gritty
- **光线**:均匀梦幻光,无影
- **色彩**:灰白/雾蓝/淡粉,低饱和
- **构图**:悬浮结构,无尽延伸,错位透视
- **示例**:dreamlike liminal, a floating staircase in a fog-filled hall, impossible architecture, corridor leading to nowhere, soft diffused light, muted pastel tones, gravity defied, quiet wonder, surreal but calm
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D12. 蒸汽波（Vaporwave）
- **触发词**:vaporwave, 蒸汽波
- **关键词**:pink and cyan grid, chrome statues, roman busts, neon sunset, retro computer, glitch text, tape deck, mall aesthetic, nostalgic 80s digital, VHS scanlines
- **负面词**:natural color, photorealistic, warm film, modern clean
- **光线**:霓虹紫粉+青蓝,荧光感
- **色彩**:品红/青蓝/紫,高饱和荧光
- **构图**:地平线网格,居中雕像,对称
- **示例**:vaporwave, pink and cyan grid horizon, chrome roman bust statue, neon sunset gradient, retro computer interface, glitch text, VHS scanlines, 80s digital nostalgia, mall aesthetic, purple-pink glow, surreal synthetic mood
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D13. 噩梦核（Nightmarecore）
- **触发词**:nightmarecore
- **关键词**:dark shadows, twisted forms, childhood fear, corrupted innocence, dim nightmare light, distorted toys, black and red, uncanny horror, dread
- **负面词**:bright, cheerful, cozy, clean, comedic
- **光线**:昏暗,阴影吞噬,红光局部
- **色彩**:黑+暗红+褪色局部
- **构图**:失衡,阴影笼罩,扭曲主体
- **示例**:nightmarecore, a twisted childhood bedroom in darkness, distorted shadows on the wall, a corrupted teddy bear in a corner, dim nightmare light, black and deep red palette, dread and unease, familiar space made wrong, oppressive gloom
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D14. 糖果核（Candycore）
- **触发词**:candycore, pastel sweet
- **关键词**:pastel pink blue mint, candy clouds, frosting textures, sugary fantasy, soft toys, marshmallow landscape, bubblegum, cute kawaii, sweet dream
- **负面词**:dark, gritty, realistic, muted, horror
- **光线**:柔光,奶油感
- **色彩**:粉/薄荷绿/天蓝,奶甜调
- **构图**:圆润造型,柔软质感
- **示例**:candycore, pastel pink and mint landscape made of frosting textures, candy clouds in a bubblegum sky, soft plush toys, marshmallow hills, sugary fantasy, cute kawaii mood, dreamy sweet glow, soft rounded shapes
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D15. 花核（Bloomcore）
- **触发词**:bloomcore, floral dream
- **关键词**:flowers everywhere, overgrown petals, soft focus, botanical dream, pink blossoms, petals in air, gentle nostalgia, garden reverie, spring haze
- **负面词**:winter, dead, minimal, urban concrete
- **光线**:柔焦透光,花瓣透光
- **色彩**:樱粉/嫩绿/雾白
- **构图**:花海满铺,花瓣飘落,虚化
- **示例**:bloomcore, flowers covering an old wooden house, soft focus, pink petals drifting through air, overgrown garden dream, botanical reverie, gentle nostalgia, spring haze, warm dreamy light, lush and soft
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

### D16. 赛博核（Cybercore）
- **触发词**:cybercore
- **关键词**:digital grid, circuit patterns, glowing data streams, futuristic helmet, holographic code, neon veins, synthwave energy, machine beauty
- **负面词**:organic natural, retro 80s mall, vaporwave pink, rustic
- **光线**:霓虹+屏幕光,数据流光
- **色彩**:电青/霓虹紫+荧光绿
- **构图**:网格透视,数据流线,发光元素
- **示例**:cybercore, a figure in futuristic helmet with glowing circuit patterns, holographic code floating, neon data streams, digital grid floor, synthwave energy, electric cyan and violet, machine beauty, glowing veins of light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开氛围细节;→Seedream 要素齐全

---

## E. 摄影风格

### E1. 胶片摄影（Film Photography）
- **触发词**:35mm film, analog photo
- **关键词**:film grain, Kodak Portra, Fujifilm, natural colors, soft contrast, light leak, halation, organic tones
- **负面词**:digital sharpness, HDR, plastic look, oversaturated
- **光线**:自然光,略过曝
- **色彩**:Portra 暖调/富士绿调
- **构图**:纪实抓拍,不完美构图
- **示例**:35mm film photo, Kodak Portra 400, soft natural tones, film grain, gentle contrast, slight light leak, organic warm skin tones, candid moment, analog feel
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E2. 长曝光（Long Exposure）
- **触发词**:long exposure
- **关键词**:silky water, light trails, star trails, motion blur clouds, ND filter, smooth surfaces, time compression
- **负面词**:frozen action, sharp moving objects, handheld shake
- **光线**:低光+慢门,夜晚/黎明
- **色彩**:冷蓝夜+暖光轨
- **构图**:静止前景+流动背景
- **示例**:long exposure city night, car light trails streaming through streets, silky river water, star trails above, ND filter smoothness, cold blue night with warm light trails, time compressed
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E3. 航拍（Aerial）
- **触发词**:aerial view, drone shot
- **关键词**:top-down, bird's eye, patterns, geometry from above, landscape abstraction, DJI, satellite-like, scale revealed
- **负面词**:ground level, eye level, close-up
- **光线**:正午顶光/黄昏低角
- **色彩**:地形色块,高饱和
- **构图**:俯视图案化,对称
- **示例**:aerial drone view, top-down of terraced rice fields, geometric patterns, lush green terraces with water reflections, DJI Hasselblad look, pattern abstraction, morning light, sweeping scale
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E4. 微距（Macro）
- **触发词**:macro photography
- **关键词**:extreme close-up, insect eye, dew drop, petal texture, shallow depth of field, magnification, tiny world, bokeh
- **负面词**:wide scene, landscape, distant subject
- **光线**:环形灯/自然侧光
- **色彩**:局部高饱和+背景虚化
- **构图**:主体充满,浅景深
- **示例**:macro photography, extreme close-up of a dragonfly on a leaf, dew drops, wing texture visible, shallow depth of field, creamy bokeh background, morning light, tiny world detail
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E5. 移轴（Tilt-Shift）
- **触发词**:tilt-shift, miniature effect
- **关键词**:selective focus, miniature city, toy-like, bokeh blur top and bottom, forced perspective, tiny people
- **负面词**:deep focus, realistic scale, full sharpness
- **光线**:明亮均匀
- **色彩**:鲜艳玩具感
- **构图**:高处俯视,焦点窄带
- **示例**:tilt-shift photo, miniature city effect, cars and people look like toys, narrow sharp focus band, blur top and bottom, high angle, bright cheerful light, forced perspective
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E6. 双重曝光（Double Exposure）
- **触发词**:double exposure
- **关键词**:two images merged, silhouette with landscape inside, transparency overlap, ghostly, layered, film magic
- **负面词**:single exposure, clean separation, photorealistic single subject
- **光线**:逆光剪影为底
- **色彩**:底图色+叠加图调
- **构图**:人形/山形轮廓+内部风景
- **示例**:double exposure, silhouette of a woman's profile filled with a pine forest and misty mountains, ghostly transparency, layered film effect, warm light through trees, poetic
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E7. 黑白街拍（Monochrome Street）
- **触发词**:monochrome street photography
- **关键词**:black and white, high contrast, decisive moment, shadow play, urban geometry, candid, grain, Leica, documentary
- **负面词**:color, soft pastel, studio, posed
- **光线**:硬光强影,侧逆光
- **色彩**:纯黑白,灰阶丰富
- **构图**:抓拍瞬间,光影切割,几何框
- **示例**:monochrome street photography, Leica look, high contrast black and white, decisive moment, shadow slicing across alley, candid pedestrian, film grain, urban geometry, documentary feel
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E8. 红外摄影（Infrared）
- **触发词**:infrared photography
- **关键词**:false color, foliage glowing white-pink, surreal sky, dark water, eerie vegetation, dreamlike landscape, IR filter
- **负面词**:natural colors, normal green foliage, realistic skin tone
- **光线**:强日光(红外需要光)
- **色彩**:叶白/天深蓝/水近黑
- **构图**:树木剪影,水面反射,超现实场景
- **示例**:infrared photography, trees glowing white and pink, deep blue sky, water nearly black, surreal dreamlike landscape, eerie vegetation glow, strong sunlight, IR false color, otherworldly mood
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E9. 宝丽来（Polaroid）
- **触发词**:polaroid, instant photo
- **关键词**:white frame, faded print, square format, soft muted colors, light leak, vintage snapshot, slightly blurry, nostalgic texture, dated aesthetic
- **负面词**:sharp digital, HDR, high contrast, professional studio
- **光线**:自然光,略过曝,偏色
- **色彩**:褪色暖调/偏绿偏黄,低对比
- **构图**:随意快照,主体偏离中心,生活片段
- **示例**:polaroid instant photo, white frame, faded square print, a dog on a lawn in summer, soft muted colors, light leak on one edge, slightly blurry, nostalgic snapshot texture, dated aesthetic
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E10. 水下摄影（Underwater）
- **触发词**:underwater photography
- **关键词**:light rays through water, bubbles, floating hair, deep blue gradient, marine life, suspended particles, weightless motion, scuba light
- **负面词**:above water, beach surface, dry, crowded
- **光线**:水面透光柱,散射光
- **色彩**:深蓝/青绿渐变,透亮感
- **构图**:光柱透视,上升气泡,自由悬浮
- **示例**:underwater photography, light rays penetrating deep blue water, rising bubbles, a figure floating weightless, suspended particles, soft caustics on skin, deep blue to teal gradient, serene weightless mood
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E11. 剪影（Silhouette）
- **触发词**:silhouette
- **关键词**:black shape against bright background, rim light only, sunset backlight, profile outline, dramatic sky, no detail in shadow, minimal
- **负面词**:detailed face, mid-tone lighting, colorful foreground
- **光线**:强逆光,背景亮主体纯黑
- **色彩**:主体纯黑+背景暖橙/冷蓝
- **构图**:主体居中或三分,地平线低
- **示例**:silhouette, a person standing on a cliff edge, pure black shape against vivid orange sunset, rim light outline, dramatic sky, no detail in shadow, minimal composition, emotional contrast
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E12. 人像摄影（Portrait）
- **触发词**:portrait photography
- **关键词**:catchlight in eyes, shallow depth of field, creamy bokeh, natural skin texture, 85mm, headshot, candid expression, flattering light
- **负面词**:plastic skin, over-smoothed, distorted face, HDR
- **光线**:窗光/柔光箱,眼神光
- **色彩**:自然肤色,背景虚化暖调
- **构图**:85mm 半身/特写,三分线
- **示例**:portrait photography, 85mm headshot, shallow depth of field, creamy bokeh background, soft window light, catchlight in eyes, natural skin texture, candid warm expression, professional flattering light
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E13. 风光摄影（Landscape）
- **触发词**:landscape photography
- **关键词**:sweeping vista, foreground interest, leading lines, golden hour, dramatic sky, long depth of field, layered depth, Ansel Adams feel, grand scale
- **负面词**:flat light, cluttered, urban, noon harsh
- **光线**:黄金时刻/蓝调,顺光或侧光
- **色彩**:自然饱和,天空地面层次
- **构图**:前景引导线,三分地平,层叠
- **示例**:landscape photography, sweeping mountain vista, foreground rocks as leading lines, golden hour light, dramatic clouds, deep depth of field, layered ridges fading, grand natural scale, rich warm tones
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E14. 天文摄影（Astrophotography）
- **触发词**:astrophotography
- **关键词**:star trails, milky way core, deep sky objects, long exposure, telescope view, nebula colors, dark site, tracking mount, night landscape
- **负面词**:daytime, light pollution, blurry stars, city
- **光线**:极暗+星光+长时间曝光
- **色彩**:深黑+星云红蓝紫
- **构图**:星轨拱环,银河横贯,地景剪影
- **示例**:astrophotography, milky way core rising over a mountain silhouette, long exposure, deep sky colors in red and blue, star trails beginning, dark site sky, no light pollution, telescope sharpness, vast cosmic scale
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E15. 夜景摄影（Night Cityscape）
- **触发词**:night cityscape, city lights
- **关键词**:bokeh lights, neon reflections, long exposure trails, high ISO grain, city glow, silhouetted skyline, light painting, dusk blue hour
- **负面词**:daytime, flat, underexposed black void, blurry
- **光线**:城市灯光+蓝色时刻
- **色彩**:深蓝+暖黄+霓虹点缀
- **构图**:车流光轨,楼群剪影,倒影
- **示例**:night cityscape, blue hour sky, skyscraper silhouettes with glowing windows, long exposure car light trails, neon reflections on wet street, bokeh lights, high ISO grain, urban energy at night
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E16. 美食摄影（Food）
- **触发词**:food photography
- **关键词**:steam rising, glistening texture, shallow depth of field, natural window light, styled plating, macro detail, warm appetizing tones, garnish
- **负面词**:flat lighting, unappetizing, plastic look, dull
- **光线**:侧窗光,45 度柔光,蒸汽背光
- **色彩**:暖食物色,高饱和诱惑
- **构图**:45 度俯拍,浅景深特写,桌面层次
- **示例**:food photography, steaming bowl of noodles, natural window side light, glistening texture, shallow depth of field, warm appetizing tones, styled plating, chopsticks lifting noodles, 45 degree angle, steam backlit
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

### E17. 纪实摄影（Documentary）
- **触发词**:documentary photography
- **关键词**:real moment, unposed, available light, gritty texture, storytelling, human condition, candid, natural color, photojournalism
- **负面词**:posed, studio, polished, staged, fake
- **光线**:现有光,自然光源
- **色彩**:自然色,不过度调色
- **构图**:抓拍,中景叙事,环境交代
- **示例**:documentary photography, unposed market scene, available light, real working hands, gritty natural texture, storytelling composition, candid faces, photojournalism style, natural color, human moment
- **适配**:→Kolors 删相机型号写中文;→Qwen 保留镜头参数;→Seedream 要素齐全(人像最强)

---

## 第二部分 · 氛围系

### M1. 荒芜孤寂（Desolation）
- **触发词**:desolation, desolate
- **关键词**:vast empty landscape, lone figure, abandoned structures, muted colors, oppressive silence, endless horizon, isolation
- **负面词**:crowded, lively, colorful, joyful
- **光线**:阴天/黄昏漫射
- **色彩**:低饱和,灰褐/冷蓝
- **构图**:极远景,人物极小,负空间
- **示例**:desolate coastal plain, vast empty space, a single tiny figure standing at the edge, abandoned concrete bunker, overcast sky, muted grey-blue tones, oppressive silence, endless horizon, sense of isolation
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M2. 孤独深夜（Nocturne Loneliness）
- **触发词**:loneliness at night, night solitude
- **关键词**:empty street at night, single warm window, streetlight pool, fog, quiet city, reflections on wet asphalt, solitary figure
- **负面词**:crowded street, party, bright daylight, cheerful
- **光线**:路灯暖光孤岛,月光冷衬
- **色彩**:深蓝黑+暖黄灯点缀
- **构图**:人物背影,路灯成孤岛
- **示例**:empty city street at night, fog, one streetlight casting a warm pool of light, solitary figure walking away, wet asphalt reflecting the light, quiet melancholy, deep blue-black with warm yellow accent
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M3. 神圣庄严（Sacred Awe）
- **触发词**:sacred, awe
- **关键词**:cathedral-like space, shaft of light, dust motes, vaulted ceiling, silence, reverence, monumental void, stained glass
- **负面词**:noisy, casual, mundane, crowded
- **光线**:天窗光束,神圣感
- **色彩**:暖金+深影
- **构图**:仰视穹顶,对称
- **示例**:sacred monumental hall, shaft of light from high window, dust motes floating, vaulted ceiling, profound silence, reverence, warm golden light against deep shadow, symmetric composition
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M4. 静谧田园（Pastoral Serenity）
- **触发词**:pastoral, serene
- **关键词**:rolling hills, morning mist, farmhouse, golden light, wildflowers, peaceful, birds, dew, quiet countryside
- **负面词**:urban, industrial, dark, chaotic
- **光线**:晨光/黄金时刻,薄雾
- **色彩**:嫩绿/暖金/雾白
- **构图**:层叠丘陵,引导线
- **示例**:pastoral landscape, rolling green hills in morning mist, small farmhouse, golden sunrise light, wildflowers in foreground, dew on grass, peaceful serene mood, soft warm tones
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M5. 末世寂灭（Post-Human Silence）
- **触发词**:post-human, after humanity
- **关键词**:overgrown city, silent architecture, nature reclaiming, no humans, frozen time, moss covered, silent streets, civilization's echo
- **负面词**:people, vehicles, active, bright commercial
- **光线**:阴天/雾,无阳光
- **色彩**:灰绿/棕褐,低饱和
- **构图**:无人巨构,植被入侵
- **示例**:post-human city, extreme wide aerial view, overgrown silent streets, moss covered buildings, vines on skyscrapers, no humans no vehicles, frozen time, grey-green tones, nature reclaiming civilization, silent echo, flat overcast light
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M6. 温暖治愈（Cozy Warmth）
- **触发词**:cozy, hygge
- **关键词**:warm light, fireplace glow, soft blanket, cup of tea, rainy window, warm wood, comfortable, intimate, gentle
- **负面词**:cold, clinical, empty, harsh light, spacious void
- **光线**:壁炉暖光,窗边柔光
- **色彩**:暖橙/木褐/奶油
- **构图**:近景,包围感
- **示例**:cozy interior, fireplace glow, soft blanket on armchair, cup of tea steaming, rain on window, warm wood tones, intimate comfortable atmosphere, soft warm light, gentle shadows
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M7. 悬疑紧张（Suspense）
- **触发词**:suspense, thriller mood
- **关键词**:dark corridor, half-open door, single light source, long shadows, tension, ambiguous, off-frame threat, muted cold light
- **负面词**:bright, cheerful, cozy, daylight, mundane
- **光线**:单光源,硬阴影
- **色彩**:冷蓝黑,局部暖警示
- **构图**:门缝视角,前景遮挡
- **示例**:suspenseful hallway, half-open door at the end, single harsh light source, long distorted shadows, tension in the air, cold blue-black palette, off-frame implied threat, ambiguous mood
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M8. 敬畏崇高（Sublime）
- **触发词**:sublime, overwhelming nature
- **关键词**:colossal scale, tiny human, storm sky, mountain vastness, ocean power, awe, insignificance, dramatic light
- **负面词**:safe, cozy, mundane, small scale
- **光线**:风暴光/破云光
- **色彩**:暗色+破晓金光
- **构图**:极端尺度对比
- **示例**:sublime landscape, tiny climber on colossal cliff face, storm clouds breaking with a shaft of light, overwhelming scale, awe and insignificance, dramatic contrast, dark tones with golden break
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M9. 静谧清晨（Quiet Dawn）
- **触发词**:quiet dawn, early morning
- **关键词**:soft mist, first light, dew, empty street, birdsong, pale blue sky, calm water, fresh air, peaceful stillness
- **负面词**:dark night, harsh midday, crowded, noisy
- **光线**:日出前柔光,薄雾
- **色彩**:淡蓝/粉橙/雾白
- **构图**:开阔远景,低对比
- **示例**:quiet dawn, thin mist over calm lake, first soft light, pale blue and pink sky, empty lakeside path, dew on grass, peaceful stillness, birdsong implied, gentle tones
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M10. 暴风雨前（Before the Storm）
- **触发词**:before the storm, storm brewing
- **关键词**:dark clouds gathering, oppressive sky, still air, tense atmosphere, muted colors, light fading, anticipation, wind bending grass
- **负面词**:bright sunny, cheerful, clear sky, settled
- **光线**:乌云遮日,最后一缕光
- **色彩**:墨灰+土黄,高对比暗调
- **构图**:低角度仰天,空旷地平线
- **示例**:before the storm, dark clouds gathering over flat farmland, oppressive sky, still air, one last shaft of light on the horizon, wind bending grass, tense anticipation, muted grey-yellow tones
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M11. 烟火人间（Everyday Warmth）
- **触发词**:everyday life, human warmth
- **关键词**:street vendor steam, market bustle, warm lanterns, evening street, family dinner, neighborhood, living moments, golden glow
- **负面词**:empty, cold, dystopian, futuristic
- **光线**:黄昏暖光,路灯,蒸汽
- **色彩**:暖橙/木褐/红灯笼
- **构图**:中景生活流,密集但不乱
- **示例**:evening street market, steam rising from food stalls, warm lanterns glowing, people in daily life, golden hour light, bustling but warm, rich orange and brown tones, human warmth
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M12. 深海静谧（Deep Sea Quiet）
- **触发词**:deep sea, underwater stillness
- **关键词**:blue gradient, light rays through water, floating particles, marine life silhouette, silent depth, bioluminescence, pressure, vast blue
- **负面词**:beach, bright sunny surface, crowded reef
- **光线**:水面透光,生物光
- **色彩**:深蓝/青/荧光点缀
- **构图**:光柱透视,俯视深渊
- **示例**:deep sea, light rays penetrating dark blue water, floating particles, a whale silhouette in the distance, bioluminescent dots, silent depth, gradient from dark navy to teal, vast and quiet
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M13. 宇宙孤寂（Cosmic Isolation）
- **触发词**:cosmic isolation, space solitude
- **关键词**:lone spacecraft, distant planet, star field, void, silent vastness, earthshine, awe of scale, cold light
- **负面词**:busy space battle, colorful nebula fantasy, crowded
- **光线**:恒星侧光,行星反照
- **色彩**:深空黑+冷蓝+暖星点
- **构图**:小飞船大虚空,对角线
- **示例**:cosmic isolation, lone spacecraft drifting near a distant ringed planet, vast star field, deep void, cold side light, silent immensity, tiny human craft against cosmic scale, dark blue-black with warm star points
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M14. 乡愁怀旧（Nostalgia）
- **触发词**:nostalgia, retro memory
- **关键词**:old photograph, faded colors, childhood home, vintage furniture, sepia tones, remembered light, worn objects, tender longing
- **负面词**:modern, new, sharp digital, cold
- **光线**:旧照片感,柔焦
- **色彩**:泛黄/褪色/暖棕
- **构图**:旧物特写,记忆碎片
- **示例**:nostalgic scene, faded old photograph look, childhood home interior, worn wooden furniture, sepia and warm brown tones, soft remembered light, dust in sunbeam, tender longing, vintage texture
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M15. 权力威压（Monumental Power）
- **触发词**:monumental power, authority
- **关键词**:colossal statue, government hall, symmetrical columns, low angle, shadows, scale of state, marble and stone, oppressive grandeur
- **负面词**:cozy, small, playful, informal
- **光线**:硬光,强明暗阴影
- **色彩**:石色+深影,高对比
- **构图**:低角度仰视,对称中轴
- **示例**:monumental power, colossal stone statue in symmetrical government hall, low angle looking up, hard side light carving deep shadows, marble and granite, oppressive grandeur, scale of state, awe and intimidation
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M16. 温暖黄昏（Golden Evening）
- **触发词**:golden hour, evening glow
- **关键词**:warm sunset, long shadows, amber light, silhouettes, dust in light, peaceful end of day, golden haze
- **负面词**:noon, harsh light, cold tones, night
- **光线**:低角度暖光,长影
- **色彩**:琥珀/橙红/深紫
- **构图**:逆光剪影,地平线
- **示例**:golden evening, low warm sun, long shadows on wheat field, amber light everywhere, silhouette of a tree and birds, dust glowing in light, peaceful end of day, golden haze, rich orange tones
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M17. 诡异不安（Uncanny Unease）
- **触发词**:uncanny, uneasy
- **关键词**:too-perfect scene, wrong details, subtle wrongness, empty space watching, muted eerie light, familiar space altered, quiet dread
- **负面词**:comfortable, bright cheerful, obvious horror, gore
- **光线**:均匀但偏色,无自然感
- **色彩**:褪色+偏绿/偏蓝
- **构图**:正常构图但细节违和
- **示例**:uncanny scene, an immaculate suburban street but the houses have no doors, wrong subtle details, muted eerie light, empty space that feels watched, familiar space altered, quiet dread, faded greenish tones, medium shot at eye level, normal daylight but slightly off
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M18. 冬季寂寥（Winter Stillness）
- **触发词**:winter stillness, snow quiet
- **关键词**:fresh snow, bare trees, frozen lake, breath fog, muted white, cold blue, silent landscape, solitary cabin
- **负面词**:summer, green, crowded, warm bright
- **光线**:阴天雪光,低角度冷阳
- **色彩**:雪白+冰蓝+枯灰
- **构图**:留白雪地,孤树/孤屋
- **示例**:winter stillness, wide shot, fresh snow on frozen lake, bare trees, silent white landscape, cold blue shadows, a solitary cabin with smoke, muted tones, breath fog implied, absolute quiet, low winter sun
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M19. 都市疏离（Urban Alienation）
- **触发词**:urban alienation, city isolation
- **关键词**:crowded street but lonely, anonymous figures, glass reflections, cold architecture, rain, no eye contact, isolated in mass, grey tones
- **负面词**:warm community, cozy, countryside
- **光线**:阴天城市光,玻璃反光
- **色彩**:冷灰蓝,低饱和
- **构图**:人群中的孤立个体,反射构图
- **示例**:urban alienation, crowded city sidewalk but everyone isolated, anonymous figures with umbrellas, cold glass reflections, rain, grey-blue tones, no eye contact, loneliness in the mass, modern architecture looming, overcast diffused daylight
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M20. 沙漠孤旅（Desert Solitude）
- **触发词**:desert solitude
- **关键词**:endless dunes, lone traveler, heat haze, vast silence, wind ripples, minimal shadow, gold and sand, slow time
- **负面词**:crowded oasis, green, rainy, urban
- **光线**:正午顶光/黄昏长影
- **色彩**:沙金/焦赭/天蓝
- **构图**:沙丘引导线,人物渺小
- **示例**:desert solitude, extreme wide shot, endless golden dunes, a lone traveler walking a ridge line, heat haze, wind ripples on sand, vast silence, minimal shadow at noon, slow time, gold and sand tones with deep blue sky, harsh high sun
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M21. 极光秘境（Aurora Dream）
- **触发词**:aurora, northern lights
- **关键词**:green and violet sky curtains, snowfield glow, star field, reflected in frozen lake, silent polar night, shimmering light, cold clean air
- **负面词**:daylight, warm tropical, crowded, city lights
- **光线**:极光为主光源,月光辅
- **色彩**:极光绿/紫+雪地蓝白
- **构图**:极光穹顶,水面倒影,前景剪影
- **示例**:aurora dream, green and violet aurora curtains over snowfield, stars visible, aurora reflected in frozen lake, silent polar night, shimmering light, cold clean air, lone cabin silhouette, blue-white snow glow
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M22. 幽暗森林（Dark Forest）
- **触发词**:dark forest, woods at dusk
- **关键词**:dense trees, filtered dim light, fog between trunks, moss ground, mysterious path, muted green-brown, quiet dread, ancient woods
- **负面词**:bright sunny, cheerful park, urban, colorful
- **光线**:树冠滤光,暮色
- **色彩**:墨绿/深棕/雾灰
- **构图**:树列透视,小径引导,光线缝隙
- **示例**:dark forest, dense ancient trees, dim light filtering through canopy, fog drifting between trunks, moss-covered ground, a faint path disappearing into shadow, muted green and brown, quiet dread, mysterious stillness
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M23. 樱花春日（Cherry Blossom Spring）
- **触发词**:cherry blossom, spring
- **关键词**:pink petals falling, soft sunlight, sakura trees in bloom, gentle breeze, pastel sky, petals on water, dreamy brightness, renewal
- **负面词**:autumn, dead branches, harsh contrast, winter
- **光线**:晨光透花,柔和逆光
- **色彩**:樱粉/天蓝/嫩绿
- **构图**:花瓣前景散景,树下人影,河道花瓣
- **示例**:cherry blossom spring, sakura trees in full bloom, pink petals falling in gentle breeze, soft morning sunlight through petals, pastel blue sky, petals floating on stream, dreamy brightness, sense of renewal, shallow depth of field
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M24. 老城烟火（Old Town Life）
- **触发词**:old town, historic street
- **关键词**:narrow alley, worn stone walls, hanging laundry, evening lamps, old shops, resident life, warm windows, layered architecture, timeless
- **负面词**:modern glass, empty, new, commercial
- **光线**:黄昏街灯,窗口暖光,天色余晖
- **色彩**:暖黄灯光+青灰墙面+褪色招牌
- **构图**:巷道纵深,门框取景,生活细节
- **示例**:old town evening, narrow stone alley, hanging laundry between buildings, warm lamps glowing, old shop signs, resident silhouettes in windows, layered historic architecture, timeless atmosphere, golden streetlight on worn walls
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M25. 雷雨将至（Approaching Thunderstorm）
- **触发词**:thunderstorm approaching
- **关键词**:dark cumulonimbus, lightning far off, wind bending trees, dust rising, sudden chill, dramatic sky, first raindrops, electricity in air, grey-gold contrast
- **负面词**:clear sky, sunny, calm settled, bright
- **光线**:乌云遮日,远处闪电微光
- **色彩**:墨黑云层+铅灰+暗金边缘
- **构图**:低角度仰天,空旷地平线,风动前景
- **示例**:approaching thunderstorm, massive dark cumulonimbus rolling in, distant lightning flicker, wind bending the wheat field, dust rising from the road, first heavy raindrops, grey-gold edge light on clouds, dramatic sky, electric tension
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M26. 晨雾山峦（Misty Mountains Dawn）
- **触发词**:misty mountains, mountain dawn
- **关键词**:layered ridges, cloud sea below, golden sunrise peak, mist flowing in valleys, silhouetted pines, fresh cold air, first light, depth fading
- **负面词**:noon, clear, harsh light, urban
- **光线**:日出低光,雾海反照
- **色彩**:黛青山影+暖金峰顶+雾白
- **构图**:层叠山脊由近及远,前景树影剪影
- **示例**:misty mountains at dawn, extreme wide shot, layered ridges fading into cloud sea, golden sunrise lighting the highest peak, mist flowing through valleys, silhouetted pine trees in foreground, cold fresh air, first light, depth fading with distance, quiet grandeur
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M27. 午夜都市（Midnight City）
- **触发词**:midnight city, city at night
- **关键词**:empty streets, streetlights, neon reflections, skyscraper canyons, quiet hum, blue hour, lone taxi, office lights, wet asphalt
- **负面词**:daytime, crowded, rural, bright cheerful
- **光线**:路灯+霓虹+玻璃反光,蓝夜
- **色彩**:深蓝黑+霓虹点缀
- **构图**:楼间峡谷透视,倒影对称
- **示例**:midnight city, empty street between skyscraper canyons, streetlights casting pools of light, neon reflections on wet asphalt, a lone taxi passing, office windows glowing, deep blue night, quiet hum, urban solitude
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M28. 林间小屋（Forest Cabin）
- **触发词**:forest cabin, woodland retreat
- **关键词**:wooden cabin, chimney smoke, pine forest, warm window, snow or autumn leaves, forest clearing, cozy isolation, morning mist
- **负面词**:city, modern concrete, crowded, desert
- **光线**:窗口暖光,森林散射光
- **色彩**:木褐/松绿+暖黄窗光
- **构图**:小屋居中,树环绕,小路引向
- **示例**:forest cabin, wooden house in a pine clearing, chimney smoke rising, warm light from the window, morning mist between trees, autumn leaves on the ground, cozy isolation, peaceful retreat, warm yellow against green-brown
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M29. 古堡暮色（Castle at Dusk）
- **触发词**:castle, fortress at dusk
- **关键词**:stone battlements, crenellations, drawbridge, dark ivy, dramatic sky, torches, medieval, hillside fortress, last light
- **负面词**:modern, bright midday, cheerful, glass
- **光线**:暮色余晖,火把暖光
- **色彩**:石灰+墨蓝天空+火把橙
- **构图**:低角度仰视城堡,剪影天际线
- **示例**:castle at dusk, stone battlements against deep blue evening sky, last warm light on the walls, dark ivy climbing, torches flickering on the walls, medieval fortress on a hillside, dramatic silhouette, ancient solemnity
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M30. 候车大厅（Train Station）
- **触发词**:train station, station hall
- **关键词**:vaulted glass roof, steam from trains, sunbeams through glass, travelers, departure board, echo, vintage clock, platform
- **负面词**:empty modern mall, airport lounge, no people
- **光线**:天窗光束,蒸汽透光
- **色彩**:铸铁黑+玻璃白+暖灯
- **构图**:拱顶透视,光柱,人影剪影
- **示例**:train station hall, vaulted glass and iron roof, sunbeams streaming through, steam drifting from a departing train, travelers silhouetted, vintage clock, echoes, sense of journey, warm light through glass
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M31. 海底遗迹（Sunken Ruins）
- **触发词**:sunken ruins, underwater ruins
- **关键词**:submerged temple, columns underwater, fish among stones, green-blue water, light shafts, seaweed, ancient mystery, silt
- **负面词**:above water, modern, bright surface, dry
- **光线**:水面光柱,深海微光
- **色彩**:深青绿+透光蓝绿
- **构图**:柱列沉没,光柱斜射,鱼群
- **示例**:sunken ruins, an ancient temple submerged in clear green-blue water, marble columns leaning, light shafts from surface, fish swimming through the pillars, seaweed and silt, mysterious ancient atmosphere, quiet depth
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M32. 星空旷野（Starry Field）
- **触发词**:starry night, milky way
- **关键词**:milky way visible, no light pollution, silhouette meadow, tent glow, meteor, constellations, deep navy sky, earth glow on horizon
- **负面词**:city lights, overcast, daytime, pollution
- **光线**:银河光,帐篷微光,地照
- **色彩**:深蓝黑+星点+暖帐篷光
- **构图**:银河拱桥,地平线剪影
- **示例**:starry night, milky way arching over a dark meadow, no light pollution, a tent with warm glow, meteors streaking, constellations vivid, deep navy sky, earth glow on horizon, vast and silent, sense of wonder
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M33. 秋日落叶（Autumn Leaves）
- **触发词**:autumn, fall season
- **关键词**:golden leaves, falling foliage, warm low sun, maple red, crisp air, leaf-covered path, cozy sweater, harvest light, amber tones
- **负面词**:winter, spring green, harsh noon, bleak
- **光线**:低角度暖阳,透叶金光
- **色彩**:金黄/枫红/琥珀+树影
- **构图**:落叶引导线,逆光叶影
- **示例**:autumn scene, golden maple leaves falling, low warm sunlight through branches, leaf-covered park path, crisp air, amber and red tones, a bench half-buried in leaves, soft backlit glow, harvest warmth
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M34. 夏日午后（Summer Afternoon）
- **触发词**:summer afternoon, lazy summer
- **关键词**:dappled shade, cicada heat, ice cold drink, white curtain, fan breeze, bright green, afternoon nap, heat haze, iced tea
- **负面词**:winter, dark, gloomy, autumn
- **光线**:斑驳树影,透窗强光
- **色彩**:亮绿/天空蓝+冷饮透亮
- **构图**:窗台静物,树影投墙,慵懒中景
- **示例**:summer afternoon, dappled shade on a white wall, iced tea glass with condensation, bright green leaves outside, white curtain moving, cicada summer feel, heat haze in distance, bright airy light, lazy warm mood
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M35. 篝火之夜（Campfire Night）
- **触发词**:campfire, bonfire night
- **关键词**:warm fire glow, sparks rising, faces lit orange, dark forest around, smoke curling, marshmallow, night sky stars, crackling warmth, circle of light
- **负面词**:daytime, cold blue, city lights, wet
- **光线**:篝火暖光为主,周围黑暗
- **色彩**:火橙+暗蓝夜+星点
- **构图**:火光包围圈,仰视星火,剪影围坐
- **示例**:campfire night, warm orange fire glow on faces, sparks rising into dark sky, smoke curling, dark pine forest surrounding, stars visible above, cozy circle of light against deep night, crackling warmth, contrast of fire orange and night blue
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M36. 黄昏海岸（Dusk Shore）
- **触发词**:dusk shore, coastal evening
- **关键词**:purple-pink sky, tide going out, wet sand reflection, lighthouse far, gentle waves, last light, seagulls, cool wind, blue hour
- **负面词**:noon, bright sunny, inland, crowded
- **光线**:日落余晖,蓝调时刻,海面反光
- **色彩**:紫粉天空+深蓝海+沙金
- **构图**:水平线低,倒影对称,远景灯塔
- **示例**:dusk shore, purple-pink sky over quiet sea, tide pools reflecting the last light, wet sand mirror, distant lighthouse, gentle waves, seagulls passing, blue hour, cool sea breeze, peaceful end of day, soft gradient sky
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M37. 雪夜（Snow Night）
- **触发词**:snow night, snowfall
- **关键词**:falling snow, streetlamp glow, footprints in snow, silent street, warm window, cold blue, snowflakes, muffled quiet, winter lights
- **负面词**:summer, rain, bright colorful, dry
- **光线**:路灯暖光+雪反冷光
- **色彩**:冷蓝白+暖黄灯
- **构图**:雪中灯光锥,脚印延伸,窗光暖点
- **示例**:snow night, heavy snow falling, streetlamp casting warm cone of light, fresh footprints in snow, silent street, a warm window glowing, cold blue shadows, snowflakes catching light, muffled quiet, winter stillness with warmth
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M38. 废弃游乐园（Abandoned Amusement Park）
- **触发词**:abandoned amusement park
- **关键词**:rusted ferris wheel, overgrown carousel, faded paint, silent roller coaster, broken lights, cracked pavement, weeds through rides, eerie nostalgia
- **负面词**:crowded, functioning, bright new, cheerful
- **光线**:阴天漫射/黄昏斜光,破败氛围
- **色彩**:褪色红蓝+锈棕+灰
- **构图**:摩天轮剪影,空荡过道,植被入侵
- **示例**:abandoned amusement park, rusted ferris wheel against overcast sky, overgrown carousel with faded horses, weeds through cracked pavement, silent roller coaster, peeling paint, eerie nostalgia, quiet decay, late afternoon shadow
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M39. 夜市（Night Market）
- **触发词**:night market
- **关键词**:string lights, steam from stalls, glowing lanterns, crowded warmth, sizzling food, colorful signage, smoke and aroma, night bustle, red glow
- **负面词**:empty, cold, daytime, minimal
- **光线**:灯笼+摊位灯,暖色满铺
- **色彩**:暖红/金黄+食物色
- **构图**:街道纵深,蒸汽光柱,密集摊位
- **示例**:night market, string lights overhead, steam rising from food stalls, glowing red lanterns, sizzling grill smoke, colorful signs, crowded warm bustle, night energy, golden and red glow, inviting chaos
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M40. 竹林幽径（Bamboo Path）
- **触发词**:bamboo forest, bamboo path
- **关键词**:tall bamboo stalks, filtered light, green shade, winding path, leaves rustling, mist between stalks, quiet green, gentle breeze
- **负面词**:urban, bright open, desert, harsh
- **光线**:滤光斑驳,雾中散射
- **色彩**:竹绿/深绿+光斑白
- **构图**:竹列透视,小径弯曲,仰视竹梢
- **示例**:bamboo forest path, tall stalks lining a winding trail, light filtering through leaves, green shade, mist between stalks, gentle breeze, quiet stillness, deep green tones, path disappearing into fog, serene seclusion
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M41. 麦田黄昏（Wheat Field Evening）
- **触发词**:wheat field, golden field
- **关键词**:ripe wheat, golden hour, wind ripples, lone tree, horizon glow, harvest, birds scattering, warm breeze, amber sea
- **负面词**:urban, winter, green field, cloudy dull
- **光线**:低角度暖阳,逆光穗影
- **色彩**:金黄/琥珀+暖橙天空
- **构图**:麦浪层次,孤树剪影,地平线低
- **示例**:wheat field at golden hour, ripe grain rippling in wind, a lone tree silhouetted, horizon glowing warm, birds scattering, amber sea of wheat, low sun backlight, harvest warmth, serene endlessness
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M42. 老电影院（Old Cinema）
- **触发词**:old cinema, vintage theater
- **关键词**:red velvet seats, dusty projector beam, film grain, marquee lights, old posters, worn carpet, vintage screen glow, nostalgic darkness
- **负面词**:modern multiplex, bright clean, empty new, digital
- **光线**:放映机光束,钨丝壁灯
- **色彩**:暗红+暖金+银幕亮
- **构图**:座椅排透视,光束锥,舞台框
- **示例**:old cinema interior, red velvet seats in rows, dusty projector beam through the dark, vintage marquee light glowing, worn carpet, old movie posters, film grain, nostalgic darkness, warm tungsten wall lamps, screen glow ahead
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线/色彩细节;→Seedream 要素齐全

### M43. 雨夜（Rainy Night）
- **触发词**:rainy night, night rain
- **关键词**:rain streaks, wet umbrella, streetlight halos, reflections on road, footsteps in puddle, muffled sounds, dark blue, window rain
- **负面词**:dry, sunny, bright cheerful, clear sky
- **光线**:路灯晕圈,雨丝反光
- **色彩**:深蓝黑+暖黄灯晕
- **构图**:湿路倒影,伞下视角,窗内看雨
- **示例**:rainy night, rain streaking past a streetlight halo, wet asphalt reflecting orange light, a lone umbrella crossing the street, puddles catching glow, deep blue night, muffled quiet, droplets on window glass, melancholic calm
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线细节;→Seedream 要素齐全

### M44. 雾都（Foggy City）
- **触发词**:foggy city, misty metropolis
- **关键词**:skyscrapers in fog, blurred skyline, ghostly buildings, muffled city, low visibility, damp air, floating mist, layered silhouettes
- **负面词**:clear sky, sharp, sunny, dry
- **光线**:雾中漫射,轮廓柔和
- **色彩**:灰白+浅蓝灰
- **构图**:楼群层次渐隐,仰视雾中高楼
- **示例**:foggy city, skyscraper silhouettes fading into dense fog, ghostly layered skyline, blurred streetlights, muffled atmosphere, damp grey air, buildings half-hidden, low visibility, cold urban mystery
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开层次细节;→Seedream 要素齐全

### M45. 湖畔晨光（Lake Morning）
- **触发词**:lake morning, lakeside dawn
- **关键词**:mirror water, morning mist, fishing boat, reeds, soft sunrise, mist over water, silence, reflection, gentle ripples
- **负面词**:windy waves, midday harsh, city, crowded
- **光线**:日出柔光,水面反照
- **色彩**:淡金+雾灰+水蓝
- **构图**:水平线低,倒影对称,芦苇前景
- **示例**:lake morning, mirror-still water reflecting soft sunrise, thin mist over the lake, a fishing boat silhouette, reeds in foreground, gentle ripples, absolute calm, pale gold and grey-blue, peaceful solitude
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开光线细节;→Seedream 要素齐全

### M46. 草原牧歌（Grassland Pastoral）
- **触发词**:grassland, prairie
- **关键词**:endless green meadow, grazing herds, rolling hills, big sky, wind through grass, distant mountains, nomad tent, clouds shadows
- **负面词**:urban, desert, forest, crowded
- **光线**:大面日光,云影流动
- **色彩**:嫩绿+天空蓝+云白
- **构图**:地平线低,羊群散点,云影
- **示例**:grassland pastoral, wide shot, endless green meadow under big sky, grazing sheep scattered, rolling hills, wind rippling the grass, distant blue mountains, nomad tent, cloud shadows drifting, vast open space, serene freedom, bright midday sun
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开草原细节;→Seedream 要素齐全

### M47. 高原经幡（Plateau Prayer Flags）
- **触发词**:plateau, prayer flags
- **关键词**:colorful prayer flags, snow mountains, thin air, wind fluttering, tibetan plateau, clear blue sky, stupa, high altitude, spiritual stillness
- **负面词**:sea level, forest, humid, city
- **光线**:高原强日光,雪山反光
- **色彩**:经幡五色+雪山白+天空蓝
- **构图**:经幡前景,雪山远景,仰视
- **示例**:plateau with prayer flags, colorful flags fluttering in wind, snow peaks behind, vivid blue sky, thin clear air, stupa in the distance, high altitude light, spiritual stillness, wind as movement, majestic calm
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开经幡细节;→Seedream 要素齐全

### M48. 瀑布（Waterfall）
- **触发词**:waterfall
- **关键词**:cascading water, mist spray, mossy rocks, rainbows in spray, thunderous sound, deep pool, green gorge, power of water, fresh cold air
- **负面词**:dry, flat water, desert, city
- **光线**:透林光,水雾反光,彩虹
- **色彩**:水白+苔绿+岩褐
- **构图**:竖幅飞流,前景岩石,仰视
- **示例**:waterfall, water cascading over mossy cliffs into a deep pool, mist spray catching light, a faint rainbow in the spray, green gorge walls, rainbows in mist, powerful flow, fresh cold air, vertical composition, wild beauty
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开水雾细节;→Seedream 要素齐全

### M49. 火山（Volcano）
- **触发词**:volcano, volcanic
- **关键词**:glowing lava, ash plume, crater, molten rock, smoke column, black slopes, night glow, destruction and creation, heat haze
- **负面词**:calm meadow, cold blue, green valley, settled
- **光线**:熔岩橙光,夜空对比
- **色彩**:熔岩橙红+黑灰+夜蓝
- **构图**:喷发剪影,岩浆流线,广角全景
- **示例**:volcano at night, glowing lava flowing down black slopes, ash plume rising, crater glow against dark sky, molten red-orange veins, smoke column, heat haze, raw destructive power, dramatic contrast of fire and night
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开熔岩细节;→Seedream 要素齐全

### M50. 老书店（Old Bookstore）
- **触发词**:old bookstore, used bookshop
- **关键词**:stacked books, dusty sunlight, wooden shelves, paper smell, reading lamp, worn armchair, floor to ceiling shelves, quiet haven, warm amber
- **负面词**:modern minimal, empty shelves, e-reader, cold lighting
- **光线**:窗光+台灯暖光,灰尘光束
- **色彩**:书脊彩色+木褐+暖黄
- **构图**:书架透视,光束,阅读角落
- **示例**:old bookstore, floor-to-ceiling wooden shelves packed with books, dusty sunbeams through window, a warm reading lamp on a worn armchair, paper texture, quiet haven, amber light, cat on a bookshelf, cozy literary stillness
- **适配**:→Kolors 压缩为中文描述;→Qwen 展开细节;→Seedream 要素齐全

---

## 附录

### 风格组合规则
- 同类可混:砼核 × 阈限空间 × 荒芜(同源氛围)
- 异类慎混:砼核 × 赛博朋克(霓虹毁荒芜),梦核 × 哥特(色彩冲突)
- 一个画面一个主风格,氛围词 1-2 个,不堆砌

### 通用质检(每条 prompt 自检)
- [ ] 无空话词(cinematic/beautiful/8k 已删)
- [ ] 有具体光源(方向+色温)
- [ ] 有景别/角度
- [ ] 有相机锚定(型号+焦段)或明确不写
- [ ] 负面词防跑偏
- [ ] 长度 80-150 词

*风格库持续扩充中。新增条目请按上述格式(A/B/C/M 编号),保证每个都有完整配方+示例。*
