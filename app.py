from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Innovartus Technologies</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #0a0e27; color: #fff; min-height: 100vh; }
        .hero { text-align: center; padding: 80px 20px; background: linear-gradient(135deg, #0a0e27, #1a1f4e); }
        h1 { font-size: 3em; color: #00d4ff; margin-bottom: 15px; }
        .tagline { font-size: 1.3em; color: #8892b0; margin-bottom: 40px; }
        .badge { display: inline-block; background: #00d4ff; color: #0a0e27; padding: 12px 30px; border-radius: 25px; font-weight: bold; font-size: 1.1em; margin: 10px; }
        .stats { display: flex; justify-content: center; gap: 40px; margin: 60px 20px; flex-wrap: wrap; }
        .stat { background: #1a1f4e; padding: 30px 40px; border-radius: 15px; border: 1px solid #00d4ff33; text-align: center; }
        .stat-num { font-size: 2.5em; color: #00d4ff; font-weight: bold; }
        .stat-label { color: #8892b0; margin-top: 8px; }
        .features { padding: 60px 20px; max-width: 900px; margin: 0 auto; }
        .feature { background: #1a1f4e; padding: 20px 25px; border-radius: 10px; margin: 15px 0; border-left: 4px solid #00d4ff; }
        .feature h3 { color: #00d4ff; margin-bottom: 8px; }
        .feature p { color: #8892b0; line-height: 1.6; }
        .footer { text-align: center; padding: 30px; color: #444; border-top: 1px solid #1a1f4e; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>Innovartus Technologies</h1>
        <p class="tagline">Cloud-native SaaS platform — built for scale</p>
        <span class="badge">✅ Live on Render</span>
        <span class="badge">🚀 CI/CD Enabled</span>
    </div>
    <div class="stats">
        <div class="stat">
            <div class="stat-num">99.9%</div>
            <div class="stat-label">Uptime SLA</div>
        </div>
        <div class="stat">
            <div class="stat-num">PaaS</div>
            <div class="stat-label">Deployment Model</div>
        </div>
        <div class="stat">
            <div class="stat-num">Auto</div>
            <div class="stat-label">Scaling</div>
        </div>
        <div class="stat">
            <div class="stat-num">&lt;2min</div>
            <div class="stat-label">Deploy Time</div>
        </div>
    </div>
    <div class="features">
        <div class="feature">
            <h3>Pay-As-You-Go Pricing</h3>
            <p>Innovartus only pays for compute resources actually consumed. No upfront costs, no idle server charges. Costs scale proportionally with user growth.</p>
        </div>
        <div class="feature">
            <h3>Continuous Deployment</h3>
            <p>Every push to GitHub automatically triggers a new deployment. Zero manual steps, zero downtime deployments. Features reach users within minutes.</p>
        </div>
        <div class="feature">
            <h3>Automatic Scaling</h3>
            <p>Platform automatically scales from 10 to 10,000 users without configuration changes. No DevOps engineer required to handle traffic spikes.</p>
        </div>
    </div>
    <div class="footer">
        <p>Innovartus Technologies &copy; 2026 | Deployed: {{ time }} | Cloud Computing Case Study 3</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/health')
def health():
    return {"status": "healthy", "service": "Innovartus SaaS", "version": "1.0.0"}

if __name__ == '__main__':
    app.run(debug=True)
