---
title: "Hugo + GitHub Pages 部署指南"
date: 2026-08-09T14:00:00+08:00
draft: false
tags: ["hugo", "github-pages", "devops"]
categories: ["tech"]
description: "使用 Hugo + GitHub Actions 自动部署到 GitHub Pages"
---

## 架构概览

1. **Hugo** - 静态站点生成器
2. **PaperMod** - 简洁优雅的主题
3. **GitHub Actions** - 自动构建部署
4. **Cloudflare** - CDN + HTTPS + DNS

## 关键配置

### hugo.toml
```toml
baseURL = "https://blog.kelibb.top/"
theme = "PaperMod"
```

### GitHub Actions 工作流
见 `.github/workflows/hugo.yml`

## 自定义域名

1. 仓库根目录添加 `CNAME` 文件
2. Cloudflare 添加 CNAME 记录指向 `baisuyy.github.io`
3. 开启 Cloudflare 代理 (橙云)

---

更多细节请查看 [Hugo 官方文档](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
