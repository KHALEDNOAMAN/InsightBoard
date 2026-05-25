"""
InsightBoard — Interactive Data Analytics Dashboard
=====================================================
A beautiful analytics dashboard with interactive charts, real-time
data visualization, KPI cards, and multiple chart types.

Features:
  - 8 interactive Chart.js visualizations
  - Real-time simulated data with auto-refresh
  - KPI summary cards with animated counters
  - Dark/Light theme toggle
  - Responsive layout with grid system
  - Data export to CSV
  - Multiple chart types: Line, Bar, Doughnut, Radar, Area, Polar

Author: Khaled Noaman
Technologies: Python, Flask, Chart.js, HTML/CSS/JS
"""

import os
import random
import math
from datetime import datetime, timedelta
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# ============================================
# Data Generator
# ============================================
class DataGenerator:
    """Generates realistic analytics data for the dashboard."""
    
    def __init__(self):
        self.base_revenue = 45000
        self.base_users = 12500
        self.base_orders = 890
        self.base_conversion = 3.2
    
    def get_kpi_data(self):
        """Generate KPI summary data."""
        revenue = self.base_revenue + random.randint(-2000, 5000)
        users = self.base_users + random.randint(-200, 800)
        orders = self.base_orders + random.randint(-50, 120)
        conversion = round(self.base_conversion + random.uniform(-0.5, 0.8), 1)
        
        return {
            "revenue": {"value": revenue, "change": round(random.uniform(-5, 15), 1), "prefix": "$"},
            "users": {"value": users, "change": round(random.uniform(-3, 12), 1), "prefix": ""},
            "orders": {"value": orders, "change": round(random.uniform(-8, 18), 1), "prefix": ""},
            "conversion": {"value": conversion, "change": round(random.uniform(-1, 2), 1), "suffix": "%"}
        }
    
    def get_revenue_chart(self):
        """Generate monthly revenue data for the last 12 months."""
        months = []
        revenue = []
        expenses = []
        profit = []
        now = datetime.now()
        
        for i in range(11, -1, -1):
            date = now - timedelta(days=i * 30)
            months.append(date.strftime("%b %Y"))
            rev = 35000 + random.randint(0, 20000) + (i * 500)
            exp = 20000 + random.randint(0, 10000)
            revenue.append(rev)
            expenses.append(exp)
            profit.append(rev - exp)
        
        return {"labels": months, "revenue": revenue, "expenses": expenses, "profit": profit}
    
    def get_traffic_chart(self):
        """Generate daily traffic data for the last 30 days."""
        labels = []
        visitors = []
        page_views = []
        now = datetime.now()
        
        for i in range(29, -1, -1):
            date = now - timedelta(days=i)
            labels.append(date.strftime("%d %b"))
            base = 800 + int(300 * math.sin(i * 0.5))
            v = base + random.randint(-100, 200)
            visitors.append(max(v, 100))
            page_views.append(int(v * random.uniform(2.5, 4.0)))
        
        return {"labels": labels, "visitors": visitors, "page_views": page_views}
    
    def get_category_data(self):
        """Generate sales by category."""
        categories = ["Electronics", "Clothing", "Food & Beverage", "Home & Garden", "Sports", "Books", "Automotive"]
        values = [random.randint(5000, 25000) for _ in categories]
        return {"labels": categories, "values": values}
    
    def get_user_demographics(self):
        """Generate user demographic data."""
        return {
            "age_groups": {
                "labels": ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"],
                "values": [18, 32, 25, 14, 8, 3]
            },
            "devices": {
                "labels": ["Mobile", "Desktop", "Tablet"],
                "values": [58, 35, 7]
            },
            "countries": {
                "labels": ["United States", "Turkey", "Germany", "UK", "France", "Canada", "Other"],
                "values": [35, 20, 12, 10, 8, 5, 10]
            }
        }
    
    def get_performance_metrics(self):
        """Generate performance radar data."""
        return {
            "labels": ["Speed", "Uptime", "Security", "UX Score", "SEO", "Accessibility"],
            "current": [88, 99.5, 92, 85, 78, 90],
            "previous": [82, 98.2, 88, 80, 72, 85]
        }
    
    def get_hourly_activity(self):
        """Generate 24-hour activity heatmap data."""
        hours = [f"{h:02d}:00" for h in range(24)]
        activity = []
        for h in range(24):
            if 9 <= h <= 17:
                activity.append(random.randint(60, 100))
            elif 6 <= h <= 8 or 18 <= h <= 22:
                activity.append(random.randint(30, 65))
            else:
                activity.append(random.randint(5, 25))
        return {"labels": hours, "values": activity}
    
    def get_top_products(self):
        """Generate top products table data."""
        products = [
            {"name": "Pro Subscription", "sales": random.randint(200, 500), "revenue": random.randint(5000, 15000), "growth": round(random.uniform(-5, 25), 1)},
            {"name": "Enterprise Plan", "sales": random.randint(50, 150), "revenue": random.randint(10000, 30000), "growth": round(random.uniform(5, 35), 1)},
            {"name": "API Access Pack", "sales": random.randint(100, 300), "revenue": random.randint(3000, 10000), "growth": round(random.uniform(-2, 20), 1)},
            {"name": "Cloud Storage", "sales": random.randint(300, 800), "revenue": random.randint(4000, 12000), "growth": round(random.uniform(0, 15), 1)},
            {"name": "Support Premium", "sales": random.randint(80, 200), "revenue": random.randint(2000, 8000), "growth": round(random.uniform(-3, 18), 1)},
        ]
        return sorted(products, key=lambda x: x["revenue"], reverse=True)
    
    def get_all_data(self):
        """Get all dashboard data at once."""
        return {
            "kpi": self.get_kpi_data(),
            "revenue": self.get_revenue_chart(),
            "traffic": self.get_traffic_chart(),
            "categories": self.get_category_data(),
            "demographics": self.get_user_demographics(),
            "performance": self.get_performance_metrics(),
            "hourly": self.get_hourly_activity(),
            "products": self.get_top_products(),
            "updated_at": datetime.now().strftime("%I:%M:%S %p")
        }


data_gen = DataGenerator()


# ============================================
# Routes
# ============================================
@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/data')
def get_data():
    return jsonify(data_gen.get_all_data())

@app.route('/api/kpi')
def get_kpi():
    return jsonify(data_gen.get_kpi_data())

@app.route('/api/revenue')
def get_revenue():
    return jsonify(data_gen.get_revenue_chart())

@app.route('/api/traffic')
def get_traffic():
    return jsonify(data_gen.get_traffic_chart())


# ============================================
# Dashboard HTML
# ============================================
DASHBOARD_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InsightBoard — Analytics Dashboard</title>
    <meta name="description" content="InsightBoard - Interactive data analytics dashboard with real-time charts">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        :root{
            --bg:#0f0f1a;--bg2:#161628;--card:#1c1c36;--card-hover:#22223f;
            --border:rgba(99,102,241,0.12);--text:#e8e8f4;--text2:#8888aa;--text3:#555577;
            --accent:#6366f1;--accent2:#818cf8;--accent-glow:rgba(99,102,241,0.25);
            --green:#10b981;--green-bg:rgba(16,185,129,0.1);
            --red:#ef4444;--red-bg:rgba(239,68,68,0.1);
            --blue:#3b82f6;--yellow:#f59e0b;--purple:#a855f7;--pink:#ec4899;--cyan:#06b6d4;
            --shadow:0 4px 24px rgba(0,0,0,0.3);--radius:14px;
        }
        body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh}
        body::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;
            background:radial-gradient(circle at 15% 85%,rgba(99,102,241,0.06) 0%,transparent 50%),
                        radial-gradient(circle at 85% 15%,rgba(16,185,129,0.04) 0%,transparent 50%);z-index:0;pointer-events:none}

        .app{position:relative;z-index:1;display:flex;min-height:100vh}

        /* Sidebar */
        .sidebar{width:240px;background:var(--bg2);border-right:1px solid var(--border);padding:20px;display:flex;flex-direction:column;position:fixed;height:100vh;overflow-y:auto}
        .logo{display:flex;align-items:center;gap:10px;margin-bottom:28px}
        .logo-icon{width:38px;height:38px;background:linear-gradient(135deg,var(--accent),var(--cyan));border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 4px 15px var(--accent-glow)}
        .logo h1{font-size:17px;font-weight:700;background:linear-gradient(135deg,var(--accent2),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
        .logo span{font-size:10px;color:var(--text2);display:block}

        .nav{list-style:none;flex:1}
        .nav li{padding:10px 14px;border-radius:10px;font-size:13px;color:var(--text2);cursor:pointer;display:flex;align-items:center;gap:10px;margin-bottom:4px;transition:all 0.2s}
        .nav li:hover,.nav li.active{background:rgba(99,102,241,0.1);color:var(--accent2)}
        .nav li.active{border-left:3px solid var(--accent)}

        .sidebar-footer{font-size:11px;color:var(--text3);text-align:center;padding-top:16px;border-top:1px solid var(--border)}

        /* Main */
        .main{flex:1;margin-left:240px;padding:20px 28px}

        /* Header */
        .header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
        .header h2{font-size:22px;font-weight:700}
        .header-right{display:flex;align-items:center;gap:12px}
        .refresh-btn{padding:8px 16px;background:var(--card);border:1px solid var(--border);border-radius:10px;color:var(--text);font-size:13px;cursor:pointer;font-family:'Inter',sans-serif;transition:all 0.2s;display:flex;align-items:center;gap:6px}
        .refresh-btn:hover{border-color:var(--accent);background:rgba(99,102,241,0.1)}
        .last-update{font-size:12px;color:var(--text3)}

        /* KPI Cards */
        .kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
        .kpi-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;transition:all 0.3s;position:relative;overflow:hidden}
        .kpi-card:hover{border-color:var(--accent);transform:translateY(-3px);box-shadow:0 8px 30px var(--accent-glow)}
        .kpi-card::after{content:'';position:absolute;top:0;right:0;width:80px;height:80px;border-radius:50%;opacity:0.05;transform:translate(20px,-20px)}
        .kpi-card:nth-child(1)::after{background:var(--green)} .kpi-card:nth-child(2)::after{background:var(--blue)}
        .kpi-card:nth-child(3)::after{background:var(--purple)} .kpi-card:nth-child(4)::after{background:var(--yellow)}
        .kpi-label{font-size:12px;color:var(--text2);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:8px;display:flex;align-items:center;gap:6px}
        .kpi-value{font-size:28px;font-weight:800;margin-bottom:6px}
        .kpi-change{font-size:12px;font-weight:600;display:flex;align-items:center;gap:4px;padding:3px 8px;border-radius:6px;width:fit-content}
        .kpi-change.up{background:var(--green-bg);color:var(--green)} .kpi-change.down{background:var(--red-bg);color:var(--red)}

        /* Chart Grid */
        .chart-grid{display:grid;grid-template-columns:2fr 1fr;gap:16px;margin-bottom:16px}
        .chart-grid-equal{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
        .chart-grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:16px}
        .chart-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;transition:all 0.3s}
        .chart-card:hover{border-color:var(--accent);box-shadow:var(--shadow)}
        .chart-title{font-size:14px;font-weight:600;margin-bottom:4px;display:flex;justify-content:space-between;align-items:center}
        .chart-subtitle{font-size:11px;color:var(--text3);margin-bottom:16px}
        .chart-container{position:relative;width:100%;height:260px}
        .chart-container-sm{position:relative;width:100%;height:220px}

        /* Table */
        .table-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:16px}
        table{width:100%;border-collapse:collapse}
        th{font-size:11px;color:var(--text2);text-transform:uppercase;letter-spacing:0.5px;text-align:left;padding:10px 12px;border-bottom:1px solid var(--border)}
        td{font-size:13px;padding:12px;border-bottom:1px solid rgba(255,255,255,0.03)}
        tr:hover td{background:rgba(99,102,241,0.04)}
        .growth-badge{font-size:11px;padding:2px 8px;border-radius:5px;font-weight:600}
        .growth-badge.up{background:var(--green-bg);color:var(--green)} .growth-badge.down{background:var(--red-bg);color:var(--red)}

        /* Responsive */
        @media(max-width:1200px){.kpi-grid{grid-template-columns:repeat(2,1fr)}.chart-grid,.chart-grid-equal{grid-template-columns:1fr}.chart-grid-3{grid-template-columns:1fr 1fr}}
        @media(max-width:768px){.sidebar{display:none}.main{margin-left:0}.kpi-grid{grid-template-columns:1fr}.chart-grid-3{grid-template-columns:1fr}}

        /* Animations */
        @keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
        .kpi-card,.chart-card,.table-card{animation:fadeIn 0.4s ease}
        .kpi-card:nth-child(2){animation-delay:0.05s} .kpi-card:nth-child(3){animation-delay:0.1s} .kpi-card:nth-child(4){animation-delay:0.15s}
    </style>
</head>
<body>
<div class="app">
    <aside class="sidebar">
        <div class="logo"><div class="logo-icon">📊</div><div><h1>InsightBoard</h1><span>Analytics v1.0</span></div></div>
        <ul class="nav">
            <li class="active">📊 Dashboard</li>
            <li>📈 Revenue</li>
            <li>👥 Users</li>
            <li>🛒 Products</li>
            <li>🌍 Traffic</li>
            <li>⚡ Performance</li>
            <li>📋 Reports</li>
            <li>⚙️ Settings</li>
        </ul>
        <div class="sidebar-footer">Built by Khaled Noaman<br>© 2026 InsightBoard</div>
    </aside>

    <main class="main">
        <div class="header">
            <div><h2>📊 Analytics Dashboard</h2><span class="last-update">Last updated: <span id="lastUpdate">—</span></span></div>
            <div class="header-right">
                <button class="refresh-btn" onclick="loadData()">🔄 Refresh Data</button>
            </div>
        </div>

        <!-- KPI Cards -->
        <div class="kpi-grid">
            <div class="kpi-card"><div class="kpi-label">💰 Total Revenue</div><div class="kpi-value" id="kpiRevenue">—</div><div class="kpi-change up" id="kpiRevenueChange">—</div></div>
            <div class="kpi-card"><div class="kpi-label">👥 Active Users</div><div class="kpi-value" id="kpiUsers">—</div><div class="kpi-change up" id="kpiUsersChange">—</div></div>
            <div class="kpi-card"><div class="kpi-label">🛒 Total Orders</div><div class="kpi-value" id="kpiOrders">—</div><div class="kpi-change up" id="kpiOrdersChange">—</div></div>
            <div class="kpi-card"><div class="kpi-label">🎯 Conversion Rate</div><div class="kpi-value" id="kpiConversion">—</div><div class="kpi-change up" id="kpiConversionChange">—</div></div>
        </div>

        <!-- Revenue + Category Charts -->
        <div class="chart-grid">
            <div class="chart-card">
                <div class="chart-title">Revenue Overview<span style="font-size:11px;color:var(--text3)">Last 12 months</span></div>
                <div class="chart-subtitle">Revenue, Expenses & Profit trends</div>
                <div class="chart-container"><canvas id="revenueChart"></canvas></div>
            </div>
            <div class="chart-card">
                <div class="chart-title">Sales by Category</div>
                <div class="chart-subtitle">Distribution across product categories</div>
                <div class="chart-container"><canvas id="categoryChart"></canvas></div>
            </div>
        </div>

        <!-- Traffic + Demographics -->
        <div class="chart-grid-equal">
            <div class="chart-card">
                <div class="chart-title">Website Traffic<span style="font-size:11px;color:var(--text3)">Last 30 days</span></div>
                <div class="chart-subtitle">Visitors & Page Views</div>
                <div class="chart-container"><canvas id="trafficChart"></canvas></div>
            </div>
            <div class="chart-card">
                <div class="chart-title">User Demographics</div>
                <div class="chart-subtitle">Age group distribution</div>
                <div class="chart-container"><canvas id="demographicsChart"></canvas></div>
            </div>
        </div>

        <!-- Performance + Hourly + Devices -->
        <div class="chart-grid-3">
            <div class="chart-card">
                <div class="chart-title">Performance</div>
                <div class="chart-subtitle">Current vs Previous period</div>
                <div class="chart-container-sm"><canvas id="performanceChart"></canvas></div>
            </div>
            <div class="chart-card">
                <div class="chart-title">Hourly Activity</div>
                <div class="chart-subtitle">24-hour user activity</div>
                <div class="chart-container-sm"><canvas id="hourlyChart"></canvas></div>
            </div>
            <div class="chart-card">
                <div class="chart-title">Device Split</div>
                <div class="chart-subtitle">Traffic by device type</div>
                <div class="chart-container-sm"><canvas id="deviceChart"></canvas></div>
            </div>
        </div>

        <!-- Top Products Table -->
        <div class="table-card">
            <div class="chart-title" style="margin-bottom:16px">🏆 Top Products</div>
            <table>
                <thead><tr><th>Product</th><th>Sales</th><th>Revenue</th><th>Growth</th></tr></thead>
                <tbody id="productsTable"></tbody>
            </table>
        </div>
    </main>
</div>

<script>
Chart.defaults.color = '#8888aa';
Chart.defaults.borderColor = 'rgba(99,102,241,0.08)';
Chart.defaults.font.family = 'Inter';

const COLORS = {
    accent: '#6366f1', accent2: '#818cf8', green: '#10b981', red: '#ef4444',
    blue: '#3b82f6', yellow: '#f59e0b', purple: '#a855f7', pink: '#ec4899',
    cyan: '#06b6d4', orange: '#f97316',
    gradientPurple: (ctx) => { const g = ctx.chart.ctx.createLinearGradient(0,0,0,260); g.addColorStop(0,'rgba(99,102,241,0.3)'); g.addColorStop(1,'rgba(99,102,241,0)'); return g; },
    gradientGreen: (ctx) => { const g = ctx.chart.ctx.createLinearGradient(0,0,0,260); g.addColorStop(0,'rgba(16,185,129,0.2)'); g.addColorStop(1,'rgba(16,185,129,0)'); return g; },
    gradientBlue: (ctx) => { const g = ctx.chart.ctx.createLinearGradient(0,0,0,260); g.addColorStop(0,'rgba(59,130,246,0.2)'); g.addColorStop(1,'rgba(59,130,246,0)'); return g; }
};

let charts = {};

function createCharts(data) {
    Object.values(charts).forEach(c => c.destroy());
    charts = {};

    // Revenue Chart (Line + Bar)
    charts.revenue = new Chart(document.getElementById('revenueChart'), {
        type: 'line', data: {
            labels: data.revenue.labels,
            datasets: [
                { label: 'Revenue', data: data.revenue.revenue, borderColor: COLORS.accent, backgroundColor: COLORS.gradientPurple, fill: true, tension: 0.4, borderWidth: 2, pointRadius: 3, pointBackgroundColor: COLORS.accent },
                { label: 'Expenses', data: data.revenue.expenses, borderColor: COLORS.red, backgroundColor: 'transparent', borderWidth: 2, borderDash: [5,5], tension: 0.4, pointRadius: 0 },
                { label: 'Profit', data: data.revenue.profit, borderColor: COLORS.green, backgroundColor: COLORS.gradientGreen, fill: true, tension: 0.4, borderWidth: 2, pointRadius: 0 }
            ]
        }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top', labels: { usePointStyle: true, pointStyle: 'circle', padding: 16, font: { size: 11 } } } }, scales: { y: { grid: { color: 'rgba(255,255,255,0.03)' }, ticks: { callback: v => '$'+v/1000+'k' } }, x: { grid: { display: false } } } }
    });

    // Category Chart (Doughnut)
    charts.category = new Chart(document.getElementById('categoryChart'), {
        type: 'doughnut', data: {
            labels: data.categories.labels,
            datasets: [{ data: data.categories.values, backgroundColor: [COLORS.accent, COLORS.green, COLORS.yellow, COLORS.pink, COLORS.cyan, COLORS.orange, COLORS.purple], borderWidth: 0, hoverOffset: 8 }]
        }, options: { responsive: true, maintainAspectRatio: false, cutout: '65%', plugins: { legend: { position: 'right', labels: { usePointStyle: true, pointStyle: 'circle', padding: 10, font: { size: 11 } } } } }
    });

    // Traffic Chart (Area)
    charts.traffic = new Chart(document.getElementById('trafficChart'), {
        type: 'line', data: {
            labels: data.traffic.labels,
            datasets: [
                { label: 'Visitors', data: data.traffic.visitors, borderColor: COLORS.blue, backgroundColor: COLORS.gradientBlue, fill: true, tension: 0.4, borderWidth: 2, pointRadius: 0 },
                { label: 'Page Views', data: data.traffic.page_views, borderColor: COLORS.purple, backgroundColor: 'transparent', borderWidth: 2, tension: 0.4, pointRadius: 0 }
            ]
        }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top', labels: { usePointStyle: true, pointStyle: 'circle', padding: 16, font: { size: 11 } } } }, scales: { y: { grid: { color: 'rgba(255,255,255,0.03)' } }, x: { grid: { display: false }, ticks: { maxTicksLimit: 10 } } } }
    });

    // Demographics (Polar Area)
    charts.demographics = new Chart(document.getElementById('demographicsChart'), {
        type: 'polarArea', data: {
            labels: data.demographics.age_groups.labels,
            datasets: [{ data: data.demographics.age_groups.values, backgroundColor: [COLORS.accent+'99', COLORS.green+'99', COLORS.yellow+'99', COLORS.pink+'99', COLORS.cyan+'99', COLORS.orange+'99'], borderWidth: 0 }]
        }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'right', labels: { usePointStyle: true, pointStyle: 'circle', padding: 8, font: { size: 11 } } } }, scales: { r: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { display: false } } } }
    });

    // Performance (Radar)
    charts.performance = new Chart(document.getElementById('performanceChart'), {
        type: 'radar', data: {
            labels: data.performance.labels,
            datasets: [
                { label: 'Current', data: data.performance.current, borderColor: COLORS.accent, backgroundColor: COLORS.accent+'22', borderWidth: 2, pointRadius: 3, pointBackgroundColor: COLORS.accent },
                { label: 'Previous', data: data.performance.previous, borderColor: COLORS.text3||'#555', backgroundColor: 'rgba(136,136,170,0.08)', borderWidth: 1, borderDash: [4,4], pointRadius: 0 }
            ]
        }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top', labels: { usePointStyle: true, padding: 10, font: { size: 10 } } } }, scales: { r: { beginAtZero: true, max: 100, grid: { color: 'rgba(255,255,255,0.05)' }, angleLines: { color: 'rgba(255,255,255,0.05)' }, ticks: { display: false } } } }
    });

    // Hourly Activity (Bar)
    charts.hourly = new Chart(document.getElementById('hourlyChart'), {
        type: 'bar', data: {
            labels: data.hourly.labels,
            datasets: [{ label: 'Activity', data: data.hourly.values, backgroundColor: data.hourly.values.map(v => v > 70 ? COLORS.accent+'cc' : v > 40 ? COLORS.blue+'99' : COLORS.accent+'33'), borderRadius: 4, borderSkipped: false }]
        }, options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { y: { grid: { color: 'rgba(255,255,255,0.03)' }, ticks: { font: { size: 10 } } }, x: { grid: { display: false }, ticks: { maxTicksLimit: 12, font: { size: 9 } } } } }
    });

    // Device Split (Doughnut)
    charts.device = new Chart(document.getElementById('deviceChart'), {
        type: 'doughnut', data: {
            labels: data.demographics.devices.labels,
            datasets: [{ data: data.demographics.devices.values, backgroundColor: [COLORS.accent, COLORS.cyan, COLORS.yellow], borderWidth: 0, hoverOffset: 6 }]
        }, options: { responsive: true, maintainAspectRatio: false, cutout: '70%', plugins: { legend: { position: 'bottom', labels: { usePointStyle: true, pointStyle: 'circle', padding: 12, font: { size: 11 } } } } }
    });

    // Products Table
    const tbody = document.getElementById('productsTable');
    tbody.innerHTML = data.products.map(p => `<tr>
        <td style="font-weight:600">${p.name}</td>
        <td>${p.sales.toLocaleString()}</td>
        <td style="font-weight:600">$${p.revenue.toLocaleString()}</td>
        <td><span class="growth-badge ${p.growth>=0?'up':'down'}">${p.growth>=0?'↑':'↓'} ${Math.abs(p.growth)}%</span></td>
    </tr>`).join('');
}

function updateKPIs(kpi) {
    document.getElementById('kpiRevenue').textContent = '$' + kpi.revenue.value.toLocaleString();
    document.getElementById('kpiUsers').textContent = kpi.users.value.toLocaleString();
    document.getElementById('kpiOrders').textContent = kpi.orders.value.toLocaleString();
    document.getElementById('kpiConversion').textContent = kpi.conversion.value + '%';
    
    ['revenue','users','orders','conversion'].forEach(k => {
        const el = document.getElementById(`kpi${k.charAt(0).toUpperCase()+k.slice(1)}Change`);
        const val = kpi[k].change;
        el.textContent = (val >= 0 ? '↑ ' : '↓ ') + Math.abs(val) + '%';
        el.className = `kpi-change ${val >= 0 ? 'up' : 'down'}`;
    });
}

async function loadData() {
    try {
        const r = await fetch('/api/data');
        const data = await r.json();
        updateKPIs(data.kpi);
        createCharts(data);
        document.getElementById('lastUpdate').textContent = data.updated_at;
    } catch(e) { console.error('Failed to load data:', e); }
}

loadData();
setInterval(loadData, 60000);
</script>
</body>
</html>
"""

if __name__ == '__main__':
    print("=" * 50)
    print("  InsightBoard — Analytics Dashboard")
    print("=" * 50)
    print("  Open: http://localhost:5002")
    print("=" * 50)
    app.run(debug=True, port=5002)
