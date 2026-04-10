# MiniMax Text-to-Image (T2I)

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

A skill for generating images from text prompts using MiniMax AI, with automatic prompt expansion and Feishu integration. Works with openclaw, Claude Code, Codex, and other tools that support skills.

### Installation (openclaw example)

**Method 1: Clone to skills directory**
```bash
cd /root/.openclaw/skills
git clone https://github.com/yeqing17/minimax-image-t2i.git
```

**Method 2: Install from .skill file**

Download from [Releases](https://github.com/yeqing17/minimax-image-t2i/releases), then:
```bash
cp minimax-image-t2i.skill /root/.openclaw/skills/
```

### Configuration

Set your MiniMax API key (Linux/macOS/Windows Git Bash):
```bash
export MINIMAX_API_KEY=your_api_key_here
```

Optional: Customize output directory (default: `~/minimax-images`)
```bash
export MINIMAX_OUTPUT_DIR="/path/to/your/output"
```

### Usage

Once installed, the skill will automatically trigger when you ask to generate images.

**Trigger phrases:** "generate image", "create image", "draw me", "text-to-image", "生成图片", "画一张图", "帮我画"

**Examples:**
- "帮我生成一张可爱的卡通螃蟹"
- "Generate a sunset beach scene"
- "画3张猫咪的图片"

### Features

- 🎨 Text-to-Image via MiniMax API
- ✨ Auto prompt expansion for short prompts
- 📱 Feishu integration
- 🌐 Bilingual (EN/CN)

---

<a name="中文"></a>
## 中文

一个基于 MiniMax AI 的技能，支持从文本提示生成图片，具有自动提示词扩写和飞书集成功能。适用于 openclaw、Claude Code、Codex 等支持 skills 的工具。

### 安装（以 openclaw 为例）

**方式 1：克隆到技能目录**
```bash
cd /root/.openclaw/skills
git clone https://github.com/yeqing17/minimax-image-t2i.git
```

**方式 2：通过 .skill 文件安装**

从 [Releases](https://github.com/yeqing17/minimax-image-t2i/releases) 下载，然后：
```bash
cp minimax-image-t2i.skill /root/.openclaw/skills/
```

### 配置

设置 MiniMax API 密钥 (Linux/macOS/Windows Git Bash)：
```bash
export MINIMAX_API_KEY=your_api_key_here
```

可选：自定义输出目录（默认：`~/minimax-images`）
```bash
export MINIMAX_OUTPUT_DIR="/path/to/your/output"
```

### 使用

安装后，当你请求生成图片时，技能会自动触发。

**触发短语：** "generate image", "create image", "draw me", "生成图片", "画一张图", "帮我画"

**示例：**
- "帮我生成一张可爱的卡通螃蟹"
- "Generate a sunset beach scene"
- "画3张猫咪的图片"

### 功能特性

- 🎨 通过 MiniMax API 文生图
- ✨ 短提示词自动扩写
- 📱 飞书集成
- 🌐 中英双语支持

---

## Script Reference (脚本说明)

The skill includes a Python script `scripts/minimax-image.py` for direct usage.

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `prompt` | Image description (required) | - |
| `-n, --num` | Number of images (1-9) | 1 |
| `-a, --aspect` | Aspect ratio | 1:1 |
| `-m, --model` | Model (image-01 / image-01-live) | image-01 |
| `-o, --output` | Output filename | image.png |
| `--no-expand` | Disable prompt expansion | - |

**Aspect ratios:** `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`

### Prompt Expansion

Short prompts (< 30 chars) are auto-expanded using MiniMax LLM.

**Example:**
- Input: `"一只猫"` / `"a cat"`
- Expanded: `"A fluffy adorable cat sitting on a windowsill, soft natural lighting, warm afternoon sun, photorealistic, 4K, high detail, front view"`

---

## License

MIT
