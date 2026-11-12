# Blue Hour Portfolio

A bilingual (English / Spanish) Jekyll portfolio for a software engineer. It keeps the structure of
[jekyll-professional-resume](https://github.com/byanko55/jekyll-professional-resume) (profile
introduction with contact icons, one data file per section, switchable color themes, side navigation)
and gives it a pixel-art twilight look with a few interactions.

Everything you see is sample text. You only edit **text files**, never the HTML.

---

## 1. Run it on your computer

You need Ruby 3.x and Bundler.

```bash
bundle install
bundle exec jekyll serve --livereload
```

Open http://localhost:4000. Every time you save a file the page refreshes.
(Spanish version: http://localhost:4000/es/)

---

## 2. Fill in your information

| What | File |
|---|---|
| Name, photo, email, phone, LinkedIn, GitHub, site address | `_config.yml` |
| Job title, tagline, "At a glance" facts, summary, what you look for | `_data/en/about.yml` |
| Projects (GitHub repo, skills developed, tools, languages) | `_data/en/projects.yml` |
| Work experience | `_data/en/experience.yml` |
| Skills with levels | `_data/en/skills.yml` |
| Education and certifications | `_data/en/education.yml` |
| Spoken languages (own section) | `_data/en/languages.yml` |
| Research project | `_data/en/research.yml` |
| Buttons and labels | `_data/ui.yml` |

The Spanish texts are the same files inside `_data/es/`.
Each file starts with comments that explain the fields and give tips for recruiters.

**Photo:** put a square picture in `assets/img/` (for example `me.jpg`) and set `profile_img: /assets/img/me.jpg` in `_config.yml`.

**CV download button:** put your PDF in `assets/cv/` and write its path in `cv_url` inside `about.yml`
(for example `/assets/cv/Your-Name-CV-EN.pdf`). Leave it empty and the button is hidden.

**Project screenshot:** add `image: /assets/img/taskflow.png` to a project. Without it, a small pixel scene is drawn for that project.

### How the skill counters work
In `skills.yml`, each skill shows "×N" = in how many projects it appears. The match is made by name
with the `languages` and `tools` lists of `projects.yml`, so write them the same way (`PostgreSQL`, not `Postgres`).
Clicking a skill, or a technology tag inside a project, filters the project list.

---

## 3. Order and sections

In `_config.yml`, the list `sections:` controls what appears and in which order. Delete a line to hide a
section. If you are changing careers, keep `projects` above `experience` so people see your code first.

Languages and Education are separate sections (`languages` and `education`).

## 4. Languages of the site

- English lives at `/` (file `index.html` + `_data/en/`).
- Spanish lives at `/es/` (file `es/index.html` + `_data/es/`).
- To add another language, copy `es/` and `_data/es/` to a new code, translate, and add it to `languages:` in `_config.yml`
  plus a block of texts in `_data/ui.yml`.
- English only: delete the `es` entry in `languages:`, the `es/` folder and `_data/es/`.

## 5. Themes

Three themes are included and visitors can switch them with the colored squares in the top bar:
**Blue Hour** (default), **Daybreak** (light) and **Midnight**.
The colors are plain variables at the top of `assets/css/main.css`. Change `default_theme` in `_config.yml`
to start with another one. To create a new theme, copy a `:root[data-theme="..."]` block, rename it,
change the colors and add `{ id, label }` to `themes:` in `_config.yml`.
The pixel sky also reads these colors (`--sky-1` to `--win`).

## 6. Publish with GitHub Pages

1. Create a repository named `YOUR-USERNAME.github.io` and upload these files.
   (Any other name works too: then set `baseurl: "/repo-name"` in `_config.yml`.)
2. In the repository go to **Settings → Pages → Source** and choose **GitHub Actions**.
3. Push to the `main` branch. The workflow in `.github/workflows/pages.yml` builds and publishes the site.
4. Set `url: "https://YOUR-USERNAME.github.io"` in `_config.yml`.

---

## 7. Checklist before you send the link to recruiters

- [ ] First screen: job title says the role and 2 main technologies. "At a glance" is true and current.
- [ ] 3 to 5 projects, newest first. Each one has a GitHub link, one number, and what **you** did.
- [ ] Every GitHub repo has a README with a screenshot, how to run it and how to run the tests.
- [ ] Experience in non-software jobs: filled "Relevant to software engineering" for each.
- [ ] No placeholder left (search the files for `[`, `Your Name`, `example.com`, `your-username`).
- [ ] CV PDF uploaded and the button works. The same job title appears on LinkedIn.
- [ ] Open the site on your phone and in both languages. Print it once (Ctrl+P): it prints as a clean one-column resume.
- [ ] Ask a friend to read the first screen for 10 seconds and tell you what you do.

---

## What is inside

```
_config.yml            site settings
_data/                 all your texts (en/, es/, ui.yml)
_layouts/home.html     page skeleton (introduction, navigation)
_includes/sections/    one template per section
assets/css/main.css    themes and pixel styling
assets/js/main.js      theme switch, filters, slide-in, copy email
assets/js/sky.js       the animated pixel sky
```

Accessibility and recruiters: all text is real HTML (readable by screen readers and application-tracking
systems), animations stop if the visitor prefers reduced motion, the page works without JavaScript,
and it has structured data (schema.org Person) and English/Spanish `hreflang` links for search engines.

## Credits and licenses

- Structure and idea: [jekyll-professional-resume](https://github.com/byanko55/jekyll-professional-resume) by Yankos (MIT). See `LICENSE`.
- Contact and button icons: Font Awesome Free (CC BY 4.0). See `assets/img/ICONS-LICENSE.txt`.
- Fonts from Google Fonts: Pixelify Sans, Nunito, Silkscreen (SIL Open Font License).
- Technology logos (optional): [devicon](https://devicon.dev) (MIT), loaded from a CDN.
- Pixel portrait, favicon, sky scene and styling: original to this project.
