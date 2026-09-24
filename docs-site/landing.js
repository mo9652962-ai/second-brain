/* ============================================================
   Second Brain — Landing 3D Interactions
   Three.js WebGL 3D 知识图谱宇宙 + 3D 纵深星云背景 + 卡片 3D 悬浮视差
   新增：自举演化剖析器 + 知识域实时筛选 + 24H 自动化雷达 + Web Audio 空间合成音效
   ============================================================ */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 真实数据：18 个知识域（git ls-files 统计）─────────── */
  var DOMAINS = [
    { key: 'Research',     n: 235, label: '研究',   copy: '论文、文献、研究方法', color: 0x22d3ee },
    { key: 'Dev',          n: 143, label: '开发',   copy: 'Web 开发、工具链、DevOps', color: 0x7c5cff },
    { key: 'Productivity', n: 54,  label: '生产力', copy: '工作流、变现、自动化', color: 0x34d399 },
    { key: 'Security',     n: 53,  label: '安全',   copy: '网安、CTF、防御加固', color: 0x7c5cff },
    { key: 'cards',        n: 37,  label: '知识卡', copy: '原子化知识卡片', color: 0xffb454 },
    { key: 'Daily',        n: 34,  label: '日常',   copy: '每日回顾与沉淀', color: 0xffb454 },
    { key: 'Hardware',     n: 21,  label: '硬件',   copy: 'PCB、单片机、CAD', color: 0x22d3ee },
    { key: 'AI',           n: 19,  label: 'AI',     copy: 'Agent、模型、提示词', color: 0x7c5cff },
    { key: 'Finance',      n: 16,  label: '金融',   copy: '投资与市场研究', color: 0xffb454 },
    { key: 'Archive',      n: 13,  label: '归档',   copy: '历史资料归档', color: 0x7d7a8c },
    { key: 'Content',      n: 10,  label: '内容',   copy: '自媒体与选题池', color: 0x34d399 },
    { key: 'SOP',          n: 10,  label: 'SOP',    copy: '标准作业流程', color: 0x34d399 },
    { key: 'META',         n: 9,   label: '元信息', copy: '知识库治理', color: 0x7d7a8c },
    { key: 'Creative',     n: 6,   label: '创意',   copy: '设计与视觉', color: 0xffb454 },
    { key: 'gaming',       n: 4,   label: '游戏',   copy: '游戏研究与 mod', color: 0x22d3ee },
    { key: 'Product',      n: 2,   label: '产品',   copy: '产品化与商业化', color: 0x34d399 },
    { key: 'Projects',     n: 2,   label: '项目',   copy: '项目记录', color: 0x7c5cff },
    { key: 'Education',    n: 1,   label: '教育',   copy: '教学与练习设计', color: 0x22d3ee }
  ];
  var MAXN = DOMAINS[0].n;

  var CROSS = [
    ['AI', 'Dev'], ['AI', 'Research'], ['Dev', 'Security'], ['Research', 'Education'],
    ['Hardware', 'Dev'], ['Productivity', 'SOP'], ['Product', 'Finance'],
    ['Content', 'Creative'], ['cards', 'META'], ['gaming', 'Creative']
  ];

  /* ── 自举演化真实案例文档 ───────────────────────── */
  var BOOTSTRAP_DATA = {
    workflow: {
      title: '自举演化剖析 · 01 交互自举',
      pain: '凌晨 1 小时投入产出大改动，因未对齐用户偏好次日全被撤销。',
      rule: '假设先验证 + 小步提交立即 push + 产出归属前置确认，不自作主张推向上游。',
      solid: 'hermes-workflow-preferences.md + AGENTS.md P0 红线区强制执行。'
    },
    reliability: {
      title: '自举演化剖析 · 02 可靠性自举',
      pain: '45 个定时任务集中触发引发 API 429 限流与并发资源雪崩。',
      rule: '错峰调度阶梯 (06:00/06:30/07:15) + 自动重试机制与静默失效心跳监控。',
      solid: 'hermes-automation-patterns.md 生产级调度守护。'
    },
    knowledge: {
      title: '自举演化剖析 · 03 知识自举',
      pain: '全天被动响应任务，零主动新知识与前沿动态输入。',
      rule: '每日知识吸收底线守门员：arXiv / GitHub Trending / HN 自动化采集沉淀。',
      solid: 'daily-knowledge-absorption-gate.md + 18 域 MOC 知识体系。'
    },
    tool: {
      title: '自举演化剖析 · 04 工具调用自举',
      pain: 'Windows 下 git ls-files 中文路径带引号致 Linux CI cp 失败 (219个非ASCII路径)。',
      rule: 'git 路径遍历必须使用 -c core.quotePath=false 与 -z 原样输出。',
      solid: 'tool-call-bootstrapping.md + scripts/check-site.py 强制门禁。'
    },
    code: {
      title: '自举演化剖析 · 05 代码质量自举',
      pain: '前端修改样式后存在无效声明或 CSS 括号不平衡被静默忽略。',
      rule: '严格坚持双轴 Code Review + esbuild/AST 语法自检 + 真实浏览器像素验证。',
      solid: 'code-quality-bootstrapping.md + 自动化验证流水线。'
    },
    style: {
      title: '自举演化剖析 · 06 输出风格自举',
      pain: '长对话后模型输出漂移、废话套话增多、结论淹没在冗长解释中。',
      rule: '结论置顶 + 表格结构化 + 严格去 AI 味与禁止套路开场白。',
      solid: 'output-style-bootstrapping.md + SOUL.md 核心人设锚定。'
    },
    context: {
      title: '自举演化剖析 · 07 上下文管理自举',
      pain: '重要项目约束与环境事实在长会话压缩后被稀释遗忘。',
      rule: '四级记忆体系 (瞬时 → 会话 → 任务 → 核心记忆) + 结构化紧凑持久化。',
      solid: 'context-management-bootstrapping.md + MEMORY.md 精简注入。'
    }
  };

  /* ══ 1. Web Audio 原生合成音效引擎 (零外部文件) ══════ */
  var soundEnabled = false;
  var audioCtx = null;

  function playTone(freq, type, dur, gainVal) {
    if (!soundEnabled || reduce) return;
    try {
      if (!audioCtx) {
        var AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) audioCtx = new AudioContextClass();
      }
      if (!audioCtx) return;
      if (audioCtx.state === 'suspended') audioCtx.resume();

      var osc = audioCtx.createOscillator();
      var gain = audioCtx.createGain();
      osc.type = type || 'sine';
      osc.frequency.setValueAtTime(freq || 800, audioCtx.currentTime);
      gain.gain.setValueAtTime(gainVal || 0.05, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + (dur || 0.08));

      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + (dur || 0.08));
    } catch (e) {}
  }

  function initSoundToggle() {
    var btn = document.querySelector('[data-action="sound"]');
    if (!btn) return;
    var iconOff = btn.querySelector('.i-sound-off');
    var iconOn = btn.querySelector('.i-sound-on');

    btn.addEventListener('click', function () {
      soundEnabled = !soundEnabled;
      btn.setAttribute('aria-pressed', soundEnabled ? 'true' : 'false');
      btn.classList.toggle('is-active', soundEnabled);
      if (iconOff) iconOff.style.display = soundEnabled ? 'none' : 'block';
      if (iconOn) iconOn.style.display = soundEnabled ? 'block' : 'none';

      if (soundEnabled) {
        playTone(520, 'sine', 0.06, 0.06);
        setTimeout(function () { playTone(1040, 'sine', 0.09, 0.05); }, 50);
      }
    });
  }

  /* ══ 2. 主题 ══════════════════════════════════════════ */
  function initTheme() {
    var saved = null;
    try { saved = localStorage.getItem('sb-theme'); } catch (e) {}
    root.dataset.theme = saved || 'dark';
  }
  initTheme();

  /* ══ 3. 知识域网格（DOM API 构建，防 XSS）═════════════ */
  function renderDomains() {
    var host = document.querySelector('[data-domains]');
    if (!host) return;
    var frag = document.createDocumentFragment();
    for (var i = 0; i < DOMAINS.length; i++) {
      var d = DOMAINS[i];
      var w = Math.max(8, Math.round((d.n / MAXN) * 100));

      var a = document.createElement('a');
      a.className = 'dom reveal';
      a.href = './kb/';
      a.setAttribute('data-dom', d.key);
      a.setAttribute('data-copy', d.copy);

      var strong = document.createElement('strong');
      strong.textContent = d.label;

      var span = document.createElement('span');
      span.textContent = d.key + ' · ' + d.n;

      var desc = document.createElement('small');
      desc.className = 'dom-desc';
      desc.textContent = d.copy;

      var bar = document.createElement('i');
      bar.style.setProperty('--w', w + '%');

      a.appendChild(strong);
      a.appendChild(span);
      a.appendChild(desc);
      a.appendChild(bar);
      frag.appendChild(a);
    }
    host.appendChild(frag);
  }
  renderDomains();

  /* ══ 4. 滚动进场（带 rAF 兜底）═════════════════════════ */
  function initReveal() {
    var els = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
    if (reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }

    var pending = els.slice();

    function show(el) {
      el.classList.add('is-in');
      var i = pending.indexOf(el);
      if (i >= 0) pending.splice(i, 1);
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var sibs = el.parentElement ? el.parentElement.children : [];
        var pos = Array.prototype.indexOf.call(sibs, el);
        setTimeout(function () { show(el); }, Math.min(pos, 7) * 70);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });

    var ticking = false;
    function sweep() {
      ticking = false;
      var vh = window.innerHeight;
      for (var i = pending.length - 1; i >= 0; i--) {
        var r = pending[i].getBoundingClientRect();
        if (r.top < vh * 0.92) show(pending[i]);
      }
      if (!pending.length) window.removeEventListener('scroll', onScroll);
    }
    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(sweep);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    setTimeout(sweep, 120);
  }

  /* ══ 5. 数字计数 + 进度条 ═════════════════════════════ */
  function animateCount(el, target) {
    if (reduce) { el.textContent = target.toLocaleString(); return; }
    var start = null, dur = 1500;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 4);
      el.textContent = Math.round(target * eased).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function initCounters() {
    var nums = document.querySelectorAll('[data-count]');
    if (!('IntersectionObserver' in window)) {
      nums.forEach(function (n) { n.textContent = (+n.dataset.count).toLocaleString(); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          animateCount(en.target, +en.target.dataset.count || 0);
          io.unobserve(en.target);
        });
      }, { threshold: 0.5 });
      nums.forEach(function (n) { io.observe(n); });
    }

    var meters = document.querySelectorAll('.meter');
    if (!('IntersectionObserver' in window)) {
      meters.forEach(function (m) { m.style.setProperty('--w', m.dataset.pct + '%'); m.classList.add('is-on'); });
    } else {
      var io2 = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var m = en.target;
          m.style.setProperty('--w', m.dataset.pct + '%');
          setTimeout(function () { m.classList.add('is-on'); }, 120);
          io2.unobserve(m);
        });
      }, { threshold: 0.6 });
      meters.forEach(function (m) { io2.observe(m); });
    }
  }

  /* ══ 6. 卡片 3D 悬浮视差与全息光泽 ═════════════════════ */
  function initCard3DTilt() {
    if (reduce || window.innerWidth < 860) return;
    var cards = document.querySelectorAll('.card, .step');
    cards.forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var cx = rect.width / 2;
        var cy = rect.height / 2;
        var dx = (x - cx) / cx;
        var dy = (y - cy) / cy;
        card.style.transform = 'perspective(1000px) rotateX(' + (-dy * 7).toFixed(2) + 'deg) rotateY(' + (dx * 7).toFixed(2) + 'deg) translateZ(8px)';
        card.style.setProperty('--mx', Math.round((x / rect.width) * 100) + '%');
        card.style.setProperty('--my', Math.round((y / rect.height) * 100) + '%');
      });
      card.addEventListener('pointerleave', function () {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
      });
    });
  }

  /* ══ 7. 3D 立体架构解构切换 ════════════════════════════ */
  function initStack3D() {
    var stackWrap = document.querySelector('[data-stack-container]');
    var treeWrap = document.querySelector('[data-tree-container]');
    var buttons = document.querySelectorAll('[data-stack-view]');
    if (!stackWrap || !treeWrap || !buttons.length) return;

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.classList.remove('is-active'); });
        btn.classList.add('is-active');
        var view = btn.dataset.stackView;
        if (view === '3d') {
          stackWrap.style.display = 'block';
          treeWrap.style.display = 'none';
        } else {
          stackWrap.style.display = 'none';
          treeWrap.style.display = 'grid';
        }
        playTone(480, 'sine', 0.06, 0.04);
      });
    });
  }

  /* ══ 8. 自举演化剖析交互面板 ══════════════════════════ */
  function initBootstrapInspector() {
    var cards = document.querySelectorAll('.card[data-bootstrap-id]');
    var titleEl = document.querySelector('[data-inspector-title]');
    var painEl = document.querySelector('[data-diff-pain]');
    var ruleEl = document.querySelector('[data-diff-rule]');
    var solidEl = document.querySelector('[data-diff-solid]');
    if (!cards.length || !titleEl) return;

    cards.forEach(function (card) {
      card.style.cursor = 'pointer';
      card.addEventListener('click', function () {
        cards.forEach(function (c) { c.classList.remove('is-active'); });
        card.classList.add('is-active');
        var id = card.dataset.bootstrapId;
        var data = BOOTSTRAP_DATA[id];
        if (data) {
          titleEl.textContent = data.title;
          painEl.textContent = data.pain;
          ruleEl.textContent = data.rule;
          solidEl.textContent = data.solid;
          playTone(640, 'triangle', 0.08, 0.05);
        }
      });
    });
  }

  /* ══ 9. 知识域实时筛选 & 3D 联动 ══════════════════════ */
  function initDomainFilter() {
    var input = document.querySelector('[data-domain-search]');
    var clearBtn = document.querySelector('[data-search-clear]');
    var tags = document.querySelectorAll('[data-filter-tags] .tag-btn');
    var doms = document.querySelectorAll('.dom-grid .dom');
    if (!input || !doms.length) return;

    var currentTag = 'all';
    var currentQuery = '';

    var TAG_MAP = {
      tech: ['Dev', 'AI', 'Security', 'Projects', 'META'],
      hardware: ['Hardware', 'Dev', 'gaming'],
      research: ['Research', 'Education', 'cards'],
      ops: ['Productivity', 'Content', 'SOP', 'Finance', 'Product', 'Daily', 'Archive']
    };

    function applyFilter() {
      var q = currentQuery.trim().toLowerCase();
      if (clearBtn) clearBtn.style.display = q ? 'grid' : 'none';

      doms.forEach(function (dom) {
        var key = dom.dataset.dom || '';
        var copy = dom.getAttribute('data-copy') || '';
        var text = dom.textContent.toLowerCase();

        var matchTag = (currentTag === 'all') || (TAG_MAP[currentTag] && TAG_MAP[currentTag].indexOf(key) >= 0);
        var matchQuery = !q || text.indexOf(q) >= 0 || key.toLowerCase().indexOf(q) >= 0 || copy.toLowerCase().indexOf(q) >= 0;

        if (matchTag && matchQuery) {
          dom.style.display = 'grid';
        } else {
          dom.style.display = 'none';
        }
      });
    }

    input.addEventListener('input', function (e) {
      currentQuery = e.target.value;
      applyFilter();
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', function () {
        input.value = '';
        currentQuery = '';
        applyFilter();
        input.focus();
        playTone(400, 'sine', 0.05, 0.03);
      });
    }

    tags.forEach(function (tagBtn) {
      tagBtn.addEventListener('click', function () {
        tags.forEach(function (t) { t.classList.remove('is-active'); });
        tagBtn.classList.add('is-active');
        currentTag = tagBtn.dataset.tag || 'all';
        applyFilter();
        playTone(720, 'sine', 0.05, 0.04);
      });
    });

    doms.forEach(function (dom) {
      dom.addEventListener('click', function () {
        var key = dom.dataset.dom;
        if (window.focus3DDomain) {
          window.focus3DDomain(key);
        }
      });
    });
  }

  /* ══ 10. 24H 自动化时钟雷达 ═══════════════════════════ */
  function initRadarClock() {
    var clockEl = document.querySelector('[data-radar-clock]');
    if (!clockEl) return;
    function update() {
      var now = new Date();
      var h = String(now.getHours()).padStart(2, '0');
      var m = String(now.getMinutes()).padStart(2, '0');
      clockEl.textContent = 'GMT+8 ' + h + ':' + m + ' · 45 JOBS RUNNING';
    }
    update();
    setInterval(update, 30000);
  }

  /* ══ 11. Three.js 核心动态载入 ═════════════════════════ */
  function ensureThree(callback) {
    if (window.THREE) {
      callback(window.THREE);
      return;
    }
    var existing = document.querySelector('script[src*="three"]');
    if (existing) {
      existing.addEventListener('load', function () { callback(window.THREE); });
      return;
    }
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    script.crossOrigin = 'anonymous';
    script.onload = function () { callback(window.THREE); };
    script.onerror = function () { initGraphFallback(); };
    document.head.appendChild(script);
  }

  /* ══ 12. 全景 3D 纵深星空与知识神经元 (Three.js WebGL) ══ */
  function initBackground3D(THREE) {
    var canvas = document.getElementById('webgl-bg');
    if (!canvas) return;

    var renderer;
    try {
      renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: false, powerPreference: 'low-power' });
    } catch (e) {
      return;
    }

    var W = window.innerWidth;
    var H = window.innerHeight;
    renderer.setSize(W, H);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(60, W / H, 0.1, 1000);
    camera.position.z = 50;

    var count = 380;
    var geometry = new THREE.BufferGeometry();
    var positions = new Float32Array(count * 3);
    var colors = new Float32Array(count * 3);

    var c1 = new THREE.Color(0x7c5cff);
    var c2 = new THREE.Color(0x22d3ee);

    for (var i = 0; i < count; i++) {
      positions[i * 3]     = (Math.random() - 0.5) * 180;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 140;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 160;

      var mixed = c1.clone().lerp(c2, Math.random());
      colors[i * 3]     = mixed.r;
      colors[i * 3 + 1] = mixed.g;
      colors[i * 3 + 2] = mixed.b;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    var material = new THREE.PointsMaterial({
      size: 2.2,
      vertexColors: true,
      transparent: true,
      opacity: 0.65,
      blending: THREE.AdditiveBlending
    });

    var points = new THREE.Points(geometry, material);
    scene.add(points);

    /* 浮动 3D 概念标签 */
    var TOKENS = ['Obsidian', 'Hermes', 'MOC', 'CAD', 'PCB', 'AI Agent', 'CTF', 'FSRS', 'Self-Evolving', 'Z-Axis', 'Prompt', 'Memory'];
    var tokenGroup = new THREE.Group();
    scene.add(tokenGroup);

    TOKENS.forEach(function (token, idx) {
      var tc = document.createElement('canvas');
      tc.width = 160; tc.height = 48;
      var ctx = tc.getContext('2d');
      ctx.fillStyle = 'rgba(124, 92, 255, 0.18)';
      ctx.strokeStyle = 'rgba(34, 211, 238, 0.55)';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect ? ctx.roundRect(2, 2, 156, 44, 12) : ctx.rect(2, 2, 156, 44);
      ctx.fill(); ctx.stroke();
      ctx.fillStyle = '#b9b6c4';
      ctx.font = '600 18px sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(token, 80, 24);

      var tex = new THREE.CanvasTexture(tc);
      tex.minFilter = THREE.LinearFilter;
      var smat = new THREE.SpriteMaterial({ map: tex, transparent: true, opacity: 0.65, depthWrite: false });
      var sp = new THREE.Sprite(smat);
      sp.scale.set(7.5, 2.25, 1);
      var angle = (idx / TOKENS.length) * Math.PI * 2;
      var rad = 35 + Math.random() * 25;
      sp.position.set(Math.cos(angle) * rad, (Math.random() - 0.5) * 50, (Math.random() - 0.5) * 60);
      tokenGroup.add(sp);
    });

    var mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
    window.addEventListener('pointermove', function (e) {
      mouse.targetX = (e.clientX / window.innerWidth) * 2 - 1;
      mouse.targetY = -(e.clientY / window.innerHeight) * 2 + 1;
    });

    var scrollProgress = 0;
    function onScroll() {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress = Math.min(1, Math.max(0, window.scrollY / (max || 1)));
    }
    window.addEventListener('scroll', onScroll, { passive: true });

    function onResize() {
      W = window.innerWidth; H = window.innerHeight;
      camera.aspect = W / H;
      camera.updateProjectionMatrix();
      renderer.setSize(W, H);
    }
    window.addEventListener('resize', onResize);

    var clock = new THREE.Clock();
    function animate() {
      if (!reduce) requestAnimationFrame(animate);
      var t = clock.getElapsedTime();

      mouse.x += (mouse.targetX - mouse.x) * 0.05;
      mouse.y += (mouse.targetY - mouse.y) * 0.05;

      points.rotation.y = t * 0.015 + mouse.x * 0.15;
      points.rotation.x = Math.sin(t * 0.02) * 0.08 + mouse.y * 0.1;

      tokenGroup.rotation.y = t * 0.012;
      camera.position.z = 50 - scrollProgress * 55;
      camera.position.y = -scrollProgress * 25;

      renderer.render(scene, camera);
    }
    animate();
  }

  /* ══ 13. Hero 区域 3D 知识图谱宇宙 (Three.js WebGL) ═════ */
  function initHero3D(THREE) {
    var canvas = document.querySelector('canvas[data-graph]');
    if (!canvas) return;

    var renderer;
    try {
      renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true, powerPreference: 'high-performance' });
    } catch (e) {
      initGraphFallback();
      return;
    }

    var stage = canvas.closest('.stage');
    var status = document.querySelector('[data-graph-status]');
    var dTitle = document.querySelector('[data-detail-title]');
    var dCopy = document.querySelector('[data-detail-copy]');
    var resetBtn = document.querySelector('[data-graph-reset]');
    var expandBtn = document.querySelector('[data-graph-expand]');

    var rect = canvas.getBoundingClientRect();
    var W = Math.max(10, rect.width);
    var H = Math.max(10, rect.height);
    renderer.setSize(W, H);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(46, W / H, 0.1, 200);
    camera.position.set(0, 0, 31);

    var worldGroup = new THREE.Group();
    scene.add(worldGroup);

    /* 3D HOME 中心核心 */
    var coreGeo = new THREE.SphereGeometry(2.3, 32, 32);
    var coreMat = new THREE.MeshBasicMaterial({ color: 0x7c5cff });
    var coreMesh = new THREE.Mesh(coreGeo, coreMat);
    worldGroup.add(coreMesh);

    var shellGeo = new THREE.IcosahedronGeometry(3.1, 1);
    var shellMat = new THREE.MeshBasicMaterial({ color: 0x22d3ee, wireframe: true, transparent: true, opacity: 0.55 });
    var shellMesh = new THREE.Mesh(shellGeo, shellMat);
    worldGroup.add(shellMesh);

    var ring1Geo = new THREE.TorusGeometry(5.2, 0.08, 16, 90);
    var ring1Mat = new THREE.MeshBasicMaterial({ color: 0x7c5cff, transparent: true, opacity: 0.7 });
    var ring1 = new THREE.Mesh(ring1Geo, ring1Mat);
    ring1.rotation.x = Math.PI / 3;
    worldGroup.add(ring1);

    var ring2Geo = new THREE.TorusGeometry(5.9, 0.07, 16, 90);
    var ring2Mat = new THREE.MeshBasicMaterial({ color: 0x22d3ee, transparent: true, opacity: 0.6 });
    var ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
    ring2.rotation.y = Math.PI / 4;
    ring2.rotation.x = -Math.PI / 6;
    worldGroup.add(ring2);

    /* 文字 Sprite 生成器（CanvasTexture 动态药丸标签）*/
    function createTextSprite(label, count, colorHex) {
      var cvs = document.createElement('canvas');
      cvs.width = 240; cvs.height = 64;
      var ctx = cvs.getContext('2d');

      ctx.fillStyle = 'rgba(10, 10, 14, 0.88)';
      ctx.strokeStyle = colorHex || '#7c5cff';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.roundRect ? ctx.roundRect(4, 4, 232, 56, 16) : ctx.rect(4, 4, 232, 56);
      ctx.fill(); ctx.stroke();

      ctx.fillStyle = '#f2f0f5';
      ctx.font = '600 24px -apple-system, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(label + ' · ' + count, 120, 32);

      var tex = new THREE.CanvasTexture(cvs);
      tex.minFilter = THREE.LinearFilter;
      var mat = new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false });
      var sp = new THREE.Sprite(mat);
      sp.scale.set(3.8, 1.01, 1);
      return sp;
    }

    /* HOME 标签 */
    var homeLabel = createTextSprite('HOME', 1093, '#22d3ee');
    homeLabel.position.set(0, 4.4, 0);
    worldGroup.add(homeLabel);

    /* 18 个 3D 领域节点（球形 Fibonacci 空间分布）*/
    var domainNodes = [];
    var GA = Math.PI * (3 - Math.sqrt(5));
    var sphereR = 14.5;

    for (var i = 0; i < DOMAINS.length; i++) {
      var d = DOMAINS[i];
      var y = 1 - (i / (DOMAINS.length - 1)) * 2;
      var rAtY = Math.sqrt(Math.max(0, 1 - y * y));
      var theta = GA * i;
      var px = Math.cos(theta) * rAtY * sphereR;
      var py = y * sphereR;
      var pz = Math.sin(theta) * rAtY * sphereR;

      var nodeR = 0.85 + (d.n / MAXN) * 0.95;
      var nodeGeo = new THREE.SphereGeometry(nodeR, 24, 24);
      var nodeMat = new THREE.MeshBasicMaterial({ color: d.color });
      var nodeMesh = new THREE.Mesh(nodeGeo, nodeMat);
      nodeMesh.position.set(px, py, pz);
      nodeMesh.userData = { key: d.key, label: d.label, n: d.n, copy: d.copy, baseScale: 1 };
      worldGroup.add(nodeMesh);

      var labelSprite = createTextSprite(d.label, d.n, d.color === 0x22d3ee ? '#22d3ee' : (d.color === 0xffb454 ? '#ffb454' : '#7c5cff'));
      labelSprite.position.set(px, py + nodeR + 1.2, pz);
      worldGroup.add(labelSprite);

      domainNodes.push({ mesh: nodeMesh, label: labelSprite, data: d, pos: new THREE.Vector3(px, py, pz) });
    }

    /* 3D 动态能量连线与流光光子 */
    var lineGroup = new THREE.Group();
    worldGroup.add(lineGroup);

    var curves = [];
    var photonGroup = new THREE.Group();
    worldGroup.add(photonGroup);

    var photonCvs = document.createElement('canvas');
    photonCvs.width = 32; photonCvs.height = 32;
    var pctx = photonCvs.getContext('2d');
    var grd = pctx.createRadialGradient(16, 16, 0, 16, 16, 16);
    grd.addColorStop(0, 'rgba(34, 211, 238, 1)');
    grd.addColorStop(1, 'rgba(124, 92, 255, 0)');
    pctx.fillStyle = grd; pctx.fillRect(0, 0, 32, 32);
    var photonTex = new THREE.CanvasTexture(photonCvs);
    var photonMat = new THREE.SpriteMaterial({ map: photonTex, transparent: true, opacity: 0.9, blending: THREE.AdditiveBlending });

    domainNodes.forEach(function (node, idx) {
      var p0 = new THREE.Vector3(0, 0, 0);
      var p2 = node.pos;
      var p1 = p2.clone().multiplyScalar(0.5).add(new THREE.Vector3(0, 2.2, 0));
      var curve = new THREE.QuadraticBezierCurve3(p0, p1, p2);
      curves.push(curve);

      var pts = curve.getPoints(24);
      var lgeo = new THREE.BufferGeometry().setFromPoints(pts);
      var lmat = new THREE.LineBasicMaterial({ color: 0x7c5cff, transparent: true, opacity: 0.28 });
      var line = new THREE.Line(lgeo, lmat);
      lineGroup.add(line);

      var photon = new THREE.Sprite(photonMat);
      photon.scale.set(1.2, 1.2, 1);
      photon.userData = { curveIdx: curves.length - 1, offset: (idx / DOMAINS.length) };
      photonGroup.add(photon);
    });

    /* 跨域 3D 连线 */
    CROSS.forEach(function (pair) {
      var n1 = domainNodes.filter(function (n) { return n.data.key === pair[0]; })[0];
      var n2 = domainNodes.filter(function (n) { return n.data.key === pair[1]; })[0];
      if (n1 && n2) {
        var mid = n1.pos.clone().add(n2.pos).multiplyScalar(0.5).add(new THREE.Vector3(0, 1.5, 0));
        var c = new THREE.QuadraticBezierCurve3(n1.pos, mid, n2.pos);
        var pts = c.getPoints(20);
        var lgeo = new THREE.BufferGeometry().setFromPoints(pts);
        var lmat = new THREE.LineBasicMaterial({ color: 0x22d3ee, transparent: true, opacity: 0.35 });
        lineGroup.add(new THREE.Line(lgeo, lmat));
      }
    });

    /* 3D 鼠标拖拽与惯性系统 */
    var rot = { x: -0.18, y: 0.45 };
    var vel = { x: 0, y: 0.0018 };
    var drag = { on: false, lx: 0, ly: 0, moved: false };

    function getCanvasCoords(ev) {
      var r = canvas.getBoundingClientRect();
      return {
        x: ((ev.clientX - r.left) / r.width) * 2 - 1,
        y: -((ev.clientY - r.top) / r.height) * 2 + 1,
        px: ev.clientX - r.left,
        py: ev.clientY - r.top
      };
    }

    canvas.addEventListener('pointerdown', function (e) {
      drag.on = true; drag.moved = false;
      drag.lx = e.clientX; drag.ly = e.clientY;
      canvas.setPointerCapture(e.pointerId);
    });

    var raycaster = new THREE.Raycaster();
    var mouseNorm = new THREE.Vector2(-999, -999);
    var hoveredNode = null;

    canvas.addEventListener('pointermove', function (e) {
      if (drag.on) {
        var dx = e.clientX - drag.lx;
        var dy = e.clientY - drag.ly;
        if (Math.abs(dx) + Math.abs(dy) > 2) drag.moved = true;
        rot.y += dx * 0.0055;
        rot.x = Math.max(-1.1, Math.min(1.1, rot.x + dy * 0.005));
        vel.y = dx * 0.0015;
        vel.x = dy * 0.0008;
        drag.lx = e.clientX; drag.ly = e.clientY;
      }
      var c = getCanvasCoords(e);
      mouseNorm.x = c.x; mouseNorm.y = c.y;
    });

    function endDrag(e) {
      if (!drag.on) return;
      drag.on = false;
      try { canvas.releasePointerCapture(e.pointerId); } catch (err) {}
      if (!drag.moved) {
        raycaster.setFromCamera(mouseNorm, camera);
        var hits = raycaster.intersectObjects(domainNodes.map(function (n) { return n.mesh; }));
        if (hits.length > 0) {
          selectNode(hits[0].object.userData);
        }
      }
    }
    canvas.addEventListener('pointerup', endDrag);
    canvas.addEventListener('pointercancel', endDrag);

    function selectNode(data) {
      if (!data) return;
      if (status) status.textContent = '已选中 3D 节点 · ' + data.key;
      if (dTitle) dTitle.textContent = data.label + ' · ' + data.key;
      if (dCopy) dCopy.textContent = data.n + ' 篇 · ' + data.copy;

      var targetNode = domainNodes.filter(function (n) { return n.data.key === data.key; })[0];
      if (targetNode) {
        var targetRotY = -Math.atan2(targetNode.pos.x, targetNode.pos.z);
        rot.y = targetRotY;
        rot.x = 0;
        vel.y = 0; vel.x = 0;
        playTone(960, 'sine', 0.08, 0.06);
      }
    }

    /* 暴露供 2D 交互联动调用 */
    window.focus3DDomain = function (key) {
      var targetNode = domainNodes.filter(function (n) { return n.data.key === key; })[0];
      if (targetNode) {
        selectNode(targetNode.data);
        var heroEl = document.querySelector('.hero');
        if (heroEl) heroEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    };

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        rot.x = -0.18; rot.y = 0.45; vel.x = 0; vel.y = 0.0018;
        if (status) status.textContent = '视角已重置';
        if (dTitle) dTitle.textContent = 'Research';
        if (dCopy) dCopy.textContent = '235 篇 · 论文、文献、研究方法';
        playTone(480, 'sine', 0.07, 0.04);
      });
    }

    if (expandBtn) {
      expandBtn.addEventListener('click', function () {
        var isExp = stage.classList.toggle('is-expanded');
        expandBtn.textContent = isExp ? '退出沉浸' : '全屏沉浸';
        expandBtn.classList.toggle('is-active', isExp);
        document.body.classList.toggle('webgl-expanded', isExp);
        setTimeout(resizeHero, 100);
        playTone(isExp ? 720 : 420, 'sine', 0.08, 0.05);
      });
    }

    function resizeHero() {
      var r = canvas.getBoundingClientRect();
      W = Math.max(10, r.width);
      H = Math.max(10, r.height);
      camera.aspect = W / H;
      camera.updateProjectionMatrix();
      renderer.setSize(W, H);
    }
    window.addEventListener('resize', resizeHero);

    var clock = new THREE.Clock();
    function animate() {
      if (!reduce) requestAnimationFrame(animate);
      var t = clock.getElapsedTime();

      if (!drag.on) {
        rot.y += vel.y;
        rot.x += vel.x;
        vel.y += (0.0016 - vel.y) * 0.02;
        vel.x *= 0.95;
      }

      worldGroup.rotation.y = rot.y;
      worldGroup.rotation.x = rot.x;

      shellMesh.rotation.y = -t * 0.25;
      shellMesh.rotation.x = t * 0.15;
      ring1.rotation.z = t * 0.35;
      ring2.rotation.z = -t * 0.28;

      /* 光子脉冲沿着 3D 曲线穿梭流动 */
      photonGroup.children.forEach(function (photon) {
        var cIdx = photon.userData.curveIdx;
        var offset = photon.userData.offset;
        if (curves[cIdx]) {
          var prog = (t * 0.28 + offset) % 1.0;
          photon.position.copy(curves[cIdx].getPoint(prog));
        }
      });

      /* 3D 射线拾取与悬停反馈 */
      raycaster.setFromCamera(mouseNorm, camera);
      var intersects = raycaster.intersectObjects(domainNodes.map(function (n) { return n.mesh; }));
      if (intersects.length > 0) {
        var hit = intersects[0].object;
        if (hoveredNode !== hit) {
          if (hoveredNode) hoveredNode.scale.set(1, 1, 1);
          hoveredNode = hit;
          hoveredNode.scale.set(1.55, 1.55, 1.55);
          canvas.style.cursor = 'pointer';
          var d = hoveredNode.userData;
          if (status) status.textContent = '悬停 3D 节点 · ' + d.label + ' (' + d.n + ' 篇)';
          if (dTitle) dTitle.textContent = d.label + ' · ' + d.key;
          if (dCopy) dCopy.textContent = d.n + ' 篇 · ' + d.copy;
          playTone(1100, 'sine', 0.03, 0.02);
        }
      } else {
        if (hoveredNode) {
          hoveredNode.scale.set(1, 1, 1);
          hoveredNode = null;
          canvas.style.cursor = 'grab';
        }
      }

      renderer.render(scene, camera);
    }
    animate();
  }

  /* ══ 14. Canvas 2D 降级方案（离线或无 Three.js 时使用）═══ */
  function initGraphFallback() {
    var canvas = document.querySelector('canvas[data-graph]');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    if (!ctx) return;

    var status = document.querySelector('[data-graph-status]');
    var dTitle = document.querySelector('[data-detail-title]');
    var dCopy = document.querySelector('[data-detail-copy]');
    var resetBtn = document.querySelector('[data-graph-reset]');

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var W = 0, H = 0, cx = 0, cy = 0, R = 0;

    function resize() {
      var r = canvas.getBoundingClientRect();
      W = Math.max(1, r.width); H = Math.max(1, r.height);
      canvas.width = Math.round(W * dpr);
      canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      cx = W / 2; cy = H / 2; R = Math.min(W, H) * 0.33;
    }

    var nodes = [{ key: 'HOME', label: 'HOME', n: 1093, hub: true, x: 0, y: 0, z: 0 }];
    var GA = Math.PI * (3 - Math.sqrt(5));
    for (var i = 0; i < DOMAINS.length; i++) {
      var y = 1 - (i / (DOMAINS.length - 1)) * 2;
      var rad = Math.sqrt(Math.max(0, 1 - y * y));
      var th = GA * i;
      nodes.push({ key: DOMAINS[i].key, label: DOMAINS[i].label, n: DOMAINS[i].n, x: Math.cos(th) * rad, y: y, z: Math.sin(th) * rad });
    }

    var rot = { x: -0.18, y: 0.5 };
    var vel = { x: 0, y: 0.0016 };
    var t = 0;

    function project(p) {
      var cy1 = Math.cos(rot.y), sy1 = Math.sin(rot.y);
      var x1 = p.x * cy1 - p.z * sy1;
      var z1 = p.x * sy1 + p.z * cy1;
      var cx1 = Math.cos(rot.x), sx1 = Math.sin(rot.x);
      var y1 = p.y * cx1 - z1 * sx1;
      var z2 = p.y * sx1 + z1 * cx1;
      var persp = 1 / (1.75 - z2 * 0.62);
      return { x: cx + x1 * R * persp * 1.7, y: cy + y1 * R * persp * 1.7, z: z2, s: persp };
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var pts = nodes.map(project);
      for (var e = 1; e < pts.length; e++) {
        var a = pts[0], b = pts[e];
        ctx.strokeStyle = 'rgba(124,92,255,0.22)';
        ctx.lineWidth = 0.8;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      }
      pts.forEach(function (p, idx) {
        ctx.fillStyle = idx === 0 ? '#7c5cff' : '#22d3ee';
        ctx.beginPath(); ctx.arc(p.x, p.y, idx === 0 ? 8 : 4, 0, Math.PI * 2); ctx.fill();
      });
    }

    function loop() {
      rot.y += vel.y; t += 16; draw();
      if (!reduce) requestAnimationFrame(loop);
    }
    resize();
    window.addEventListener('resize', resize);
    loop();
  }

  /* ══ 15. 基础 UI 交互（主题 / 菜单 / 复制 / 滚动）═════ */
  function initChrome() {
    var themeBtn = document.querySelector('[data-action="theme"]');
    if (themeBtn) {
      themeBtn.addEventListener('click', function () {
        var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
        root.dataset.theme = next;
        try { localStorage.setItem('sb-theme', next); } catch (e) {}
        playTone(next === 'dark' ? 380 : 760, 'sine', 0.08, 0.04);
      });
    }

    var menuBtn = document.querySelector('[data-action="menu"]');
    var mobile = document.querySelector('[data-mobile-nav]');
    if (menuBtn && mobile) {
      menuBtn.addEventListener('click', function () {
        var open = mobile.classList.toggle('is-open');
        menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        document.body.classList.toggle('menu-open', open);
        playTone(open ? 640 : 420, 'sine', 0.06, 0.04);
      });
      mobile.addEventListener('click', function (ev) {
        if (ev.target.tagName === 'A') {
          mobile.classList.remove('is-open');
          menuBtn.setAttribute('aria-expanded', 'false');
          document.body.classList.remove('menu-open');
        }
      });
    }

    document.querySelectorAll('[data-copy]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var text = btn.dataset.copy;
        var done = function () {
          var old = btn.textContent;
          btn.textContent = '已复制';
          setTimeout(function () { btn.textContent = old; }, 1600);
          playTone(880, 'sine', 0.05, 0.05);
          setTimeout(function () { playTone(1320, 'sine', 0.08, 0.05); }, 50);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, done);
        } else {
          var ta = document.createElement('textarea');
          ta.value = text; document.body.appendChild(ta); ta.select();
          try { document.execCommand('copy'); } catch (e) {}
          document.body.removeChild(ta); done();
        }
      });
    });

    var nav = document.querySelector('[data-nav]');
    if (nav) {
      var onScroll = function () {
        nav.classList.toggle('is-scrolled', window.scrollY > 24);
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  }

  /* ══ 16. 启动 ════════════════════════════════════════ */
  function boot() {
    initSoundToggle();
    initReveal();
    initCounters();
    initCard3DTilt();
    initStack3D();
    initBootstrapInspector();
    initDomainFilter();
    initRadarClock();
    initChrome();

    ensureThree(function (THREE) {
      if (THREE) {
        initBackground3D(THREE);
        initHero3D(THREE);
      } else {
        initGraphFallback();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
