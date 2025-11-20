# Deployment Guide - Wyckoff Trading Assistant

This guide covers multiple free deployment options for the Wyckoff Trading Assistant.

## 🚀 Quick Start - Render (Recommended)

### Prerequisites
- GitHub account
- Render account (sign up at render.com)

### Steps

1. **Push to GitHub**
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

2. **Deploy on Render**
- Go to [dashboard.render.com](https://dashboard.render.com)
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Render will auto-detect the `render.yaml` configuration
- Click "Create Web Service"
- Wait 5-10 minutes for build to complete

3. **Access Your App**
- Your app will be available at: `https://wyckoff-trading-assistant.onrender.com`
- Auto-deploys on every git push!

### Important Notes
- **Model File Size**: The `.pth` model file (~300MB) might be too large for GitHub
  - Option A: Use Git LFS (Large File Storage)
  - Option B: Upload directly to Render's persistent disk
  - Option C: Host model on Google Drive and download on startup

---

## 🚂 Alternative: Railway

### Steps

1. **Sign up at Railway**
- Visit [railway.app](https://railway.app)
- Sign up with GitHub

2. **Deploy**
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose your repository
- Railway auto-detects Python/Flask
- Set environment variables if needed
- Deploy!

3. **Configure Start Command** (if not auto-detected)
```bash
cd Wyckoff_chatbot && gunicorn app:app --bind 0.0.0.0:$PORT
```

**Free Tier**: $5 credit per month

---

## 🐍 Alternative: PythonAnywhere

### Steps

1. **Create Account**
- Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
- Choose free "Beginner" account

2. **Upload Code**
```bash
# In PythonAnywhere bash console
git clone https://github.com/pankhuri0209/Transformer-based-Richard-Wyckoff-Trading-Assistant.git
cd Transformer-based-Richard-Wyckoff-Trading-Assistant/Wyckoff_chatbot
pip3 install --user -r requirements.txt
```

3. **Configure Web App**
- Go to Web tab
- Add new web app → Flask → Python 3.9
- Set source code directory: `/home/yourusername/Transformer-based-Richard-Wyckoff-Trading-Assistant/Wyckoff_chatbot`
- Edit WSGI file:
```python
import sys
import os

project_home = '/home/yourusername/Transformer-based-Richard-Wyckoff-Trading-Assistant/Wyckoff_chatbot'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from app import app as application
```
- Reload web app

**Free Tier**: Limited CPU, persistent storage

---

## 📦 Handling Large Model Files

Your `transformer_chatbot_gpu_deco_2.pth` file is likely large. Here are solutions:

### Option 1: Git LFS (Large File Storage)
```bash
# Install Git LFS
brew install git-lfs  # macOS
git lfs install

# Track .pth files
git lfs track "*.pth"
git add .gitattributes
git add Wyckoff_chatbot/assets/transformer_chatbot_gpu_deco_2.pth
git commit -m "Add model file with LFS"
git push origin main
```

### Option 2: Google Drive + Download on Startup
1. Upload model to Google Drive
2. Get shareable link
3. Modify `model_handler.py`:
```python
import gdown

def download_model_if_needed(model_path):
    if not os.path.exists(model_path):
        logger.info("Downloading model from Google Drive...")
        gdown.download(
            "https://drive.google.com/uc?id=YOUR_FILE_ID",
            model_path,
            quiet=False
        )
```
4. Add `gdown` to requirements.txt

### Option 3: Use Hugging Face Hub
```bash
# Upload model
huggingface-cli upload wyckoff-model transformer_chatbot_gpu_deco_2.pth

# Download in code
from huggingface_hub import hf_hub_download
model_path = hf_hub_download(repo_id="yourname/wyckoff-model", filename="transformer_chatbot_gpu_deco_2.pth")
```

---

## 🔧 Environment Variables

Set these on your deployment platform:

```bash
FLASK_ENV=production
PORT=8080  # Auto-set by most platforms
PYTHON_VERSION=3.9.18
```

---

## 📝 Deployment Checklist

- [x] Add `gunicorn` to requirements.txt
- [x] Create `Procfile` for Heroku/Railway
- [x] Create `render.yaml` for Render
- [x] Update `app.py` to use PORT environment variable
- [x] Add `.gitignore` to exclude unnecessary files
- [x] Handle large model file (Git LFS or download on startup)
- [ ] Test locally with gunicorn: `gunicorn app:app`
- [ ] Push to GitHub
- [ ] Deploy on chosen platform
- [ ] Test deployed application
- [ ] Set up custom domain (optional)

---

## 🎯 Recommended Workflow

1. **Start with Render** - Best free tier, easiest setup
2. If model file issues → Use Google Drive download method
3. Monitor usage and upgrade if needed

---

## 🆘 Troubleshooting

### Build fails due to model size
- Use Git LFS or Google Drive download method

### Out of memory during build
- Reduce worker count in Procfile: `--workers 1`
- Consider upgrading to paid tier

### Cold starts (app sleeps)
- Use cron job or uptime monitoring service to ping every 14 minutes
- Example: [UptimeRobot](https://uptimerobot.com) (free)

### CORS issues
- Add Flask-CORS if accessing from different domain
```python
from flask_cors import CORS
CORS(app)
```

---

## 📊 Performance Tips

1. **Optimize Model Loading**
   - Load model once on startup, not per request
   - Use CPU inference (GPU not available on free tiers)

2. **Cache Responses**
   - Implement caching for frequently asked questions
   - Use Redis if available

3. **Reduce Cold Starts**
   - Keep app warm with periodic pings
   - Use lighter model for free tier

---

## 🌐 Custom Domain (Optional)

After deployment, you can add a custom domain:

**Render**: Settings → Custom Domains → Add domain
**Railway**: Settings → Domains → Add custom domain
**PythonAnywhere**: Web tab → Enter custom domain (Paid only)

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [PythonAnywhere Help](https://help.pythonanywhere.com)
- [Git LFS Tutorial](https://git-lfs.github.com)

---

**Need help?** Check the deployment platform's documentation or create an issue on GitHub!
