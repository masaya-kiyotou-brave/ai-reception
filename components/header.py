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
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 20px;
        background-color: #f8f9fa;
        border-bottom: 1px solid #e0e0e0;
      }
      .logo-area {
        display: flex;
        align-items: center;
        gap: 12px;
      }
      .logo-icon {
        font-size: 32px;
      }
      .logo-name {
        font-weight: 600;
        font-size: 18px;
      }
      .logo-sub {
        font-size: 12px;
        color: #666;
      }
      .clock-area {
        text-align: right;
      }
      .clock-time {
        font-size: 24px;
        font-weight: 600;
        font-family: 'Courier New', monospace;
      }
      .clock-date {
        font-size: 12px;
        color: #666;
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
