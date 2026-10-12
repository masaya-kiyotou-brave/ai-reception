"""
components/header.py
ヘッダーバー（ロゴ + リアルタイム時計）
"""

import streamlit as st


def _get_clock_html() -> str:
    """現在時刻・日付のHTMLを返す（ブラウザのローカルタイムゾーンで表示）"""
    return """
    <div class="clock-area">
      <div class="clock-time" id="js-clock">--:--</div>
      <div class="clock-date" id="js-date">--月--日（-）</div>
    </div>
    """


def render_header() -> None:
    """ヘッダーバーを描画する"""
    st.markdown(f"""
    <div class="header-bar">
      <div class="logo-area">
        <div class="logo-icon">🏢</div>
        <div>
          <div class="logo-name">Reception AI</div>
          <div class="logo-sub">Smart Front Desk</div>
        </div>
      </div>
      {_get_clock_html()}
    </div>
    """, unsafe_allow_html=True)
    
    # JavaScript を別コンポーネントで実行（height を 0 から変更）
    st.components.v1.html("""
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
    """, height=1)
