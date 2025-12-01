<h1 align="center">Screen-Naping  Monitor</h1>
<p align="center">
  <strong>Multi-PC Screen Monitoring | VPS Compatible | Real-Time Viewer | Search & Highlight</strong><br>
  Extract screen text from one PC and view it live on another — across LAN or VPS.
</p>

<hr>

<h2>🌟 Features</h2>

<h3>📌 Reader Agent (PC #1)</h3>
<ul>
  <li>Runs silently in background</li>
  <li>Auto-detects Text area from screen</li>
  <li>Uses EasyOCR to read messages</li>
  <li>Sends only <b>new messages</b> to server</li>
  <li>Timestamped JSON format</li>
  <li>Configurable auto-start on Windows</li>
</ul>

<h3>🖥 Server (PC #2 or VPS)</h3>
<ul>
  <li>Lightweight Flask backend</li>
  <li>Stores Text messages in memory</li>
  <li>Provides two APIs:
    <ul>
      <li><code>/upload</code> – Reader agent sends text</li>
      <li><code>/fetch</code> – Receiver GUI fetches history</li>
    </ul>
  </li>
</ul>

<h3>💻 Receiver GUI (PC #2)</h3>
<ul>
  <li>Live Text viewer (auto-update)</li>
  <li><b>Keyword search with yellow highlight</b></li>
  <li><b>Time-range filter:</b>
    <ul>
      <li>All</li>
      <li>Today</li>
      <li>Yesterday</li>
      <li>Last 1 Hour</li>
      <li>Last 24 Hours</li>
    </ul>
  </li>
  <li>Smooth scroll and clean layout</li>
</ul>

<hr>

<h2>📦 Architecture</h2>

<pre>
 PC #1 (target Machine)
 ┌───────────────────┐
 │ Reader Agent      │──┐  OCR + Timestamp
 └───────────────────┘  │
                        ▼
                 ┌───────────────┐
                 │ Flask Server   │  (PC #2 or VPS)
                 └───────────────┘
                        ▲
                        │  JSON /fetch
                        │
 PC #2 (Viewer GUI) ────┘  Real-Time Display
</pre>

<hr>

<h2>🛠 Installation</h2>

<h3>Common Requirements</h3>
<pre>Python 3.8+</pre>

<h3>Reader Agent</h3>
<pre>
pip install easyocr mss numpy requests pystray pillow
</pre>

<h3>Server</h3>
<pre>
pip install flask
</pre>

<h3>Receiver GUI</h3>
<pre>
pip install requests
</pre>

<hr>

<h2>🚀 Setup Guide</h2>

<h3>1️⃣ Start Server (PC #2 or VPS)</h3>

<p>Run:</p>
<pre>python server.py</pre>

<p>Server starts at:</p>
<pre>http://0.0.0.0:5000</pre>

<h3>2️⃣ Start Reader Agent (PC #1)</h3>

<p>Set the server IP inside <code>reader.py</code>:</p>

<pre>
SERVER_UPLOAD_URL = "http://ip:5000/upload"
</pre>

<pre>python reader.py</pre>

<p>Or run hidden:</p>
<pre>reader_agent.pyw</pre>

<p>To auto-start:</p>
<pre>shell:startup</pre>

<h3>3️⃣ Start Receiver GUI (PC #2)</h3>

<p>Set the server IP inside <code>gui.py</code>:</p>

<pre>
SERVER_FETCH_URL = "http://ip:5000/fetch"
</pre>

Then run:

<pre>python gui.py</pre>

<hr>

<h2>📡 VPS Support</h2>

<p>This system supports VPS hosting for global monitoring:</p>

<ul>
  <li>Run <code>server.py</code> on VPS</li>
  <li>Reader Agent → send to VPS</li>
  <li>Receiver GUI → fetch from VPS</li>
</ul>


<hr>

<h2>🔍 Search Features</h2>

<h3>🔸 Keyword Search with Highlight</h3>
<ul>
  <li>Case-insensitive</li>
  <li>Matches highlighted in yellow</li>
</ul>

<h3>🔸 Time Range Filters</h3>
<ul>
  <li>Today</li>
  <li>Yesterday</li>
  <li>Last 1 Hour</li>
  <li>Last 24 Hours</li>
  <li>All</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
/project
│── reader.py    # Screen-Naping  client (PC #1)
│── server.py    # Flask message server (PC #2 or VPS)
│── gui.py       # Viewer GUI (PC #2)
└── README.md
</pre>

<hr>

<h2>📤 JSON Payload Example</h2>

<h3>Reader → Server</h3>
<pre>{
  "timestamp": "2025-11-23T16:20:10.510120",
  "messages": ["Hi sir", "When will stock", "7 days sir"]
}
</pre>

<h3>Server → Viewer</h3>
<pre>[
  { "time": "2025-11-23T16:20:10.510120", "msg": "Hi sir" },
  { "time": "2025-11-23T16:20:12.121212", "msg": "When will stock" },
  { "time": "2025-11-23T16:20:15.918222", "msg": "7 days sir" }
]
</pre>

<hr>


<hr>

<h2>🤝 Contributing</h2>
<p>PRs are welcome! You can help add:</p>

<ul>
  <li>SQLite persistent storage</li>
  <li>Web dashboard version</li>
  <li>Multi-agent login</li>
  <li>Notification system</li>
  <li>Docker container support</li>
</ul>

<hr>

<strong>⚠️ Warning: Misuse of this tool for illegal or unethical activities can lead to legal action under cybercrime laws. The developer assumes no responsibility for any misuse or violation</strong>

<hr>

<h2>📜 License</h2>
<p>MIT License — free for personal & educational use.</p>

<hr>

<h2 align="center">⭐ If you like this project, please star the repo!</h2>

# Watch Video For More Information.
[![YouTube Video](https://img.youtube.com/vi/OFImjStiDak/0.jpg)](https://youtu.be/OFImjStiDak?feature=shared)


# Available Our [Hacking Course](https://linuxndroid.in)

# Follow Me on :

[![Instagram](https://img.shields.io/badge/IG-linuxndroid-yellowgreen?style=for-the-badge&logo=instagram)](https://www.instagram.com/linuxndroid)

[![Youtube](https://img.shields.io/badge/Youtube-linuxndroid-redgreen?style=for-the-badge&logo=youtube)](https://www.youtube.com/channel/UC2O1Hfg-dDCbUcau5QWGcgg)

[![Browser](https://img.shields.io/badge/Website-linuxndroid-yellowred?style=for-the-badge&logo=browser)](https://www.linuxndroid.in)

<p align="center">Made with ❤️ by <strong>Linuxndroid</strong></p>
