# MiniMax Text-to-Image (T2I)

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

A Claude Code skill for generating images from text prompts using MiniMax AI, with automatic prompt expansion and Feishu integration.

### Features

- 🎨 **Text-to-Image Generation** - Generate high-quality images via MiniMax API
- ✨ **Auto Prompt Expansion** - Short prompts are automatically expanded using MiniMax LLM for better results
- 📱 **Feishu Integration** - Seamlessly send generated images to users via Feishu
- 🌐 **Bilingual Support** - Documentation in both English and Chinese

### Requirements

- Python 3.x
- `requests` library
- MiniMax API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yeqing17/minimax-image-t2i.git
```

2. Install dependencies:
```bash
pip install requests
```

3. Set your MiniMax API key:
```bash
# Linux/macOS/Windows Git Bash
export MINIMAX_API_KEY=your_api_key_here
```

### Usage

Basic usage:
```bash
python minimax-image-t2i/scripts/minimax-image.py "your image description" -n 1 -a 16:9 -o output.png
```

**Examples:**
```bash
# Generate a single square image
python minimax-image.py "a cute cartoon crab" -n 1 -a 1:1 -o crab.png

# Generate 3 landscape images
python minimax-image.py "sunset beach scene" -n 3 -a 16:9 -o beach.png

# Skip prompt expansion
python minimax-image.py "your detailed prompt here" --no-expand
```

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `prompt` | Image description (required) | - |
| `-n, --num` | Number of images to generate (1-9) | 1 |
| `-a, --aspect` | Aspect ratio | 1:1 |
| `-m, --model` | Model to use (image-01 / image-01-live) | image-01 |
| `-o, --output` | Output filename | image.png |
| `--no-expand` | Disable automatic prompt expansion | - |

**Available aspect ratios:** `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`

### Prompt Expansion

Short prompts (< 30 characters) are automatically expanded using MiniMax LLM to generate more detailed and professional descriptions.

**Example:**
- **Input:** `"a cat"`
- **Expanded:** `"A fluffy adorable cat sitting on a windowsill, soft natural lighting, warm afternoon sun, photorealistic, 4K, high detail, front view"`

---

<a name="中文"></a>
## 中文

一个基于 MiniMax AI 的 Claude Code 技能，支持从文本提示生成图片，具有自动提示词扩写和飞书集成功能。

### 功能特性

- 🎨 **文生图** - 通过 MiniMax API 生成高质量图片
- ✨ **自动提示词扩写** - 短提示词会自动通过 MiniMax LLM 扩写，生成更详细专业的描述
- 📱 **飞书集成** - 无缝将生成的图片发送给用户
- 🌐 **双语支持** - 中英文文档

### 环境要求

- Python 3.x
- `requests` 库
- MiniMax API 密钥

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/yeqing17/minimax-image-t2i.git
```

2. 安装依赖：
```bash
pip install requests
```

3. 设置 MiniMax API 密钥：
```bash
# Linux/macOS/Windows Git Bash
export MINIMAX_API_KEY=your_api_key_here
```

### 使用方法

基本用法：
```bash
python minimax-image-t2i/scripts/minimax-image.py "图片描述" -n 1 -a 16:9 -o output.png
```

**示例：**
```bash
# 生成单张正方形图片
python minimax-image.py "一只可爱的卡通螃蟹" -n 1 -a 1:1 -o crab.png

# 生成3张横版风景图
python minimax-image.py "海边日落风景" -n 3 -a 16:9 -o beach.png

# 跳过提示词扩写
python minimax-image.py "你详细描述的提示词" --no-expand
```

### 参数说明

| 参数 | 描述 | 默认值 |
|------|------|--------|
| `prompt` | 图片描述（必填） | - |
| `-n, --num` | 生成图片数量 (1-9) | 1 |
| `-a, --aspect` | 宽高比 | 1:1 |
| `-m, --model` | 模型 (image-01 / image-01-live) | image-01 |
| `-o, --output` | 输出文件名 | image.png |
| `--no-expand` | 禁用自动提示词扩写 | - |

**可用宽高比：** `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`

### 提示词扩写

短提示词（< 30 字符）会自动通过 MiniMax LLM 扩写，生成更详细专业的描述。

**示例：**
- **输入：** `"一只猫"`
- **扩写后：** `"A fluffy adorable cat sitting on a windowsill, soft natural lighting, warm afternoon sun, photorealistic, 4K, high detail, front view"`

---

## License

MIT
