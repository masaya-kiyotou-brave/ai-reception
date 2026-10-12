"""
components/header.py
ヘッダーバー（ロゴ + リアルタイム時計）
"""

import streamlit as st


def render_header() -> None:
    """ヘッダーバーを描画する"""
    st.components.v1.html("""
    <style>
      .header-bar {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 0 14px;
        border-bottom: 1px solid rgba(74, 127, 165, 0.12);
        margin-bottom: 8px;
      }
      .logo-area {
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .logo-icon {
        width: 38px;
        height: 38px;
        background: linear-gradient(135deg, #4a7fa5, #6badd4);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        box-shadow: 0 3px 12px rgba(74, 127, 165, 0.28);
      }
      .logo-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 20px;
        font-weight: 400;
        color: #1a2533;
        letter-spacing: 0.04em;
      }
      .logo-sub {
        font-size: 9px;
        font-weight: 300;
        color: #8fa3b8;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-top: 1px;
      }
      .clock-area {
        text-align: right;
      }
      .clock-time {
        font-family: 'Cormorant Garamond', serif;
        font-size: 26px;
        font-weight: 300;
        color: #1a2533;
        letter-spacing: 0.06em;
      }
      .clock-date {
        font-size: 11px;
        font-weight: 300;
        color: #8fa3b8;
        letter-spacing: 0.08em;
        margin-top: 2px;
      }
    </style>
    <div class="header-bar">
      <div class="logo-area">
        <div class="logo-icon">🏢</div>
        <div>
          <div class="logo-name">Reception AI</div>
          <div class="logo-sub">Smart Front Desk</div>
        </div>
      </div>
      <div class="clock-area">
        <div class="clock-time" id="js-clock">--:--</div>
        <div class="clock-date" id="js-date">--月--日（-）</div>
      </div>
    </div>
    <script>
      function updateClock() {
        const now = new Date();
        const hh = String(now.getHours()).padStart(2,'0');
        const mm = String(now.getMinutes()).padStart(2,'0');
        const days = ['日','月','火','水','木','金','土'];
        const dateStr = (now.getMonth()+1)+'月'+now.getDate()+'日（'+days[now.getDay()]+'）';
        const el = document.getElementById('js-clock');
        const dl = document.getElementById('js-date');
        if (el) el.textContent = hh+':'+mm;
        if (dl) dl.textContent = dateStr;
      }
      updateClock();
      setInterval(updateClock, 10000);
    </script>
    """, height=100)
