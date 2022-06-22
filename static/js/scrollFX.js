// Scroll FX
window.addEventListener("load", function () { scrollFX() }), window.addEventListener("scroll", function () { scrollFX() }); var lastScrollTop = 0; function scrollFX() { var i = window.innerHeight; if (document.documentElement.scrollHeight != i) { var s = window.pageYOffset || document.documentElement.scrollTop, d = s < lastScrollTop; lastScrollTop = s <= 0 ? 0 : s; const l = document.querySelectorAll('[class*="scroll-fx-up-"], [class*="scroll-fx-down-"], [class*="scroll-fx-left-"], [class*="scroll-fx-right-"], [class*="scroll-fx-in-fade"], [class*="scroll-fx-out-fade"], [class*="scroll-fx-zoom-"]'); l.forEach(s => { var l, c, o, t, a, e, r = window.pageYOffset, n = r + 3 * i, f = s.getBoundingClientRect().top + window.scrollY; f < n && (!s.classList.contains("scroll-fx-in-range") && s.matches('[class*="scroll-fx-in-fade"], [class*="scroll-fx-out-fade"]') && s.classList.add("scroll-fx-in-range"), o = i / 2 - s.offsetHeight / 2, s.offsetHeight, t = r - f + s.offsetHeight / 100 + o, e = window.scrollY / (f - o), a = (f - o) / window.scrollY, c = (l = t / 10) + "%", n = -l + "%", r = 1 + t / 250, f = "in", o = 30, s.classList.contains("scroll-fx-continuous") && (o = 0), (0 < l || !s.matches('[class*="-in"]')) && (s.classList.contains("scroll-fx-continuous") && s.matches('[class*="-out"]') || (n = c = 0), 0 < l && (a = e = 1), s.matches('[class*="-in-fade"],[class*="-out-fade"]') && (s.style.opacity = "1.0")), o < l && s.matches('[class*="-out"]') && (f = "out", c = -Math.abs(l - o) + "%", n = Math.abs(l - o) + "%", r = 1 - t / 250 + .8), t = "", s.matches('[class*="scroll-fx-left-' + f + '"]') && (t = "translate3d(" + c + ",0,0)"), s.matches('[class*="scroll-fx-right-' + f + '"]') ? t = "translate3d(" + n + ",0,0)" : s.matches('[class*="scroll-fx-up-' + f + '"]') ? t = "translate3d(0," + n + ",0)" : s.matches('[class*="scroll-fx-down-' + f + '"]') && (t = "translate3d(0," + c + ",0)"), s.matches('[class*="scroll-fx-zoom-push"], [class*="scroll-fx-zoom-pull"]') && (e = e, s.matches('[class*="scroll-fx-zoom-push"]') && (2 < (e = a) ? e = 2 : (a = s.getAttribute("scroll-fx-last-scale"), d ? e < a && (e = a) : a < e && (e = a)), s.setAttribute("scroll-fx-last-scale", e)), s.matches('[class*="scroll-fx-up-"], [class*="scroll-fx-down-"], [class*="scroll-fx-left-"], [class*="scroll-fx-right-"]') ? t += "scale(" + e + ")" : t = "scale(" + e + ")"), s.classList.contains("scroll-fx-" + f + "-fade") && !s.matches('[class*="scroll-fx-zoom-"]') || (s.style.transform = t), s.matches('[class*="-' + f + '-fade"]') && (s.style.opacity = r)) }) } }