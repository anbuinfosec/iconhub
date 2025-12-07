# 🎨 Icon Gallery

A modern, responsive icon gallery web application for browsing and managing your icon collection. Built with vanilla JavaScript, Bootstrap 5, and a beautiful gradient UI design.

![Icon Gallery](https://img.shields.io/badge/Version-1.0.0-purple)
![License](https://img.shields.io/badge/License-MIT-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple)

## ✨ Features

- 🎯 **343+ Icons** organized in 11 categories
- 🔍 **Smart Search** - Search across all categories and icons
- 📋 **One-Click Copy** - Copy icon URL, Markdown, or HTML embed code
- 🌓 **Dark/Light Mode** - Toggle between themes with persistent storage
- 📱 **Fully Responsive** - Works perfectly on desktop, tablet, and mobile
- 🎨 **Modern UI** - Beautiful purple/blue gradient design
- ⚡ **Fast & Lightweight** - No heavy frameworks, pure vanilla JS
- 🎉 **Toast Notifications** - Visual feedback for all actions
- 🔄 **Dynamic Loading** - Icons loaded from folder structure automatically

## 📂 Categories

- ☁️ **Cloud** - AWS, Docker, GitHub, GitLab, Heroku, Terraform (23 icons)
- 🗄️ **Databases** - MySQL, PostgreSQL, MongoDB, Redis, Oracle (6 icons)
- 🎯 **Frameworks** - React, Angular, Vue, Django, Laravel (32 icons)
- 💻 **IDEs** - VS Code, IntelliJ, PyCharm, Android Studio (11 icons)
- 🖥️ **Operating Systems** - Windows, macOS, Linux distributions (12 icons)
- 🌐 **Social Icons** - Facebook, Twitter, Instagram, LinkedIn (117 icons)
- 💾 **Storage** - Dropbox, Google Drive, Nextcloud, Plex (5 icons)
- 📝 **Text Editors** - Atom, Sublime Text, Notepad++ (5 icons)
- 🔧 **Utils** - Git, npm, browsers, HTML/CSS/JSON icons (59 icons)
- 💻 **Programming Languages** - Python, JavaScript, Java, C++, Go (21 icons)
- 🔹 **Others** - Various tech brands and tools (52 icons)

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/anbuinfosec/iconhub.git
   cd iconhub
   ```

2. **Start a local server**
   
   Using Python:
   ```bash
   python -m http.server 8000
   ```
   
   Or using Node.js:
   ```bash
   npx serve
   ```

3. **Open in browser**
   ```
   http://localhost:8000
   ```

### GitHub Pages Deployment

The project uses **GitHub Actions** to automatically build and deploy to GitHub Pages:

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository **Settings** → **Pages**
   - Under "Build and deployment" select **GitHub Actions** as the source

3. **Automatic Deployment**
   - The workflow will automatically run on every push to `main`
   - Python build script generates `categories.json` from your icons
   - Site deploys automatically to `https://yourusername.github.io/iconhub`

4. **Manual Deployment** (optional)
   - Go to **Actions** tab in your repository
   - Click "Build and Deploy to GitHub Pages"
   - Click "Run workflow"

### How the Build Works

The build process uses Python to scan your `icons/` folder structure:

```bash
# Run locally to test
python3 build.py
```

This generates `categories.json` with:
- All category folders automatically detected
- Icon file lists for each category
- Proper display names and icons
- Accurate icon counts

## 📁 Project Structure

```
iconhub/
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions workflow
├── index.html               # Main HTML file
├── styles.css               # All styles including responsive design
├── script.js                # JavaScript functionality
├── build.py                 # Python build script
├── categories.json          # Generated icon data (auto-created)
├── icons/                   # Icon categories
│   ├── cloud/
│   ├── databases/
│   ├── frameworks/
│   ├── ides/
│   ├── os/
│   ├── programming_languages/
│   ├── social_icons/
│   ├── storage/
│   ├── text_editor/
│   ├── utils/
│   └── others/
├── README.md
└── LICENSE
```

## 🎨 Customization

### Adding New Icons

1. Create a new folder in `icons/` directory (e.g., `icons/my-category/`)
2. Add your icon files (SVG, PNG, JPG, GIF, WebP supported)
3. Run the build script to update categories:
   ```bash
   python3 build.py
   ```
4. The gallery will automatically detect and display them!
5. Push to GitHub and the Actions workflow will rebuild automatically

### Changing Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --bg-primary: #f5f7fb;
    --bg-secondary: #ffffff;
    /* ... more variables */
}
```

### Dark Mode Colors

```css
[data-theme="dark"] {
    --primary-gradient: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
    --bg-primary: #0f172a;
## 🛠️ Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)** - Dynamic functionality
- **Python 3** - Build script for generating category data
- **GitHub Actions** - Automated deployment workflow
- **Bootstrap 5.3.3** - UI components and utilities
- **Bootstrap Icons** - Icon library for UI elements
- **Google Fonts (Inter)** - Typography
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)** - Dynamic functionality
- **Bootstrap 5.3.3** - UI components and utilities
- **Bootstrap Icons** - Icon library for UI elements
- **Google Fonts (Inter)** - Typography

## 📱 Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Opera (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🎯 Features in Detail

### Copy Functionality
- **URL Copy** - Direct link to the icon file
- **Markdown Copy** - `![alt](url)` format for documentation
- **HTML Copy** - `<img>` tag with proper attributes

### Search
- Search by icon name across all categories
- Filter categories by name
- Real-time results with visual feedback

### Responsive Design
- **Desktop** - Multi-column grid layout
- **Tablet** - Adaptive 2-column layout
- **Mobile** - Single column with touch-optimized controls
- **Small Phones** - Optimized for 360px+ screens

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Ideas
- 🎨 Add new icon categories
- 🐛 Fix bugs or improve performance
- 📱 Enhance mobile experience
- 🌐 Add internationalization
- ♿ Improve accessibility
- 📚 Improve documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**@anbuinfosec**

- GitHub: [@anbuinfosec](https://github.com/anbuinfosec)
- Website: [Icon Gallery](https://github.com/anbuinfosec/iconhub)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

## 📸 Screenshots

### Desktop View
Modern, clean interface with gradient navbar and grid layout.

### Mobile View
Fully responsive with touch-optimized controls and vertical navigation.

### Dark Mode
Beautiful dark theme with purple accents.

## 🔮 Future Enhancements

- [ ] Drag and drop icon upload
- [ ] Icon favorites/collections
- [ ] Export icons in different formats
- [ ] Icon editor/customizer
- [ ] API for programmatic access
- [ ] Icon statistics and analytics
- [ ] User accounts and personal galleries

## 📊 Statistics

- **Total Icons**: 343+
- **Categories**: 11
- **File Size**: < 100KB (excluding icons)
- **Load Time**: < 2s
- **Mobile Score**: 95/100

## 🙏 Acknowledgments

- Bootstrap team for the amazing framework
- All icon creators and contributors
- Open source community

---

<div align="center">
  Made with ❤️ by @anbuinfosec
  <br>
  <sub>© 2025 Icon Gallery. All rights reserved.</sub>
</div>
