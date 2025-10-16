# GitHub Pages 部署说明

## 🌐 在线访问

您的Java面试八股文阅读器将部署到GitHub Pages，可以通过以下地址访问：

**https://leeyoung1.github.io/baguwen/**

### ⚠️ 首次部署需要手动启用

如果您是第一次部署，需要手动启用GitHub Pages：

1. 访问您的GitHub仓库：https://github.com/leeyoung1/baguwen
2. 点击 **Settings** 选项卡
3. 在左侧菜单中找到 **Pages**
4. 在 "Build and deployment" 部分：
   - Source 选择 **GitHub Actions**
   - 或者选择 **Deploy from a branch** 并选择 `main` 分支的 `/ (root)` 文件夹
5. 点击 **Save** 保存设置
6. 等待几分钟让GitHub Actions完成部署

### 🚀 自动部署

本项目配置了GitHub Actions自动部署，每次向`main`分支推送代码时，都会自动更新GitHub Pages网站。

### 部署流程
1. 代码推送到`main`分支
2. GitHub Actions自动触发部署工作流
3. 网站内容自动更新到GitHub Pages
4. 通常在1-2分钟内完成部署

## 📁 项目结构

```
baguwen/
├── index.html              # 主页面文件
├── README.md               # 项目说明文档
├── README-GitHub-Pages.md  # GitHub Pages部署说明（本文件）
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions部署配置
├── index.md                # 文档索引
├── 必读/                   # 必读文档
├── 面试必备/               # 面试准备文档
├── Java基础/               # Java 基础文档
├── JVM/                    # JVM 相关文档
├── Spring/                 # Spring 框架文档
├── MySQL/                  # MySQL 数据库文档
├── Redis/                  # Redis 缓存文档
└── ...                     # 其他技术分类文档
```

## 🔧 本地运行

如果您想在本地运行或修改项目：

### 方法一：使用Python（推荐）
```bash
# 克隆项目
git clone https://github.com/leeyoung1/baguwen.git
cd baguwen

# 启动本地服务器
python3 -m http.server 8000

# 在浏览器中访问
# http://localhost:8000
```

### 方法二：使用Node.js
```bash
# 安装http-server
npm install -g http-server

# 启动服务器
http-server -p 8000

# 在浏览器中访问
# http://localhost:8000
```

## ✨ 功能特点

- 🎯 **智能导航**: 自动解析文档索引，支持分类浏览
- 🔍 **实时搜索**: 快速查找所需文档
- 📱 **响应式设计**: 完美支持桌面端和移动端
- 🎨 **现代化界面**: 专业的 UI 设计和流畅的交互体验
- 📖 **高质量渲染**: 完整的 Markdown 渲染和代码高亮
- 🖼️ **图片支持**: 智能处理图片路径，确保图片正常显示
- 🚀 **在线访问**: 通过GitHub Pages随时随地访问

## 🛠 技术栈

- **前端**: HTML5 + CSS3 + JavaScript (ES6+)
- **Markdown**: marked.js
- **代码高亮**: highlight.js
- **样式**: 现代化 CSS 设计
- **架构**: 单页应用 (SPA)
- **部署**: GitHub Pages + GitHub Actions

## 📝 修改和维护

### 添加新文档
1. 将新文档放入相应的分类文件夹中
2. 更新 `index.md` 文件，添加新文档的链接
3. 提交并推送到 `main` 分支
4. GitHub Actions会自动部署更新

### 修改界面
1. 编辑 `index.html` 文件
2. 修改CSS样式或JavaScript功能
3. 在本地测试修改效果
4. 提交并推送到 `main` 分支

## 🤝 贡献指南

1. Fork 本仓库
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目仅用于个人学习目的，文档版权归原作者所有。

---

**🎉 祝您学习愉快，面试顺利！**

如有问题或建议，请在GitHub仓库中提交Issue。