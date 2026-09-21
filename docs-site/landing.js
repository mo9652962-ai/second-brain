/* ============================================================
   Second Brain — Landing interactions
   零外部依赖：Canvas 2D 伪 3D 知识图谱 + 滚动进场 + 计数
   ============================================================ */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 真实数据：18 个知识域（git ls-files 统计）─────────── */
  var DOMAINS = [
    { key: 'Research',     n: 235, label: '研究',   copy: '论文、文献、研究方法' },
    { key: 'Dev',          n: 143, label: '开发',   copy: 'Web 开发、工具链、DevOps' },
    { key: 'Productivity', n: 54,  label: '生产力', copy: '工作流、变现、自动化' },
    { key: 'Security',     n: 53,  label: '安全',   copy: '网安、CTF、防御加固' },
    { key: 'cards',        n: 37,  label: '知识卡', copy: '原子化知识卡片' },
    { key: 'Daily',        n: 34,  label: '日常',   copy: '每日回顾与沉淀' },
    { key: 'Hardware',     n: 21,  label: '硬件',   copy: 'PCB、单片机、CAD' },
    { key: 'AI',           n: 19,  label: 'AI',     copy: 'Agent、模型、提示词' },
    { key: 'Finance',      n: 16,  label: '金融',   copy: '投资与市场研究' },
    { key: 'Archive',      n: 13,  label: '归档',   copy: '历史资料归档' },
    { key: 'Content',      n: 10,  label: '内容',   copy: '自媒体与选题池' },
    { key: 'SOP',          n: 10,  label: 'SOP',    copy: '标准作业流程' },
    { key: 'META',         n: 9,   label: '元信息', copy: '知识库治理' },
    { key: 'Creative',     n: 6,   label: '创意',   copy: '设计与视觉' },
    { key: 'gaming',       n: 4,   label: '游戏',   copy: '游戏研究与 mod' },
    { key: 'Product',      n: 2,   label: '产品',   copy: '产品化与商业化' },
    { key: 'Projects',     n: 2,   label: '项目',   copy: '项目记录' },
    { key: 'Education',    n: 1,   label: '教育',   copy: '教学与练习设计' }
  ];
  var MAXN = DOMAINS[0].n;

  /* ══ 主题 ══════════════════════════════════════════ */
  function initTheme() {
    var saved = null;
    try { saved = localStorage.getItem('sb-theme'); } catch (e) {}
    root.dataset.theme = saved || 'dark';
  }
  initTheme();

  /* ══ 知识域网格 ═════════════════════════════════════ */
  function renderDomains() {
    var host = document.querySelector('[data-domains]');
    if (!host) return;
    /* 用 DOM API 构建（不用 innerHTML）：数据虽为文件内硬编码常量，
       但保持「永不拼接 HTML」的习惯，避免日后接入外部数据时引入 XSS。 */
    var frag = document.createDocumentFragment();
    for (var i = 0; i < DOMAINS.length; i++) {
      var d = DOMAINS[i];
      var w = Math.max(8, Math.round((d.n / MAXN) * 100));

      var a = document.createElement('a');
      a.className = 'dom reveal';
      a.href = './kb/';
      a.setAttribute('data-dom', d.key);

      var strong = document.createElement('strong');
      strong.textContent = d.label;

      var span = document.createElement('span');
      span.textContent = d.key + ' · ' + d.n;

      var bar = document.createElement('i');
      bar.style.setProperty('--w', w + '%');

      a.appendChild(strong);
      a.appendChild(span);
      a.appendChild(bar);
      frag.appendChild(a);
    }
    host.appendChild(frag);
  }
  renderDomains();

  /* ══ 滚动进场 ══════════════════════════════════════ */
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

    /* 安全网：锚点跳转 / 快速滚动 / 直接落地中段时，IO 可能不触发，
       元素会永久停在 opacity:0。用 rAF 节流的滚动检查兜底，
       把「已进入或在视口上方」的元素直接显示出来。 */
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
    /* 首屏兜底：DOM 就绪后立刻扫一次（含 hash 直接定位的情形） */
    setTimeout(sweep, 120);
  }

  /* ══ 数字计数 + 进度条 ═════════════════════════════ */
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

  /* ══ Canvas 伪 3D 知识图谱 ═════════════════════════ */
  function initGraph() {
    var canvas = document.querySelector('[data-graph]');
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
      cx = W / 2; cy = H / 2;
      R = Math.min(W, H) * 0.33;
    }

    /* 节点：hub 在中心，18 个域分布在球面（Fibonacci 球）*/
    var nodes = [{ key: 'HOME', label: 'HOME', n: 1093, hub: true, x: 0, y: 0, z: 0 }];
    var GA = Math.PI * (3 - Math.sqrt(5));
    for (var i = 0; i < DOMAINS.length; i++) {
      var y = 1 - (i / (DOMAINS.length - 1)) * 2;
      var rad = Math.sqrt(Math.max(0, 1 - y * y));
      var th = GA * i;
      nodes.push({
        key: DOMAINS[i].key, label: DOMAINS[i].label, n: DOMAINS[i].n,
        x: Math.cos(th) * rad, y: y, z: Math.sin(th) * rad
      });
    }

    /* 边：hub→每个域 + 若干跨域关联（真实语义）*/
    var CROSS = [
      ['AI', 'Dev'], ['AI', 'Research'], ['Dev', 'Security'], ['Research', 'Education'],
      ['Hardware', 'Dev'], ['Productivity', 'SOP'], ['Product', 'Finance'],
      ['Content', 'Creative'], ['cards', 'META'], ['gaming', 'Creative']
    ];
    var edges = [];
    for (var e = 1; e < nodes.length; e++) edges.push([0, e]);
    CROSS.forEach(function (pair) {
      var a = -1, b = -1;
      for (var k = 0; k < nodes.length; k++) {
        if (nodes[k].key === pair[0]) a = k;
        if (nodes[k].key === pair[1]) b = k;
      }
      if (a > 0 && b > 0) edges.push([a, b]);
    });

    var rot = { x: -0.18, y: 0.5 };
    var vel = { x: 0, y: 0.0016 };
    var drag = { on: false, lx: 0, ly: 0 };
    var focused = -1;
    var t = 0;

    function project(p) {
      /* 绕 Y 再绕 X 旋转 */
      var cy1 = Math.cos(rot.y), sy1 = Math.sin(rot.y);
      var x1 = p.x * cy1 - p.z * sy1;
      var z1 = p.x * sy1 + p.z * cy1;
      var cx1 = Math.cos(rot.x), sx1 = Math.sin(rot.x);
      var y1 = p.y * cx1 - z1 * sx1;
      var z2 = p.y * sx1 + z1 * cx1;
      var persp = 1 / (1.75 - z2 * 0.62);
      return { x: cx + x1 * R * persp * 1.7, y: cy + y1 * R * persp * 1.7, z: z2, s: persp };
    }

    function css(name) {
      return getComputedStyle(root).getPropertyValue(name).trim() || '#888';
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var cViolet = css('--violet'), cCyan = css('--cyan'), cInk = css('--ink'), cMuted = css('--muted');

      var pts = nodes.map(project);

      /* 呼吸脉动 */
      var breathe = 1 + Math.sin(t * 0.0011) * 0.045;
      for (var i = 0; i < pts.length; i++) {
        pts[i].x = cx + (pts[i].x - cx) * breathe;
        pts[i].y = cy + (pts[i].y - cy) * breathe;
      }

      /* 边 */
      for (var j = 0; j < edges.length; j++) {
        var a = pts[edges[j][0]], b = pts[edges[j][1]];
        var depth = (a.z + b.z) / 2;
        var alpha = 0.1 + (depth + 1) * 0.13;
        var isCross = edges[j][0] !== 0 && edges[j][1] !== 0;
        ctx.strokeStyle = isCross
          ? 'rgba(34,211,238,' + (alpha * 0.72) + ')'
          : 'rgba(124,92,255,' + alpha + ')';
        ctx.lineWidth = isCross ? 0.7 : 0.9;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.lineTo(b.x, b.y);
        ctx.stroke();

        /* hub 连线上的流动光点 */
        if (edges[j][0] === 0 && !reduce) {
          var f = ((t * 0.00042) + j * 0.11) % 1;
          var px = a.x + (b.x - a.x) * f;
          var py = a.y + (b.y - a.y) * f;
          ctx.fillStyle = 'rgba(34,211,238,' + (0.75 * Math.max(0, depth + 1) / 2 + 0.15) + ')';
          ctx.beginPath();
          ctx.arc(px, py, 1.5, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      /* 节点：按深度排序（远→近）*/
      var order = pts.map(function (p, idx) { return idx; })
                     .sort(function (m, n) { return pts[m].z - pts[n].z; });

      for (var k = 0; k < order.length; k++) {
        var idx = order[k];
        var p = pts[idx];
        var node = nodes[idx];
        var isFocus = idx === focused;
        var base = node.hub ? 8.5 : 3.4 + (node.n / MAXN) * 3.4;
        var rr = base * p.s * (isFocus ? 1.5 : 1);

        /* 光晕 */
        var glow = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, rr * 4.5);
        var gc = node.hub ? '124,92,255' : (isFocus ? '255,180,84' : '124,92,255');
        glow.addColorStop(0, 'rgba(' + gc + ',' + (0.34 + (p.z + 1) * 0.12) + ')');
        glow.addColorStop(1, 'rgba(' + gc + ',0)');
        ctx.fillStyle = glow;
        ctx.beginPath(); ctx.arc(p.x, p.y, rr * 4.5, 0, Math.PI * 2); ctx.fill();

        /* 实心 */
        ctx.fillStyle = node.hub ? cViolet : (isFocus ? '#ffb454' : cCyan);
        ctx.beginPath(); ctx.arc(p.x, p.y, rr, 0, Math.PI * 2); ctx.fill();

        /* 标签：hub / 聚焦 / 前排 */
        if (node.hub || isFocus || p.z > 0.42) {
          ctx.font = (node.hub ? '600 11px' : '500 10px') + ' ui-monospace, monospace';
          ctx.fillStyle = isFocus ? '#ffb454' : cInk;
          ctx.globalAlpha = 0.55 + (p.z + 1) * 0.22;
          ctx.textAlign = 'left';
          ctx.fillText(node.label, p.x + rr + 5, p.y + 3);
          ctx.globalAlpha = 1;
        }
      }
    }

    function loop() {
      if (!drag.on) {
        rot.y += vel.y;
        rot.x += vel.x;
        vel.y += (0.0016 - vel.y) * 0.02;
        rot.x += Math.sin(t * 0.0003) * 0.00025;
      }
      t += 16;
      draw();
      requestAnimationFrame(loop);
    }

    /* 拾取最近节点 */
    function pick(mx, my) {
      var best = -1, bd = 1e9;
      for (var i = 0; i < nodes.length; i++) {
        var p = project(nodes[i]);
        var d = Math.hypot(p.x - mx, p.y - my);
        if (d < 26 && d < bd) { bd = d; best = i; }
      }
      return best;
    }

    function focusNode(idx) {
      focused = idx;
      var node = nodes[idx];
      if (!node) return;
      if (node.hub) {
        if (status) status.textContent = '已聚焦 HOME · 1093 篇笔记总入口';
        if (dTitle) dTitle.textContent = 'HOME';
        if (dCopy) dCopy.textContent = '1093 篇 · 总索引与目标级联';
      } else {
        var d = DOMAINS.filter(function (x) { return x.key === node.key; })[0];
        if (status) status.textContent = '已选中 ' + node.key;
        if (dTitle) dTitle.textContent = d.label + ' · ' + node.key;
        if (dCopy) dCopy.textContent = d.n + ' 篇 · ' + d.copy;
      }
    }

    var moved = false;
    function pos(ev) {
      var r = canvas.getBoundingClientRect();
      return { x: ev.clientX - r.left, y: ev.clientY - r.top };
    }

    canvas.addEventListener('pointerdown', function (ev) {
      drag.on = true; moved = false;
      var p = pos(ev); drag.lx = p.x; drag.ly = p.y;
      canvas.setPointerCapture(ev.pointerId);
    });
    canvas.addEventListener('pointermove', function (ev) {
      if (!drag.on) return;
      var p = pos(ev);
      var dx = p.x - drag.lx, dy = p.y - drag.ly;
      if (Math.abs(dx) + Math.abs(dy) > 2) moved = true;
      rot.y += dx * 0.006;
      rot.x = Math.max(-1.2, Math.min(1.2, rot.x + dy * 0.005));
      vel.y = dx * 0.0016;
      vel.x = 0;
      drag.lx = p.x; drag.ly = p.y;
    });
    function endDrag(ev) {
      if (!drag.on) return;
      drag.on = false;
      try { canvas.releasePointerCapture(ev.pointerId); } catch (e) {}
      if (!moved) {
        var p = pos(ev);
        var idx = pick(p.x, p.y);
        if (idx >= 0) focusNode(idx);
      }
    }
    canvas.addEventListener('pointerup', endDrag);
    canvas.addEventListener('pointercancel', endDrag);

    /* 键盘可达性 */
    canvas.tabIndex = 0;
    canvas.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowRight' || ev.key === 'ArrowDown') {
        focusNode((focused + 1 + nodes.length) % nodes.length); ev.preventDefault();
      } else if (ev.key === 'ArrowLeft' || ev.key === 'ArrowUp') {
        focusNode((focused - 1 + nodes.length) % nodes.length); ev.preventDefault();
      } else if (ev.key === 'Escape') {
        focused = -1; if (status) status.textContent = '拖动 / 点击节点查看领域';
      }
    });

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        rot.x = -0.18; rot.y = 0.5; vel.x = 0; vel.y = 0.0016;
        focused = -1;
        if (status) status.textContent = '视角已重置';
        if (dTitle) dTitle.textContent = 'Research';
        if (dCopy) dCopy.textContent = '235 篇 · 论文、文献、研究方法';
      });
    }

    resize();
    window.addEventListener('resize', resize);
    if (reduce) { draw(); } else { requestAnimationFrame(loop); }
  }

  /* ══ 主题 / 菜单 / 复制 / 滚动 ═════════════════════ */
  function initChrome() {
    var themeBtn = document.querySelector('[data-action="theme"]');
    if (themeBtn) {
      themeBtn.addEventListener('click', function () {
        var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
        root.dataset.theme = next;
        try { localStorage.setItem('sb-theme', next); } catch (e) {}
      });
    }

    var menuBtn = document.querySelector('[data-action="menu"]');
    var mobile = document.querySelector('[data-mobile-nav]');
    if (menuBtn && mobile) {
      menuBtn.addEventListener('click', function () {
        var open = mobile.classList.toggle('is-open');
        menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        document.body.classList.toggle('menu-open', open);
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

  /* ══ 启动 ═════════════════════════════════════════ */
  function boot() {
    initReveal();
    initCounters();
    initGraph();
    initChrome();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
