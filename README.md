# MiniMax Text-to-Image (T2I)

Generate images from text prompts using MiniMax AI. 使用 MiniMax AI 从文本提示生成图片。

## Features

- 🎨 Text-to-image generation via MiniMax API
- ✨ Auto prompt expansion for short prompts
- 📱 Feishu integration for result delivery
- 🌐 Bilingual documentation (EN/CN)

## Requirements

- Python 3.x
- `requests` library: `pip install requests`
- MiniMax API key

## Setup

Set your MiniMax API key (Linux/macOS/Windows Git Bash):
```bash
export MINIMAX_API_KEY=your_api_key_here
```

## Usage

```bash
python minimax-image-t2i/scripts/minimax-image.py "your prompt" -n 1 -a 16:9 -o output.png
```

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `-n` | Number of images (1-9) | 1 |
| `-a` | Aspect ratio (1:1, 16:9, 4:3, etc.) | 1:1 |
| `-o` | Output filename | image.png |
| `--no-expand` | Disable prompt expansion | - |

## License

MIT
