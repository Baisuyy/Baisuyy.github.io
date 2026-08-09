---
title: Hexo + GitHub Pages 部署指南
date: 2026-08-09 14:00:00
tags: [hexo, github-pages, devops]
categories: [tech]
description: 使用 Hexo + GitHub Actions 自动部署到 GitHub Pages
---

## 架构概览

1. **Hexo** - 快速、简洁且高效的博客框架
2. **Butterfly** - 优雅美观的主题
3. **GitHub Actions** - 自动构建部署
4. **Cloudflare** - CDN + HTTPS + DNS

## 关键配置

### _config.yml
```yaml
url: https://blog.kelibb.top
theme: butterfly
deploy:
  type: git
  repo: git@github.com:Baisuyy/Baisuyy.github.io.git
  branch: gh-pages
```

### GitHub Actions 工作流
见 `.github/workflows/deploy.yml`

## 自定义域名

1. `source/CNAME` 文件添加域名
2. Cloudflare 添加 CNAME 记录指向 `baisuyy.github.io`
3. 开启 Cloudflare 代理 (橙云)

---

更多细节请查看 [Hexo 官方文档](https://hexo.io/docs/)
