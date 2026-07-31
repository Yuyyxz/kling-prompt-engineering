# Anti-Slop 替换表 (Anti-Slop Lexicon)
# 独立可查的参考文件

## 概述

这是 Anti-Slop 弱词替换表的独立参考文件。
Skill 是"怎么做"，Reference 是"查什么"。

---

## 硬删除规则

以下词汇如果出现在用户输入或 Agent 草稿中，在最终输出前必须被完全移除，不做任何替换：

### 画质词（由 API 参数控制）

| 词汇 | 删除原因 |
|------|----------|
| 4K | 分辨率由 API 参数 resolution=3840x2160 控制 |
| 8K | 分辨率由 API 参数控制 |
| ultra HD | 分辨率由 API 参数控制 |
| high resolution | 分辨率由 API 参数控制 |
| high quality | 画质词是废话 |
| masterpiece | 画质词是废话 |
| best quality | 画质词是废话 |
| top quality | 画质词是废话 |

### 形容词（废话）

| 词汇 | 删除原因 |
|------|----------|
| beautiful | 应该用具体的技术描述替代 |
| stunning | 应该用具体的技术描述替代 |
| amazing | 应该用具体的技术描述替代 |
| awesome | 应该用具体的技术描述替代 |
| epic | 应该用具体的技术描述替代 |

### 特殊规则

| 词汇 | 处理方式 | 原因 |
|------|----------|------|
| cinematic | 删除，除非后面跟了具体景别+光源 | 应该用具体的技术描述替代 |

---

## 替换规则

以下词汇应该被替换为具体的技术描述：

### 视觉风格类

| 弱词 | 替换为 | 示例 |
|------|--------|------|
| cinematic | 电影级质感 | ❌ cinematic shot → ✅ 中景，眼平角度；缓慢推进；侧光，营造层次感 |
| beautiful | 精美 | ❌ beautiful scene → ✅ 远景，夕阳下的海边，金色光芒洒在海面上 |
| stunning | 震撼 | ❌ stunning visual → ✅ 特写，眼睛的特写，瞳孔中倒映出火焰 |
| breathtaking | 令人窒息 | ❌ breathtaking view → ✅ 远景，广阔的草原上，一个孤独的身影 |
| epic | 史诗级 | ❌ epic scene → ✅ 远景，千军万马，尘土飞扬 |
| dramatic | 戏剧性 | ❌ dramatic lighting → ✅ 侧光，一半脸在阴影中，一半脸在光明中 |

### 情感类

| 弱词 | 替换为 | 示例 |
|------|--------|------|
| emotional | 情感丰富 | ❌ emotional scene → ✅ 近景，眼神中透露出悲伤，泪水在眼眶中打转 |
| powerful | 强烈 | ❌ powerful moment → ✅ 特写，拳头紧握，青筋暴起 |
| intense | 紧张 | ❌ intense scene → ✅ 快速推进，手持晃动，心跳声加速 |
| touching | 感人 | ❌ touching moment → ✅ 近景，母亲抚摸孩子的脸，眼神温柔 |

### 运动类

| 弱词 | 替换为 | 示例 |
|------|--------|------|
| smooth | 流畅 | ❌ smooth movement → ✅ 缓慢推进，稳定器跟拍，无晃动 |
| dynamic | 动态 | ❌ dynamic shot → ✅ 快速推进，手持晃动，节奏感强 |
| elegant | 优雅 | ❌ elegant movement → ✅ 缓慢横移，稳定器跟拍，动作流畅 |

### 光影类

| 弱词 | 替换为 | 示例 |
|------|--------|------|
| moody | 氛围感 | ❌ moody lighting → ✅ 侧光，一半脸在阴影中，营造神秘感 |
| atmospheric | 氛围 | ❌ atmospheric scene → ✅ 远景，雾气弥漫，若隐若现 |
| warm | 温暖 | ❌ warm lighting → ✅ 暖色调，金色光芒，温馨感 |
| cold | 冷峻 | ❌ cold lighting → ✅ 冷色调，蓝光为主，科技感 |

---

## 执行方式

1. **正则匹配删除**：不是"建议不用"，是"必须删除"
2. **删除后重写**：如果句子不通顺，重写该句
3. **替换为具体描述**：用具体的技术描述替代弱词

---

## 使用示例

### 示例 1：删除画质词

**输入：**
```
一个 cinematic、beautiful、epic 的 4K masterpiece 视频
```

**处理：**
1. 删除 4K（画质词）
2. 删除 masterpiece（画质词）
3. 替换 cinematic → 电影级质感
4. 替换 beautiful → 精美
5. 替换 epic → 史诗级

**输出：**
```
一个电影级质感、精美、史诗级的视频
```

### 示例 2：替换情感词

**输入：**
```
一个 emotional、powerful、intense 的场景
```

**处理：**
1. 替换 emotional → 情感丰富
2. 替换 powerful → 强烈
3. 替换 intense → 紧张

**输出：**
```
一个情感丰富、强烈、紧张的场景
```

### 示例 3：完整处理

**输入：**
```
帮我做一个 cinematic、beautiful、epic 的 4K masterpiece 视频，
画面 stunning，motion smooth，非常 realistic
```

**处理：**
1. 删除 4K（画质词）
2. 删除 masterpiece（画质词）
3. 替换 cinematic → 电影级质感
4. 替换 beautiful → 精美
5. 替换 epic → 史诗级
6. 替换 stunning → 震撼
7. 替换 smooth → 流畅
8. 替换 realistic → 写实

**输出：**
```
帮我做一个电影级质感、精美、史诗级的视频，
画面震撼，motion 流畅，非常写实
```

---

## 约束条件

- 硬删除规则必须执行，不是建议
- 删除后如果句子不通顺，必须重写
- 替换为具体的技术描述，不是同义词
- 正则匹配删除，不是手动删除
