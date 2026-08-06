# Prompt 库 — 风格与氛围大全

> 文生图/图生视频提示词库。每个条目 = 完整配方:触发词 + 关键词 + 负面词 + 光线色彩 + 构图 + 示例 prompt。
> 原则:宁可少而精,不要多而滥。每个条目都经过 prompt_lint 质检(无空话、有光源、有景别、有锚定)。
> 使用方式:复制"示例 prompt"直接粘贴,或用"关键词"自行组合。

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
- **详见**:research/concretecore-style-guide.md + 22-text-to-image.md「33. 砼核」

### A2. 水墨国风（Chinese Ink Wash）
- **触发词**:Chinese ink painting style
- **关键词**:ink wash rendering, layered mountains, misty clouds, brush strokes, rice paper texture, negative space, breathing room, mountains fading into white mist, traditional Chinese painting
- **负面词**:oil painting, 3d render, photorealistic, vibrant colors, digital art, neon
- **光线**:留白即光,雾霭层次
- **色彩**:墨色浓淡(焦浓重淡清),宣纸白,极少量朱砂/花青点缀
- **构图**:S 形构图,留白 > 实景,远山淡影
- **示例**:traditional Chinese landscape painting, ink wash rendering, layered mountains in different ink densities, pine trees on cliff edges, a small pavilion half-hidden in clouds, negative space, rice paper texture, soft morning mist light, pale sky glow

### A3. 油画古典（Classical Oil Painting）
- **触发词**:classical oil painting
- **关键词**:Rembrandt lighting, chiaroscuro, impasto brushstrokes, canvas texture, rich warm tones, 17th century portraiture, dramatic shadow, Old Master style
- **负面词**:photorealistic, digital art, flat lighting, modern minimalist, anime
- **光线**:伦勃朗光,明暗对照,暖烛光感
- **色彩**:深褐/赭石/鎏金/暗红,厚重层次
- **构图**:三分法,主体受光面朝光源
- **示例**:classical oil painting of a merchant in 17th century Dutch clothing, Rembrandt lighting, chiaroscuro, impasto brushstrokes, canvas texture, rich warm brown and gold tones, dramatic shadow falling across the face

### A4. 浮世绘（Ukiyo-e）
- **触发词**:ukiyo-e style
- **关键词**:Japanese woodblock print, flat color planes, bold outlines, Hokusai, waves, Edo period, grain of woodblock paper
- **负面词**:3d, photorealistic, oil painting, soft gradient shading
- **光线**:平面化,无真实光影
- **色彩**:普鲁士蓝/朱红/山吹黄,高饱和平面色
- **构图**:大胆对角线,装饰性边框
- **示例**:ukiyo-e woodblock print, great wave style, bold blue outlines, flat color planes, Hokusai influence, Edo period aesthetic, grain texture, even flat light with no shadows, high-contrast outline against pale sky

### A5. 赛博朋克（Cyberpunk）※砼核反义词,谨慎混用
- **触发词**:cyberpunk, neon noir
- **关键词**:rain-soaked streets, neon reflections, holographic advertisements, megacity, augmented reality, cybernetic, high contrast, magenta and cyan
- **负面词**:noir (纯黑白), rural, nature, daytime, desaturated
- **光线**:霓虹主光,雨夜反射,紫青对撞
- **色彩**:品红/青/电光蓝,高饱和
- **构图**:拥挤街道,仰视巨楼,密集招牌
- **示例**:cyberpunk city street at night, rain-soaked asphalt reflecting neon signs, holographic ads, crowded megacity, magenta and cyan palette, high contrast, wet reflections, wide shot

### A6. 蒸汽朋克（Steampunk）
- **触发词**:steampunk
- **关键词**:brass gears, steam pipes, Victorian machinery, clockwork mechanisms, goggles, dirigibles, copper and bronze
- **负面词**:modern tech, clean futuristic, neon, minimalism
- **光线**:钨丝暖光,蒸汽体积光
- **色彩**:黄铜金/深棕/铁锈红/墨绿
- **构图**:机械细节特写,齿轮分层
- **示例**:steampunk workshop interior, brass gears and steam pipes, Victorian machinery, clockwork mechanisms, warm tungsten light through steam, copper and bronze tones, intricate mechanical details

### A7. 黑色电影（Film Noir）
- **触发词**:film noir
- **关键词**:high contrast, low-key lighting, venetian blind shadows, cigarette smoke, rain-soaked streets, 1950s detective, monochrome, chiaroscuro
- **负面词**:colorful, bright, daylight, neon, comedy
- **光线**:低调光,强对比,百叶窗影,烟雾
- **色彩**:黑白,深灰阶
- **构图**:斜线构图,人物半脸阴影
- **示例**:film noir scene, detective in trench coat, venetian blind shadows across face, cigarette smoke, high contrast low-key lighting, monochrome, rain-soaked street through window

### A8. 超现实主义（Surrealism）
- **触发词**:surrealism, dreamlike
- **关键词**:melting objects, impossible geometry, floating elements, Dali, Magritte, dream logic, scale distortion, empty sky
- **负面词**:realistic, mundane, coherent architecture, everyday
- **光线**:均匀梦幻光/矛盾光源
- **色彩**:低饱和,单一主调 + 强调色
- **构图**:错位透视,悬浮物体,极端尺度
- **示例**:surrealist scene, a colossal whale floating above a desert highway, impossible scale, dream logic, Dali influence, muted earth tones with one red accent, soft dreamlike light

### A9. 极简主义（Minimalism）
- **触发词**:minimalist, minimal composition
- **关键词**:negative space, single subject, clean lines, monochrome, quiet mood, flat color, simplicity
- **负面词**:busy, cluttered, ornate, detailed background, multiple subjects
- **光线**:均匀柔光,少阴影
- **色彩**:单色系,靠明度拉开
- **构图**:大量留白,主体极小/居中
- **示例**:minimalist composition, a single black stone on white sand, vast negative space, clean lines, quiet mood, soft diffused light, monochrome

### A10. 波普艺术（Pop Art）
- **触发词**:pop art
- **关键词**:bold colors, halftone dots, Andy Warhol, comic style, consumer culture, thick outlines, flat colors
- **负面词**:photorealistic, subtle, muted, realistic lighting
- **光线**:平面光,无真实感
- **色彩**:原色对撞,高饱和
- **构图**:重复网格,单主体放大
- **示例**:pop art portrait, bold primary colors, halftone dots, thick black outlines, Andy Warhol style, flat color planes, consumer culture aesthetic, hard studio flash lighting, graphic contrast

### A11. 哥特式（Gothic）
- **触发词**:gothic architecture
- **关键词**:pointed arches, flying buttresses, stained glass, cathedral, gargoyles, dark stone, candlelight, vaulted ceiling
- **负面词**:modern, bright, cheerful, minimalist, glass curtain wall
- **光线**:烛光,彩色玻璃光斑,昏暗
- **色彩**:暗石灰/深蓝紫/彩窗红蓝
- **构图**:仰视拱顶,对称中轴
- **示例**:gothic cathedral interior, pointed arches and vaulted ceiling, stained glass casting colored light, candlelight, gargoyles in shadow, dark stone, solemn atmosphere

### A12. 浮世梦核（Chinese Dreamcore）※中式梦核
- **触发词**:中式梦核, Chinese dreamcore
- **关键词**:千禧年记忆, 旧小区, 老式家具, 斑驳墙面, 阳光斜照, VHS质感, 半透明窗帘, 记忆模糊感, 怀旧不安
- **负面词**:现代建筑, 科幻, 恐怖, 鲜艳, 清晰锐利
- **光线**:过曝柔光,夕阳斜照,记忆感模糊
- **色彩**:米黄/粉彩/褪色,低饱和
- **构图**:日常场景错位,熟悉又陌生
- **示例**:中式梦核, 千禧年旧小区的楼道, 老式防盗门, 斑驳的米黄墙面, 夕阳从窗户斜照进来, 地面有拖把的水痕, VHS质感, 怀旧而微微不安

### A13. 印象派（Impressionism）
- **触发词**:impressionist painting
- **关键词**:visible brushstrokes, loose texture, light and color study, Monet, Renoir, soft edges, plein air, atmospheric color, dappled light, pastel dabs
- **负面词**:photorealistic, sharp edges, dark chiaroscuro, digital airbrush
- **光线**:户外自然光,光斑,薄雾感
- **色彩**:高亮低对比,补色并置(蓝橙/紫黄)
- **构图**:随意截取,非中心构图
- **示例**:impressionist oil painting, Monet style water lilies, visible brushstrokes, dappled light on water, soft edges, plein air color study, pastel dabs of blue and pink, glow of low morning sun, no hard lines, wide landscape view, even natural light

### A14. 新艺术运动（Art Nouveau）
- **触发词**:art nouveau
- **关键词**:flowing organic lines, floral motifs, whiplash curves, stained glass, Mucha, decorative borders, gilded details, elegant female figure
- **负面词**:geometric, brutalist, minimal, industrial
- **光线**:平面装饰光,柔和
- **色彩**:金/祖母绿/赭红,装饰性高饱和
- **构图**:对称装饰框,曲线主导
- **示例**:art nouveau poster, Mucha style, flowing organic lines, floral motifs, whiplash curves, elegant female figure with flowing hair, decorative gold border, emerald and ochre palette, stained glass background, soft diffused backlight glow

### A15. 巴洛克（Baroque）
- **触发词**:baroque style
- **关键词**:dramatic chiaroscuro, opulent detail, Caravaggio, rich drapery, gilded frames, intense emotion, heavenly light, grand composition
- **负面词**:minimal, flat lighting, modern, austere
- **光线**:强明暗对照,天光穿透
- **色彩**:深褐/鎏金/宝蓝/绯红
- **构图**:对角线动势,强舞台感
- **示例**:baroque painting, Caravaggio style, dramatic chiaroscuro, a figure in rich crimson drapery caught in heavenly light from above, gilded details, intense emotional expression, opulent dark background, grand diagonal composition

### A16. 国潮插画（Chinese Trendy Illustration）
- **触发词**:国潮, Chinese trendy illustration
- **关键词**:traditional motifs modernized, red and gold, dragon and phoenix, ink lines with flat color, chinoiserie, festive, graphic design, bold shapes
- **负面词**:western style, minimal, muted, realistic photography
- **光线**:平面光,装饰性
- **色彩**:中国红/鎏金/墨黑/青花蓝,高饱和
- **构图**:对称,纹样满铺,中心主体
- **示例**:国潮插画, 中国传统纹样现代化, 龙与凤, 朱红与鎏金配色, 墨线勾勒配平面色块, 装饰性构图, 对称排列, 喜庆而时尚, 平面设计感, 均匀平光无阴影, 无西方写实感

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

### B2. 诺兰（Christopher Nolan）
- **触发词**:nolan style, IMAX feel
- **关键词**:large format, wide angle, cold tones, high contrast, natural light, practical effects, gravity-defying, monumental scale
- **负面词**:neon, colorful, playful, sitcom lighting
- **光线**:自然光,低调光
- **色彩**:冷蓝灰,高对比
- **构图**:广角畸变,人物小环境大
- **示例**:nolan style, IMAX large format, wide angle lens distortion, cold blue tones, high contrast, monumental architecture dwarfing a tiny figure, natural light, practical feel

### B3. 王家卫（Wong Kar-wai）
- **触发词**:wong kar wai style
- **关键词**:high saturation, neon + warm tones, handheld, slow shutter, frame skipping, close-up, rain, cigarette smoke, longing atmosphere
- **负面词**:clean, bright daylight, static tripod, documentary
- **光线**:霓虹混合色温,慢门拖影
- **色彩**:高饱和霓虹+暖色对撞
- **构图**:框中框,前景遮挡,特写
- **示例**:wong kar wai style, high saturation neon and warm tones, handheld camera, slow shutter motion blur, close-up of a woman in rain, cigarette smoke, longing atmosphere, frame skipping

### B4. 塔可夫斯基（Andrei Tarkovsky）
- **触发词**:tarkovsky style
- **关键词**:long takes, natural elemental, water rain earth, slow meditative pace, muted color, religious iconography, vast landscapes, ruined spaces
- **负面词**:fast cutting, bright commercial, colorful, dialogue-driven
- **光线**:自然光,雾,潮湿感
- **色彩**:土黄/灰绿/暗褐,低饱和
- **构图**:缓慢横移,人物渺小于自然
- **示例**:tarkovsky style, vast misty landscape with a lone figure, extreme wide shot, wet earth and rain, muted earth tones, slow meditative composition, ruined wooden structure, natural elemental atmosphere, low overcast light

### B5. 宫崎骏（Hayao Miyazaki）
- **触发词**:ghibli style, miyazaki style
- **关键词**:hand-drawn animation, soft watercolor backgrounds, lush nature, whimsical, warm palette, detailed mechanical, floating clouds, gentle light
- **负面词**:photorealistic, dark, gritty, neon, horror
- **光线**:自然光,黄金时刻,柔光
- **色彩**:暖色柔和色板,清新绿/天空蓝
- **构图**:平视,多景别,自然融入
- **示例**:ghibli style, hand-drawn animation, lush green valley with whimsical small house, soft watercolor background, warm golden light, floating clouds, detailed grass blades, gentle peaceful mood

### B6. 新海诚（Makoto Shinkai）
- **触发词**:shinkai style, makoto shinkai
- **关键词**:hyper-detailed sky, volumetric clouds, lens flare, vivid blue, light rays, cityscape, romantic longing, bokeh
- **负面词**:flat sky, muted, desaturated, gloomy
- **光线**:逆光,丁达尔,光斑
- **色彩**:高饱和蓝天,黄昏橙紫渐变
- **构图**:天空占 2/3,人物小,远景大
- **示例**:shinkai style, hyper-detailed cumulus clouds, vivid blue sky with light rays, lens flare, distant cityscape, small figure on hill, romantic longing mood, bokeh

### B7. 昆汀（Quentin Tarantino）
- **触发词**:tarantino style
- **关键词**:bold saturated colors, trunk shot, retro cars, diner neon, 70s grain, close-up on eyes, pop culture props, stylized violence, dialogue tension
- **负面词**:muted, realistic boring, modern clean, desaturated
- **光线**:霓虹+钨丝混合,硬光
- **色彩**:高饱和红黄,复古暖调
- **构图**:低角度仰视,特写循环,车内/餐桌场景
- **示例**:tarantino style, retro 70s diner interior, bold saturated red and yellow, neon sign glow, trunk shot angle, close-up on eyes, vintage car outside, film grain, stylized tension, pop culture props

### B8. 是枝裕和（Hirokazu Kore-eda）
- **触发词**:kore-eda style, 是枝裕和
- **关键词**:natural everyday, warm family moments, soft window light, handheld gentle, shallow depth, quiet observation, domestic details, muted warm tones
- **负面词**:dramatic, stylized, high contrast, action
- **光线**:窗边自然柔光,黄昏暖光
- **色彩**:低饱和暖调,米白/木褐
- **构图**:固定机位长镜,日常局部特写
- **示例**:kore-eda style, family dinner scene in small apartment, soft window light, gentle handheld, shallow depth of field, quiet observation of everyday gesture, warm muted tones, domestic details, tender stillness

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

### C2. 后末日废土（Post-Apocalyptic）
- **触发词**:post-apocalyptic, wasteland
- **关键词**:overgrown ruins, abandoned city, rusted vehicles, dust, collapsed buildings, nature reclaiming, desolate highway, survivors' camp, muted brown-grey
- **负面词**:clean, futuristic tech, neon, crowded, pristine
- **光线**:扬尘昏黄,破云光柱,烟霾
- **色彩**:土黄/锈棕/灰绿,低饱和
- **构图**:废墟中渺小人物,引导线
- **示例**:post-apocalyptic wasteland, extreme wide shot, overgrown abandoned city ruins, rusted vehicles half-buried in dust, collapsed skyscrapers, nature reclaiming concrete, dusty haze, muted brown-grey tones, lone survivor walking the highway, harsh noon light through dust

### C3. 阈限空间（Liminal Space）※砼核的空间版
- **触发词**:liminal space, liminalcore
- **关键词**:empty transition space, infinite corridor, vacant pool, abandoned mall, fluorescent lighting, no people, uncanny familiarity, the backrooms
- **负面词**:people, furniture, lived-in, cozy, colorful decor
- **光线**:荧光灯冷白,均匀无影
- **色彩**:冷白/米黄,褪色感
- **构图**:单点透视,对称,无限延伸
- **示例**:liminal space, empty mall corridor at closing time, fluorescent lights, polished floor reflecting, no people, no signs of life, uncanny familiarity, one-point perspective, eerie stillness

### C4. 巨构城市（Megacity）
- **触发词**:megacity, megastructure
- **关键词**:colossal cityscape, towering megastructures, aerial perspective, endless urban sprawl, scale contrast, tiny figures, monumental urbanism
- **负面词**:rural, single building, flat skyline, cozy
- **光线**:蓝时/黄昏,城市灯光,雾
- **色彩**:冷蓝灰+暖窗灯点缀
- **构图**:航拍极远景,尺度对比
- **示例**:megacity aerial view, colossal megastructures towering to the sky, endless urban sprawl fading into fog, tiny figures on plaza for scale, blue hour, cold blue-grey with warm window lights, monumental urbanism

### C5. 中式园林（Chinese Garden）
- **触发词**:Chinese classical garden, 中式园林
- **关键词**:rockery, moon gate, pavilion, lattice window, koi pond, mist, bonsai, bamboo, curved eaves, poetic atmosphere
- **负面词**:modern glass, western palace, crowded, neon
- **光线**:晨雾柔光,月光,灯笼暖光
- **色彩**:黛瓦白墙,竹青,木褐,水影
- **构图**:框景(月洞门/花窗),借景,留白
- **示例**:Chinese classical garden, white wall and dark tiles, rockery with moss, moon gate framing bamboo, koi pond with mist, lattice window, morning soft light, poetic quiet atmosphere, ink-wash color palette

### C6. 废墟神庙（Ruined Temple）
- **触发词**:ruined temple, ancient ruins
- **关键词**:crumbling columns, broken statues, overgrown stone, dappled light, sacred decay, moss, fallen blocks, eternal silence
- **负面词**:modern, restored, bright, tourist-filled, pristine
- **光线**:树影斑驳,斜阳穿林
- **色彩**:石灰+苔绿+暖金斜光
- **构图**:柱列透视,仰视断柱
- **示例**:ruined ancient temple, crumbling marble columns, broken statue half-covered in moss, dappled sunlight through trees, overgrown stone blocks, sacred decay, eternal silence, warm gold light on grey stone

### C7. 太空港（Spaceport）
- **触发词**:spaceport, space station
- **关键词**:massive docking bay, spacecraft, industrial corridors, panoramic space view, launch towers, engineering scale, cold metal and glass, orbital station
- **负面词**:cyberpunk neon, fantasy, steam, medieval
- **光线**:舷窗硬光,空间站冷白照明
- **色彩**:金属灰/深空黑+舷窗蓝
- **构图**:巨构对比小人,对称轴线
- **示例**:spaceport interior, massive docking bay with a spacecraft, industrial catwalks, panoramic window showing planet below, launch tower, engineering scale, tiny technicians for scale, cold metal and glass, hard window light, symmetrical axis

### C8. 江南水乡（Jiangnan Water Town）
- **触发词**:江南水乡, Jiangnan water town
- **关键词**:whitewashed walls, black tiles, stone bridge, canal, gondola, willows, misty morning, lanterns, water reflection, rain
- **负面词**:modern skyscraper, desert, neon, western
- **光线**:晨雾柔光,黄昏灯笼暖光,雨幕
- **色彩**:黛瓦白墙/青灰水面/红灯笼点缀
- **构图**:河道透视,拱桥框架,倒影对称
- **示例**:江南水乡, 白墙黛瓦沿河而建, 石拱桥跨过河道, 乌篷船停靠, 晨雾弥漫, 水面倒影, 柳枝垂落, 几点红灯笼, 青灰调, 宁静诗意, 雨后湿润感

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

### D2. 怪核（Weirdcore）
- **触发词**:weirdcore
- **关键词**:low quality, glitch, uncanny, distorted, cryptic text, out of place, unsettling, liminal, analog distortion, eerie collage
- **负面词**:clean, polished, beautiful, coherent, high quality
- **光线**:过曝/欠曝,不自然光
- **色彩**:褪色/灰绿/局部鲜艳
- **构图**:失衡,拼贴感,违和元素
- **示例**:weirdcore image, low quality analog photo, glitch distortion, a bedroom with a tree growing through the floor, cryptic handwritten text, uncanny unsettling mood, faded colors, distorted perspective, harsh unnatural flash lighting

### D3. 雨核（Raincore）
- **触发词**:raincore
- **关键词**:heavy rain, wet reflections, window raindrops, blurred city, cozy inside, moody sky, water droplets, grey-blue tones, rain sound
- **负面词**:sunny, dry, bright cheerful, harsh shadows
- **光线**:阴雨漫射,室内暖灯
- **色彩**:冷灰蓝+室内暖光
- **构图**:窗内看外,雨中街道,水洼倒影
- **示例**:raincore, heavy rain on window glass, blurred city outside, a warm lamp glowing inside the room, water droplets running down, cold grey-blue tones with warm indoor light, wet reflections, close-up through window, shallow depth of field

### D4. 池核（Poolcore）
- **触发词**:poolcore
- **关键词**:empty swimming pool, still water, tiles, reflection, indoor pool light, echo, chlorine blue, liminal water, vacant
- **负面词**:crowded, beach, sunny fun, people swimming
- **光线**:天窗光,水面反光
- **色彩**:池水蓝绿+瓷砖白
- **构图**:俯视水面,对称泳道,空无一人
- **示例**:poolcore, empty indoor swimming pool, perfectly still turquoise water, white tile walls, skylight reflection on water surface, no people, echo of silence, liminal atmosphere, blue-green tones

### D5. 植核（Plantcore）
- **触发词**:plantcore, overgrown
- **关键词**:plants reclaiming, moss covered, vines on structures, greenhouse, lush greenery, nature takeover, humid, ferns, botanical ruins
- **负面词**:desert, dead, sterile, minimal
- **光线**:温室散射光,叶影
- **色彩**:深绿/苔绿/雾白
- **构图**:植被前景框架,爬藤引导线
- **示例**:plantcore, abandoned greenhouse overgrown with ferns and vines, moss covering concrete paths, lush green everywhere, humid atmosphere, soft diffused light through glass, nature reclaiming, deep greens

### D6. 中式梦核（Chinese Dreamcore）
- **触发词**:中式梦核, Chinese dreamcore
- **关键词**:千禧年记忆, 旧小区, 老式家具, 斑驳墙面, 阳光斜照, VHS质感, 半透明窗帘, 记忆模糊感, 怀旧不安
- **负面词**:现代建筑, 科幻, 恐怖, 鲜艳, 清晰锐利
- **光线**:过曝柔光,夕阳斜照,记忆感模糊
- **色彩**:米黄/粉彩/褪色,低饱和
- **构图**:日常场景错位,熟悉又陌生
- **示例**:中式梦核, 千禧年旧小区的楼道, 老式防盗门, 斑驳的米黄墙面, 夕阳从窗户斜照进来, 地面有拖把的水痕, VHS质感, 怀旧而微微不安

### D7. 旧核（Oldcore / 复古核）
- **触发词**:oldcore, retro core
- **关键词**:1950s-80s nostalgia, old photographs, CRT TV, wood paneling, vintage tech, family album, retro kitchen, warm decay, forgotten era
- **负面词**:modern clean, futuristic, sharp digital, neon cyberpunk
- **光线**:旧照片泛黄光,CRT 荧幕光
- **色彩**:棕褐/米黄/褪色红,暖旧调
- **构图**:家庭旧物堆叠,电视/收音机时代道具
- **示例**:oldcore aesthetic, 1980s family living room, wood paneling walls, CRT television glowing, retro kitchen appliances, faded family photos on shelf, warm decay, forgotten era, vintage texture, brown and beige tones

### D8. 云核（Cloudcore）
- **触发词**:cloudcore
- **关键词**:floating islands, clouds below, soft dreamy sky, surreal altitude, lone structure on cloud, gentle pastel, weightless, ethereal
- **负面词**:dark, stormy, grounded, gritty, neon
- **光线**:高空柔光,云海反照
- **色彩**:云白/天空蓝/淡金
- **构图**:云海为地平,悬浮主体,留白
- **示例**:cloudcore, a small white chapel floating on a cloud sea, wide shot, soft dreamy sky, pastel blue and gold, ethereal weightless atmosphere, clouds below as horizon, gentle surrealism, lone structure, airy composition, high-altitude soft light

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

### E2. 长曝光（Long Exposure）
- **触发词**:long exposure
- **关键词**:silky water, light trails, star trails, motion blur clouds, ND filter, smooth surfaces, time compression
- **负面词**:frozen action, sharp moving objects, handheld shake
- **光线**:低光+慢门,夜晚/黎明
- **色彩**:冷蓝夜+暖光轨
- **构图**:静止前景+流动背景
- **示例**:long exposure city night, car light trails streaming through streets, silky river water, star trails above, ND filter smoothness, cold blue night with warm light trails, time compressed

### E3. 航拍（Aerial）
- **触发词**:aerial view, drone shot
- **关键词**:top-down, bird's eye, patterns, geometry from above, landscape abstraction, DJI, satellite-like, scale revealed
- **负面词**:ground level, eye level, close-up
- **光线**:正午顶光/黄昏低角
- **色彩**:地形色块,高饱和
- **构图**:俯视图案化,对称
- **示例**:aerial drone view, top-down of terraced rice fields, geometric patterns, lush green terraces with water reflections, DJI Hasselblad look, pattern abstraction, morning light, sweeping scale

### E4. 微距（Macro）
- **触发词**:macro photography
- **关键词**:extreme close-up, insect eye, dew drop, petal texture, shallow depth of field, magnification, tiny world, bokeh
- **负面词**:wide scene, landscape, distant subject
- **光线**:环形灯/自然侧光
- **色彩**:局部高饱和+背景虚化
- **构图**:主体充满,浅景深
- **示例**:macro photography, extreme close-up of a dragonfly on a leaf, dew drops, wing texture visible, shallow depth of field, creamy bokeh background, morning light, tiny world detail

### E5. 移轴（Tilt-Shift）
- **触发词**:tilt-shift, miniature effect
- **关键词**:selective focus, miniature city, toy-like, bokeh blur top and bottom, forced perspective, tiny people
- **负面词**:deep focus, realistic scale, full sharpness
- **光线**:明亮均匀
- **色彩**:鲜艳玩具感
- **构图**:高处俯视,焦点窄带
- **示例**:tilt-shift photo, miniature city effect, cars and people look like toys, narrow sharp focus band, blur top and bottom, high angle, bright cheerful light, forced perspective

### E6. 双重曝光（Double Exposure）
- **触发词**:double exposure
- **关键词**:two images merged, silhouette with landscape inside, transparency overlap, ghostly, layered, film magic
- **负面词**:single exposure, clean separation, photorealistic single subject
- **光线**:逆光剪影为底
- **色彩**:底图色+叠加图调
- **构图**:人形/山形轮廓+内部风景
- **示例**:double exposure, silhouette of a woman's profile filled with a pine forest and misty mountains, ghostly transparency, layered film effect, warm light through trees, poetic

### E7. 黑白街拍（Monochrome Street）
- **触发词**:monochrome street photography
- **关键词**:black and white, high contrast, decisive moment, shadow play, urban geometry, candid, grain, Leica, documentary
- **负面词**:color, soft pastel, studio, posed
- **光线**:硬光强影,侧逆光
- **色彩**:纯黑白,灰阶丰富
- **构图**:抓拍瞬间,光影切割,几何框
- **示例**:monochrome street photography, Leica look, high contrast black and white, decisive moment, shadow slicing across alley, candid pedestrian, film grain, urban geometry, documentary feel

### E8. 红外摄影（Infrared）
- **触发词**:infrared photography
- **关键词**:false color, foliage glowing white-pink, surreal sky, dark water, eerie vegetation, dreamlike landscape, IR filter
- **负面词**:natural colors, normal green foliage, realistic skin tone
- **光线**:强日光(红外需要光)
- **色彩**:叶白/天深蓝/水近黑
- **构图**:树木剪影,水面反射,超现实场景
- **示例**:infrared photography, trees glowing white and pink, deep blue sky, water nearly black, surreal dreamlike landscape, eerie vegetation glow, strong sunlight, IR false color, otherworldly mood

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

### M2. 孤独深夜（Nocturne Loneliness）
- **触发词**:loneliness at night, night solitude
- **关键词**:empty street at night, single warm window, streetlight pool, fog, quiet city, reflections on wet asphalt, solitary figure
- **负面词**:crowded street, party, bright daylight, cheerful
- **光线**:路灯暖光孤岛,月光冷衬
- **色彩**:深蓝黑+暖黄灯点缀
- **构图**:人物背影,路灯成孤岛
- **示例**:empty city street at night, fog, one streetlight casting a warm pool of light, solitary figure walking away, wet asphalt reflecting the light, quiet melancholy, deep blue-black with warm yellow accent

### M3. 神圣庄严（Sacred Awe）
- **触发词**:sacred, awe
- **关键词**:cathedral-like space, shaft of light, dust motes, vaulted ceiling, silence, reverence, monumental void, stained glass
- **负面词**:noisy, casual, mundane, crowded
- **光线**:天窗光束,神圣感
- **色彩**:暖金+深影
- **构图**:仰视穹顶,对称
- **示例**:sacred monumental hall, shaft of light from high window, dust motes floating, vaulted ceiling, profound silence, reverence, warm golden light against deep shadow, symmetric composition

### M4. 静谧田园（Pastoral Serenity）
- **触发词**:pastoral, serene
- **关键词**:rolling hills, morning mist, farmhouse, golden light, wildflowers, peaceful, birds, dew, quiet countryside
- **负面词**:urban, industrial, dark, chaotic
- **光线**:晨光/黄金时刻,薄雾
- **色彩**:嫩绿/暖金/雾白
- **构图**:层叠丘陵,引导线
- **示例**:pastoral landscape, rolling green hills in morning mist, small farmhouse, golden sunrise light, wildflowers in foreground, dew on grass, peaceful serene mood, soft warm tones

### M5. 末世寂灭（Post-Human Silence）
- **触发词**:post-human, after humanity
- **关键词**:overgrown city, silent architecture, nature reclaiming, no humans, frozen time, moss covered, silent streets, civilization's echo
- **负面词**:people, vehicles, active, bright commercial
- **光线**:阴天/雾,无阳光
- **色彩**:灰绿/棕褐,低饱和
- **构图**:无人巨构,植被入侵
- **示例**:post-human city, extreme wide aerial view, overgrown silent streets, moss covered buildings, vines on skyscrapers, no humans no vehicles, frozen time, grey-green tones, nature reclaiming civilization, silent echo, flat overcast light

### M6. 温暖治愈（Cozy Warmth）
- **触发词**:cozy, hygge
- **关键词**:warm light, fireplace glow, soft blanket, cup of tea, rainy window, warm wood, comfortable, intimate, gentle
- **负面词**:cold, clinical, empty, harsh light, spacious void
- **光线**:壁炉暖光,窗边柔光
- **色彩**:暖橙/木褐/奶油
- **构图**:近景,包围感
- **示例**:cozy interior, fireplace glow, soft blanket on armchair, cup of tea steaming, rain on window, warm wood tones, intimate comfortable atmosphere, soft warm light, gentle shadows

### M7. 悬疑紧张（Suspense）
- **触发词**:suspense, thriller mood
- **关键词**:dark corridor, half-open door, single light source, long shadows, tension, ambiguous, off-frame threat, muted cold light
- **负面词**:bright, cheerful, cozy, daylight, mundane
- **光线**:单光源,硬阴影
- **色彩**:冷蓝黑,局部暖警示
- **构图**:门缝视角,前景遮挡
- **示例**:suspenseful hallway, half-open door at the end, single harsh light source, long distorted shadows, tension in the air, cold blue-black palette, off-frame implied threat, ambiguous mood

### M8. 敬畏崇高（Sublime）
- **触发词**:sublime, overwhelming nature
- **关键词**:colossal scale, tiny human, storm sky, mountain vastness, ocean power, awe, insignificance, dramatic light
- **负面词**:safe, cozy, mundane, small scale
- **光线**:风暴光/破云光
- **色彩**:暗色+破晓金光
- **构图**:极端尺度对比
- **示例**:sublime landscape, tiny climber on colossal cliff face, storm clouds breaking with a shaft of light, overwhelming scale, awe and insignificance, dramatic contrast, dark tones with golden break

### M9. 静谧清晨（Quiet Dawn）
- **触发词**:quiet dawn, early morning
- **关键词**:soft mist, first light, dew, empty street, birdsong, pale blue sky, calm water, fresh air, peaceful stillness
- **负面词**:dark night, harsh midday, crowded, noisy
- **光线**:日出前柔光,薄雾
- **色彩**:淡蓝/粉橙/雾白
- **构图**:开阔远景,低对比
- **示例**:quiet dawn, thin mist over calm lake, first soft light, pale blue and pink sky, empty lakeside path, dew on grass, peaceful stillness, birdsong implied, gentle tones

### M10. 暴风雨前（Before the Storm）
- **触发词**:before the storm, storm brewing
- **关键词**:dark clouds gathering, oppressive sky, still air, tense atmosphere, muted colors, light fading, anticipation, wind bending grass
- **负面词**:bright sunny, cheerful, clear sky, settled
- **光线**:乌云遮日,最后一缕光
- **色彩**:墨灰+土黄,高对比暗调
- **构图**:低角度仰天,空旷地平线
- **示例**:before the storm, dark clouds gathering over flat farmland, oppressive sky, still air, one last shaft of light on the horizon, wind bending grass, tense anticipation, muted grey-yellow tones

### M11. 烟火人间（Everyday Warmth）
- **触发词**:everyday life, human warmth
- **关键词**:street vendor steam, market bustle, warm lanterns, evening street, family dinner, neighborhood, living moments, golden glow
- **负面词**:empty, cold, dystopian, futuristic
- **光线**:黄昏暖光,路灯,蒸汽
- **色彩**:暖橙/木褐/红灯笼
- **构图**:中景生活流,密集但不乱
- **示例**:evening street market, steam rising from food stalls, warm lanterns glowing, people in daily life, golden hour light, bustling but warm, rich orange and brown tones, human warmth

### M12. 深海静谧（Deep Sea Quiet）
- **触发词**:deep sea, underwater stillness
- **关键词**:blue gradient, light rays through water, floating particles, marine life silhouette, silent depth, bioluminescence, pressure, vast blue
- **负面词**:beach, bright sunny surface, crowded reef
- **光线**:水面透光,生物光
- **色彩**:深蓝/青/荧光点缀
- **构图**:光柱透视,俯视深渊
- **示例**:deep sea, light rays penetrating dark blue water, floating particles, a whale silhouette in the distance, bioluminescent dots, silent depth, gradient from dark navy to teal, vast and quiet

### M13. 宇宙孤寂（Cosmic Isolation）
- **触发词**:cosmic isolation, space solitude
- **关键词**:lone spacecraft, distant planet, star field, void, silent vastness, earthshine, awe of scale, cold light
- **负面词**:busy space battle, colorful nebula fantasy, crowded
- **光线**:恒星侧光,行星反照
- **色彩**:深空黑+冷蓝+暖星点
- **构图**:小飞船大虚空,对角线
- **示例**:cosmic isolation, lone spacecraft drifting near a distant ringed planet, vast star field, deep void, cold side light, silent immensity, tiny human craft against cosmic scale, dark blue-black with warm star points

### M14. 乡愁怀旧（Nostalgia）
- **触发词**:nostalgia, retro memory
- **关键词**:old photograph, faded colors, childhood home, vintage furniture, sepia tones, remembered light, worn objects, tender longing
- **负面词**:modern, new, sharp digital, cold
- **光线**:旧照片感,柔焦
- **色彩**:泛黄/褪色/暖棕
- **构图**:旧物特写,记忆碎片
- **示例**:nostalgic scene, faded old photograph look, childhood home interior, worn wooden furniture, sepia and warm brown tones, soft remembered light, dust in sunbeam, tender longing, vintage texture

### M15. 权力威压（Monumental Power）
- **触发词**:monumental power, authority
- **关键词**:colossal statue, government hall, symmetrical columns, low angle, shadows, scale of state, marble and stone, oppressive grandeur
- **负面词**:cozy, small, playful, informal
- **光线**:硬光,强明暗阴影
- **色彩**:石色+深影,高对比
- **构图**:低角度仰视,对称中轴
- **示例**:monumental power, colossal stone statue in symmetrical government hall, low angle looking up, hard side light carving deep shadows, marble and granite, oppressive grandeur, scale of state, awe and intimidation

### M16. 温暖黄昏（Golden Evening）
- **触发词**:golden hour, evening glow
- **关键词**:warm sunset, long shadows, amber light, silhouettes, dust in light, peaceful end of day, golden haze
- **负面词**:noon, harsh light, cold tones, night
- **光线**:低角度暖光,长影
- **色彩**:琥珀/橙红/深紫
- **构图**:逆光剪影,地平线
- **示例**:golden evening, low warm sun, long shadows on wheat field, amber light everywhere, silhouette of a tree and birds, dust glowing in light, peaceful end of day, golden haze, rich orange tones

### M17. 诡异不安（Uncanny Unease）
- **触发词**:uncanny, uneasy
- **关键词**:too-perfect scene, wrong details, subtle wrongness, empty space watching, muted eerie light, familiar space altered, quiet dread
- **负面词**:comfortable, bright cheerful, obvious horror, gore
- **光线**:均匀但偏色,无自然感
- **色彩**:褪色+偏绿/偏蓝
- **构图**:正常构图但细节违和
- **示例**:uncanny scene, an immaculate suburban street but the houses have no doors, wrong subtle details, muted eerie light, empty space that feels watched, familiar space altered, quiet dread, faded greenish tones, medium shot at eye level, normal daylight but slightly off

### M18. 冬季寂寥（Winter Stillness）
- **触发词**:winter stillness, snow quiet
- **关键词**:fresh snow, bare trees, frozen lake, breath fog, muted white, cold blue, silent landscape, solitary cabin
- **负面词**:summer, green, crowded, warm bright
- **光线**:阴天雪光,低角度冷阳
- **色彩**:雪白+冰蓝+枯灰
- **构图**:留白雪地,孤树/孤屋
- **示例**:winter stillness, wide shot, fresh snow on frozen lake, bare trees, silent white landscape, cold blue shadows, a solitary cabin with smoke, muted tones, breath fog implied, absolute quiet, low winter sun

### M19. 都市疏离（Urban Alienation）
- **触发词**:urban alienation, city isolation
- **关键词**:crowded street but lonely, anonymous figures, glass reflections, cold architecture, rain, no eye contact, isolated in mass, grey tones
- **负面词**:warm community, cozy, countryside
- **光线**:阴天城市光,玻璃反光
- **色彩**:冷灰蓝,低饱和
- **构图**:人群中的孤立个体,反射构图
- **示例**:urban alienation, crowded city sidewalk but everyone isolated, anonymous figures with umbrellas, cold glass reflections, rain, grey-blue tones, no eye contact, loneliness in the mass, modern architecture looming, overcast diffused daylight

### M20. 沙漠孤旅（Desert Solitude）
- **触发词**:desert solitude
- **关键词**:endless dunes, lone traveler, heat haze, vast silence, wind ripples, minimal shadow, gold and sand, slow time
- **负面词**:crowded oasis, green, rainy, urban
- **光线**:正午顶光/黄昏长影
- **色彩**:沙金/焦赭/天蓝
- **构图**:沙丘引导线,人物渺小
- **示例**:desert solitude, extreme wide shot, endless golden dunes, a lone traveler walking a ridge line, heat haze, wind ripples on sand, vast silence, minimal shadow at noon, slow time, gold and sand tones with deep blue sky, harsh high sun

### M21. 极光秘境（Aurora Dream）
- **触发词**:aurora, northern lights
- **关键词**:green and violet sky curtains, snowfield glow, star field, reflected in frozen lake, silent polar night, shimmering light, cold clean air
- **负面词**:daylight, warm tropical, crowded, city lights
- **光线**:极光为主光源,月光辅
- **色彩**:极光绿/紫+雪地蓝白
- **构图**:极光穹顶,水面倒影,前景剪影
- **示例**:aurora dream, green and violet aurora curtains over snowfield, stars visible, aurora reflected in frozen lake, silent polar night, shimmering light, cold clean air, lone cabin silhouette, blue-white snow glow

### M22. 幽暗森林（Dark Forest）
- **触发词**:dark forest, woods at dusk
- **关键词**:dense trees, filtered dim light, fog between trunks, moss ground, mysterious path, muted green-brown, quiet dread, ancient woods
- **负面词**:bright sunny, cheerful park, urban, colorful
- **光线**:树冠滤光,暮色
- **色彩**:墨绿/深棕/雾灰
- **构图**:树列透视,小径引导,光线缝隙
- **示例**:dark forest, dense ancient trees, dim light filtering through canopy, fog drifting between trunks, moss-covered ground, a faint path disappearing into shadow, muted green and brown, quiet dread, mysterious stillness

### M23. 樱花春日（Cherry Blossom Spring）
- **触发词**:cherry blossom, spring
- **关键词**:pink petals falling, soft sunlight, sakura trees in bloom, gentle breeze, pastel sky, petals on water, dreamy brightness, renewal
- **负面词**:autumn, dead branches, harsh contrast, winter
- **光线**:晨光透花,柔和逆光
- **色彩**:樱粉/天蓝/嫩绿
- **构图**:花瓣前景散景,树下人影,河道花瓣
- **示例**:cherry blossom spring, sakura trees in full bloom, pink petals falling in gentle breeze, soft morning sunlight through petals, pastel blue sky, petals floating on stream, dreamy brightness, sense of renewal, shallow depth of field

### M24. 老城烟火（Old Town Life）
- **触发词**:old town, historic street
- **关键词**:narrow alley, worn stone walls, hanging laundry, evening lamps, old shops, resident life, warm windows, layered architecture, timeless
- **负面词**:modern glass, empty, new, commercial
- **光线**:黄昏街灯,窗口暖光,天色余晖
- **色彩**:暖黄灯光+青灰墙面+褪色招牌
- **构图**:巷道纵深,门框取景,生活细节
- **示例**:old town evening, narrow stone alley, hanging laundry between buildings, warm lamps glowing, old shop signs, resident silhouettes in windows, layered historic architecture, timeless atmosphere, golden streetlight on worn walls

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
